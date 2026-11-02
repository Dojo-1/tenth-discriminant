# Phase177 — the real-place upper on the *same* original thin Gram

**Evidence H until pinned Lean exact-head checks pass.** This is the
first new-domain analytic upper determinant theorem target; it is not
a field-discriminant theorem by itself.

We freeze the **entire observation-to-Gram map**:

[
Q_{m thin}(D)=mathrm{ellipsePairs}(D,lceil(11/25)D^{3/4}ceil),
quad R(D)=lfloor D/4floor,quad S(D)=lfloor R(D)/25floor,
]
[
G_{m thin}=mathrm{integerRectangularTraceGram}
(Q_{m thin},D,S,R,S).
]

All rows are the same original ordinary-(Z)-jet rows. All
weights are the existing (2,2D) trace pairing. No rational
rescaling or transfer from (det G_{m old}) is admitted.

The proposed theorem is

[
rac{logdet G_{m thin}}{R^2S}
le rac45log D-rac{1849}{2000}
qquad(Dge377^4).
]

## Proof decomposition and evidence

1. **P** (merged Phase170): the unchanged original thin-Q node set
passes the interpolation count; in particular (G_{m thin}>0)
can be obtained from the generic original integer-Gram lemma.
2. **H** (Phase174, individually verified, combined CI pending):
(Q_{m thin}subseteq Q_{m old}), so its node count is at
most the **existing** padded majorant (N_{m old}>0).
This is only a count inequality and NEVER compares determinants.
3. **H** (Phase171 rechecked): the original thin radius is
(le(8/9)ho_{m old}), and lies in ([10,R)).
4. **P** (existing generic statement): the unchanged
`TightRadialSaving.normalized_integer_upper_tight`
reapplies the full ordinary-jet Gram Hadamard inequality to
(Q_{m thin}), with the old majorant only as (n), and
supplies the original (-23/2000) real-place saving.
5. **P** (existing generic statement): the original
`Tuned.upperB_tenth_saving` contributes another (1/10)
from contracting the radius without changing rows or support.
6. **H** (Phase176): the original padded scalar expression
itself admits the same old (-813/1000) normalized upper
at (Dge377^4). Phase176 rederives that input using
the true (log Dge23.7), not the false (log Dge24).

The arithmetic gives
(-813/1000-1/10-23/2000=-1849/2000).
The numerical equality is **not enough** to promote the
theorem: the exact source/field transport must also survive.

## Kill condition

Reject if any old (Dge450^4) theorem is called with a new
domain, if a different Gram is substituted, or if exact-head
Lean/axiom/source/negative controls fail.

Even if the candidate compiles, the same-Gram normalized
prime+binary lower must be assembled under its actual field
hypotheses, the logarithmic strict gap applied on the **identical
positive determinant**, and the full number-field chart handled.

Independent mathematical review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50)
is separate from CI. See [#82](https://github.com/Dojo-1/tenth-discriminant/issues/82).
