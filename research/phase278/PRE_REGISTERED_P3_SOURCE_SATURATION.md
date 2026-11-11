# Phase278 — prospectively frozen primitive p3 saturation on original D283 trace Gram

**Pre-registration date:** 2026-11-11. This protocol is committed BEFORE writing the new high-precision program or seeing its results. Phases206–208 are earlier work; previously viewed p3 K=6 levels and p5 primitive-unit results are *known data*, not prospective predictions.

## Exact source and objective

The unchanged number field parameter D=283, rho=31, R=70, S=J=2, all 169 points in ellipsePairs 283 31 and all ordinary partial_Z^j derivatives, j=0,1, with conjugate W HELD FIXED during differentiation. Original rectangular E has 140 rows x 676 integer coordinate columns, with exact metric B=diag(2,566,2,566,...). No Hasse replacement, missing last jet, changed point set, changed Q, cherry-picked minor, or Euclidean B.

**Primary p=3 test:** inert (-283|3)=-1, with existing OLD unimodular Frobenius row F_(r,s)=Z^(r-3k) W^s (Z^3-W)^k and k=min(floor(r/3),1-s), so k is 0 or 1, old F3=67. Normalize these old rows once to C0=Delta_old^-1 U_old E. The next stage is a Smith reduction of C0 over Z/3^K with *tracked invertible row operations*; column operations can be used ONLY to identify pivot ranks/levels, NEVER to modify original metric B. The exact chosen precision is **K=18**, WITHOUT post-hoc escalation.

**Secondary negative control:** p=5, inert and identical original D283 E and B, old F5=65; run the earlier Phase206 K=6 normalization to reproduce its complete additional index 195, primitive H unit rank 140, det(H) mod5 = 3 and total v5(det original G)=520. The p5 result is PRIOR ART, not a new discovery.

## Test oracle and expected prefix

Prior p3 K=6 truncated Smith levels AFTER old Frobenius, as reported in Phase206:
{0:36, 1:9, 2:9, 4:36, 5:9, >=6:41}.
The new K=18 profile, when capped at 6, MUST reproduce these counts. This is a mandatory source/algorithm consistency check.

Output the complete K18 histogram, the exact second-index sum IF all levels <18, or its certified lower bound and number unresolved at >=18 otherwise. Record the row-operation matrix mod3 and verify invertibility. If all levels resolve, construct a primitive Cprim from U*C0 divided by 3^level (not from column-normalized A), assert rank(Cprim mod3)=140 by two structurally distinct rank computations, and compute Hprim=Cprim B Cprim^T mod3.

- Hprim full rank: primitive residual valuation is exactly zero, and v3(det G)=2*(67+index) at this frozen source.
- Hprim deficient rank: residual valuation is at least 140-rank(Hprim mod3); the exact valuation remains unresolved pending a separately preregistered higher-precision lift of Hprim.
- K18 unresolved levels: give only certified lower bounds; DO NOT infer primitive residual or exact determinant valuation.

## Adversarial controls and stopping conditions

1. Signed metric check: at p3, both B channel weights 2 and 566 are units. A naive Euclidean substitution Bflat=(2,2,...) is forbidden. Check a deterministic sample of signed exact integer ordinary jets against Phase204's independent oracle BEFORE normalization.
2. Column action negative: all elementary column operations used inside Smith elimination stay in the **internal rank algorithm**. Primitive rows are recovered exclusively as U*C0, with division by p^level verified before reduction. No full change-of-basis U on B is allowed (B is a column-domain pairing).
3. p5 primitive-unit negative check on the same E and B; p7 split is NOT assigned an inert Frobenius factor (Phase277 already fixed the exact p7 negative control).
4. Check that K18 prefix reduction reproduces the historic K6 histogram; K18 != K6 or mismatch terminates claim, no adaptive choice of new K after viewing output.
5. If Hprim has mod3 radical, verify its rank by two distinct elimination implementations; no single trial's first-layer radical is claimed as a uniform asymptotic exponent.
6. Only report a calculated arithmetic invariant relative to the **same source**; a universal extra conductor-scale R²S*logD statement remains H.

## Evidence and conjecture ladder

- P (classical): U E = Delta Cprim over Z_p with U row-invertible implies v_p(det G)=2 sum(levels)+v_p(det(Cprim B Cprim^T)), once old Frobenius exponents are included exactly once. A determinant of a positive rational Gram is assumed nonzero when interpreting exact valuation.
- M (once GitHub CI passes): K18 finite Smith histogram and local rank/det controls on frozen D283; p5 replay.
- H: an additional primitive residual p3 factor exists at D283 after full saturation; even if yes, a UNIFORM, *uncounted* growing prime mass for the original production family remains separately open.
- R: interpreting unsaturated C0 radical dim26/28 as new exponents (refuted by Phase277 counterexample and already completed p5 primitive-unit source).
- H/stop: whether the analytic Siegel-zero problem can ever benefit from new local prime mass requires a source-compatible uniform lower of order R²S logD, or a distinct changed analytic coefficient route. One finite D283 result does NOT settle it.

**Merge gate:** independent fresh CI run, actual exact implementation, no theorem/novelty overpromotion, and compatibility with merged Phase272–276. Independent source-to-field human review #50 for PR157 remains OPEN; this work does not address or waive it.
