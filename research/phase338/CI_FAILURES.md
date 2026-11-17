# Phase338 — verification and failure ledger

## 17 November 2026 — first exact-head field build (run 44033778240)

[Full workflow](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44033778240) ran at source head `508c0d16159dfc8c66fd06131b59d55b906d2214`.

**What passed:** the standalone Phase338 recovered lower at 313,
the previously verified Phase336 scalar and Phase337 original-Gram
analytic upper (Phase337 separately passed
[run 44033778266](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44033778266)).

**What failed:** `Phase338JointLower313.lean:53:18` referenced
`joint_binary_odd_log_of_pos`, which is defined in
`TenthDiscriminant.Phase331JointBinaryOddLog315` but was
not imported explicitly. The dependent theorem
`original_source_joint_normalized_lower_313` was unproved at this head
and printed `sorryAx`; the actual-field candidate was not compiled
to a checked theorem.

**Controlled correction:** add only
`import TenthDiscriminant.Phase331JointBinaryOddLog315`
to the Phase338 joint-lower module. Do NOT alter prime exponents,
the unimodular binary row action, the 313 hypothesis, normalized
coefficients, original Qthin, old count majorant, trace pairing,
ordinary Z-jet convention, determinant identity, or field conclusion.

**Promotion gate:** a fresh complete Phase338 build including the
actual-field theorem and `#print axioms` output must succeed.
This file remains an auditable failed-attempt receipt even after
subsequent correction.

## 17 November 2026 — second failed field build (run 44035309207)

[Full workflow](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44035309207) at `dc3f7b7b0a46a017ab33fc36e2f0204119a35f41` again failed in `Phase338JointLower313.lean`, now line 54. The explicit import was present, but the reference `joint_binary_odd_log_of_pos` remained unqualified; the actual theorem is in namespace `TenthDiscriminant.Phase331`. Lean reported `unknown identifier` and dependent `unsolved goals`, and printed `sorryAx` for the unfinished lower. The final field candidate was not checked in this run.

**Repair:** refer to `TenthDiscriminant.Phase331.joint_binary_odd_log_of_pos` explicitly. Change only the theorem reference, keeping all operands, hypotheses, the single original Gram, the odd-prime factor and joint binary exponent invariant. Independent Phase337 source upper remains [verified](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44033778266). Another complete field CI and axiom inspection are required.
