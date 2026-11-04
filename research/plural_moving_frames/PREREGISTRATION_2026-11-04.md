# Preregistration: plural arithmetic–geometric obstructions under moving frames

Date: 2026-11-04 (Europe/Madrid). Status: **H (research programme)** with separate **P (elementary deductions)**, **M (finite tests)** and **R (retired overstatements)**. Authorship/provenance: user's seed is plural algebraic and geometric observables with evolving moving frames; the formal carrier, conjecture ladder, controls and tests below were developed in AI-assisted dialogue. No external mathematical endorsement or priority claim.

## Frozen baseline and noninterference

The control is the original ordinary-Z-jet, W-held-fixed, integer-pair trace Gram in Dojo-1/tenth-discriminant:
- Q_thin(D) = ellipsePairs D (Tuned.thinRadius D);
- rows (r,s) in the original R-by-S rectangle, J=S, R=floor(D/4), S=floor(R/25);
- integer trace form B_D((a,b),(c,d))=2(ac+Dbd);
- G_D=integerRectangularTraceGram Q_thin D S R S; norm N(D)=R*S*R (the existing comparisonScale, verify its definition rather than replacing it by conjecture);
- original odd class-one inert-prime argument, original binary factor, unchanged actual-field return.

Source exact field theorem at research branch research/phase200-same-gram-field322, commit 1356c77e12b7d1da259faefaa11d78e40e36a381: focused 322^4 field run 41721077426 succeeded on 2026-11-03. This is **P relative to encoding**; not a source-semantic audit and not a mainline claim at preregistration. Frozen 323^4 mainline predecessor at dc7e19ebefe2aecb0f2644b2ccd2b42203200a55. Do not change the current endpoint construction, primes or proofs in this exploratory branch. Issue #50 independent semantic review remains open.

## Carriers, typed maps, and information that must not be collapsed

For fixed D>0, integers J,R,S>=1, n=R*S, and finite Q subset Z^2, let E(Q) be the original integer ordinary-jet observation matrix and G(Q)=E(Q) B_D E(Q)^T in Mat_n(Z). When G(Q)>0 as a real symmetric form:

**Arithmetic profile:** delta_k(G) is the nonnegative gcd of all k-by-k minors, k=1,...,n; delta_0=1. It is a determinantal divisor / Smith-invariant profile. The p-adic profile is a_{p,k}=v_p(delta_k), for delta_k>0. delta_n=|det G|. This is *not* a collection of independently defined arbitrary matrices.

**Geometric profile:** ordered eigenvalues lambda_1>=...>=lambda_n>0, principal-minor values, and elementary symmetric polynomials. The determinant is only their product. The continuous geometric moving frame U(t) belongs to GL_n(R), but a lattice-preserving frame U_k belongs to GL_n(Z). Do not assume a nonconstant smooth path in GL_n(Z): it is discrete.

**Compatibility relation:** R_D consists only of pairs of profiles induced by an *actual same-source integer Gram*. An obstruction can be (A_D x B_D) intersect R_D = empty; neither profile must be scalar. Any cross-profile comparison must be typed with a proved transformation or bound. For varying D, n(D) varies; no naive common-dimensional smooth bundle or untyped differential in D. Work in fixed-size charts or a discrete groupoid with explicit partial maps and remainders.

**Observation transport:** Q subset Q' induces G(Q')-G(Q)>=0 in PSD order for fixed D,J,R,S. If G(Q)>0, then det G(Q')>=det G(Q). It does NOT imply v_p(det G(Q'))>=v_p(det G(Q)). Keep the exact small counterworld below.

**Integral row transport:** U in GL_n(Z) maps G to U G U^T; all delta_k stay unchanged by Cauchy–Binet / unimodular invertibility. A general U in GL_n(R) does not preserve these integer invariants.

## P: an exact new-to-this-project consequence of the existing row factorization

Assume p prime, e_i>=0 integers, integral U with det U=+/-1, integral K, and U G U^T = diag(p^{e_i}) K diag(p^{e_i}). For each 1<=k<=n set

    tau_k = min over I subset {1,...,n}, |I|=k, of sum_{i in I} e_i

(the sum of the k smallest exponents, with multiplicity).

Then **p^{2 tau_k} divides delta_k(G)**.

Proof outline: each k-by-k minor of diag(p^{e_i}) K diag(p^{e_i}) factors as p^{sum_{i in I}e_i+sum_{j in J}e_j} times an integer minor of K. This is divisible by p^{2 tau_k}. Cauchy–Binet expresses minors of U G U^T as integer linear combinations of minors of G, and the inverse integral unimodular U^{-1} gives the converse containment of determinantal ideals. At k=n, tau_n=sum e_i and this recovers the already encoded p^{2F(p)} determinant factor; at k<n it is a stronger *profile statement*, not automatically a stronger field result.

For several distinct primes, each admitting its own U_p and exponent family, the product over p of p^{2 tau_k(p)} divides delta_k(G) by coprimality. **Do not** add the binary component without its own specific row-exponent derivation.

**Geometric comparison (fixed G positive definite):**

    product_p p^{2 tau_k(p)} <= delta_k(G)
                                 <= min_{|I|=k} det G[I,I]
                                 <= min_{|I|=k} product_{i in I} G[i,i].

The first inequality assumes known nonzero positive delta_k (e.g. G>0). The second uses divisibility of each positive integral principal minor and the third is Hadamard for principal minors. This yields plural order-k sandwiches. It can be weak/trivial for small k because tau_k may vanish.

**Caution:** Some profile inequalities may follow from existing scalar information or be too coarse numerically. A claim of improved cutoff requires exact arithmetic/geometric estimates at the same source, no manufactured independence of minors and no appeal to apparent frame dynamics.

## H ladder and registered falsifiers

H0 (feasibility): The whole k-profile can be reconstructed from existing prime-row identities without altering Q or the derivative convention. Acceptance: an exact pilot and, separately, a Lean lemma with all assumptions explicit. Refutation: a counterexample showing the alleged integral row-factor premise or determinantal-ideal invariance fails.

H1 (mathematical utility, unproved): For some 1<=k<n (likely k close to n) and original thin source, the order-k arithmetic profile lower and geometric principal-minor upper establish an incompatible inequality in a regime not excluded by the existing scalar determinant envelope. Acceptance: concrete fixed D or a uniform D-range with exact rational certificates, including prime exponents, positivity, bounds and control comparison. Weakening/retirement: all tested k are trivial or uniformly dominated by the scalar baseline.

H2 (moving frames, unproved practical gain): Admissible discrete integral row frames, continuous real observation frames with corrected determinant distortion, or changes of Q with explicit PSD / information-loss remainder reveal a profile obstruction not expressible by the *current scalar bounds*. Acceptance: explicit typed maps plus a strict numerically certified new obstruction. Falsifier: only coordinate artifacts, integrality losses or transformed constraints identical to the existing scalar inequality.

No originality claim is registered. Determinantal divisors/Smith normal form, Cauchy–Binet, Hadamard, spectral calculus and moving-frame correction are classical. Novelty versus the original challenge is **not checked**. This is a proposed application and falsification study.

## Small exact tests fixed before computation

T1. Counterworld for false valuation monotonicity, J=R/2=S=1 as appropriate and rows [1,Z] (R=2,S=1,J=1), Q1={(1,0),(4,0)}, Q2=Q1 union {(2,0)}. Direct original trace Gram expected G1=[[4,10],[10,34]], det=36 and G2=[[6,14],[14,42]], det=56, so v_3 drops 2 to 0 despite Q1 subset Q2. These Q are not asserted to satisfy the imaginary quadratic class-one/inertness assumptions.

T2. Positive definite 3x3 K=[[2,1,0],[1,2,1],[0,1,2]], p=3, exponents e=[0,1,2], Lambda=diag(1,3,9), U=[[1,1,0],[0,1,1],[0,0,1]] unimodular. Build G=U^{-1} Lambda K Lambda (U^{-1})^T. Check det G = det(K)*3^6; profile delta_k invariant under U; p^{2 tau_k}|delta_k for k=1,2,3, with tau=[0,1,3]. Inspect whether k=2 yields genuinely new arithmetic information over k=3 alone.

T3. Tiny rectangular p=3 row exponent pilot at R=4,S=2, e_{r,s}=min(floor(r/3), S-1-s). Only (r,s)=(3,0) has exponent 1; tau_k=0 for k<8. This negative control predicts the proper partial-minor lower is trivial at small ranks. If any implementation outputs a stronger k<8 lower from these exponents alone, reject it.

T4. Nonintegral moving frame U(t)=diag(exp(t),exp(-t)) on G=I_2. det stays 1; eigenvalues change. Integral determinantal-divisor profile is **undefined off the integer lattice**, not invariant under the real frame. Any claim that the change of spectrum is intrinsic without correcting the frame must be retired.

## Evidence gates, stop rule and next sequence

1. Commit this preregistration before executing T1–T4; keep test results in separate commits so prediction and observation can be distinguished.
2. Run the exact finite pilot without relying on floating-point approximations; record successful and failed tests as M, not as a proof of general statements.
3. Extract or implement the general partial-minor divisibility lemma in an isolated Lean module if feasible; do not integrate into production root until it independently compiles and passes axiom audit.
4. Test whether the k-profile is nontrivial and yields a *strict advantage* over the current scalar certificate. If no discriminating candidate emerges in the first exact pilots and one analytic comparison, mark H1/H2 **unresolved or weak**, not a claimed new result.
5. Separately finish the original 322 field line: add exact root import, full-root lake build, source correspondence, axiom audit, negative controls, peer-style check of odd/even maximal-order return. Mainline promotion only after whole-root CI and with issue #50 still open for independent mathematical semantics.

## Research governance and remainders

P means mathematically proved relative to stated axioms or exact Lean checked scope; M means finite exact computation; H means conjectural research extension; S means interpretation; R means refuted variant. The independent reconstruction of field theory and ordinary jet arithmetic remains R_sem. Frame cross-regime ambiguity remains R_transport. Missing Lean declarations remain R_formal. Full-range arithmetic/geometry advantage remains R_emp.

We will prefer sharper mathematics over decorative higher geometry. No auxiliary primes, replacement Gram, silent support change, Hasse-derivative substitution, or speculative claim of novelty is allowed in this preregistered track.
