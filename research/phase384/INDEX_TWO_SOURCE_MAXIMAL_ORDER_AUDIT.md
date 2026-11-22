# Phase384 — Original trace lattice and the maximal quadratic order: the index-two seam

**22 November 2026. Research draft, independently evaluated algebra and bounded tests.**

## Objective and frozen source

Professor Tao's tenth-discriminant/Siegel-zero challenge remains the governing objective. In the *original* Dojo-1/Tenth-Discriminant source, `IntegerTraceGram.lean` represents each sample as the pair `(x,y)` for `x+y sqrt(-D)`; the complex hermitian trace pairing is exactly

`integerPairTrace D a b = 2*(a.x*b.x+D*a.y*b.y)`.

Its ordinary `Z` derivatives hold the conjugate `W` factor fixed. The source lattice is `Z[sqrt(-D)]`; for squarefree positive `D % 4 = 3` the maximal ring of integers is `O_K = Z[(1+sqrt(-D))/2]`. The two must NOT be identified without the index-two bridge.

The following is elementary integer arithmetic, not a new class-number bound or a replacement for the existing Lean mainline field chart.

## Exact chart and ring isomorphism away from the index

Write `beta=sqrt(-D)`, `omega=(1+beta)/2`, `c=(D+1)/4`. Then `omega^2=omega-c`. For integer source coordinates `(x,y)`, set

`T(x,y)=(x-y,2*y)`.

This is the exact coordinate identity `x+y beta=(x-y)+2y omega`. In matrices (column coordinates),

```
T = [[1,-1],[0,2]], det(T)=2.
B_max = [[2,1],[1,2c]]
B_src = [[2,0],[0,2D]]
T^T B_max T = B_src.
det(B_max)=D; det(B_src)=4D.
```

These **positive conjugate-trace** determinants are not the signed field discriminant `disc(K)=-D`, and they are not the determinant of the full rectangular ordinary-jet trace Gram. Do not multiply the huge jet determinant by 4 without deriving a complete rank/dimension-dependent basis change; this 2x2 identity cannot license that.

The multiplication in maximal basis is

`(a,b)*(u,v)=(a*u-c*b*v, a*v+b*u+b*v)`.

The source multiplication `(x,y)*(u,v)=(x*u-D*y*v,x*v+y*u)` satisfies `T(srcMul(p,q))=maxMul(Tp,Tq)`. The same T preserves the original source conjugate trace exactly, as the 2x2 congruence predicts.

Over `Z/pZ`, T is invertible for **odd** prime p (2 is a unit), but has rank one at p=2. Equivalently the element `omega=(0,1)` in maximal coordinates has no integral preimage `(x,y)`, since `2y=1` would be required. The original 2-primary arithmetic must therefore be audited separately; it does not follow by blindly reusing the odd-prime maximal-order chart.

## Source evidence and controlled claims

- **Source inspected:** `lean/TenthDiscriminant/IntegerTraceGram.lean` on main, including `pairMul`, `integerDerivativeRow`, `integerPairTrace` and `integerRectangularTraceGram`; `Arithmetic.lean`, `OddPrimeTwo.lean`, `SameGramLower322.lean`, `ThinUpper322.lean`, and `ActualField322.lean`.
- **P, elementary algebra:** the coordinate map, multiplication/trace compatibility, determinant identity and odd-prime invertibility follow by direct calculation.
- **M, bounded independent reference:** `order_index_two_oracle.py` checked **42** squarefree positive `D<200` in the odd chart, **26,250** ordered integer pair-pair combinations over coordinates -2..2, matrix congruence and reductions mod 2,3,5,7,11,13. Passed in the local execution environment.
- **H until CI:** new `lean/TenthDiscriminant/OrderIndexTwoTraceBridge.lean`, source-typed into the original `pairMul` and `integerPairTrace`, with exact proof and axiom-print targets. It must pass exact-head full-root Lean build before promotion. No independent mathematical referee is claimed.
- **H, decisive original theorem seam:** transport the actual odd-prime **Frobenius ordinary-jet divisibility** from the maximal order into the selected source lattice, accounting for its integral row operations. The index-two lemma is necessary context but is **not a proof** of `originalGram_binary_oddMass_unconditional` or its exponent `2 valuationWeight`.
- **H, independent arithmetic upper:** the padded ellipse is only a cardinality majorant for the same source thin-ellipse `G_D`; never replace `det G_{thin}` with `det G_{padded}`.
- **P relative to existing encoding:** the original mainline 322^4 scalar collision has positive rational margin 2853/500000000 under its two encoded Gram inequalities. This margin does not validate their semantic antecedents independently.

**Reviewer's critical question:** For a fixed inert odd prime p and one ordinary-Z derivative row, is the row-divisibility factor proven for the source coordinate lattice `Z[beta]` using the same sample set and unmodified `W` convention? The invertibility of T mod p justifies transfer of *coordinate spaces*, not automatic equality of the entire high-jet Smith normal form. Independent reconstruction or a reproducible counterexample here is more valuable than another numerical threshold.

**Stop rule:** do not advertise a smaller unconditional field discriminant bound until the source-typed (p)-adic row-divisor argument and its integral index-two interface have received independent review. Keep mainline classification, Phase383 two-prime draft and human review issue #50 separate. No change to Masullo, Dirichlet RH, Selberg or Ihara theorems is inferred.
