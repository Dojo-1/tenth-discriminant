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
