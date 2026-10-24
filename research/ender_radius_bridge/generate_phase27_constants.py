"""Emit fixed untrusted four-constant data and exact proof candidates."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEAN = HERE.parents[1] / "lean" / "TenthDiscriminant"


def write(path, lines):
    path.write_text("\n".join(lines)+"\n", encoding="utf-8", newline="\n")


def main():
    data = json.loads((HERE / "PHASE27_CONSTANT_CANDIDATE.json").read_text(encoding="utf-8"))
    assert (data["Q"], data["P"], data["scale"], data["row_count"]) == (7, 10000, 10**12, 1229)
    rows, totals = data["rows"], data["totals"]
    assert totals == {"a": 8646130782816, "b": 6856198325360,
                      "c": 133259338177, "e": 9892590181957053}
    chunks = [rows[i:i+32] for i in range(0, len(rows), 32)]
    header = ["namespace TenthDiscriminant.FirstCertificate", "set_option autoImplicit false",
              "set_option maxRecDepth 100000", "set_option maxHeartbeats 20000000", ""]
    body = ["import TenthDiscriminant.PrimeLogCertificate", "",
            "/-! Generated data; each rounded constant row must be checked. -/"]+header
    for i, chunk in enumerate(chunks):
        body.append(f"def constantChunk{i:02} : List ConstantRow := [")
        body += ["  ⟨"+", ".join(str(r[k]) for k in ("p", "a", "b", "c", "e"))+"⟩"+
                 ("," if j+1<len(chunk) else "") for j, r in enumerate(chunk)]
        body += ["]", ""]
    body += ["def constantRows : List ConstantRow := ["+
             ", ".join(f"constantChunk{i:02}" for i in range(len(chunks)))+"].flatten",
             "", "end TenthDiscriminant.FirstCertificate"]
    write(LEAN / "PrimeLogConstantData.lean", body)
    proof = ["import TenthDiscriminant.PrimeLogConstantData",
             "import TenthDiscriminant.FirstIntervalRows",
             "import TenthDiscriminant.FirstIntervalCoverage", ""]+header
    fields = ("a", "b", "c", "e")
    for i, chunk in enumerate(chunks):
        proof += [f"theorem constantChunk{i:02}_checked :",
            f"    checkConstantRows firstChunk{i:02} constantChunk{i:02} = true := by decide +kernel", "",
            f"theorem constantChunk{i:02}_totals :"]
        for j, k in enumerate(fields):
            value = sum(r[k] for r in chunk)
            suffix = " ∧" if j<3 else " := by"
            proof.append(f"    (constantChunk{i:02}.map ConstantRow.{k}).sum = {value}"+suffix)
        proof += [f"  norm_num [constantChunk{i:02}, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]", ""]
    proof += ["theorem constant_rows_related :",
        "    List.Forall₂ (fun r t => checkConstantRow r t = true) firstRows constantRows := by",
        "  apply List.rel_flatten", "  exact"]
    for i in range(len(chunks)):
        proof.append(f"    .cons (checkConstantRows_sound _ _ constantChunk{i:02}_checked) (")
    proof.append("    .nil"+")"*len(chunks))
    proof += ["", "theorem constant_units_totals :"]
    for j, k in enumerate(fields):
        suffix = " ∧" if j<3 else " := by"
        proof.append(f"    (constantRows.map ConstantRow.{k}).sum = {totals[k]}"+suffix)
    projections = ("1", "2.1", "2.2.1", "2.2.2")
    for j, proj in enumerate(projections):
        if j<3:
            proof.append("  constructor")
            indent = "  · "
        else:
            indent = "  "
        proof += [indent+"simp only [constantRows, List.map_flatten, List.sum_flatten, List.map_map,",
            "      List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, "+
            ", ".join(f"constantChunk{i:02}_totals.{proj}" for i in range(len(chunks)))+"]",
            ("    " if j<3 else "  ")+"norm_num"]
    proof += ["", "noncomputable section", ""]
    names = ("factorialConstantUpper", "linearConstantLower", "squareConstantUpper", "errorConstantUpper")
    for name, k in zip(names, fields):
        proof.append(f"def {name} : Real := {totals[k]} / 1000000000000")
    proof += ["", "theorem certified_prime_log_constants :",
        "    primeLogFactorialConstant 10000 ≤ factorialConstantUpper ∧",
        "      linearConstantLower ≤ primeLogLinearConstant 7 10000 ∧",
        "      primeLogSquareConstant 7 10000 ≤ squareConstantUpper ∧",
        "      primeLogErrorConstant 7 10000 ≤ errorConstantUpper := by",
        "  have h := four_prime_log_bounds firstRows constantRows first_rows_coverage",
        "    (List.all_eq_true.mp first_rows_checked) constant_rows_related",
        "  simpa only [constant_units_totals.1, constant_units_totals.2.1,",
        "    constant_units_totals.2.2.1, constant_units_totals.2.2.2, scale,",
        "    Nat.cast_ofNat, factorialConstantUpper, linearConstantLower,",
        "    squareConstantUpper, errorConstantUpper] using h", "",
        "theorem constant_upper_rounding_down_rejected :",
        "    checkConstantRow (firstChunk00[0]'(by decide))",
        "      { constantChunk00[0]'(by decide) with a := (constantChunk00[0]'(by decide)).a - 1 } = false := by decide +kernel", "",
        "theorem constant_lower_rounding_up_rejected :",
        "    checkConstantRow (firstChunk00[3]'(by decide))",
        "      { constantChunk00[3]'(by decide) with b := (constantChunk00[3]'(by decide)).b + 1 } = false := by decide +kernel", "",
        "end", "end TenthDiscriminant.FirstCertificate"]
    write(LEAN / "PrimeLogConstants.lean", proof)
    print(json.dumps({"scope": "untrusted fixed proof candidates", "rows": len(rows),
                      "chunks": len(chunks), "totals": totals}, indent=2))


if __name__ == "__main__":
    main()
