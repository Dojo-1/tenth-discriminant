# The Tenth Discriminant: one determinant, two incompatible pressures

*A human first reading of the current Lean theorem — 2 November 2026.*

**The result.** The checked declaration
[`ThinIntegratedEndpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_41floor`](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean)
states:

> If a number field \(K\) has degree two over \(\mathbb Q\), is totally
> complex, and has class number one, then
> \( |\operatorname{disc}(K)| < 41{,}006{,}250{,}000.\)

This is a claim about the **actual field discriminant**, not a determinant
invented for a calculation. It is not a new classification of the nine
imaginary quadratic class-number-one fields; classical mathematics already
has much stronger results. The interest here is whether the arithmetic
and analytic paths can be reconstructed *on one well-specified integer*.
[Combined-head Lean, source, axiom and negative controls passed](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41410529603);
[external human semantic review](https://github.com/Dojo-1/tenth-discriminant/issues/50) is still open.

## The object in the middle

Take a squarefree positive parameter \(D\) describing an imaginary quadratic
field. In the odd chart \(D\equiv3\pmod4\), work with the original integer
pairs \((x,y)\) representing \(x+y\sqrt{-D}\). Choose a finite set of pairs
\(Q\). For each rectangular monomial \(Z^rW^s\), evaluate its
**ordinary** \(Z\)-derivatives at each chosen pair, with \(W\) held
constant during differentiation and set to the conjugate value only at
evaluation. Record **both integer coordinate channels** of each result.
The trace pairing encodes the two quadratic embeddings; it does **not**
silently add another observation point to \(Q\). Those original rows form
\(E_Q\).
With the unchanged positive trace weights \(2\) and \(2D\), form

\[
G_Q=E_Q B_Q E_Q^{\mathsf T},\qquad \Delta_Q=\det G_Q.
\]

Every letter matters. \(\Delta_Q\) is a positive **integer** when the
interpolation count holds; it is **not** \(|\operatorname{disc}(K)|\).
It is the common witness by which we eventually constrain the field.

For the current endpoint, choose
\(Q_{\rm thin}=\operatorname{ellipsePairs}(D,\rho_{\rm thin})\), where
\(\rho_{\rm thin}\) is the tuned \(\lceil (11/25)D^{3/4}\rceil\) radius.
For \(D\ge450^4=41{,}006{,}250{,}000\), the Lean count theorem proves the
**sufficient**, not necessary, positivity guard
\(2(R-1)+(S-1)<|Q_{\rm thin}|\).

## Why the same integer cannot satisfy both bounds

**Arithmetic pulls up.** Under the explicit squarefree,
class-number-one and inert-prime conditions, an integral upper-unitriangular
row operation exposes powers of *eligible odd primes* dividing
\(\Delta_{Q_{\rm thin}}\). The original ordinary jets and both sides of
the trace metric are retained; the lower bound is established **directly
for the thin sample**, not transported from an old ellipse's determinant.
The certified lower pressure is

\[
\frac{\log\Delta_{Q_{\rm thin}}}{R^2S}
\ge
\frac{999997}{1000000}\log D-\frac{5739}{1000}.
\tag{L}
\]

**Geometry pushes down.** The smaller thin ellipse has enough nodes but
a tighter real norm envelope. The already certified old padded count
is used as a **common upper majorant**, never as a claim that the two
sample sets yield equal determinants. The preserved radial/Hadamard
argument gives

\[
\frac{\log\Delta_{Q_{\rm thin}}}{R^2S}
\le
\frac45\log D-\frac{1849}{2000}.
\tag{U}
\]

The Lean rational logarithm certificate verifies
\(\log D\ge 241/10\) whenever \(D\ge450^4\). At that threshold,
subtracting (U) from (L) gives **at least**

\[
\left(\frac{999997}{1000000}-\frac45\right)\frac{241}{10}
-\left(\frac{5739}{1000}-\frac{1849}{2000}\right)
=\frac{54277}{10000000}>\frac1{500}>0.
\]

Thus the two inequalities would contradict one another if a class-number-one
odd-chart field existed at or above the threshold. Separate existing
even-chart facts and explicit number-field equivalences return to
\(\operatorname{disc}(K)\) rather than replacing that discriminant with
\(\Delta_Q\).

## Read the Lean in the order a human would prove it

| Human obligation | Corresponding checked source |
| --- | --- |
| The original integer-pair jets really use ordinary derivatives and the original trace metric | [`IntegerTraceGram.lean`](../../lean/TenthDiscriminant/IntegerTraceGram.lean) |
| The thinner observation set still has sufficient points | [`ThinEllipseCount.lean`](../../lean/TenthDiscriminant/ThinEllipseCount.lean) |
| The same thin determinant satisfies the real upper bound | [`thin_production_normalized_upper`](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean) |
| The exact eligible odd-prime mass bounds that very determinant from below | [`recovered_mass_le_thin_log`](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean) |
| The rational logarithm bracket gives positive separation | [`endpoint_certificate`, `endpoint_separation`](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean) |
| The contradiction excludes large class-number-one parameters and returns to the **actual** field discriminant | [`totallyComplex_degree_two_classNumber_one_discriminant_bound_41floor`](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean) |

Do **not** conflate three useful but distinct directions:

- **Finite minimal-node geometry:** [Phase142](../ellipsoid_trimming/PHASE142_LEVERAGE_AND_UNISOLVENCE.md)
  exhibits a four-nonreal-node rank witness at \(D=19\); it does not give a
  uniform smaller-radius theorem, and fewer nodes can make the determinant
  *larger*.
- **Extra arithmetic factors:** the checked [Phase162 source-Gram theorem](../../lean/TenthDiscriminant/BinaryNullTraceGram.lean)
  proves a separate \(2\)-adic divisor on the original Gram. The proposed
  four-generator exponent 1358 remains a finite/paper certificate until its
  exact unimodular row action is formalized; no binary factor is counted twice.
- **A new lower field cutoff:** the [Phase164 integration programme](https://github.com/Dojo-1/tenth-discriminant/issues/82)
  must compare the extra arithmetic on this **same** thin Gram and separately
  prove new count/radius guards if it wishes to work below \(450^4\).

## What independent review should try to break

A reviewer can ask four concrete questions without accepting our vocabulary:

1. Does the class-number-one hypothesis refer to the right maximal order,
   including the index-two chart, and are the required primes truly eligible?
2. Can one independently construct the integer row quotient for **ordinary**
   derivatives, not a Hasse-jet surrogate?
3. Is positivity checked for the **same Q** used by both inequalities, and
   are the trace weights and row normalization unchanged?
4. Does the final equivalence return to the field's **actual discriminant**,
   with the rational strict margin reproduced using exact arithmetic?

A green Lean build validates an encoded theorem with its dependency and
axiom envelope. It does not establish the intention of every definition or
replace an independent mathematician's reconstruction.

**Reproduce** (Lean 4.19.0 with pinned Mathlib): from `lean/`, run
`lake exe cache get`, `python3 verify_sources.py`, `lake build`,
`python3 audit.py`, and `python3 negative_controls.py`.

The old [47-billion human reconstruction](../tight_radial_v1/HUMAN_RECONSTRUCTION.md)
remains a historical explanation, not the current endpoint. The repository
is an AI-assisted investigation under Jesús Vilela Jato's research direction,
motivated by [Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
No independent endorsement is implied.

## A newer arithmetic fact — not a newer field bound

[Phase164's merged Lean bridge](../../lean/TenthDiscriminant/BinaryThinGramBridge.lean) strengthens what we can say about the **same** thin-Q determinant: its existing univariate binary divisor `2^Λ₁` multiplies the already justified odd-prime product by coprimality, and their product is at most the positive integer `det G_thin`. [This short mathematical guide](PHASE164_BINARY_ODD_SAME_GRAM.md) gives the source object, three theorem declarations, and their dependencies. The source and proof checks [passed](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41417184165). This is not yet incorporated into a **uniform improved logarithmic comparison** or the field endpoint above; neither the proposed `2^1358` four-generator Gram factor nor a 20.2-billion discriminant bound has been proved in Lean.
