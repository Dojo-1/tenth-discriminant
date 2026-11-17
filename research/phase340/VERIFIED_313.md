# Phase340 — source-locked `313^4` research certificate

**Date:** 17 November 2026. **Branch:** `research/phase309-original-source-picard-minors`.
**Exact mathematical source head:** [`745f47dff7002b65272e3c8d2f79017ff04fe4a5`](https://github.com/Dojo-1/tenth-discriminant/commit/745f47dff7002b65272e3c8d2f79017ff04fe4a5).
**Verification:** [GitHub Actions run 44040958164](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44040958164), job 133895160367; both Lean compilation and independent final `#check`/`#print axioms` steps succeeded.

> **P — formal mathematics relative to the encoded model.** The result is a Lean-checked theorem at the exact source head. This certificate does not claim first discovery of a quadratic class-number-one discriminant bound, independent human review, an external challenge acceptance, or a merge to `main`.

## Exact exported field statement

```lean
TenthDiscriminant.Threshold313.totallyComplex_degree_two_classNumber_one_discriminant_bound_313
    (K : Type u) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (313 : Nat)^4
```

Here `313^4 = 9597924961`. `NumberField.discr K` is the **actual field discriminant**. The proof does not rely on a preloaded list of imaginary quadratic class-number-one fields.

## Source identity: both estimates constrain one original Gram

```lean
integerRectangularTraceGram
  (ellipsePairs D (Tuned.thinRadius D))
  D (Tuned.S D) (Tuned.R D) (Tuned.S D)
```

The proof uses ordinary Z derivatives (W held fixed), the original row-major rectangular monomials, and the integral positive trace pairing `2*(a_x*b_x + D*a_y*b_y)`. No maximal-order resampling, padded determinant, modified jet convention, or surrogate field discriminant is used.

The normalized expression `log(det G_D) / comparisonScale (Tuned.R D) (Tuned.S D)` occurs literally in BOTH bounds, so the final contradiction is enforced by Lean's types:

- **P — arithmetic lower:** `TenthDiscriminant.Phase338.original_source_joint_normalized_lower_313` (imports the previously established *single* joint binary + odd-prime product; the original combined binary row construction is counted once). This is conditional on the explicit squarefreeness, odd maximal-order chart, class number one, and positive original determinant.
- **P — analytic upper:** `TenthDiscriminant.Phase337.thin_production_normalized_upper_stronger_313`, with original `Qthin` and a stronger 17/20 radius estimate; the padded ellipse supplies only a cardinality majorant.
- **P — strict scalar separation:** `TenthDiscriminant.Phase336.no_scalar_overlap_313_without_mixed`; the source lower and upper are disjoint for D >= 313^4.
- **P — positive determinant:** `TenthDiscriminant.FirstCertificate.Tuned.thin_original_gram_pos_313`.
- **P — field transfer:** `Phase338Field313Candidate.lean` transports the contradiction through the existing imaginary quadratic/maximal-order chart to the actual totally-complex degree-two field.

**Not used:** the unproved extra mixed-`H(Z,W)` binary determinant factor, or any claim of independent local exponents from different frames.

## Reproduced axiom audit

The exact-head build and final import-time axiom inspection both printed ONLY:

```text
[propext, Classical.choice, Quot.sound]
```

for `original_source_joint_normalized_lower_313`, `thin_production_normalized_upper_stronger_313`, and `totallyComplex_degree_two_classNumber_one_discriminant_bound_313`. **No `sorryAx`** appears in the checked theorem dependencies.

This is a valid **formal verification receipt**, not evidence that an independent reviewer has reconstructed every lemma or assessed novelty.

## Supersession, failures and branch boundaries

The predecessor `315^4` research statement was previously checked; this exact `313^4` formal result supersedes it **within the research branch**. The public `main` branch still advertises `322^4`.

All three failed Phase338 checks remain in [CI_FAILURES.md](../phase338/CI_FAILURES.md):

1. [44033778240](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44033778240): missing joint-prime-log import;
2. [44035309207](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44035309207): unqualified `Phase331` joint-log theorem;
3. [44038115535](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44038115535): unqualified `Phase331` joint odd-mass lemma.

The fourth run [44040958164](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44040958164) passed with source-head `745f47dff700...`, without weakening the theorem.

## Independent mathematical review still required

A human or separate implementation should reconstruct, not merely re-run, the following:

1. The exact coordinate-to-trace pairing and ordinary polynomial-jet semantics over `Z[sqrt(-D)]`.
2. The source positivity and Hadamard upper at the full `313^4` domain; no padded Gram substituted.
3. The joint unimodular binary valuation, coprimality with *all* selected odd prime powers, and no double-counted exponent.
4. The classical class-number-one prime inertness implication and its field-chart/discriminant transfer.
5. The numerical root-floor and log certificates and their endpoint guards.
6. The relation between this (large) bound and known classical results; do not advertise a new classification or a historically strongest absolute bound.

**Release rule:** keep `main` unchanged pending independent reconstruction; if a semantic gap is found, demote P to A/H/R as appropriate and retain the offending theorem and failure evidence in the ledger.
