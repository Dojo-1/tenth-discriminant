# Phase334 failed-build record — retained

## 16 November 2026, first exact-head run

- Exact source head: `32f1db4ef78724bcf5c70f22abe52cb6af383c16`.
- [Actions run 43947209729](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43947209729).
- Finite Python residue-ring tests: **PASS**.
- Lean module: **FAIL** at line 89 inside
  `source_mod_two_has_nonzero_nilpotent`.
- Diagnostic: `change` rejected the desired simplification from
  `pairDvd 2 (pairMul D (1,1) (1,1))` to
  `2 ∣ 1-(D:Int) ∧ 2 ∣ 2`. The two expressions are algebraically
  equal but not definitionally identical with symbolic `D`.
- The module's other requested theorem declarations printed standard
  axioms, but the failed lemma temporarily reported `sorryAx`.
- This is a proof-elaboration defect, not evidence of a counterexample.

**Repair boundary:** replace `change` with `simpa [pairDvd,pairMul]`
using the already proved divisibility `2∣1-D`. Preserve the theorem's
hypotheses, original source values, source polynomial, maximal-order
multiplication, exact finite controls, and both D163/D7 negative controls.
Do not promote Phase334 to P until an exact-head pass.

Retained as a failed-attempt receipt even after subsequent success.
