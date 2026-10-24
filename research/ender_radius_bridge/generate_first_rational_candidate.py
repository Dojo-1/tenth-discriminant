"""Fixed Phase-25 rational candidate; generated data are not Lean proofs.

All arithmetic below is exact Fraction/integer arithmetic. Output is a
mechanically generated certificate candidate, to be independently checked.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
import ender

R, S, P, RHO, Y = 175000000000, 8750000000, 10000, 408406701, 488
N, SCALE = 8, 10**12


def prefix(z):
    return sum((2 * z ** (2*k + 1) / (2*k + 1) for k in range(N)), Q(0))


def remainder(z):
    return 2 * z ** (2*N + 1) / ((2*N + 1) * (1 - z*z))


def floor_q(x):
    return x.numerator // x.denominator


def ceil_q(x):
    return -floor_q(-x)


def log_bounds(x):
    assert x >= 1
    k = max(0, x.numerator.bit_length() - x.denominator.bit_length())
    if Q(2)**k > x:
        k -= 1
    t = x / Q(2)**k
    assert 1 <= t < 2
    z = (t - 1) / (t + 1)
    lo = k * prefix(Q(1, 3)) + prefix(z)
    hi = lo + k * remainder(Q(1, 3)) + remainder(z)
    return Q(floor_q(lo*SCALE), SCALE), Q(ceil_q(hi*SCALE), SCALE), k


def main():
    v, w = R*(R-1)//2, R*(R-1)*(2*R-1)//6
    small_up = Q(0)
    exact_down = Q(0)
    coarse_down = Q(0)
    rows = []
    scalar_logs = []
    def scalar_bounds(name, x):
        lo, hi, k = log_bounds(x)
        scalar_logs.append({"name": name, "numerator": x.numerator, "denominator": x.denominator,
                            "binary_k": k, "lo_units": int(lo*SCALE), "hi_units": int(hi*SCALE)})
        return lo, hi
    for p in ender.small_primes():
        lp, up, k = log_bounds(Q(p))
        coefficient, power = 0, p
        while power < R:
            coefficient += ender.floor_sum(R, power)
            power *= p
        exact = ender.F_exact(p, R, S) if p != 2 else 0
        # A potential lower bound on the same original valuationWeight.
        # Its all-quotient inequality is a separate Lean proof obligation.
        c = (Q(S)-Q(1, 2))*ender.floor_sum(R, p) - Q(w, 2*p*p)
        coarse = max(0, floor_q(c)) if p != 2 else 0
        small_up += coefficient * up
        exact_down += exact * lp
        coarse_down += coarse * lp
        rows.append({"p": p, "binary_k": k,
                     "log_lo_units": int(lp*SCALE), "log_hi_units": int(up*SCALE),
                     "factorial_coefficient": coefficient,
                     "exact_odd_weight": exact, "coarse_odd_weight": coarse})
    n = R-1
    l_n = scalar_bounds("factorial_N", Q(n))[0]
    h_low = Q(n*n, 2)*l_n - Q(3*n*n, 4) + Q(n, 2) + Q(1, 4)
    i_up = scalar_bounds("tail_P_plus_one", Q(P+1))[1]/P + scalar_bounds("tail_ratio", 1+Q(1, P))[1]
    tail_down = (Q(S)-Q(1, 2))*(h_low-small_up-v*i_up) - Q(w, 2)*i_up
    lower_exact = 2*(exact_down+max(tail_down, Q(0)))
    lower_coarse = 2*(coarse_down+max(tail_down, Q(0)))
    pi_up = Q(314159265358979323847, 10**20)
    sqrt_d1_lo = Q(836660026534075547, 10**12)
    n_up = pi_up*RHO*RHO/sqrt_d1_lo + 2*RHO+2*Y+1
    log_n_up = scalar_bounds("upper_count_log_argument", 2*n_up*S)[1]
    log_rho_up = scalar_bounds("radius", Q(RHO))[1]
    log_ratio_up = scalar_bounds("radius_ratio", Q(R, RHO))[1]
    upper = R*S*log_n_up
    upper += 2*log_rho_up*(S*R*(R-1)//2+R*S*(S-1)//2)
    upper += 2*S*(S-1)*(R*log_ratio_up-R+RHO+log_ratio_up)
    result = {"scope": "exact rational candidate, not kernel-checked interval exclusion",
              "R": R, "S": S, "P": P, "rho": RHO, "Y": Y,
              "series_terms": N, "log_scale": SCALE,
              "coefficient_power_cutoff": 38,
              "lower_exact_floor": floor_q(lower_exact),
              "lower_coarse_floor": floor_q(lower_coarse),
              "upper_ceil": ceil_q(upper),
              "strict_exact_rational_comparison": lower_exact > upper,
              "strict_coarse_rational_comparison": lower_coarse > upper,
              "row_count": len(rows), "small_upper_units": int(small_up*SCALE),
              "coarse_lower_units": int(coarse_down*SCALE),
              "scalar_logs": scalar_logs, "rows": rows}
    target = Path(__file__).with_name("PHASE25_RATIONAL_CANDIDATE.json")
    metadata = {key: value for key, value in result.items() if key != "rows"}
    text = json.dumps(metadata, indent=2)[:-2] + ',\n  "rows": [\n'
    text += ",\n".join("    "+json.dumps(row, separators=(",", ":")) for row in rows)
    target.write_text(text+"\n  ]\n}\n", encoding="utf-8")
    lean_target = Path(__file__).resolve().parents[2] / "lean" / "TenthDiscriminant" / "FirstIntervalData.lean"
    lean_rows = ["import TenthDiscriminant.NumericalCertificate", "",
                 "/-! Mechanically generated candidate data; validity is a separate proof obligation. -/",
                 "namespace TenthDiscriminant.FirstCertificate", ""]
    chunks = [rows[i:i+32] for i in range(0, len(rows), 32)]
    for chunk_index, chunk in enumerate(chunks):
        lean_rows.append(f"def firstChunk{chunk_index:02} : List Row := [")
        for index, row in enumerate(chunk):
            fields = [row["p"], row["binary_k"], row["log_lo_units"], row["log_hi_units"],
                      row["factorial_coefficient"], row["coarse_odd_weight"]]
            lean_rows.append("  ⟨" + ", ".join(map(str, fields)) + "⟩" + ("," if index+1 < len(chunk) else ""))
        lean_rows.extend(["]", ""])
    lean_rows.append("def firstRows : List Row := ["+
                     ", ".join(f"firstChunk{i:02}" for i in range(len(chunks)))+"].flatten")
    lean_rows.extend(["", "end TenthDiscriminant.FirstCertificate", ""])
    lean_target.write_text("\n".join(lean_rows), encoding="utf-8")
    attempt = Path(__file__).with_name("FirstIntervalTableCheck.lean")
    proof_lines = ["import TenthDiscriminant.FirstIntervalData", "",
                   "/-! Phase-25 full-table proof attempt; no interval claim until accepted and audited. -/",
                   "namespace TenthDiscriminant.FirstCertificate",
                   "set_option autoImplicit false", "set_option maxRecDepth 100000",
                   "set_option maxHeartbeats 20000000", ""]
    for chunk_index in range(len(chunks)):
        name = f"firstChunk{chunk_index:02}"
        proof_lines.extend([f"theorem {name}_checked : {name}.all checkRow = true := by decide", ""])
    proof_lines.extend(["theorem first_rows_checked : firstRows.all checkRow = true := by",
        "  rw [firstRows, List.all_flatten]",
        "  apply List.all_eq_true.mpr", "  intro chunk hmem",
        "  simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem",
        "  rcases hmem with "+" | ".join("rfl" for _ in chunks)])
    for chunk_index in range(len(chunks)):
        proof_lines.append(f"  · exact firstChunk{chunk_index:02}_checked")
    proof_lines.extend(["",
        "theorem first_rows_coverage : firstRows.map Row.p = primeList := by decide", "",
        "theorem first_rows_budgets :",
        "    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧",
        "      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by decide", "",
        "end TenthDiscriminant.FirstCertificate", ""])
    attempt.write_text("\n".join(proof_lines), encoding="utf-8")
    summary = {k: value for k, value in result.items() if k != "rows"}
    print(json.dumps(summary, indent=2))
    return 0 if lower_exact > upper and lower_coarse > upper else 1


if __name__ == "__main__":
    raise SystemExit(main())
