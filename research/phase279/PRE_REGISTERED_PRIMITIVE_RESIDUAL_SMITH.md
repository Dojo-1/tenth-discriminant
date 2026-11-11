# Phase279 — pre-registration: primitive residual Smith depth, original D283/p3

**Date:** 2026-11-11. This note is committed BEFORE the first Phase279 higher-residual computation. It follows the genuinely new Phase278 measured result, not falsely labeled prospective:
- K18 normalized source after old p3 Frobenius has exact index 527, histogram {0:36,1:9,2:9,4:36,5:9,6:9,8:31,9:1}.
- Original-source primitive evaluation rank = 140/140 mod3.
- Primitive restricted trace pairing Hprim has rank 124/140 mod3, hence residual v3(det Hprim) >=16.
- Previous p5 same-source saturated pairing is a p-unit with index195 and v5(det original G)=520.

## Fixed primary test and precision

Freeze D=283,rho31,R70,S=J2, full original ellipse Q169, original signed integer-coordinate trace B=(2,566), original ordinary Z derivatives j=0,1 with W held fixed and all 676 columns. Keep old Frobenius exponent F3=67 and the **complete Phase278 K=18** Smith row normalization.

Reconstruct the primitive Cprim modulo **3^L with L=6** (fixed), solely via tracked INVERTIBLE row operations U on the original C0, then dividing row i by 3^a_i, where a_i is the complete K18 Smith exponent. Internal Smith column operations are permitted for pivot discovery, but NEVER applied to B or used to reconstruct a source-changed primitive pairing. K18 - max(a_i)=9 >= L=6: the known source precision is sufficient for this fixed truncated residual experiment.

Compute Hprim=Cprim B Cprim^T modulo 3^6, check symmetry and its previously recorded rank modulo3 =124. Compute the complete Smith histogram of Hprim modulo 3^6 with tracked invertible row operations and elementary unimodular column operations in the *internal Smith algorithm*.

- If EVERY residual Smith exponent <6, infer the EXACT finite residual valuation v3(det Hprim)=sum_i b_i and therefore exact finite v3(det original G)=2*(67+527)+sum b_i. This follows from the p-adic unit determinant of row change, not from an asserted literal integer determinant equality.
- If any residual Smith factor is still >=6, report the capped histogram, the lower bound v3(det Hprim)>=sum_i min(b_i,6), and **stop**. Do not infer an exact determinant valuation or raise precision in this phase.
- Full primitive C rank140 and H rank124 are mandatory input controls; any contradiction invalidates the test.

## Matched controls

1. Replay the previously verified Phase278 p5 K6 primitive-unit result on the same original D283 source within the CI job; do not treat its replay as a new discovery.
2. Recompute the K18 source Smith levels independently of the Phase278 helper's returned Cmod3 and require equal p3 histogram.
3. Test original trace weights B=(2,566) with signed coordinate channels; note B and fake flat B=(2,2) look equal mod3 but differ modulo9. This is a failure mode for shallow modular comparisons.
4. Transform Hprim by a deterministic unitriangular integral row shear P=I+E_01; residual Smith histogram must remain unchanged. This is the moving-frame invariance gate.
5. Cross-check a fixed selection of primitive H entries against a distinct explicit weighted dot-product calculation. No reliance on any p-adic determinant from a surrogate Hasse or Euclidean Gram.
6. The actual old Frobenius term 67 and the evaluation-index 527 have already been counted once. The new residual valuation, if identified, is a **separate** p-adic summand—not "extra" if an earlier published bound already implicitly included it. No uniform asymptotic gain is asserted.

## Stop rule and meaning

Outcome statuses: EXACT_FINITE if all factors resolve; TRUNCATED_LOWER if any remain at cap; FAIL if mismatched source/ranks/metric/frame invariance. No adaptive threshold adjustment, no "Siegel zeroes excluded" claim.

This is a bounded *falsifiable* research increment within Phase278's existing draft PR. It does not create a new class-number-one field, improve the field cutoff, or discharge human semantic review #50 of analytic PR #157. Extending to a second D or a growing prime family would require a separately preregistered and source-typed programme.
