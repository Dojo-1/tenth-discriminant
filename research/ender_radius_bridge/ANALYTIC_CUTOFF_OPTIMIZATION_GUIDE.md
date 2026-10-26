# A smaller analytic cutoff from a sharper floor bound

## What changed

The new direct analytic theorem states: for positive squarefree d, actual
class number one of the canonical Q(sqrt(-d)) forces both d and its actual
absolute field discriminant below200000000000. Its public names end in
`radicand_bound_200b` and `discriminant_bound_200b` in
[OptimizedAnalyticCutoff.lean](../../lean/TenthDiscriminant/OptimizedAnalyticCutoff.lean).
Local targeted acceptance, whole-library checks and exact publication-head
CI are separate evidence stages; consult the final PR verification record.

This improves the analytic threshold from700 billion to200 billion, a
factor3.5. It is not the classification consequence d<=163 recycled as an
analytic argument. The new proof must pass its own compiled input check,
excluding the classification, positive-case theorem, finite certificates
and old public cutoff. Independent human review remains open.

## The insight: do not pay for unnecessary rounding loss

Keep exactly the existing auxiliary family

    R=floor(D/4), S=floor(R/20), rho=ceil((11/20)*D^(3/4)).

The same integer Gram determinant, ordinary derivatives, prime constants,
radius and upper-error terms remain in use. Nothing in the frozen Ender
campaign or original finite certificate is modified.

The old uniform proof used R>=D/5, hence logR>=logD-1.61. For large D,
floor rounding loses at most one, not a fifth of D. The checked refinement
is249D<=1000R for D>=1000. An exact rational logarithm certificate gives
log(1000/249)<=1.4, so logR>=logD-1.4.

That small local improvement survives the normalization T=R^2*S:

    old lower: L/T >= 0.999997*u-5.845,
    new lower: L/T >= 0.999997*u-5.635,
    same upper: U/T <= (13/16)*u-0.7965,  u=logD.

These are rational constants, not floating measurements. At u=26 the
new lower exceeds the upper by0.036422. The slope difference is positive,
so the separation persists for every larger u. The new comparison fails
at u=25; the old lower still fails at26. Both controls are retained.

The endpoint D>=200000000000 supplies u>=26 directly:
200000000000=2^12*5^11, a checked log5>=1.609 and the existing log2 lower
bound suffice. No high-precision numerical cutoff hypothesis is assumed.

## Why the scalar crossing is not the whole proof

Every dimensional, floor/ceiling, chosen-radius, positivity and upper-error
guard is rechecked on the enlarged domain. In particular t=D^(1/4)>=300
still holds; so do rho<R, the point-count bound and all correction bounds.
Strict inertness still comes from D=3 mod4, not a rounded endpoint.
The actual positive integer determinant would have to satisfy L<=U,
contradicting the separated envelopes.

The even fundamental chart is handled by the existing prime-two norm
argument. It forces d=1 or2 under class number one. The explicit field
equivalence and actual discriminant identity supply both public bounds;
there is no field-identification or numerical premise left to assume.

## Scope and verification

The first registered target build passed in129.0500323 seconds, peak
2919235584 bytes, within600 seconds/8192MB. No repair or alternate cutoff
was tried. The original700-billion public cutoff statements and full finite
interval remain intact. Low-level helper domains are strengthened where
their guards now hold down to200 billion.

The [Phase38 provenance map](PROOF_INPUT_GUIDE.md) remains a frozen audit of
its earlier proof head; it is not automatically transferred to changed
mathematical sources. Phase39 supplies a new compiled input-exclusion and
axiom check, followed by full pinned CI. The final record must distinguish
completed local checks from pending publication-head CI.

This is a modest improvement within the same credited method, not a novelty
or optimality claim. Much smaller thresholds in the dated prior-art note
have not been re-reviewed here. Systematic comparison, independent semantic
review, upstream review and human-authored external reporting remain open.
