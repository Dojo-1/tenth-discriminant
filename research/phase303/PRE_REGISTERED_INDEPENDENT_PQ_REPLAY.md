# Phase303-F — preregister second exact algebra engine and independent 5-adic Smith for the maximal source

**2026-11-13, AFTER Phase303 A–E exact-source results but BEFORE F code/results.** This is an explicitly POST-result adversarial reproduction, not a blind prediction. Preserve previous code, source, norm cutoff and Smith profiles. Stacked DRAFT, no Work mode, merge or new field theorem.

## Independent arithmetic representation

Do NOT calculate the new Gram in `(a,b)` ω coordinates with `ω²=ω−41` (the A–E implementation). Instead represent every maximal-order algebraic integer by an integral pair `(p,q)` with `z=(p+q sqrt(-163))/2`, `p≡q (mod2)`. Its norm is `(p²+163q²)/4`; the source is ALL parity-compatible pairs with `p²+163q²≤4*441=1764`. Enumerate `q=-3..3, p=-44..44` with explicit proof that points outside the bounds cannot occur. The EVEN-q source must have 109 points, the FULL source 225, including 116 odd-q points. Do not reuse the original Phase303 `qmax()` enumeration to generate the source.

Define multiplication **independently**:
```
(p,q)*(r,s)=((p*r−163*q*s)/2, (p*s+q*r)/2),
conjugate(p,q)=(p,−q),
Trace(z conj w)=(p_z*p_w+163*q_z*q_w)/2.
```
All divisions by2 must be EXACT integers for parity-compatible pairs. Build powers z^r for r=0..39 as integer pairs. Compute ALL1600 integer Gram entries for both even-q and full-q norm-ball samples, with NO use of `ω²=ω−41`, the A-source's trace formula, or its high_precision_smith implementation. Match all1600 big integer cells to the pinned Phase303-A reference implementation **only AFTER** independently constructing the matrix.

## Independent local Smith algorithm

Implement a completely separate **pure Python** DVR row/column reduction modulo `5^16`, choosing a pivot with minimal p5 valuation at each submatrix step, then clearing its column and row via modular inverses of the pivot's unit. Record the entire 40-element elementary divisor list, not merely the determinant sum. Require all grades strictly <16. Compare the independent result with the previously measured expected profiles ONLY as post-result replay:
```
 old-even {0:15,2:8,3:7,4:10}, v5(det)=77;
 full     {0:25,2:15},          v5(det)=30.
```
Also verify rank mod5 from the number of zero elementary grades (15/25). Use a small hostile matrix with nontrivial off-diagonal pivot and a known Smith profile, and a matrix with a zero p-adic pivot to test the reduction rather than accidentally assuming diagonal Gram. Do not import numpy or any p16 Smith solver in the **independent** arithmetic core; the comparison-only boundary may import Phase303 source to compare integer matrices after the standalone result is constructed.

**Stop rules:** any sample count discrepancy, nonintegral division, 1600 integer cell mismatch, unexpectedly censored p16 Smith, or separate Smith profile mismatch. Preserve failures and do not change p,D,rho, R, support or expected prior profiles. Even a success remains *same AI author with different implementation*, NOT external independent proof or an improved tenth-discriminant bound.

[P] exact (p,q)-basis norm/multiplication/trace identities and Smith DVR elementary operations; [M after CI] alternate-engine original maximal source and Smith profiles; [H] uniform number field class-one p-adic theorem; [R] treating same-model reimplementation as independent peer review.
