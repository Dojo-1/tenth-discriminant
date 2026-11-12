# Phase290 — observed Noether–Smith wall, local radical depth, and higher-corank frontier

**12 November 2026. POST-RESULT mathematical ledger; AI-authored and not independently human-reviewed.** User-supplied historical source: Emmy Noether, *Ideal Theory in Rings*, §9 (modules) and §12 (integer-matrix elementary-divisor **classes**, distinct from general two-sided matrix ideals; D. Berlyne translation, arXiv:1401.2577). Current modern reference for module Fitting ideals: [Stacks Project Tag 07Z6](https://stacks.math.columbia.edu/tag/07Z6); for a simple-root p-adic Hensel statement: [Stacks Tag 04GE](https://stacks.math.columbia.edu/tag/04GE). These classical results are NOT new priority claims by this project, and Fitting-ideal terminology should not be retroactively attributed to Noether's precise §12 formulation.

## Universal source-wall algebra [P-paper; classical]

For unchanged original integer row lattice Z^n and nested original observation supports, `Eplus=[Eminus,C]` after a *column permutation*. Thus
`im Eminus ⊆ im Eplus` and the identity on Z^n induces an exact sequence

```
0 -> im(Eplus)/im(Eminus) -> coker(Eminus) -> coker(Eplus) -> 0.
```

At fixed row count, the determinantal/Fitting ideals of E can only enlarge under adding observation columns, and their p-local cokernel lengths (when finite) can only decrease. This is not a monotonicity law for the trace Gram.

For the original unchanged metric B_delta (2 and 2D), the exact **integer** wall presentation is
`W=[[Gminus,C Bdelta],[Bdelta C^T,-Bdelta]] = U diag(Gplus,-Bdelta) U^T`,
`U=[[I,-C],[0,I]] in GL_Z`.
Thus `coker W ≅ coker Gplus ⊕ coker Bdelta`, where the known metric factors are recorded ONCE, not added again as original-Gram valuation. No isomorphism of coker Gminus and coker Gplus follows. Real Loewner growth says nothing about p-local Gram Smith monotonicity. Fixed positive integral trace-weight-2 toys show p3 valuation 0->1 and 1->0 while evaluation coker remains zero.

C2 central inversion acts by P_(r,s)=(-1)^(r+s) on rows, and signed point exchange T_(j,q)=(-1)^j (j,-q) on observation channels: P E=E T, T B T^T=B. It yields an exact integral **row** parity block of G, distinct from the illegitimate binary **observation** projector (I±T)/2, which generally has index-two denominators. This is not a physical Noether conserved-current theorem, and the moving Gaussian or Schr toy of Phase287 remains separate.

## Four exact finite original-source certificates [M; self-authored CI]

Freeze original D563 rho51 R140 S=J5, all the original 700 row labels, Qfull359 and inner diagnostic Q285 and y=±2 DeltaQ74. **Numerical Smith work uses only the six preregistered original principal rows** [(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)] with all 5 ordinary Z jets and the unchanged signed real/imag coordinate trace metric diag(2,2D). Do not infer full n700 arithmetic from these six rows.

- [Phase290-A exact CI #43255011442](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43255011442): independent direct ordinary jets and source Phase206 mixed moments match on Qminus/DeltaQ/Qplus; Gplus=Gminus+Gdelta; p-local source rank and SIX-BY-SIX Smith gcd-all-minors are:
  
  | p | rank Eminus->Eplus (mod p) | v_p(det Gminus)->v_p(det Gplus) | new Smith exponents |
  |---|---|---|---|
  | 2 | 5->5 | 11->11 | (1,1,2,2,2,3) |
  | 3 | 6->6 | 0->0 | (0,0,0,0,0,0) |
  | 5 | 6->6 | 0->2 | (0,0,0,0,0,2) |
  | 7 | 6->6 | 0->1 | (0,0,0,0,0,1) |
  | 563 | 6->6 | 0->0 | (0,0,0,0,0,0) |

  A **separate 26x26** two-point new-orbit wall verifies the exact unimodular congruence, signed symmetry and known B torsion v2(B)=20,v563(B)=10; those are NOT full 700-row facts. The primitive pairing becomes singular mod5/7 even though E remains full row rank at those primes.

- [Phase290-B modular lift #43255880299](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43255880299): p5 primitive null vector v=(0,2,0,0,0,1) has odd row parity and lifts mod25 but not125 (left-obstruction 1 mod5); p7 v=(4,0,1,0,1,0) has even row parity and cannot lift mod49 (left-obstruction 1 mod7). A completely separate 720-term Leibniz determinant polynomial `f(t)=det(Gminus+t DeltaG)` has f'(1)=4 mod5 and 5 mod7, both p-units. This DOES NOT mean a double polynomial root mod5; f is simple mod5 and mod7 at t=1.

- [Phase290-C 37-orbit gradient #43256792781](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43256792781): the 74 outer points decompose into 37 C2 inversion pairs. True micro-walls occur at `rho² >= 4D+x²` for |x|=0..18, not all at once. At the ALL-ONE original source, exactly 37/37 orbit partial derivatives are nonzero mod5, 32/37 mod7. Their integer adjugate gradients sum EXACTLY to independent f'(1). This is a 37-dimensional formal parameter family of observation weightings; only all-one is the original full source.

- [Phase290-D rank-one local oracle #43257354606](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43257354606): since rank(G modp)=5, `adj(G)=gamma vv^T modp` with gamma5=4 and gamma7=5 for the frozen kernel normalizations. For ALL 37 new orbits, source-local computation WITHOUT local Grams or an orbit adjugate checks
  `partial_orbit det(G)=gamma*(E_orbit^T v)^T B_orbit(E_orbit^T v) modp`.
  It reproduces exactly the 37/37 p5 and 32/37 p7 witnesses. Thus on **corank-one** Gram singularities, one primitive modular null vector and local original jets suffice to identify active transverse directions. A nonzero evaluation vector can still have zero self-pairing over Fp, so do not assert the converse without the quadratic scalar test.

**Prime-local wall geometry [P-paper conditional on measured f']:** By the simple-root Hensel lemma there is a unique root tau_p in Zp reducing to 1 of the formal one-variable f(t). Since f'(1) is a p-unit, Taylor expansion at tau_p gives `v_p(f(1))=v_p(1-tau_p)`. Therefore the formal p5 root satisfies tau_5≡1 mod25 but NOT mod125; the p7 root satisfies tau_7≡1 mod7 but NOT mod49. These are formal weighting parameters, NOT extra original arithmetic sources, physical adiabatic motion, or continuous GL_Z gauges.

## Higher-corank mathematical bridge [P-paper, classical derivation]

For any field k and symmetric n×n matrix A with **corank r**, choose a basis P with
`P^T A P = diag(M,0_r)`, M nonsingular. For any symmetric perturbation H, write `P^T H P = [[H11,H12],[H21,H22]]`. Schur expansion over the formal power series ring k[[t]] gives

```
det(P)^2 det(A+tH)
 = det(M+tH11) * det(t H22 - t^2 H21*(M+tH11)^(-1)*H12)
 = t^r * det(M)*det(H22) + O(t^(r+1)).
```

The leading order is AT LEAST r; it is **exactly r iff** the perturbation restricted to the kernel, H22, is nonsingular. For r=1 this recovers our gamma*(v^T H v) local test (up to fixed basis normalization). For r>1 the correct higher-dimensional carrier is the FULL radical space `ker(A modp)` and the observable is the determinant of its orbit-restricted Gram, **not** a one-coordinate scalar or full expensive adjugate. The formula applies algebraically in characteristic 2 as well, but p2 observation parity splitting is a separate integral-lattice issue.

## Claim status and next discriminating action

[P-paper] cokernel exact sequence, unimodular wall, Smith/Fitting, corank-r leading term, simple-root Hensel. [M] finite six-row original source, four exact CI runs and their explicit guards. [H] a scalable full n700 primitive kernel/radical extraction with ALL original high derivatives and a uniform production-D orbit-response bound, beyond already-counted Frobenius/trace-metric factors. [R] p-local valuation monotonicity under PSD wall addition; interpreting 5² as a double t-root; treating high-dimensional weighted corrections as independent arithmetic factors.

**Next smallest test:** on an ACTUAL full-original D563 row module at a chosen odd p, compute its primitive restricted pairing corank **after** the previously certified Frobenius extraction (count those indices once). If corank r=1, use the exact null-vector orbit test; if r>1, test the r-dimensional restricted orbit pairing determinant. Only then compare across increasing original D and prove a uniform result if evidence allows it. Do NOT merge or promote a new actual-field cutoff without independent human source-to-field review (#50) and comparator gate (#51). PR157 remains draft/unmodified.
