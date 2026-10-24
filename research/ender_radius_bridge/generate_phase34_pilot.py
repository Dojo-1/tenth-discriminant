"""Generate untrusted literal masks for the fixed Phase34 Lean cost pilot.

This does not run the production sieve or certify any interval. Lean must
check every mask and every requested Boolean certificate separately.
"""
from pathlib import Path
import json
from math import isqrt

ROOT = Path(__file__).resolve().parents[2]
BASE = [3, 5, 7, 11, 13, 17, 19, 23]


def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n) + 1))


def mask(p):
    bits = 0
    for r in range(p):
        bits |= 1 << ((-r * r) % p)
    return bits


def entries(ps):
    return "[" + ",\n  ".join(f"({p},{mask(p)})" for p in ps) + "]"


def main():
    extras = [p for p in range(29, 100000) if prime(p)][:200]
    target = ROOT / "lean/TenthDiscriminant/ResidueMaskPilotData.lean"
    source = """import TenthDiscriminant.ResidueMaskCore

/-! Generated untrusted literals. Fixed Phase34 parameters, not an interval
certificate or a claim that these masks have the required meaning. -/
namespace TenthDiscriminant
set_option autoImplicit false
"""
    source += f"\ndef phase34Base : List (Nat×Nat) :=\n  {entries(BASE)}\n"
    source += f"\ndef phase34Extra : List (Nat×Nat) :=\n  {entries(extras)}\n"
    source += "\nend TenthDiscriminant\n"
    target.write_text(source, encoding="utf-8", newline="\n")
    for k in [0, 1, 392, 784]:
        check = ROOT / f"research/ender_radius_bridge/Phase34Translate{k}Check.lean"
        check.write_text("import TenthDiscriminant.ResidueMaskPilotData\n\n"
                         "namespace TenthDiscriminant\n"
                         "example : maskTranslateClear (maskWheelResidues phase34Base)\n"
                         f"    892371480 1000000 700000000000 {k} phase34Extra=true := by decide +kernel\n"
                         "end TenthDiscriminant\n", encoding="utf-8", newline="\n")
    print(json.dumps({"generated": str(target.relative_to(ROOT)),
                      "extra_count": len(extras), "extra_first": extras[0],
                      "extra_last": extras[-1], "period": 892371480,
                      "padded_quotient_count": 700000000000 // 892371480 + 1,
                      "fixed_quotients": [0, 1, 392, 784],
                      "status": "untrusted literals only"}, indent=2))


if __name__ == "__main__":
    main()
