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

## 17 November 2026 — third failed field build (run 44038115535)

[Run 44038115535](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44038115535) at commit `964b625794cdc288b2f2e9be4bd9759c1b5a810b` advanced past the previously unresolved `joint_binary_odd_log_of_pos` reference. The next unsatisfied identifier was `jointOddMass_ge_old_plus_three_five_and_ten` in `Phase338JointLower313.lean:57`. Inspecting `Phase331OddMassSplit315.lean` confirms this theorem is defined in namespace `TenthDiscriminant.Phase331`. The dependent lower proof again printed `sorryAx`; the actual-field theorem still did not build.

**Controlled repair:** open the already imported Phase331 namespace inside the Phase338 joint-lower module, or qualify its arithmetic declarations explicitly. Preserve the entire normalized inequality, original Gram determinant, 313-domain hypothesis, existing odd/binary valuations and class-number-one bridge. **No formal field theorem is established until the complete exact-head run and axiom inspection pass.**

## Superseding verification — fourth run 44040958164 PASSED

[Run 44040958164](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44040958164) at exact source head `745f47dff7002b65272e3c8d2f79017ff04fe4a5` **passed both Lean compilation and explicit axiom inspection**. The source joint lower `TenthDiscriminant.Phase338.original_source_joint_normalized_lower_313`, analytic same-Gram upper `TenthDiscriminant.Phase337.thin_production_normalized_upper_stronger_313` and actual-field target `TenthDiscriminant.Threshold313.totallyComplex_degree_two_classNumber_one_discriminant_bound_313` each printed only `[propext, Classical.choice, Quot.sound]`; no `sorryAx` was reported. The theorem has the actual discriminant conclusion and requires total complexity, quadratic degree and class number one.

**Status update:** P as a formal Lean theorem relative to the explicitly encoded source, **not** independently human-reviewed or merged to `main`. Independent mathematical-source audit remains open. The three failed CI runs above remain part of the record; their failures were import/namespace issues, not changed numerical or field hypotheses. [Locked claim graph and review gates](../phase340/VERIFIED_313.md).
