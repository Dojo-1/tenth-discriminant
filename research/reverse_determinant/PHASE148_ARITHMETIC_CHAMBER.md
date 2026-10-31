# Phase148: arithmetic chamber, common support, exact Hadamard minimax

31 October 2026. **[M]** Exhaustive exact-integer finite tests with original ordinary Z jets, verified by GitHub Actions. **[P-paper]** Classical finite-field cokernel, Hermite image and diagonal Hadamard reasoning, not Lean formalized. **[H]** Parameter-uniform support theorem and stronger actual-field discriminant bound remain open. **[R]** Any claim that 2/3/5 always certify integral adequacy or that local metric savings directly imply a certified field bound remains retired.

**Source and reconstruction.** [Executable](phase148_arithmetic_chamber.py); inherits the entrywise original-Phase140-checked [Phase147 source](phase147_prime_adequacy.py). The unaltered ordinary partial Z derivatives of Z^r W^s hold W fixed. Every point contributes J=4 ordinary derivative slots, each with both integer real and imaginary coordinates. Rows run 0<=r<8, 0<=s<4 (32 rows). For the D-dependent positive trace metric, B=diag(2,2D,...). No Hasse/horizontal interpolation substitute.

The **same 21 integer observation points** form the ellipse Omega_D={(x,y):x^2+D*y^2<=25} for every D in the five-value chamber D={17,18,19,20,21}. We study the image M_D=im_Z E_Omega(D) and its finite relative group F_(Q,D)=M_D/im_Z E_Q(D), for each sampled subset Q. Using the certified Hermite basis H_D of M_D, C_(Q,D)=H_D^(-1) E_Q(D) is integral, and image equality is equivalent to HNF(C_(Q,D))=I_32. Its reduction ranks r_p(Q,D) are **necessary** for equality; every such support must have r_p=32 for every prime.

## A two-parameter arithmetic incompatibility

Exhaust all 203,490 eight-point subsets of this identical 21-point universe. Exactly **35,748** preserve rank 32 mod 2 *simultaneously for D=17 and D=18*. None preserves rank 32 mod 3 at D=18: the maximum is **30**. The exact rank-3 histogram for these 35,748 is 13:2, 17:194, 18:1082, 21:1812, 22:11074, 24:256, 25:2560, 26:14704, 28:608, 29:448, 30:3008. Fast GF(2)/GF(3) routines are cross-checked against independent generic finite-field elimination on deterministic samples.

Even the **pair** D17/D18 cannot share an eight-point full-integral-image support. This obstruction is not a cardinality change of the ellipse, and it is visible at small primes in two different arithmetic specializations. For all five D, 1,728 eight-point candidates pass the binary test simultaneously, and zero also pass all five ternary tests.

## A finite exact minimum support of nine

The explicit common support

Q_star = {(-2,-1),(-2,0),(-1,-1),(-1,0),(0,-1),(0,0),(1,-1),(1,0),(2,-1)}

has 9 points and **exact** HNF(C_(Q_star,D))=I_32 separately at D=17,18,19,20,21, with a checked nonzero odd square minor used as an admissible modular-HNF modulus in every case.

The 8-point exclusion and 9-point positive certificate prove the **minimum common support is exactly 9** both for the two-value chamber {17,18} and the full five-value chamber {17,18,19,20,21}. This is a verified finite statement, not a new parameter-uniform mathematical theorem.

## A second, independently optimized property

The original same-Gram trace diagonal for row (r,s) is precisely

g_(r,s)(Q,D)=2 sum_(x,y in Q) sum_(j=0..min(r,J-1))
  [(r)_falling_j]^2 (x^2+D*y^2)^(r+s-j).

The raw monomial Hadamard product U(Q,D)=product_(r,s) g_(r,s)(Q,D) is an **exact integer upper** for det G_Q(D), independent of the unknown inverse Gram. All exponents are nonnegative; hence each diagonal, and U, are monotone in positive D. The worst case across this chamber is U(Q,21).

Exhausting all 293,930 nine-point subsets gives **11,232** passing all five binary tests; **768** of those also pass all five ternary tests. The exact integer U(Q,21) was minimized over all 768 necessary-filter survivors. The **smallest** is attained by Q_star above, and Q_star passes exact integral HNF for all five values. Therefore Q_star is **globally minimax-optimal for this particular raw Hadamard upper among all image-preserving nine-point supports of this finite chamber**, not just a greedy winner. Among the modular-filter survivors there are **64 tied supports at that same minimum objective**; uniqueness or adequacy of all ties is not asserted. Changing the moving frame or the objective may change this optimum.

| D | log det(full Gram) | log det(Q_star Gram) | log raw upper(Q_star) |
|---:|---:|---:|---:|
| 17 | 524.339771 | 455.491642 | 578.300561 |
| 18 | 527.353309 | 459.527102 | 584.970724 |
| 19 | 530.285191 | 463.376450 | 591.369893 |
| 20 | 533.145815 | 467.057207 | 597.519724 |
| 21 | 535.941562 | 470.584426 | 603.439350 |

All determinants and Hadamard bounds are **exact integers**; natural logarithms are for display only. The upper remains much greater than the actual log determinant. No production cutoff improvement can be claimed from the finite support savings.

## Prime-primary counterworld: a second fixed support

For Q_bad={(-2,0),(-1,-1),(-1,0),(0,0),(0,1),(1,1),(5,0)}, the exact relative finite quotients have the following orders / nontrivial Smith factors under the **same** 21-point geometric support:

| D | Relative index | Nonunit Smith factors |
|---:|---:|---|
| 17 | 1377 | 3,3,3,51 |
| 18 | 2187 | 3,3,3,3,3,9 |
| 19 | 1 | none |
| 20 | 12960000 | 60,60,60,60 |
| 21 | 2401 | 7,7,7,7 |

Both the 7-primary failure at D21 and the 17-primary factor at D17 are visible. Since other factors, for example 3 at D20, need not divide D, **ramification-only explanations are insufficient**. These are exactly typed abelian quotient groups, not real spectral scores.

## Parameter geometry: theorem spine and limits

At every fixed sample point and derivative slot, each original integer coordinate is an integer polynomial in D. This follows from the multiplication rule (a,b)(c,e)=(ac-D*b*e,a*e+b*c) in Z[sqrt(-D)] and from the original falling factorials. Thus the raw matrices E_Q(D) lie in Mat(Z[D]) and obey E_Q(D+p^k)=E_Q(D) mod p^k for each fixed Q, prime p and k>=1. Note: D+p^k may be **outside** the sampling ellipse chamber; that identity is algebraic parameter transport only. It does **not** immediately imply identical relative cokernels because the full-image normalization H_D can change.

The next well-posed [H] target is a p-adic determinantal-chamber description of relative Smith invariants under parameter deformation, with explicit rank and index conditions, not a rhetorical identification of geometry with prime arithmetic. Beyond that: construct a deterministic arithmetic-adaptive support Q(D) valid for a meaningful unbounded number-field family, and prove an independent analytic upper on *exactly the same* Gram without querying its inverse. Test against the original production interpolation guard and prime-mass hypotheses before any public bound claim.

Prior mathematical ingredients belong to established arithmetic matroid and matroid-over-ring theory; see Fink and Moci, *Matroids over a ring*, JEMS 18 (2016), 681-731, DOI https://doi.org/10.4171/JEMS/600. The claimed contribution is the **source-specific bounded exact experiment** and its verifiable reconstruction, not global novelty of this algebra.

**Reproduce** from repo root using Python 3 and SymPy 1.14: run research/reverse_determinant/phase148_arithmetic_chamber.py. The branch-specific GitHub workflow also runs Phase147 regression and Phase148 exact tests. No new PR, no merge, no Lean theorem or field cutoff.
