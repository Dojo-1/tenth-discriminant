"""One fixed preregistered Arb pilot, not a universal proof."""
import json
from pathlib import Path
import sys

from flint import arb, ctx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from ender import factorial_lower
from green_h1_ellipse import upper_B


def main():
    ctx.prec = 256
    D = 700000000003
    R, S = D // 4, (D // 4) // 20
    d, r, s = arb(D), arb(R), arb(S)
    t = d.sqrt().sqrt()
    candidate = arb(11) / 20 * t**3
    rho = int(candidate.ceil().unique_fmpz())
    Y = int((arb(rho) / d.sqrt()).floor().unique_fmpz())
    n = arb.pi() * rho**2 / d.sqrt() + 2 * rho + 2 * Y + 1
    radius_guard = arb(1001) / 1000 * (arb(3 * R + S) * d.sqrt() / arb.pi()).sqrt() + 10 * d.sqrt()
    A, B = arb(8646130782816) / 10**12, arb(6856198325360) / 10**12
    C, E = arb(133259338177) / 10**12, arb(9892590181957053) / 10**12
    I = arb(9210440367148) / 10**16 + arb(99995001) / 10**12
    V, W, a = r * (r-1)/2, r*(r-1)*(2*r-1)/6, s-arb(1)/2
    small = a * V * B - a * r * E - W * C / 2
    tail = a * (factorial_lower(R) - V * A - V * I) - W * I / 2
    # At this fixed input both signs must be certified before unclipped addition.
    assert small > 0 and tail > 0
    lower, upper = 2 * (small + tail), upper_B(R, S, S, n, arb(rho))
    T, u = r*r*s, d.log()
    lower_target = arb(999997) / 10**6 * u - arb(5845) / 1000
    upper_target = arb(13) / 16 * u - arb(1593) / 2000
    checks = {
        "dimensions": R >= 2 and S >= 1 and R <= 10000*S,
        "strict_inertness": 4*R < D+1,
        "strict_radius_branch": rho < R,
        "chosen_radius": bool(radius_guard <= rho),
        "strict_comparison": bool(upper < lower),
        "lower_envelope": bool(lower_target <= lower/T),
        "upper_envelope": bool(upper/T <= upper_target),
    }
    result = {"scope": "single observational Arb pilot, NOT a universal or Lean proof",
              "precision_bits": ctx.prec, "D": D, "R": R, "S": S,
              "rho": rho, "Y": Y, "new_auxiliary_radius_not_frozen_campaign": True,
              "checks": checks,
              "balls": {k: v.str(65) for k, v in {
                  "radius_candidate": candidate, "radius_guard": radius_guard,
                  "count_upper": n, "lower_over_T": lower/T, "upper_over_T": upper/T,
                  "lower_target": lower_target, "upper_target": upper_target,
                  "normalized_gap": (lower-upper)/T}.items()},
              "exit_code": 0 if all(checks.values()) else 1}
    (HERE / "PHASE28_PILOT.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return result["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
