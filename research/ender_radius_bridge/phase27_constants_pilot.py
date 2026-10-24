"""One preregistered exact-rational pilot; not itself a Lean certificate."""
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
R, S, Q, P, SCALE = 175000000000, 8750000000, 7, 10000, 10**12


def main():
    data = json.loads((HERE / "PHASE25_RATIONAL_CANDIDATE.json").read_text(encoding="utf-8"))
    assert (data["R"], data["S"], data["P"], data["log_scale"]) == (R, S, P, SCALE)
    rows = []
    for r in data["rows"]:
        p, lo, hi = r["p"], r["log_lo_units"], r["log_hi_units"]
        assert 2 <= p <= P
        a = (hi+p-2)//(p-1)
        b = lo//p if Q <= p else 0
        c = (hi+p*p-1)//(p*p) if Q <= p else 0
        e = hi if Q <= p else 0
        assert hi <= a*(p-1)
        assert Q > p or (b*p <= lo and hi <= c*p*p)
        rows.append({"p": p, "a": a, "b": b, "c": c, "e": e})
    totals = {k: sum(row[k] for row in rows) for k in ("a", "b", "c", "e")}
    v, w, coeff = F(R*(R-1), 2), F(R*(R-1)*(2*R-1), 6), F(2*S-1, 2)
    upper = v*F(totals["a"], SCALE)
    lower = coeff*v*F(totals["b"], SCALE)-coeff*R*F(totals["e"], SCALE)-w*F(totals["c"], 2*SCALE)
    result = {"scope": "external exact-rational fixed pilot, not Lean verification",
              "R": R, "S": S, "Q": Q, "P": P, "scale": SCALE,
              "row_count": len(rows), "totals": totals,
              "factorial_upper": str(upper), "odd_lower": str(lower),
              "existing_factorial_budget_met": upper <= 1324*10**20,
              "existing_odd_budget_met": 7995*10**29 <= lower, "rows": rows}
    metadata = {k:v for k,v in result.items() if k != "rows"}
    text = json.dumps(metadata, indent=2)[:-2]+',\n  "rows": [\n'
    text += ",\n".join("    "+json.dumps(row, separators=(",", ":")) for row in rows)
    (HERE / "PHASE27_CONSTANT_CANDIDATE.json").write_text(
        text+"\n  ]\n}\n", encoding="utf-8", newline="\n")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, indent=2))
    return 0 if result["existing_factorial_budget_met"] and result["existing_odd_budget_met"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
