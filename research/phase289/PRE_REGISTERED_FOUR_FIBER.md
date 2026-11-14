# Phase289 — preregistered four-fiber Noether/Fischer coarsening on the ORIGINAL source

**12 November 2026; registered before Phase289 code or execution.** This is a new *finite-source exact* analytic upper experiment, not a new p-adic divisor or a uniform tenth-discriminant cutoff. The human-directed research step is to seek a genuinely stronger determinant upper on the SAME original integer trace Gram after Phase288's integral transverse transport proved no new Smith mass. The geometric frame is subordinate to source integrity.

## Source, exact prior baseline and provenance

Immutable helper blobs:
- `research/phase206/source_probe.py`: `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`;
- `research/phase204/ordinary_jet_filtration.py`: `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`.

Use ORIGINAL centered ellipse `Q_D` and all original monomial rows `Z^r W^s`, **ordinary** Z-jets (W held fixed) for every j<J, original signed integer-coordinate trace metric `diag(2,2D)` for each (j,q). No new maximal-order half coset, dyadic Gaussian weights, reoptimized source or omitted jets. D283 has (rho31,R70,S=J2,Q169,n140); D403 has (rho40,R100,S=J4,Q219,n400). Both are FINITE stress tests, not class-number-one hypotheses.

Phase206 already defines radial fibers `I_d={(r,s):r-s=d}` and parity-matched, consecutive two-fiber pairs `(d,d+2)`. Phase207 [prior result] measured a D403 normalized finite pair saving, with a rigorous threshold-layer-cake certificate `L_pairs>=251 ln2` relative to `V_rad`. Phase206's matching is **already counted** and MUST NOT be claimed again.

## Fixed nested partition, chosen without inspecting new gains

For each parity h=0,1, sort all available fiber labels d in range(1-S,R) with d mod2=h. First form EXACTLY the Phase206 adjacent two-fiber pairs in that sequence. Next group consecutive TWO such pairs into a FOUR-fiber block `(d,d+2,d+4,d+6)`, leaving a last unmatched pair and/or singleton unchanged. Never move a fiber between parity strata, never pair nonadjacent fibers based on observed gains, never reorder after seeing results.

Expected **combinatorial** counts (predicted directly from R,S, not empirical gains):
- D283: 35 baseline fiber pairs, 17 four-fiber blocks, one leftover two-fiber pair, one singleton, all 140 original rows covered exactly once.
- D403: 51 baseline fiber pairs, 25 four-fiber blocks, one leftover two-fiber pair, one singleton, all 400 original rows covered exactly once.

Let `V_pairs` be the product of principal determinants over the Phase206 pairs/singletons, and `V_four` the analogous product over the new four-fiber groups and leftovers, always on original G. For any 4-block with first adjacent pair A, second B and cross C, exact Schur/Fischer gives
`0<det(G_four)=det(A)*det(B-C^T*A^{-1}*C) <= det(A)*det(B)`.
Strict iff C != 0, assuming SPD. All groups are in a fixed parity, so the Noether involution is respected. Therefore
`0<det G <= V_four <= V_pairs <= V_rad`.
Do not confuse this with the identity `det G=det G_even*det G_odd`: coarsening to all parity rows would be a tautological full-determinant calculation, not a practical analytic estimate.

## Independent, computable per-group lower certificate

For each 4-fiber block, inspect the ORIGINAL cross entries C in fixed lexicographic order and take the FIRST nonzero entry `c=G_ij` if any. Write `u=G_ii`, `v=G_jj`, `q=c^2/(uv)`. SPD ensures 0<q<1; a canonical correlation argument gives

`det G_four/(det A det B) <= 1-q`, or the integer-only equivalent
`det G_four * u*v <= det A*det B * (u*v-c^2)`.

This permits a *source-computable*, non-oracle bound even if no full quartet determinant is evaluated: `log(V_pairs/V_four)>=sum -log(1-q)>=sum q`. Validate the stronger exact Schur/Fischer ratio separately using fraction-free Bareiss.

The **primary new exact metric** is a strict dyadic gain in full-source block-product ratio, not a fitted float:
For each quartet, let `k_i>=0` be the largest integer satisfying `2^k_i * det G_four < det A det B` (k_i=0 when the ratio is close to one). Sum `K=sum k_i`; then `V_pairs >= 2^K V_four`, strictly if any cross C is nonzero. Report K as an exact integer and optional decimal estimates as *illustrations*, not a new class-number theorem. Require at least ONE strict nonzero C and ONE positive k_i across each D source; if these fail, report a legitimate negative result without changing the pre-registration.

The D403 **prior** threshold certificate `log V_rad-log V_pairs >=251 ln2` can then combine with the new source-exact K, as long as the nested pair partition is checked to be IDENTICAL to Phase206. Thus `log det G<= log V_rad-(251+K)ln2` is a finite D403 source upper, not a production-scale uniform inequality. It is not legitimate to add K a second time to the old Phase207 estimate.

## Moving-moving frame and typed evidence

On each positive quartet block G=[A C; C^T B], define a real/rational continuous row-frame shear
`F_t=[[I,0],[-t*C^T*A^{-1},I]]`, `0<=t<=1`.
It has determinant one, and
`F_t G F_t^T=[[A,(1-t)C],[(1-t)C^T, B-t(2-t)C^T*A^{-1}C]]`.
At t=1, the old first-pair and the conditioned second-pair become orthogonal. The end-frame Schur residual is B-C^T A^{-1} C; the determinant stays identical for every t. The moving frame is real, generally **not** in GL(Z); do NOT transport p-local Smith invariants through it. The Phase288 integral stabilizations and their original trace-Gram remain unmodified.

For the exact finite source, reconstruct one frozen first quartet via a separate ordinary-jet weighted sum and verify this shear at t in {0,1/2,1}. This is a classical congruence, **not** a quantum adiabatic theorem; an adiabatic claim needs a separate generator and spectral gap.

## Falsifiers / negative controls

1. Freeze source blobs, D parameters and full original Q. Derive the row labels directly, verify the partition covers all RS labels exactly once, and the baseline pair set equals Phase206's deterministic matching.
2. For EVERY four-fiber group compute the exact Gram via original `source_probe.gram` (which independently checks the mixed-moment formula), compute exact A,B and quartet det by fraction-free Bareiss, and assert positivity, Fischer bound and witness `q` inequality, including the first nonzero cross entry. Never replace B or drop any j.
3. Verify the witness cross entry with a SECOND original ordinary-jet oracle from Phase204, using the ORIGINAL full point set and original (2,2D) weights.
4. Check the real/rational shear identity at 0,1/2,1 for one first eligible quartet using `fractions.Fraction`, no floating interpolation, and exact determinant invariance. Distinguish this real gauge from integer GL_Z. A naive wrong Schur sign/control must fail.
5. Retain a symmetry negative case: one even and one odd original row have exact zero cross entry under central inversion, so no strict pair saving can be claimed there.
6. Report exact dyadic K, number of strict quartets, and total original row coverage at D283 and D403. Kill any extrapolation to uniform normalized savings from these two samples alone; retain the D283 hostile shallow-spectrum observations from Phase207.
7. Stop on any source mismatch, changed partition, missing positive determinant, failed integer certificate, nonzero opposite-parity cross, wrong shear, or false old/new gain accounting.

**Evidence types**: [P-paper] classical Schur/Fischer and nested partition inequalities; [M only after exact-head CI] frozen D283/D403 quartet savings and per-block witnesses; [H] a uniform source-computable production-scale improvement `Omega(R²S)` over the already-certified real-place envelope; [R] re-counting Phase206 pair gain or claiming integer covariance for real shears. Keep D=403 analytic-only; PR157/issue #50 human semantic field theorem gates independent. Require focused CI + whole-root Lean + Markdown + human source review before any merge.
