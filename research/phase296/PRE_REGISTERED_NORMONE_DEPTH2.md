# Phase296-B — preregister full norm-one affine transporter at p²=25

**13 Nov 2026. Registered AFTER successful Phase296-A [CI #43373033299](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373033299), BEFORE B implementation or measured outcomes.** Phase296-A was preregistered at commit `cbe92c33`; the initial CI run failed on an incorrectly strict bound for NONMAXIMAL y0 multiplicities (21, not 19), fixed minimally at `d47255a3` without modifying the theorem. The successful full 1200-element F25 exhaustive search produced: min d=3 for all affine-semilinear maps (best slopes norm4, nonisometric); min d=64 for norm-one multipliers with ANY translations; min d=3 for F5-coefficient affine maps; min d=104 for norm-one AND base-F5 coefficient maps. No affine-semilinear map exactly matches Q at p5; the two unique residue sites of multiplicity22 give an elementary independent proof.

The new question [H until measured] is **how much of the 64-point best norm-one repair survives the second p-adic digit**, not whether norm-one affine exact isometry can suddenly emerge at deeper precision (impossible by reduction mod5).

## Fixed source and exhaustive search group

Original FULL D583 R145/S=J5/Q383 and FULL D587 R146/S=J5/Q383 (not the 725-row diagnostic), unchanged original Phase206 `params`; no original support or polynomial row-lattice edits. Work in `A_2=(Z/25)[u]/(u²+583)`, ring multiplication `u²=-583 mod25`. The fixed local field isometry `phi:u587→17*u583` satisfies `583*17²=587 mod25`.

Enumerate **EVERY** norm-one scalar `a=a0+a1 u` with `a0,a1∈Z/25` and `a*bar a≡1 mod25`; the expected exact count (Hensel lift of F25 kernel) is **30**. Enumerate every `b∈A_2` (625 values) and both `epsilon∈{identity,Galois}`. Thus exactly **30*625*2=37,500** triples. They act on the ORIGINAL D587 residue multiset by `g(z)=a*conj^epsilon(phi(z))+b` before comparison to literal original D583 Q. This norm-one criterion preserves the norm of DIFFERENCES under the slope, but arbitrary nonzero b is not a linear trace pairing isometry on values or automatically an original-source transport. Keep that scope explicit.

Independently implement F25/F625 coordinates and a per-residue multiplicity matching engine different from Phase296-A's candidate-by-candidate Counter transform (e.g. precomputed shifted support and Counter support intersection), then cross-check at least every best candidate and five fixed adversarial candidates against the slower Counter/sorted-list oracle. Do not use a random sample as exhaustive evidence.

**Frozen predictions before B:**
- norm-one root count30, candidate count37500 and both Galois/central inversion counterparts available.
- For every candidate, equality modulo25 implies equality modulo5, so `d25(g)>=64` because Phase296-A exhaustively proved the minimum norm-one d5=64.
- There can be NO exact support equivalence at mod25.
- **No prediction** of the exact minimum d25, its slope, translation, or multiplicity. Report all best ties and an exact distribution of 37,500 debts. Record whether every near-best mod5 norm-one map necessarily loses many more matches at mod25; preserve a surprise if not.

Optional conditional source restrictions: norm-one AND b REAL ∈Z/25 requires 30*25*2=1500 candidates; norm-one and REAL slope a∈Z/25 imposes a=±1 mod25 and has 2*625*2=2500 candidates; both norm-one a real and b real has 2*25*2=100 candidates. Report separate minima with explicit cardinalities; these are not interchangeable with the full 37,500.

## Independent controls and caveats

- Confirm the full original Q y counts and `alpha=17 mod25`, the exact root equation, norm-one cardinality, symmetry under conjugation and inversion, and the original Phase296-A script/blob unchanged.
- Positive same-field identity/inversion/conjugation support symmetries yield all 383 matches; zero translation is not implicitly a general local norm-one solution between DIFFERENT D fields.
- The broad F5-linear escape `(x,y)→(x,alpha^{-1} y)` on common chart still makes samples match **as coordinates** but is NOT an A_2-algebra automorphism or trace isometry. Do not count it as a norm-one affine candidate.
- The base-field original polynomial row lattice sees only coefficients in Z/25, and the source metric/jet derivative imposes separate compatibility, so even a small d25 in this broad norm-one-translated category proves NOTHING about the full original arithmetic sampler.
- The Phase294 divided Frobenius source counterexample remains: p-adically close points need extra digits after division by old k and secondary e. Do NOT use d25 as an extra p5 determinant factor or prove class number one bound.
- Stop if any discrepancy with previous norm-one d5>=64, root count, source geometry, independent best-candidate verification, or signed field norm. Do not increase search scope or change D/p to fit a desired minimum post hoc.

[P-paper] reduction mod25→mod5 implies nondecreasing matching debt for fixed p-adic lifts; unit norm subgroup count and preserving norm of differences under multiplication.
[M after focused CI] exhaustive 37,500-element p25 norm-one affine-semilinear matching minima and distribution.
[H] any larger permissible original row/jet transport at higher p-adic depth and uniform h1 field argument.
[R] calling norm-one affine WITH translations a trace-metric linear isometry, or treating support matching counts as Gram valuation savings.
