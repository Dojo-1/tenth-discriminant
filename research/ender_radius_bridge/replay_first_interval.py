"""One fixed Phase-25 replay. Observational Arb evidence, not a Lean certificate."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
import ender
import flint
import numpy
from flint import arb, ctx


def main():
    if flint.__version__ != "0.9.0":
        raise RuntimeError("Phase 25 requires the declared python-flint==0.9.0")
    ctx.prec = 160
    d1, d2, c = 700000000000, 875000000000, 20
    r, p = d1 // 4, ender.P
    s = j = r // c
    rho = ender.radius_for(d2, r, s)
    y = int((arb(rho) / arb(d1).sqrt()).upper().floor().unique_fmpz())
    n_up = arb.pi() * rho * rho / arb(d1).sqrt() + 2 * rho + 2 * y + 1
    lower = ender.prime_mass(r, s)
    upper = ender.upper_B(r, s, j, n_up, arb(rho))
    ok, ratio = ender.certify(d1, d2, c)
    result = {
        "scope": "one fixed production replay; no Lean numerical exclusion claim",
        "python_flint": flint.__version__,
        "numpy": numpy.__version__,
        "precision_bits": ctx.prec,
        "D1": d1, "D2": d2, "C": c, "P": p,
        "R": r, "S": s, "J": j, "rho": rho, "Y": y,
        "small_prime_count": len(ender.small_primes()),
        "lower_ball_display": lower.str(50),
        "upper_ball_display": upper.str(50),
        "ratio_ball_display": ratio.str(50),
        "production_certify_passed": bool(ok),
        "strict_ball_comparison_passed": bool(lower > upper),
    }
    print(json.dumps(result, indent=2))
    return 0 if ok and lower > upper else 1


if __name__ == "__main__":
    raise SystemExit(main())
