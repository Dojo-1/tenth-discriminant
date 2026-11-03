#!/usr/bin/env python3
"""Check README math-markup invariants without third-party dependencies.

This catches common Markdown source mistakes. It is not a MathJax renderer,
a LaTeX parser, or a mathematical proof checker.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


FENCE = re.compile(r"^\s*```([\w-]*)\s*$")
MATH_IN_CODE = re.compile(
    r"`[^`\n]*(?:\\(?:partial|Delta|Lambda|det|log|sum|mathbb|operatorname)"
    r"|[ΔΛ∑∏∣≤≥])[^\n`]*`"
)


def check(content: str) -> list[str]:
    errors: list[str] = []
    fence: str | None = None
    math_lines: list[str] = []
    math_count = 0

    for number, line in enumerate(content.splitlines(), start=1):
        match = FENCE.fullmatch(line)
        if match:
            if fence is None:
                fence = match.group(1).lower()
                if fence == "math":
                    math_lines = []
                    math_count += 1
            else:
                if fence == "math":
                    expression = "\n".join(math_lines)
                    if not expression.strip():
                        errors.append(f"line {number}: empty math fence")
                    if expression.count(r"\left") != expression.count(r"\right"):
                        errors.append(f"line {number}: unmatched \\left / \\right")
                    if expression.count(r"\begin{") != expression.count(r"\end{"):
                        errors.append(f"line {number}: unmatched \\begin / \\end")
                    depth = 0
                    for index, char in enumerate(expression):
                        if index and expression[index - 1] == "\\":
                            continue
                        if char == "{":
                            depth += 1
                        elif char == "}":
                            depth -= 1
                            if depth < 0:
                                errors.append(f"line {number}: extra closing brace in math fence")
                                break
                    if depth > 0:
                        errors.append(f"line {number}: unclosed brace in math fence")
                fence = None
            continue

        if fence is not None:
            if fence == "math":
                math_lines.append(line)
                if "$" in line:
                    errors.append(f"line {number}: dollar delimiter inside math fence")
            continue

        if line.strip() in ("$", "$$"):
            errors.append(f"line {number}: lone dollar-delimiter line (use fenced math)")

        for expression in MATH_IN_CODE.finditer(line):
            errors.append(
                f"line {number}: apparent mathematical notation in code span: "
                + expression.group(0)[:80]
            )

        # Remove ordinary inline code, then count unescaped inline math delimiters.
        without_code = re.sub(r"`[^`]*`", "", line)
        unescaped_dollars = len(re.findall(r"(?<!\\)\$", without_code))
        if unescaped_dollars % 2:
            errors.append(f"line {number}: unmatched inline math dollar")

    if fence is not None:
        errors.append(f"EOF: unclosed {fence or 'plain'} fenced block")
    if math_count < 3:
        errors.append("README should have multiple correctly fenced math examples")
    return errors


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    if not path.is_file():
        print(f"Math Markdown check: missing file {path}", file=sys.stderr)
        return 2
    errors = check(path.read_text(encoding="utf-8"))
    if errors:
        print("\n".join(f"ERROR {entry}" for entry in errors), file=sys.stderr)
        return 1
    print(f"README math-markup sanity check OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
