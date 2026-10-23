# Why an inert prime divides the trace-Gram determinant many times

**Status (23 October 2026): human-checkable proof, not an end-to-end Lean
theorem.** This reconstructs the valuation input stated in
[`ledger/ender.txt`](../../ledger/ender.txt); it makes no novelty claim.
It concerns the *existing* integer trace-Gram matrix, not a replacement
determinant. The remaining Lean and class-number/analytic links are named
below.

## Proposition

Let `D>0`, let `p` be an odd prime for which `X²+D` is irreducible over
`F_p`, and let `Q` be any finite set of pairs of integers representing
`z=x+y√(-D)`. Form the integer trace-Gram matrix `G` using the
rectangular rows `Z^r W^s` (`r<R`, `s<S`), ordinary derivatives in `Z`
of orders `j<J` with `W` fixed, and the repository's trace pairing
`2(ac+Dbd)` on coordinate pairs. Then

`p^(2F(p)) | det G`, with

`F(p) = Σ_(r<R) Σ_(t<S) min(⌊r/p⌋,t)`.

The claim allows repeated residues of distinct integer sample pairs:
the original set `Q` is summed before reduction. It does not require
`G` to be positive or nonzero. For the global argument, nonzero is a
*separate* real/geometry obligation.

## 1. The one local identity

In `A=F_p[T]/(T²+D)`, irreducibility makes `A` a field of `p²`
elements. Frobenius `a↦a^p` fixes `F_p` and cannot fix `T`: otherwise
`T` would be in `F_p`, contradicting irreducibility. It permutes the
two roots `T` and `-T` of `X²+D`, hence `T^p=-T`. Thus, for every
integer pair `z=x+yT`, including the reduction of every sample,

`z^p = x^p+y^p T^p = x-yT = bar(z)` in `A`.

Equivalently, both integer coordinates of `z^p-bar(z)` are divisible
by `p`. This implication uses the selected pair lattice; it does not
assert that the pair lattice is the full ring of integers. In Ender's
odd fundamental-discriminant setting the pair order has index `2` in
the maximal order, so an odd inert prime gives this irreducibility.
For a nonfundamental `D`, inertness in the field alone need not suffice
if `p` divides the conductor; the stated irreducibility hypothesis is
the exact local requirement.

Put `H(Z,W)=Z^p-W`. At `(z,bar z)`, the preceding identity gives a
factor `p` in both coordinates when `j=0`. For `1≤j≤p`, the ordinary
`Z`-derivative is

`∂_Z^j H = p(p-1)…(p-j+1) Z^(p-j)`, which has an integer coefficient
divisible by `p`. For `j>p`, it is zero. Therefore **every** sampled
jet of `H` is coordinatewise divisible by `p`; the derivative of `W`
is zero because `W` is held fixed. This includes arbitrarily large
`J`.

## 2. A basis change that stays inside the rectangle

For each original row `(r,s)`, set

`k_(r,s) = min(⌊r/p⌋, S-1-s)` and
`B_(r,s) = Z^(r-p*k) W^s H(Z,W)^k`.

The binomial expansion is

`B_(r,s) = Σ_(i=0)^k (-1)^i binom(k,i) Z^(r-p*i) W^(s+i)`.

Every term lies in the original rectangle: `r-p*i≥0` and
`s+i≤s+k<S`. The `i=0` term is precisely `Z^r W^s` with coefficient
one; every other term has strictly smaller `Z`-degree. Order the rows
by `r`, then `s`. The integer transition matrix `U` is unitriangular,
so `det U=1`. This is the key local-to-global move: the prime-dependent
row operation is *unimodular*, so it does not change the integer
determinant.

The ordinary higher Leibniz rule differentiates `H^k` by distributing
the derivative order among its `k` factors. Each derivative of each
factor has both coordinates divisible by `p` at a sample. Every term
therefore lies in `p^k` times the pair lattice, even after multiplying
by derivatives of `Z^(r-p*k)W^s`. Hence every sampled jet of
`B_(r,s)` is `p^k` times an integral coordinate pair. No division by
factorials occurs: these are ordinary, not divided, derivatives.

## 3. The two-sided determinant factor

Let `V` be the jet table of the transformed rows. Write its row
`(r,s)` as `p^k` times an integral jet row and put
`P=diag(p^k)`. Bilinearity of the *same* integer trace pairing gives

`U G Uᵀ = P K P`

for an integer matrix `K` (the Gram matrix of the quotient jet rows).
The left determinant is `(det U)² det G = det G`. The right determinant
is `(det P)² det K`. Therefore

`det G = p^(2 Σ_(r,s) k_(r,s)) det K`.

For each fixed `r`, the substitution `t=S-1-s` permutes
`0,…,S-1`, so `Σ_s k_(r,s)=Σ_t min(⌊r/p⌋,t)`. The sum is exactly
Ender's `F(p)`, proving the proposition.

## Interfaces, controls, and limits

- This proof supplies the **general valuation on paper** under the
  explicit irreducibility hypothesis. Lean checks all ordinary jets of
  `B(Z)(Z^p-W)^k` have both `p^k` coordinate factors under the explicit
  order-zero congruence, as well as the fixed `D=19,p=3` theorem; these
  are not a Lean proof of this proposition. A complete formal bridge
  still needs the unitriangular row transform on the actual integer
  Gram and the Frobenius/inertness interface.
- The `D=2,p=3` negative control must fail the local hypothesis:
  `X²+2=X²-1` splits modulo `3`, and `T^3=T`, not `-T`.
- Positivity of `det G` comes from the separate sampling/contact theorem.
  The cell-area count at Ender's chosen radius remains paper-only.
  Neither this divisibility proof nor the saved Arb/CRT certificates
  proves the class-number classification end to end.
- No numerical cutoff, prior-art comparison, or Tao-submission status
  changes by this result. The next mathematical glue is to formalize
  irreducibility from inertness and to link all analytic hypotheses to
  these exact `D,R,S,J,Q` parameters.
