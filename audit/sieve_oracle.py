#!/usr/bin/env python3
"""Independent Python checks of the serialized quotient-prime masks.

This checks literal mask construction and sampled affine-root equivalence.
It is not a proof that the Lean all-fibers certificate covers every input.
"""

from __future__ import annotations

import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "lean/TenthDiscriminant/QuotientFiberData.lean"
MODULUS = 892_371_480
QUOTIENT_MAX = 785
ENTRY = re.compile(r"⟨(\d+),(\d+),(\d+)⟩")


def prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def has_root(n: int, p: int) -> bool:
    return any((t * t + n) % p == 0 for t in range(p))


def read_entries() -> list[tuple[int, int, int]]:
    entries = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        if not line.startswith("def phase36Entry"):
            continue
        match = ENTRY.search(line)
        if match is None:
            raise ValueError(f"unparsed serialized entry: {line[:120]}")
        entries.append(tuple(map(int, match.groups())))
    return entries


def main() -> None:
    entries = read_entries()
    assert len(entries) == 200, f"expected 200 patterns, got {len(entries)}"
    rng = random.Random(0xA260C0DE)
    sample_count = 0

    for p, inverse, encoded in entries:
        assert prime(p), f"nonprime modulus {p}"
        assert (MODULUS * inverse) % p == 1, f"bad inverse for p={p}"

        forbidden = {(-inverse * t * t) % p for t in range(p)}
        expected = 0
        for bit in range(QUOTIENT_MAX + p):
            if bit % p not in forbidden:
                expected |= 1 << bit
        assert encoded == expected, f"serialized mask mismatch for p={p}"

        quotients = {0, 1, QUOTIENT_MAX - 1, QUOTIENT_MAX - 2}
        quotients.update(rng.randrange(QUOTIENT_MAX) for _ in range(122))
        for r in (0, 1, MODULUS - 1, rng.randrange(MODULUS)):
            shift = (inverse * r) % p
            for k in quotients:
                encoded_allows = ((encoded >> (shift + k)) & 1) == 1
                direct_allows = not has_root(r + MODULUS * k, p)
                assert encoded_allows == direct_allows, (
                    f"affine-root mismatch p={p}, r={r}, k={k}"
                )
                sample_count += 1

    print(
        f"PASS: {len(entries)} masks reconstructed exactly; "
        f"{sample_count} affine-root comparisons passed."
    )


if __name__ == "__main__":
    main()
