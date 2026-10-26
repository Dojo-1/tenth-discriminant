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
        powers = []
        while power < R:
            value = ender.floor_sum(R, power)
            quotient, rem = divmod(R, power)
            powers.append([quotient, rem, value])
            coefficient += value
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
                     "exact_odd_weight": exact, "coarse_odd_weight": coarse,
                     "linear_witness": [R//p, R%p, ender.floor_sum(R, p)],
                     "power_witnesses": powers})
    n = R-1
    assert len(rows) == 1229
    assert int(small_up*SCALE) == 132393875135023553259473658533593129
    assert int(coarse_down*SCALE) == 799592313080280706345663778036662106229815220
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
    target.write_text(text+"\n  ]\n}\n", encoding="utf-8", newline="\n")
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
            witness = lambda w: "⟨" + ", ".join(map(str, w)) + "⟩"
            extra = witness(row["linear_witness"]) + ", [" + ", ".join(
                witness(w) for w in row["power_witnesses"]) + "]"
            lean_rows.append("  ⟨" + ", ".join(map(str, fields)) + ", " + extra + "⟩" + ("," if index+1 < len(chunk) else ""))
        lean_rows.extend(["]", ""])
    lean_rows.append("def firstRows : List Row := ["+
                     ", ".join(f"firstChunk{i:02}" for i in range(len(chunks)))+"].flatten")
    lean_rows.extend(["", "end TenthDiscriminant.FirstCertificate", ""])
    lean_target.write_text("\n".join(lean_rows), encoding="utf-8", newline="\n")
    attempt = Path(__file__).with_name("FirstIntervalTableCheck.lean")
    proof_lines = ["import TenthDiscriminant.FirstIntervalData", "",
                   "/-! Phase-25 full-table proof attempt; no interval claim until accepted and audited. -/",
                   "namespace TenthDiscriminant.FirstCertificate",
                   "set_option autoImplicit false", "set_option maxRecDepth 100000",
                   "set_option maxHeartbeats 20000000", ""]
    for chunk_index in range(len(chunks)):
        name = f"firstChunk{chunk_index:02}"
        proof_lines.extend([f"theorem {name}_checked : {name}.all checkRow = true := by decide +kernel", ""])
    proof_lines.extend(["theorem first_rows_checked : firstRows.all checkRow = true := by",
        "  rw [firstRows, List.all_flatten]",
        "  apply List.all_eq_true.mpr", "  intro chunk hmem",
        "  simp only [List.mem_cons, List.not_mem_nil, or_false] at hmem",
        "  rcases hmem with "+" | ".join("rfl" for _ in chunks)])
    for chunk_index in range(len(chunks)):
        proof_lines.append(f"  · exact firstChunk{chunk_index:02}_checked")
    row_pilot = lean_target.with_name("FirstIntervalRows.lean")
    row_pilot.write_text("\n".join(proof_lines + ["", "end TenthDiscriminant.FirstCertificate", ""]),
                        encoding="utf-8", newline="\n")
    # Verify bounded blocks, then compose symbolically; do not reduce one
    # enormous 1229-row fold or a 10001-integer prime filter in the kernel.
    totals = ["import TenthDiscriminant.FirstIntervalData", "",
              "namespace TenthDiscriminant.FirstCertificate",
              "set_option maxRecDepth 100000", "set_option maxHeartbeats 20000000", ""]
    starts, lengths, smalls, odds = [], [], [], []
    block_sources = []
    start = 0
    for i, chunk in enumerate(chunks):
        end = chunk[-1]["p"]+1 if i+1 < len(chunks) else 10001
        starts.append(start); lengths.append(end-start)
        small = sum(r["factorial_coefficient"]*r["log_hi_units"] for r in chunk)
        odd = sum(r["coarse_odd_weight"]*r["log_lo_units"] for r in chunk)
        smalls.append(small); odds.append(odd)
        name = f"firstChunk{i:02}"
        totals.extend([f"theorem {name}_totals :",
            f"    ({name}.map (fun r => r.coefficient * r.hi)).sum = {small} ∧",
            f"      ({name}.map (fun r => r.weight * r.lo)).sum = {odd} := by",
            f"  norm_num [{name}, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]", "",
            f"theorem {name}_coverage : {name}.map Row.p =",
            f"    (List.range' {start} {end-start}).filter (fun p => decide p.Prime) := by decide +kernel", ""])
        block_sources.append(totals[-8:])
        start = end
    part_count = (len(chunks)+9)//10
    attempt_dir = Path(__file__).with_name("divided_totals_attempt")
    attempt_dir.mkdir(exist_ok=True)
    for group in range(part_count):
        part = totals[:6] + [line for block in block_sources[group*10:(group+1)*10]
                             for line in block]
        part += ["end TenthDiscriminant.FirstCertificate", ""]
        (attempt_dir / f"FirstIntervalTotalsPart{group:02}.lean").write_text(
            "\n".join(part), encoding="utf-8", newline="\n")
    totals = [f"import TenthDiscriminant.FirstIntervalTotalsPart{i:02}" for i in range(part_count)]
    totals += ["", "namespace TenthDiscriminant.FirstCertificate",
               "set_option maxRecDepth 100000", "set_option maxHeartbeats 20000000", ""]
    ranges = ", ".join(f"List.range' {s} {n}" for s,n in zip(starts,lengths))
    coverage_pilot = ["import TenthDiscriminant.FirstIntervalData",
        "namespace TenthDiscriminant.FirstCertificate", "set_option maxRecDepth 100000",
        "set_option maxHeartbeats 20000000", "theorem normalized_coverage_pilot :",
        "    firstChunk38.map Row.p =",
        f"      (List.range' {starts[-1]} {lengths[-1]}).filter (fun p => decide p.Prime) := by",
        "  norm_num [firstChunk38, List.range', List.filter]",
        "end TenthDiscriminant.FirstCertificate", ""]
    Path(__file__).with_name("CoverageNormalizationPilot.lean").write_text(
        "\n".join(coverage_pilot), encoding="utf-8", newline="\n")
    totals.extend([f"theorem first_range_split : List.range 10001 = [{ranges}].flatten := by",
        "  rw [List.range_eq_range']",
        "  simp only [List.flatten_cons, List.flatten_nil, List.append_nil]"])
    for i in reversed(range(len(chunks)-1)):
        totals.append(f"  rw [List.range'_append_1 (s := {starts[i]}) (m := {lengths[i]}) (n := {10001-starts[i+1]})]")
    totals.extend(["", "theorem first_rows_coverage : firstRows.map Row.p = primeList := by",
        "  unfold primeList", "  rw [first_range_split, List.filter_flatten, firstRows, List.map_flatten]",
        "  simp only [List.map_cons, List.map_nil, "+
        ", ".join(f"firstChunk{i:02}_coverage" for i in range(len(chunks)))+"]", "",
        "theorem first_rows_unit_sums :",
        f"    (firstRows.map (fun r => r.coefficient * r.hi)).sum = {sum(smalls)} ∧",
        f"      (firstRows.map (fun r => r.weight * r.lo)).sum = {sum(odds)} := by",
        "  constructor"])
    for side in [1, 2]:
        totals.extend(["  · simp only [firstRows, List.map_flatten, List.sum_flatten, List.map_map,",
            "      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, "+
            ", ".join(f"firstChunk{i:02}_totals.{side}" for i in range(len(chunks)))+"]",
            "    norm_num"])
    totals.extend(["", "theorem first_rows_budgets :",
        "    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧",
        "      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by",
        "  rw [first_rows_unit_sums.1, first_rows_unit_sums.2]", "  decide +kernel", "",
        "end TenthDiscriminant.FirstCertificate", ""])
    (attempt_dir / "FirstIntervalTotals.lean").write_text(
        "\n".join(totals), encoding="utf-8", newline="\n")
    proof_lines.extend(["",
        "theorem first_rows_coverage : firstRows.map Row.p = primeList := by decide +kernel", "",
        "theorem first_rows_budgets :",
        "    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧",
        "      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by decide +kernel", "",
        "end TenthDiscriminant.FirstCertificate", ""])
    attempt.write_text("\n".join(proof_lines), encoding="utf-8", newline="\n")
    summary = {k: value for k, value in result.items() if k != "rows"}
    print(json.dumps(summary, indent=2))
    return 0 if lower_exact > upper and lower_coarse > upper else 1


if __name__ == "__main__":
    raise SystemExit(main())
