# One determinant, two kinds of information

This is the shortest route into the Lean development. The longer
[human proof guide](HUMAN_GUIDE.md) explains the contact-count argument;
the [claim map](FORMALIZATION.md) names the checked declarations. Neither
document, nor this one, is a proof of the class-number-one classification.

## The question

Ender's **candidate** argument needs an integer determinant that is both
nonzero and highly divisible by inert primes. Geometry and a Hadamard upper
bound would then compete with arithmetic lower bounds. Lean now establishes
the nonzero side for sufficiently many samples, identifies its integer
matrix, and proves one fixed divisibility example. A
[paper proof](../research/uniform_inert_valuation/PROOF.md) reconstructs
the uniform prime-by-prime exponent; its general polynomial and
inertness interfaces are still missing in Lean.

## The object to keep in mind

Fix an integer `D>0` and a finite set `Q` of distinct pairs `(x,y)∈ℤ²`.
Work in the quadratic order

$$
A_D=\mathbb Z[t]/(t^2+D),\qquad
q=x+yt,\quad \bar q=x-yt.
$$

This is the selected lattice `ℤ[√(-D)]`, **not generally the full ring of
integers**. Its trace pairing is the concrete integral form

$$
B_D(a+bt,c+dt)=2(ac+Dbd).
$$

For `0≤r<R`, `0≤s<S` and `0≤j<J`, set

$$
v_{r,s,j}(q)=
\begin{cases}
(r)_j q^{r-j}\bar q^{\,s},&j\le r,\\
0,&j>r.
\end{cases}
\qquad
G_{(r,s),(r',s')}
=\sum_{q\in Q}\sum_{j<J}B_D(v_{r,s,j}(q),v_{r',s',j}(q)).
$$

Here `(r)_j` is the falling factorial. These are *ordinary* `Z`-derivatives
of `Z^r W^s`, with `W` held fixed; no `j!` normalization is hidden. The
factor `2` in `B_D` is the original trace normalization. Under
`t↦i√D`, Lean proves that this **entrywise** is the existing real
trace-Gram matrix at `z=x+iy√D`, and therefore has the same determinant.
See [IntegerTraceGram.lean](TenthDiscriminant/IntegerTraceGram.lean).

## Why the determinant is positive

Read `G` over `ℝ` via the proved integer-to-real embedding. For real
coefficients `c`, write
`F(Z,W)=∑_{r,s}c_{r,s}Z^rW^s`. The Gram identity says

$$
c^{\mathsf T}Gc
=2\sum_{q\in Q}\sum_{j<J}
\bigl|\partial_Z^jF(z_q,\bar z_q)\bigr|^2.
\tag{1}
$$

Thus positivity asks one clean question: can a nonzero polynomial in the
`R×S` monomial rectangle have every observed jet vanish?

The hard theorem, **not a dimension count**, is the exceptional-contact
budget. Over characteristic zero, take a nonzero `F` of bidegree `(r,s)`,
distinct parameters `w`, and an injective associated coordinate `z(w)`.
At most `2r+s` of them can have either a zero specialization `F(Z,w)` or
root multiplicity greater than `s` at `z(w)`. Here `w=\bar z`, so the
required injectivity is automatic. Taking more than `s` ordinary `Z`-jets
forces each zero-jet sample into this exceptional set.
Its proof uses a fixed-size derivative Sylvester determinant for irreducible
mixed factors, then a product rule that also handles pure factors and
repetitions. [FactorJetBudget.lean](TenthDiscriminant/FactorJetBudget.lean)
and [HUMAN_GUIDE.md §§2–5](HUMAN_GUIDE.md#2-count-exceptional-parameters-not-equations)
give the precise statement and proof.

If all `J` jets vanish and `J≥S>s`, every sample is exceptional. Since
`r≤R−1` and `s≤S−1`, the checked theorem yields

$$
R,S\ge1,\quad J\ge S,\quad
|Q|>2(R-1)+(S-1)
\quad\Longrightarrow\quad \det G>0.
\tag{2}
$$

The point-count hypothesis is **sufficient**, not claimed sharp.
[Interpolation.lean](TenthDiscriminant/Interpolation.lean) gives the public
real-matrix theorem; the exact integer-to-real identity above transfers its
positivity to `G`.

## What reduction modulo `m` does—and does not do

For every `m>0`, Lean independently computes the same jets in the
pair-coordinate model `(ℤ/mℤ)²` with `t²=−D`, and proves

$$
G_m=G\bmod m,\qquad
\det G_m=(\det G)\bmod m,\qquad
\det G_m=0\ \Longleftrightarrow\ m\mid\det G.
\tag{3}
$$

The sum remains indexed by the original `Q`: two distinct integer points
which become equal modulo `m` still contribute twice. This is integral
base change, **not** a map from `ℂ` to `ℤ/mℤ`, and (3) detects divisibility
without producing an exponent. For composite `m`, a zero determinant should
not be casually called a field-style singularity.
[ResidueTraceGram.lean](TenthDiscriminant/ResidueTraceGram.lean) includes a
collision counterexample to deduplicating the reduced samples.

## A complete small arithmetic bridge

Take `D=19`, `p=3`, `R=4`, `S=2`. The polynomial `t²+1` has no root in
`𝔽₃`, so the residue calculation has no split linear factors. In the
pair-coordinate model modulo `3`, `t²=−19≡−1`, so
`t³=−t`. The freshman's-dream identity in characteristic `3` gives

$$
q^3=(x+yt)^3=x-yt=\bar q\pmod3.
$$

Thus the two canonical rows `Z³` and `W` agree modulo `3`. More is true:
the jets of `F=Z³−W` at every lattice point are all divisible by `3`.
For `j=0` this is the displayed identity; for `j=1,2,3` the ordinary
derivatives are `3Z²`, `6Z`, and `6`; later derivatives vanish.

Replace the `Z³` row by `Z³−W` and make the matching column change. The
change of basis has determinant `1`, so it preserves `det G`. Because the
whole new jet row is `3` times an *integral* row, the Gram structure gives

$$
TGT^{\mathsf T}=\operatorname{diag}(1,\ldots,3,\ldots,1)
\,K\,\operatorname{diag}(1,\ldots,3,\ldots,1),
\quad K\in M_8(\mathbb Z),
\quad \det G=9\det K.
\tag{4}
$$

The shared diagonal entry really has two factors of `3`; merely knowing
that one row and one column are separately divisible by `3` would not prove
`9` divisibility. Equation (4) is checked for **every finite `Q` and every
`J`** in [InertPilot.lean](TenthDiscriminant/InertPilot.lean), using the
two-sided determinant lemma in
[GramDivisibility.lean](TenthDiscriminant/GramDivisibility.lean).

For the concrete integer-radius ellipse `Q=ellipsePairs 19 5`, Lean counts
`|Q|=21`; with `J=2`, (2) requires only `21>7`. Its determinant is therefore
both **strictly positive and divisible by `9`**. There is no paradox:
complex observations separate the bounded polynomials, while reduction
modulo `3` creates a relation. A `D=2,p=3` control falsifies this *row
congruence* when the irreducible-residue condition is dropped; it does not
disprove a determinant-divisibility statement. This fixed pilot is **not**
Ender's general valuation estimate.

## The uniform pattern, still a paper-to-Lean bridge

The fixed relation is one corner of a rectangular basis change. For an
odd prime `p` with `X²+D` irreducible modulo `p`, let `H=Z^p-W`. Frobenius
says `z^p=bar z` locally; every ordinary `Z`-derivative of `H` is also
`p`-divisible. At row `(r,s)` choose
`k=min(⌊r/p⌋,S-1-s)` and replace the monomial by
`Z^(r-pk)W^s H^k`. Its expansion has leading term `Z^rW^s`, and all
other terms remain in the rectangle with smaller `Z`-degree. So this is
an integral unitriangular basis change. Every transformed jet row is
divisible by `p^k`; the two Gram sides yield
`p^(2Σk)=p^(2F(p)) | det G`.

[The full written argument](../research/uniform_inert_valuation/PROOF.md)
checks the endpoints and product rule. Lean checks the abstract
unimodular two-sided determinant factor and a
[one-factor jet lemma](TenthDiscriminant/FrobeniusJet.lean): once
`z^p=bar z` holds modulo `p`, **every** ordinary jet of `Z^p-W` is
`p`-divisible. It does not yet check the `H^k` basis construction or
derive that congruence from inertness. This is inherited valuation mathematics,
not a new classification or cutoff.

## The boundary of the proof

| Link | Present status |
|---|---|
| Jet energy, contact budget, positivity; exact integer matrix; residue reduction; fixed `D=19,p=3` square factor | Lean-checked under the displayed hypotheses. |
| Ender's chosen-radius ellipse has enough points | Elementary cell-area proof on paper; exact-set and endpoint-transfer helpers in Lean, but the area inequality is not Lean-checked. |
| Uniform inert-prime valuation, class-number-one to inertness, analytic comparison, finite classification | The valuation has an explicit paper proof and a checked abstract matrix step. Its concrete Lean instantiation and the remaining links are not connected as an end-to-end theorem. The recorded numerical certificates belong to the candidate argument, not to (1)–(4). |

The quadratic order above is a useful *first doubling* with multiplication,
conjugation and trace. No higher Cayley–Dickson algebra or philosophical
local-to-global principle is a missing premise. The next substantive bridge
is a uniform arithmetic relation of the kind illustrated by (4), with the
actual class-number and radius hypotheses made explicit. For the detailed
provenance, see [STATUS.md](../STATUS.md), the
[registered pilot protocol](../research/local_global_gram/PROTOCOL.md), and
the [radius proof](../research/ender_radius_bridge/PROOF.md).
