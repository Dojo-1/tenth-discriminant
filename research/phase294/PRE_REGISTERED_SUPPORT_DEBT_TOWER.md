# Phase294 — preregister the p-adic tower of observation-support debt

**2026-11-12, BEFORE Phase294 code/results.** This is a new DRAFT stacked above Phase293 PR #184 (on #183→#182). The previous AI-authored CI is completely green but independent mathematical/source-to-field review #50/#51 remains outstanding. No Work, no merge, no edits to actual-field PR #157 or original helpers.

## Fixed source, local field map, and typed objects

Retain unchanged original `research/phase206/source_probe.py` blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6` and original ordinary `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`.

- ORIGINAL D583: `rho53,R145,S=J5,Q383` with y counts `{-2:43,-1:95,0:107,1:95,2:43}`, full original 725 rows.
- ORIGINAL D587: `rho53,R146,S=J5,Q383`, full original 730 rows; its FIRST725-row diagnostic has no authority as a replacement of the actual field's 730 rows.
- Fix odd inert p5. The **local ring isometry** `phi: A_587 -> A_583` sends the imaginary coordinate `u_587 -> alpha*u_583` with `alpha^2*583=587` in Z5 and `alpha≡2 (mod5)`. Earlier Phase293 verified `alpha=2,17,67 mod 5,25,125`, and its source moment defect rank5 mod5 and full primitive pairing isometries mod125.
- For EACH k=1,...,13 let `m=5^k`, `A_k` the multiset of ORIGINAL Q583 residues (x,y) modm, and `B_k` the multiset of **formally transformed** ORIGINAL Q587 points `(x,alpha_k*y)` modm, with `alpha_k^2*583=587 modm`. These are **observation labels**, not a new quadratic integer ring or a new source Gram.

Define the exact *support-debt filtration* (a count, NOT a determinant valuation)
```
 d_k = |Q| - sum_z min(m_Ak(z),m_Bk(z))
     = (1/2) sum_z |m_Ak(z)-m_Bk(z)|,
```
where `m_Ak,m_Bk` are residue multiplicities. `|Q|=383`. The first expression is the maximum common submultiset; therefore `d_k` is the MINIMUM number of points to ADD ON EACH SIDE to obtain equal residue multisets at depth k (common envelope has size 383+d_k), and the minimum unmatched points per side in any residue-preserving partial matching. For source with original J5 and both real/imag channels, the unmatched points correspond to `2*J*d_k` original coordinate channels PER SIDE, which is a label count and **NOT an independent rank / determinant factor**.

## Prospective predictions and kill conditions

- k1: d1=104, matched=279 (retrospective Phase293 result). Recompute it as a different exact multiplicity oracle and an independent explicit bipartite **maximum matching**, NOT just geometric literal-intersection count.
- k2: alpha≡17 mod25. For original nonzero y∈{±1,±2}, 17*y mod25 is in {8,9,16,17}, disjoint from original nonzero y residues {1,2,23,24}. Exactly the 107 y0 points survive as residues mod25. Consequently d2=383−107=276. For ALL k≥2, reduction mod25 makes any nonzero-y match impossible; the 107 exact y0 points still match. **Paper-level prediction d_k=276 for 2≤k≤13**; in fact the proof extends to all k≥2, for this fixed original support and root branch. Test exact Hensel alpha_k for all 13 levels. The second admissible root `−alpha` gives the same debt for every level because Q is invariant under y→−y.
- Monotonicity `d_{k+1}≥d_k` comes from forgetting the last residue digit: any match mod p^(k+1) is a match mod p^k. It is a theorem only of **label/point matching**, not monotonicity of p-adic Gram determinant valuation or Schur increments.
- Counterworlds: alpha=+1 and alpha=−1 preserve the whole symmetric ORIGINAL Q at every k and have d_k=0. A thin support with only y=0 has debt zero despite the nontrivial alpha. A 5×5 equally weighted full residue-square toy `Q_toy={(x,y):-2≤x,y≤2}` has **d1=0** for alpha2 (y mod5 permutes all five residues), but **d2=20** (only five y0 points match) with alpha17. This kills the inference "first-layer support match implies deep support compatibility".

## Raw original-jet **moment-localization** target

Freeze six original row labels `[(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)]`, original all five ordinary ∂_Z jets **holding W fixed**, trace weights per original (j,q) `diag(2,2D)`, *full* ORIGINAL Q383. At k=1,2,3, the quadratic ring isometry gives the exact modulo-m statement
```
 G_587(Q) = G_583(phi Q) (mod m).
```
For any explicit **maximum** matching `M_k` of Q and phi(Q) by full pair residue modulo m, ordinary derivative evaluation at matched points is congruent modulo m (integer polynomial coefficients), so their local trace-Gram summands cancel. With `U_A=Q\M_k`, `U_B=phi(Q)\M_k` of cardinalities d_k each, the EXACT *matrix* congruence is
```
 [G_587(Q) - G_583(Q)] mod m
  = [sum_(q in U_B) K_583(q) - sum_(q in U_A) K_583(q)] mod m,
 K_D(q) = sum_(j=0)^(J-1) E_(j,q) diag(2,2D) E_(j,q)^T.
```
This is a FULL 6×6 congruence, not merely one scalar moment. Verify it with two different routines: independent Phase206 `gram(D,Q,J,labels)` for left and a new modular direct original-jet local summand for right. Keep all 36 entries and exhibit rank mod5 of the original difference; do not infer positive semidefiniteness or v_p determinant factors from a SIGNED sum of unmatched moments. Test k1,k2,k3; matching lists/digests deterministic and correct.

## Essential negative control: **divided** rows require deeper point precision

For the already used Frobenius-divided integer polynomial `f(Z,W)=(Z^5-W)/5`, restricting to the real axis W=Z and ORIGINAL sampled points 0 and 5 gives:
```
 f(0,0)=0;  f(5,5)=(5^5−5)/5=624 ≡ 4 mod5,
```
even though 0≡5 mod5. Both points belong to Q383 at y0. Thus **mod5 point matching suffices for RAW original integer jets modulo5 but DOES NOT suffice for p-divided/saturated primitive row evaluation modulo5**. This is a mathematically essential counterworld, not a code bug. General sufficient precision rule: if raw integer polynomial jets at two points match modulo p^(a+ell) and both are divisible by p^a, dividing by p^a preserves congruence modulo p^ell. With max OLD k=4 and measured max secondary e=6 in the matched n725 p5 K9 source, a conservative uniform bound for primitive precision ell=3 is matching original point coordinates mod p^(4+6+3)=p^13. Test k13 support debt (276), but do NOT claim that k13 is necessary for every individual divided row; or that any congruence of raw values implies a congruence of arbitrary normalized rows without denominators accounted.

## Scope / stop conditions

STOP on an incorrect Hensel root, exact Q counts, k1/k2/13 debt, optimal matching discrepancy, toy, raw six-row moment localization, conjugation or trace metric drift, factor double count, or divided-row negative control. Retain any failed CI, do not fit a favorable `k`, D, prime, source or labels after result. A positive exact source localization does NOT prove a uniform p-adic valuation inequality or the tenth discriminant.

[P-paper] residue-multiset optimal matching and monotone filtration; 25-adic transverse-layer obstruction; polynomial congruence and division precision; raw moment localization.
[M after exact CI] 13-depth finite support-debt tower, maximum-matching certificates and six-row original matrix localization.
[H] any source-compatible primitive evaluation transport after permitted geometric support enlargement, or uniform class-number-one valuation bound.
[R] promoting d_k to independent determinant mass; assuming mod5 matching transports already-divided Frobenius rows; treating a formally enlarged support as the original field source.
