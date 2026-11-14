# Phase301-C — preregister two-direction joint Schur obstruction on the SAME original final lattice

**2026-11-13, AFTER Phase301-A's 148/28 result and Phase301-B's explicit original 15-row dual witness, BEFORE Phase301-C code and measurement.** A third separate experiment, not a retroactive prediction of A/B. Same ORIGINAL D163 Q109/J1/R40 and fixed 176 source pairs, same frozen helper blobs and full original source metric. No Work mode, no merge, no change to field theorem/cutoff PR #157, no additional valuation factor.

## An exact two-direction order-of-attachment lemma [P-paper]

Take a fixed integral nonsingular original base Gram A over Z5 and TWO later original directions u,v whose cross columns both lie in image(A), so their actual projections to A are integral. After original integral orthogonal elimination the Gram of both residual directions is

```
 S=[[a,c],[c,b]],
 a=<u',u'>,
 b=<v',v'>,
 c=<u',v'>,
```

with u',v' orthogonal to A in the ORIGINAL trace metric. The final lattice is **independent of ordering of these two original generators**. But intermediate integral projection obstructions are:

```
 debt(u then v) = max(0, v5(a)-v5(c)),
 debt(v then u) = max(0, v5(b)-v5(c)).
```

If c=0, treat v5(c)=∞, giving both debts0. This follows from the integral first-stage splitting into `A⊕[a]` or `A⊕[b]`; the extra class is in the scalar Schur cokernel. Distinct a,b valuations can lead to **different** obstruction orders even though the final Gram and determinant are identical. This statement concerns source module extension steps; never turn the intermediate cokernel subgroup index into an extra determinant term. The determinant is `det A*(ab-c²)` in either order, while the two scalar Schur factorizations `a*(b-c²/a)` and `b*(a-c²/b)` telescope to the same value.

## Independent hostile positive-definite toy [P/M]

Use Phase301-A's previously pre-registered exact positive-definite original 4×4 toy:

```
 [[25,5,5,25],
  [5,10,10,5],
  [5,10,15,6],
  [25,5,6,100]].
```

With the first two rows as A and later u=row2, v=row3, BOTH u and v have integral projections into A. The source-independent 2×2 residual Gram is `[[5,1],[1,75]]`, positive definite, with v5(a)=1, v5(b)=2, v5(c)=0. Thus **u then v** has new order5 obstruction, **v then u** has order25 obstruction; check both with separate full Gram Smith computations (not merely from the scalar formula), and confirm full Gram determinant84,150 and its p5 valuation do NOT depend on row order. This is a valid counterworld to both 'projection integrality is order independent' and 'the obstruction group order can only ever be 5'.

## Original D163 J1 source test: the SAME 176 fixed pairs in BOTH directions

Use the identical `n=(13,18,22,25,33,34,38)`, later same-parity `s<t` from original `{n+2,n+4,...,39}` and unchanged original row module `L1=span(Z^0,...,Z^n)`. Exactly 176 pairs, with NO additional or adaptively chosen cases. Previously each later s,t projected integrally onto L1 over Z5 (43 certified first-later rows).

1. Freeze `research/phase301/joint_same_parity_census.py` blob `acd72002911b284bea6fda100435f552756c1532` and all its parent helper hashes. Reconstruct original D163 G40 by original source_probe exact moment AND 218-channel original E/B=diag(2,326) methods. Check all1600 entries, central parity 800 exact zeros and the known first seven single-obstruction classes at p16.
2. For each of the 43 later original directions, compute one actual original-basis integral projection T_r into L1 using the original Gram tracked Smith solver, and check ALL original residual equations modulo5^16. Reconstruct its actual corrected original observation row `E'_r=E_r−T_r^T E_L1`, verify all original old trace pairings0. Compute all residual norms `a,b` and pairings `c` independently from corrected original E rows and check them against Gram-algebra formulas, symmetric under swapping the two directions.
3. For all176 fixed `n,s,t`, compute BOTH scalar predictions above with valuations at p16, then independently compute each actual intermediate original Gram's Smith-image index: `L1 + Z^s → Z^t` and `L1 + Z^t → Z^s`. Require exact agreement, old Smith exponents fully uncensored at K16, residual norm valuations <16, and NO changes to original source or field/prime/jet.
4. Record full forward and reverse image-index histograms, per-n counts and a transition cross table `forward debt → reverse debt` (0,1,2,etc), and first asymmetric original source witness if any. Preserve all cases, including absence of asymmetry. The preceding Phase301-A forward histogram **{0:148,1:28}** is a fixed regression control; if it changes, STOP.
5. Verify the two orders have exactly the SAME original final (n+3)×(n+3) Gram up to an integral permutation and same full Smith profile and v5 determinant; choose at least one source witness with a nontrivial obstruction if any exists. This is algebraically immediate from permutation, but check source row labels and direct transformed Gram, not a fictitious new valuation.
6. The earlier original `F25^×` power24 residue identity and source parity remain contextual; neither proves the order-specific Z5 scalar residual. Do not extrapolate to maximal-order h1 sampler, high J or tenth-discriminant bound.

[Expected outcome deliberately unknown:] no prediction of source order-asymmetry counts or reverse obstruction exponents. The toy MUST show order5/order25 as a hostile independent check. Stop on any failed source/Smith/Schur correspondence. Keep all unmerged in DRAFT.

[P-paper] classical integral-split 2×2 Schur residual order law and determinant order-independence.
[M after CI] source-measured 176 bidirectional image coker comparisons, real original Gram/jet pairings and hostile toy.
[H] source-side p-adic mechanism of the 28 forward obstructions, whether actual h1 maximal-order or high-J sources behave similarly.
[R] false universal order-independent projection or adding intermediate coker indices to original full determinant valuations.
