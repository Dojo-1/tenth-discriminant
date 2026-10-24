# All nine positive cases, without assuming class number one

Lean now proves actual class number one for all nine fields Q(sqrt(-d)),
with d=1,2,3,7,11,19,43,67,163. Together with the complete checked sieve
below one million, this gives BOTH directions of the classification there.
The full upper interval remains open; see the precise range map at the end.

## The same bridge, in the other direction

Earlier, class number one made an ideal principal, and its generator's norm
forced a local residue obstruction. Here we start with local obstructions
and use geometry to prove class number one. No class-number hypothesis is
assumed in the positive proofs.

Minkowski's theorem gives every ideal class a nonzero integral ideal with
small norm. The actual discriminants are now known, so only these two
fixed bounds are needed:

| Radicands | Representative norm | Local norms ruled out |
| --- | --- | --- |
| 11,19 | less than 3 | 2 |
| 43,67,163 | less than 9 | 2,3,5,7 |

The bounds follow already from pi>3: 4*19<9*3^2 and 4*163<9*9^2.
The previous four cases 1,2,3,7 had representative norm below two.

## Why a polynomial test excludes an ideal norm

An ideal of prime norm p has a quotient ring with p elements. The pinned
library identifies that quotient with Fp. Therefore the half-integral
generator's image z must satisfy

    z^2 - z + (d+1)/4 = 0  in Fp.

If this equation has no root, there is no ideal of norm p. Lean checks
the required finite root-absence statements for the fixed cases and primes.
At p=2 this uses the integral polynomial directly, never division by two.
The order is identified with the actual full integer ring, not a proxy.

For 11 and 19 the representative's positive integer norm is below three.
Norm two is absent, so its norm is one, and its class is trivial.

## The norm-four ideal must not be discarded

For 43,67,163 there is one more issue: the small principal ideal (2) really
has norm four. We must allow it. Here is why no nonprincipal small ideal
survives.

Take a nonzero nonunit ideal I of norm at most eight. If it factored into two
nonunit ideals, both factors would have norm at least four: norms two and
three are absent. Their product would have norm at least sixteen, impossible.
Thus I is irreducible and hence prime as an ideal.

This uses unique factorization of IDEALS in the Dedekind ring of integers.
It does not assume unique factorization of elements or class number one,
and does not claim that these rings are norm-Euclidean.

Now O/I is a finite field, of prime characteristic p. Writing n for its
cardinality, p divides n, and p belongs to I. Hence (p) is contained in I,
so n divides norm((p))=p^2 in degree two. With 1<n<=8 and norms 2,3,5,7
excluded, the only possibility is n=4,p=2. The inclusion (2) subset I
and equal nonzero norms force I=(2). It is principal after all.

Thus every Minkowski representative is principal and every ideal class is
trivial. This supplies the remaining five positive proofs, including 163.

## Two controls that prevent overclaiming

At d=11 the polynomial has root zero modulo three. That is why its proof
uses the lower norm bound, not the uniform four-prime hypothesis. At d=23
it has root zero modulo two; this field has checked class number different
from one despite absolute discriminant <=163. A small discriminant alone
does not justify dropping the local hypotheses. Lean also checks norm((2))=4.

## What is now proved, and what is not

All statements concern positive squarefree radicands and the actual field.

| Radicand range | Current proof status |
| --- | --- |
| below 1000000 | class number one iff d is in the nine-element list |
| [1000000,700000000000) | complete exclusion certificate still missing |
| at least 700000000000 | class number different from one |

The nine positive proofs are complete. The full classification is not.
No cutoff improvement, novelty, independent human review or upstream claim.

## Source and verification map

- [SmallIdealClassNumber](../../lean/TenthDiscriminant/SmallIdealClassNumber.lean):
  quotient/norm bridge, small ideal principality and both Minkowski criteria.
- [RemainingPositiveClassNumber](../../lean/TenthDiscriminant/RemainingPositiveClassNumber.lean):
  all five applications, all-nine sufficiency, bounded iff and controls.
- [Protocol](PHASE33_PROTOCOL.md), committed before edits;
  [results](PHASE33_RESULTS.json), with preserved development failures.

From `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`, and
`lake env lean ../research/ender_radius_bridge/Phase33SignatureCheck.lean`.
Exact-head full pinned CI and actual theorem hypotheses must accompany publication.
