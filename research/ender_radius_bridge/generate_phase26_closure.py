"""Fixed Phase-26 proof generation; emitted claims still require Lean checking.

Read the frozen Phase-25 candidate. Never search parameters or change a row.
Primality claims come from candidate membership, so a missing/extra prime
causes a generated proposition proof to fail, not a trusted coverage result.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
HEADER = ["import TenthDiscriminant.FirstIntervalData", "",
          "namespace TenthDiscriminant.FirstCertificate",
          "set_option autoImplicit false", "set_option maxRecDepth 100000",
          "set_option maxHeartbeats 20000000", ""]
END = ["", "end TenthDiscriminant.FirstCertificate", ""]


def write(path, lines):
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def range_partition(lines, start, end, pieces, name):
    ranges = ", ".join(f"List.range' {a} {b-a}" for a, b in pieces)
    lines += [f"theorem {name} : List.range' {start} {end-start} = [{ranges}].flatten := by",
              "  simp only [List.flatten_cons, List.flatten_nil, List.append_nil]"]
    for a, b in reversed(pieces[:-1]):
        lines.append(f"  rw [List.range'_append_1 (s := {a}) (m := {b-a}) (n := {end-b})]")
    if len(pieces) == 1:
        lines.append("  rfl")
    lines.append("")


def main():
    data = json.loads((HERE / "PHASE25_RATIONAL_CANDIDATE.json").read_text(encoding="utf-8"))
    assert (data["R"], data["S"], data["P"], data["rho"], data["Y"]) == (
        175000000000, 8750000000, 10000, 408406701, 488)
    rows = data["rows"]
    assert len(rows) == 1229 and len({r["p"] for r in rows}) == 1229
    primes = {r["p"] for r in rows}
    chunks = [rows[i:i+32] for i in range(0, len(rows), 32)]
    cover, totals = HEADER.copy(), HEADER.copy()
    intervals, smalls, odds = [], [], []
    start = 0
    for i, chunk in enumerate(chunks):
        end = chunk[-1]["p"]+1 if i+1 < len(chunks) else 10001
        intervals.append((start, end))
        pieces = [(a, min(a+16, end)) for a in range(start, end, 16)]
        windows = []
        for a, b in pieces:
            name = f"coverage_window_{a}_{b}"
            windows.append(name)
            labels = [n for n in range(a, b) if n in primes]
            cover += [f"theorem {name} :",
                f"    (List.range' {a} {b-a}).filter (fun p => decide p.Prime) = {labels} := by"]
            for k, n in enumerate(range(a, b)):
                truth = n in primes
                cover.append(f"  have b{k} : decide (Nat.Prime {n}) = {str(truth).lower()} := "
                             f"decide_eq_{str(truth).lower()} (by norm_num)")
            cover += ["  simp only [List.range', Nat.reduceAdd, List.filter_cons, List.filter_nil,",
                "    "+", ".join(f"b{k}" for k in range(b-a))+",",
                "    Bool.false_eq_true, ite_false, ite_true]", ""]
        partition = f"coverage_partition_{i:02}"
        range_partition(cover, start, end, pieces, partition)
        cover += [f"theorem firstChunk{i:02}_coverage : firstChunk{i:02}.map Row.p =",
            f"    (List.range' {start} {end-start}).filter (fun p => decide p.Prime) := by",
            f"  rw [{partition}, List.filter_flatten]",
            "  simp only [List.map_cons, List.map_nil, "+", ".join(windows)+",",
            "    List.flatten_cons, List.flatten_nil, List.cons_append, List.nil_append]",
            "  decide +kernel", ""]
        smalls.append(sum(r["factorial_coefficient"]*r["log_hi_units"] for r in chunk))
        odds.append(sum(r["coarse_odd_weight"]*r["log_lo_units"] for r in chunk))
        totals += [f"theorem firstChunk{i:02}_totals :",
            f"    (firstChunk{i:02}.map (fun r => r.coefficient * r.hi)).sum = {smalls[-1]} ∧",
            f"      (firstChunk{i:02}.map (fun r => r.weight * r.lo)).sum = {odds[-1]} := by",
            f"  norm_num [firstChunk{i:02}, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]", ""]
        start = end
    range_partition(cover, 0, 10001, intervals, "coverage_full_partition")
    cover += ["theorem first_rows_coverage : firstRows.map Row.p = primeList := by",
        "  unfold primeList", "  rw [List.range_eq_range', coverage_full_partition,",
        "    List.filter_flatten, firstRows, List.map_flatten]",
        "  simp only [List.map_cons, List.map_nil, "+
        ", ".join(f"firstChunk{i:02}_coverage" for i in range(len(chunks)))+"]"]
    totals += ["theorem first_rows_unit_sums :",
        f"    (firstRows.map (fun r => r.coefficient * r.hi)).sum = {sum(smalls)} ∧",
        f"      (firstRows.map (fun r => r.weight * r.lo)).sum = {sum(odds)} := by", "  constructor"]
    for side in (1, 2):
        totals += ["  · simp only [firstRows, List.map_flatten, List.sum_flatten, List.map_map,",
            "      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, "+
            ", ".join(f"firstChunk{i:02}_totals.{side}" for i in range(len(chunks)))+"]",
            "    norm_num"]
    assert sum(smalls) == data["small_upper_units"]
    assert sum(odds) == data["coarse_lower_units"]
    totals += ["", "theorem first_rows_budgets :",
        "    (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1324 * 10 ^ 20 * scale ∧",
        "      7995 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by",
        "  rw [first_rows_unit_sums.1, first_rows_unit_sums.2]", "  norm_num [scale]"]
    totals += ["", "theorem too_small_factorial_budget_rejected :",
        "    ¬ (firstRows.map (fun r => r.coefficient * r.hi)).sum ≤ 1323 * 10 ^ 20 * scale := by",
        "  rw [first_rows_unit_sums.1]", "  norm_num [scale]", "",
        "theorem too_large_valuation_budget_rejected :",
        "    ¬ 7996 * 10 ^ 29 * scale ≤ (firstRows.map (fun r => r.weight * r.lo)).sum := by",
        "  rw [first_rows_unit_sums.2]", "  norm_num [scale]"]
    write(REPO / "lean" / "TenthDiscriminant" / "FirstIntervalCoverage.lean", cover + END)
    write(REPO / "lean" / "TenthDiscriminant" / "FirstIntervalTotals.lean", totals + END)
    print(json.dumps({"scope": "untrusted generated proof candidates", "rows": len(rows),
                      "integer_coverage": [0, 10001], "window_max_length": 16,
                      "chunks": len(chunks)}, indent=2))


if __name__ == "__main__":
    main()
