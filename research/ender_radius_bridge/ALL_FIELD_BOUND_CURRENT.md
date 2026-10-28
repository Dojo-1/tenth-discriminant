# One actual-field bound, now in the main library

For ANY imaginary quadratic number field K with at most two ideal classes,
the actual absolute field discriminant is below 2^52. If that discriminant
is odd, the sharper bound below2^50 holds. Above2^52, class number exceeds2.

[The human proof](ALL_FIELD_TWO_CLASS_GUIDE.md) explains why a constructed
chart preserves class number/discriminant and why the even chart retains
the factor four. Phase107 checked that proof standalone; Phase108 moves
all accepted statements/proofs and four controls unchanged into the main
library. The caller supplies neither a quadratic generator nor an isomorphism.

[Exact integration evidence](PHASE108_VERIFICATION.md) records module and
full builds, fresh dependency checks and whole-library audit. Earlier
standalone status in the Phase107 guide describes that earlier checkpoint.
External CI and independent human review of this addition remain open.
[PR37's cancelled CI](PR37_CI_LIMIT_RECEIPT.md) is preserved as a distinct
stopped run; no successful completion is inferred from its PASS log text.

The class-number-one cutoff stays50billion. This broader h<=2 bound is no
optimization of that cutoff, no novelty claim and no full classification.
