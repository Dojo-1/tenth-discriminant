# Phase294 — preregister the four-orbit / forty-dimensional residue boundary carrier

**Date: 2026-11-12, BEFORE Phase294 executable code or CI.** Source is stacked draft Phase293 #184 on Phase292 #183 on Phase291 #182; none merged. The user wants symmetry, higher-dimensional operators and genuine moving-frame transport while NEVER altering or double-counting the arithmetic lattice. This is a first *raw mod-p* source-support theorem target, NOT a statement about the p-saturated primitive pairing from Phase293 nor a tenth-discriminant field bound.

## Unchanged ORIGINAL sources and source-relative difference

Freeze original `research/phase206/source_probe.py` blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8` and Phase293-A original six-row moment oracle `research/phase293/moment_transport_remainder.py` blob `a114b5b7744ed67254caa98ef91c7f11d016d80a`.

Use D583 COMPLETE original Q383, R145/S=J5, all 725 original monomial labels (r,s), all five ORDINARY Z-jets with W fixed, and original trace metric diag(2,2D583) on real/imaginary channels. Comparison B is the FIRST725-row diagnostic from D587 with the exact same original Q383 and original B587; it is NOT the full D587 730-row number-field source. Let `phi:u587->alpha*u583` with `alpha=2 mod5`. The previously verified phase293 source identity is `G587(Q)≡G583(phi Q) mod5`; **the new raw Gram defect is**
```
Delta = G587(Q) - G583(Q)
      = G583(phi Q) - G583(Q) mod5.
```
This equality is on the *raw original monomial-jet ROW lattice*. Never divide by old Frobenius factors, source Smith levels, or call Delta an extra p5 valuation. Phase293-D already ruled out a very different *primitive* fixed-label evaluation square for the canonical `Y` map; do not rewrite that result.

## New algebraic prediction BEFORE coding [P-paper candidate]

Both Q and phi Q are conjugation/central-inversion symmetric mod5. Let `m_Q(x,y)` be the multiplicity of an F5-coordinate pair after reducing all 383 original points and `delta(x,y)=m_{phi Q}(x,y)-m_Q(x,y)` as an **INTEGER** signed measure, not just a set-theoretic difference. It has 104 units of transport mass, defined as half the L1 norm of the integer signed counts.

Original x-layer counts: for y=±1, x=-47..47 gives exactly 19 points PER x residue; for y=±2, x=-21..21 gives counts `{x0:9,x1:9,x2:8,x3:8,x4:9}`. Under phi mod5, y→2y permutes the four nonzero y residues. Thus `delta` is ±10 at x residues0,1,4, and ±11 at x residues2,3. **After mod5**, only eight individual residue coordinates survive: `x∈{2,3}`, `y∈{1,2,3,4}`, each with delta=+1 or -1 modulo5. These form exactly FOUR distinct quadratic-conjugate Frobenius orbits, represented by `q=(2,1),(2,2),(3,1),(3,2)` in `F25=F5[u]/(u²+583)`.

The original odd-prime trace metric is `B=diag(2,2*583)`; the signed support defect matrix of ALL 725 raw rows is

```
Delta mod5 = E4 * M40 * E4^T,
E4 : F5^725 -> F5^40  (rows are 725, 4 Frobenius reps * 5 jets * 2 value coords),
M40 : direct sum over reps q, jet j, of 4*delta(q)*diag(1,583 mod5).
```

The factor4 comes from the q and conjugate(q) contributions of the ORIGINAL metric, not a new Frobenius or Smith factor. Every delta(q)∈{+1,-1} is a nonzero mod5 unit and 583 mod5=3≠0, so M40 is nonsingular. Under inert p5, `w=z^5` for every residue z∈F25; because j<5, ordinary Z-jets of `Z^r W^s` at residue z coincide with ordinary j-jets of the single F5 polynomial `Z^(r+5s)`. The first 40 original rows `(r,0), r=0,...,39` give Hermite interpolation at the four degree-two irreducible conjugate pairs. Their distinct minimal quadratics each to power5 have total degree `4*2*5=40`; by CRT/Hermite interpolation the resulting 40x40 submatrix of E4 is nonsingular over F5.

**FROZEN PRE-CODE prediction:** `rank_F5(Delta on ALL 725 RAW original rows)=40`, and under the original row parity `(-1)^(r+s)` its ranks are **20 EVEN + 20 ODD**, with all cross-parity entries ZERO. This is not predicted from previous six-row rank5; it is a new full-row assertion and should be rejected if the exact source mismatch exposes a wrong assumption.

**Generalizable conditional lemma [P-paper target]:** for odd inert p, 1<=J<=p, distinct conjugate residue support defect with f Frobenius orbits each of nonzero delta modp, no nonzero delta at Fp-fixed points, original row family containing s=0 and r=0..(2Jf−1), the raw ordinary-jet trace Gram defect has rank EXACTLY `2Jf` over Fp. The local trace metric must be nondegenerate and the signed residue pairing diagonal in observation channels. This lemma says nothing about changes to p-saturated primitive H, which can magnify high-order source perturbations.

## Mandatory independent original-source tests and negative controls

1. Inspect frozen source blobs; assert D583/Q383/R145/S=J5, D587's actual full R146 is unchanged, original fields remain distinct. Produce integer signed residue counts independently from full original Q and phi Q; verify 104 transport mass, exactly 8 nonzero **mod5** residues and exactly 4 Frobenius conjugate orbit reps (2,1),(2,2),(3,1),(3,2), every pair has equal delta weight.
2. Build E4 for all 725 original row labels and all five ordinary jets *directly over F25* using mod5 complex-pair multiplication and original `fall(r,j)`, with metric M40 precisely **4 delta diag(1,D583)**. Assert rank(E4)=40, rank even=20 and rank odd=20. Verify s=0 rows r0..39 make an invertible square evaluation matrix, and that their reconstructed 40x40 Gram defect is nonsingular; verify off-parity zero.
3. Crosscheck the predicted E4 M40 E4^T on the six **Phase293-A** frozen original monomial labels [(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)] against TWO independent exact-integer original Gram implementations: `source_probe.gram(587,Q,J,labels)-source_probe.gram(583,Q,J,labels)` and `source_probe.gram(583,phi Q,J,labels)-source_probe.gram(583,Q,J,labels)` modulo5. Require the old six-row defect rank exactly5.
4. Include boundary controls: alpha=1 (no moved source) => signed defect zero and rank0. alpha=-2≡3 mod5 yields **the same** moved multiset because Q contains y and -y equally. A rectangular p5 residue-balanced support `Qrect={-21<=x<=21,-2<=y<=2}` has all transverse y layers equal width; alpha=2 simply permutes its y-residue multiset, so rank0. This distinguishes actual ellipse-wall geometry from formal field isometry.
5. Include a support rank-limit toy with a single Frobenius-conjugate pair, fixed nonzero delta±1, J=1 and source monomials 1,Z: predicted rank2 (test against exact nondegenerate trace channel). An original row family with too few r values must NOT be promoted to rank2. Do not claim complex/real positive semidefiniteness for signed delta.
6. **Precision debt**: if primitive source rows are obtained by dividing raw row combinations by p^(k+e), knowing a raw support identity only modp DOES NOT allow transporting it through arbitrary p-adic divisions. Explicitly record total old and secondary row exponents up to 4+6=10, so certifying a normalized relation modulo p³ from an actual raw relation may require p^13 source precision, conditional on compatible row operations. The Phase293-C primitive pairing isometry is independent of this raw defect rank; never count the raw 40 as valuation mass.
7. On any mismatch, preserve failure and demote the rank prediction rather than alter Q, rescaling, D, p, original derivative convention, row range or signed weights. Keep the PR DRAFT, no merging, root Lean and independent human source-to-field review #50/#51 remain separate.

Evidence governance: [P-paper] finite residue measure/CRT/Hermite proof conditional on assumptions; [M after exact CI] actual full original n725 mod5 rank40 and 20+20, 104→four-orbit compression, boundary/toy controls; [H] quantitative source-compatible integral lifts through p-adic saturation and uniform h1 discriminant theorem; [R] raw modulo5 defect rank is itself a primitive pairing corank or new p5 prime factor.
