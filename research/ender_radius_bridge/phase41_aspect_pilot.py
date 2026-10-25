"""Exactly one preregistered observational input; no universal cutoff inference."""
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import flint
import numpy
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import ender


def main():
    if (flint.__version__, numpy.__version__) != ("0.9.0", "2.5.4"):
        raise RuntimeError("Registered runtime versions do not match")
    ctx.prec = 256
    D, C, P = 100000000003, 25, 10000
    R, S = D // 4, (D // 4) // C
    d, r, s = arb(D), arb(R), arb(S)
    t = d.sqrt().sqrt()
    candidate = arb(13) / 25 * t**3
    rho = int(candidate.ceil().unique_fmpz())
    y = int((arb(rho) / d.sqrt()).floor().unique_fmpz())
    n_upper = arb.pi() * rho**2 / d.sqrt() + 2*rho + 2*y + 1
    n_lower = arb.pi() * rho**2 / d.sqrt() - 2*arb(rho)/d.sqrt() - 6*rho
    guard = arb(1001)/1000 * (arb(3*R+S)*d.sqrt()/arb.pi()).sqrt() + 10*d.sqrt()
    a, b = arb(8646130782816)/10**12, arb(6856198325360)/10**12
    c, e = arb(133259338177)/10**12, arb(9892590181957053)/10**12
    tail_budget = arb(9210440367148)/10**16 + arb(99995001)/10**12
    v, w, coeff = r*(r-1)/2, r*(r-1)*(2*r-1)/6, s-arb(1)/2
    small = coeff*v*b-coeff*r*e-w*c/2
    tail = coeff*(ender.factorial_lower(R)-v*a-v*tail_budget)-w*tail_budget/2
    raw = 2*(small+tail)
    production = ender.prime_mass(R, S)
    upper = ender.upper_B(R, S, S, n_upper, arb(rho))
    scale, u = r*r*s, d.log()
    lower_target = arb(999997)/10**6*u-arb(5820)/1000
    upper_target = arb(4)/5*u-arb(813)/1000
    gap = lambda x: F(999997, 10**6)*x-F(5820, 1000)-(F(4, 5)*x-F(813, 1000))
    checks = {
        "dimensions": R >= 10**8 and S >= 500000 and R <= 10000*S and ender.P == P,
        "aspect_ratio": 10*R <= 251*S,
        "strict_integer_inertness": R < (D+1)//4,
        "radius_rounding": bool(candidate <= rho and arb(rho) < candidate+1),
        "positive_radius_below_R": 0 < rho < R,
        "chosen_radius": bool(guard <= rho),
        "direct_count_lower": bool(n_lower > 3*R+S),
        "derivative_count": S >= 2*rho+1+2*y+1,
        "positive_small_tail": bool(small > 0 and tail > 0),
        "raw_below_production": bool(raw < production),
        "production_strict_comparison": bool(upper < production),
        "raw_strict_comparison": bool(upper < raw),
        "candidate_lower_envelope": bool(lower_target <= raw/scale),
        "candidate_upper_envelope": bool(upper/scale <= upper_target),
        "candidate_scalar_gap_25_point_3": gap(F(253, 10)) > 0,
        "candidate_scalar_reject_25": gap(F(25)) <= 0,
        "floor25_equality_rejected": 100000024 > 25*(100000024//25),
    }
    result = {
        "scope": "One observational Arb input; NOT a Lean proof or universal 100-billion cutoff",
        "protocol_commit": "35dbd4c7ce3e3d5c6c7dce5d3cfdf3d4b1b1f2af",
        "python_flint": flint.__version__, "numpy": numpy.__version__,
        "precision_bits": ctx.prec, "D": D, "R": R, "S": S, "J": S,
        "C": C, "P": P, "K": "251/10", "radius_coefficient": "13/25",
        "rho": rho, "Y": y, "new_auxiliary_family_not_frozen_campaign": True,
        "squarefree_status_not_tested_or_assumed": True,
        "checks": checks,
        "exact_scalar_gap_at_25_point_3": str(gap(F(253, 10))),
        "exact_scalar_gap_at_25": str(gap(F(25))),
        "balls": {k: value.str(65) for k, value in {
            "radius_candidate": candidate, "radius_guard": guard,
            "count_lower": n_lower, "count_upper": n_upper,
            "raw_over_scale": raw/scale, "production_over_scale": production/scale,
            "upper_over_scale": upper/scale, "lower_target": lower_target,
            "upper_target": upper_target, "raw_normalized_gap": (raw-upper)/scale,
            "production_normalized_gap": (production-upper)/scale,
        }.items()},
        "exit_code": 0 if all(checks.values()) else 1,
    }
    print(json.dumps(result, indent=2))
    return result["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
