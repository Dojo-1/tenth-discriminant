#!/usr/bin/env python3
"""Fail-closed *textual* anchors connecting Phase365 Prolog fixtures to Lean.
Not a Lean parser, proof checker, or independent theorem-verification process.
No external dependencies.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "lean" / "TenthDiscriminant"


def uncomment(src: str) -> str:
    """Remove nested Lean block comments and ordinary line comments."""
    out = []
    i = 0
    depth = 0
    while i < len(src):
        two = src[i : i + 2]
        if two == "/-":
            depth += 1
            i += 2
        elif two == "-/" and depth:
            depth -= 1
            i += 2
        elif two == "--" and depth == 0:
            while i < len(src) and src[i] != "\n":
                i += 1
        elif depth:
            i += 1
        else:
            out.append(src[i])
            i += 1
    if depth:
        raise ValueError("unclosed Lean block comment")
    return "".join(out)


def condensed(text: str) -> str:
    return re.sub(r"\s+", "", text)


def declaration(filename: str, name: str) -> str:
    raw = uncomment((ROOT / filename).read_text(encoding="utf-8"))
    start = re.search(r"(?m)^\s*theorem\s+" + re.escape(name) + r"\b", raw)
    if not start:
        raise AssertionError(f"missing theorem declaration {filename}:{name}")
    rest = raw[start.end() :]
    stop = re.search(r"(?m)^\s*(?:(?:private\s+)?theorem\b|end\b|#print\s+axioms\b)", rest)
    excerpt = raw[start.start() : start.end() + (stop.start() if stop else len(rest))]
    return condensed(excerpt)


def must_have(scope: str, text: str, anchor: str) -> None:
    if anchor not in text:
        raise AssertionError(f"{scope}: missing source anchor {anchor}")


UPPER = "integerRectangularTraceGram(ellipsePairsD(Tuned.thinRadiusD))D(Tuned.SD)(Tuned.RD)(Tuned.SD)"
LOWER = "integerRectangularTraceGramQD(Tuned.SD)(Tuned.RD)(Tuned.SD)"
COMPARE = "comparisonScale(Tuned.RD)(Tuned.SD)"


def check_all(*, mutator=None) -> None:
    upper = declaration("Phase362ThinUpper301.lean", "thin_production_normalized_upper_stronger_301")
    lower = declaration("Phase363JointLower301.lean", "original_source_joint_normalized_lower_301")
    pos = declaration("Phase362SourcePositivity301.lean", "thin_original_gram_pos_301")
    odd = declaration("Phase364Field301Candidate.lean", "odd_large_classNumber_ne_one_301")
    field = declaration("Phase364Field301Candidate.lean", "totallyComplex_degree_two_classNumber_one_discriminant_bound_301")
    src = condensed(uncomment((ROOT / "IntegerTraceGram.lean").read_text(encoding="utf-8")))
    if mutator:
        upper, lower, pos, odd, field, src = mutator(upper, lower, pos, odd, field, src)

    must_have("Phase362 upper", upper, UPPER)
    must_have("Phase362 upper", upper, COMPARE)
    must_have("Phase362 upper", upper, "(4/5:Real)*Real.logD-4821/5000")

    must_have("Phase363 lower", lower, LOWER)
    if lower.count(LOWER) < 2:
        raise AssertionError("lower theorem must refer to the same Gram in premise and conclusion")
    must_have("Phase363 lower", lower, COMPARE)
    must_have("Phase363 lower", lower, "SquarefreeD")
    must_have("Phase363 lower", lower, "original_source_joint_normalized_lower_301")
    must_have("Phase362 positivity", pos, UPPER)

    must_have("Phase364 odd-chart", odd,
              "TenthDiscriminant.Phase362.thin_production_normalized_upper_stronger_301DhD")
    must_have("Phase364 odd-chart", odd,
              "TenthDiscriminant.Phase348.original_source_joint_normalized_lower_301")
    must_have("Phase364 odd-chart", odd, "(ellipsePairsD(Tuned.thinRadiusD))DhDhsqhc")
    must_have("Phase364 odd-chart", odd,
              "Tuned.thin_original_gram_pos_301DhD")
    must_have("Phase364 odd-chart", odd,
              "TenthDiscriminant.Phase361.no_scalar_overlap_301_with_sharp_radius")

    must_have("Phase364 field", field, "(NumberField.discrK).natAbs<(301:Nat)^4")
    must_have("Phase364 field", field, "NumberField.discr_eq_discr_of_algEquiv")

    must_have("original trace", src, "defintegerPairTrace(D:Nat)")
    must_have("original trace", src, "2*(a.1*b.1+(D:Int)*a.2*b.2)")
    must_have("ordinary Z derivative", src, "defintegerDerivativeRow(Drsj:Nat)")
    must_have("ordinary Z derivative", src, "r.descFactorialj")
    must_have("original row-major", src,
              "integerTraceGramMatrixQDJ(funi=>(i.val/S,i.val%S))")


def must_reject(label: str, mutator) -> None:
    try:
        check_all(mutator=mutator)
    except AssertionError:
        print("EXPECTED_REJECTION", label)
        return
    raise AssertionError(f"mutation escaped source guard: {label}")


def main() -> int:
    check_all()
    must_reject(
        "replace_thin_by_padded",
        lambda u,l,p,o,f,s: (u.replace("Tuned.thinRadiusD","Tuned.rhoD"),l,p,o,f,s)
    )
    must_reject(
        "change_lower_jet_depth",
        lambda u,l,p,o,f,s: (u,l.replace("(Tuned.SD)(Tuned.RD)(Tuned.SD)",
                                      "(Tuned.SD)(Tuned.RD)(Tuned.RD)"),p,o,f,s)
    )
    must_reject(
        "change_field_chart_sample",
        lambda u,l,p,o,f,s: (u,l,p,
                             o.replace("(ellipsePairsD(Tuned.thinRadiusD))DhDhsqhc",
                                       "(ellipsePairsD(Tuned.rhoD))DhDhsqhc"),f,s)
    )
    must_reject(
        "wrong_integer_trace_weight",
        lambda u,l,p,o,f,s: (u,l,p,o,f,
                             s.replace("2*(a.1*b.1+(D:Int)*a.2*b.2)",
                                       "a.1*b.1+(D:Int)*a.2*b.2"))
    )
    print("PHASE365_TEXTUAL_LEAN_SOURCE_ANCHORS_OK (not a proof)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("SOURCE_GUARD_FAILED:", exc, file=sys.stderr)
        sys.exit(1)
