#!/usr/bin/env python3
"""Check reader-facing Markdown math markup with no third-party dependencies.

This checks known portability/Markdown errors. It is not a MathJax renderer,
a proof checker, or an independent review of the mathematics.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE = (
    "README.md",
    "RESEARCH_NOW.md",
    "lean/HUMAN_GUIDE.md",
    "lean/MATHEMATICAL_SPINE.md",
    "research/ender_radius_bridge/*GUIDE.md",
    "research/sharp_radial_v1/*RECONSTRUCTION.md",
    "research/thin_integrated/*.md",
    "research/reverse_determinant/*.md",
    "research/ellipsoid_trimming/PHASE142_LEVERAGE_AND_UNISOLVENCE.md",
    "research/graded_moments/*.md",
)

FENCE = re.compile(r"^\s*([\x60~]{3,})([A-Za-z0-9_-]*)\s*$")
INLINE_CODE = re.compile(r"\x60[^\x60\n]*\x60")
FORBIDDEN_MACRO = re.compile(r"\\operatorname\b")
LEGACY_DELIMITER = re.compile(r"\\(?:\(|\)|\[|\])")
UNESCAPED_DOLLAR = re.compile(r"(?<!\\)\$")


def check(content: str) -> list[str]:
    errors: list[str] = []
    fence_kind: str | None = None
    fence_char = ""
    fence_length = 0
    double_dollar_block = False

    for n, line in enumerate(content.splitlines(), 1):
        marker = FENCE.fullmatch(line)
        if marker:
            chars, info = marker.groups()
            if fence_kind is None:
                fence_kind = "math" if info.lower() == "math" else "code"
                fence_char = chars[0]
                fence_length = len(chars)
            elif chars[0] == fence_char and len(chars) >= fence_length and not info:
                fence_kind = None
            continue

        if fence_kind is not None:
            if fence_kind == "math" and FORBIDDEN_MACRO.search(line):
                errors.append(f"line {n}: unsupported operatorname macro in math fence")
            continue

        visible = INLINE_CODE.sub("", line)
        stripped = visible.strip()
        if stripped == "$":
            errors.append(f"line {n}: isolated single-dollar display delimiter")
            continue
        if stripped == "$$":
            double_dollar_block = not double_dollar_block
            continue

        if FORBIDDEN_MACRO.search(visible):
            errors.append(f"line {n}: unsupported operatorname macro")
        if LEGACY_DELIMITER.search(visible):
            errors.append(f"line {n}: legacy LaTeX delimiter; use inline dollars or a math fence")
        if double_dollar_block:
            continue

        # Remove paired display-dollar tokens before counting inline math pairs.
        inline = visible.replace("$$", "")
        if len(UNESCAPED_DOLLAR.findall(inline)) % 2:
            errors.append(f"line {n}: unmatched inline dollar delimiter")

    if fence_kind is not None:
        errors.append("EOF: unclosed Markdown code/math fence")
    if double_dollar_block:
        errors.append("EOF: unclosed double-dollar display block")
    return errors


def regression_controls() -> None:
    bad = (
        r"Equation $|\operatorname{disc}(K)|$",
        "\x60\x60\x60math\n\\operatorname{Tr}(z)\n\x60\x60\x60",
        "$\nx^2\n$",
        r"The value is \(x^2\).",
        "\\[\nx^2\n\\]",
        "The value is $x^2.",
    )
    good = (
        "An expression $x^2$ is inline.",
        "\x60\x60\x60math\n\\mathrm{disc}(K)\n\x60\x60\x60",
        "$$\nx^2\n$$",
        "\x60\\operatorname{disc}\x60 is mentioned literally.",
    )
    for case in bad:
        if not check(case):
            raise AssertionError("negative markup control was not rejected")
    for case in good:
        if check(case):
            raise AssertionError("valid markup control was rejected")


def main() -> int:
    regression_controls()
    if len(sys.argv) > 1:
        paths = [ROOT / p for p in sys.argv[1:]]
    else:
        paths = sorted({p for pattern in SCOPE for p in ROOT.glob(pattern)})
    failures = 0
    for path in paths:
        if not path.is_file():
            print(f"ERROR missing file: {path}", file=sys.stderr)
            failures += 1
            continue
        for message in check(path.read_text(encoding="utf-8")):
            print(f"ERROR {path.relative_to(ROOT)}: {message}", file=sys.stderr)
            failures += 1
    if failures:
        print(f"Human math markup: {failures} finding(s)", file=sys.stderr)
        return 1
    print(f"Human math markup OK: {len(paths)} Markdown files (source checks only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
