# Granules / empirical Z+ / exact certificates: round 1

Frozen production target: 791ebf4815d8eb4be5da3b01527ca7f0877b6d0e.
This is an additive research experiment, not a modification of the determinant witness.

## Registered before execution

- Object: fixed-size derivative Sylvester matrices over Q[W]. Discover a rational W=t at which the determinant is nonzero. Such a witness certifies nonzero determinant for that CONCRETE polynomial, not the universal irreducible-factor theorem.
- Families: generic affine coefficients, leading-degree loss, high contact at a center, a vertical factor at a center, globally repeated factors, and W-constant squarefree polynomials.
- Train: four cases per family, seed 2026102201. Test: sixteen cases per family, seed 2026102202. No seed or rule tuning after results. Same-author generated tasks, not an externally held-out benchmark.
- Candidate evaluations: -3,-2,-1,0,1,2,3. Shared shuffled candidate order for each paired case.
- Policies: fixed order; crisp leading/constant coefficient guard; fuzzy membership-only; learned mixture of empirical local success distributions. All see the same cheap specialization coefficients; only the learned mixture uses the training labels. Report training cost separately.
- Granules: near leading-degree loss, near zero constant coefficient, regular. Membership uses exact rational coefficient ratios. These are routing descriptors, not truth degrees. Coordinate dependence is acknowledged; scalar rescaling must leave routing unchanged.
- Primary metric: paired mean penalized number of determinant probes on 96 test tasks; unsuccessful search is assigned budget+1=8, reported separately from actual 7 calls. Also report failures, per-family costs, and wall time descriptively.
- Promotion: no advantage claim unless learned mixture is strictly better than both crisp and membership-only baselines on the registered mean, with no extra failures and no false certificates. A finite win is not population superiority. Zero or losing gain retires only the advantage claim for this suite.
- Every returned witness is rechecked by SymPy's independently implemented resultant with the exact global degree, unmodified degree through specialization, and parity sign accounted for.
- A Z+ summary is a fuzzy event on operational cost with the empirical PMF over the DECLARED finite test population; not a probability that a theorem is true. Weighted training distributions are design-weighted empirical measures, not probabilities inferred from membership alone.
- Blending bounds requires common target, domain, units, normalization, nonnegative weights, normalized sum, and valid enclosure for every positively weighted certificate. Zero membership cannot erase uncovered cases.
- Attacks: wrong target, negative or zero-total weights, inconsistent interval, forged payload, zero specialization, overpadding, exact zero vs near-zero, repeated factor, reordering, duplicate provenance, scalar rescaling, and high-confidence/zero-result attempts.
- Stop: no new discriminant cutoff, no new global nonvanishing claim, no production changes, no merge. Record failures. Lean only reported checked after actual CI.
