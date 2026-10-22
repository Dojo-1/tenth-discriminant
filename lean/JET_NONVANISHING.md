# Nonvanishing through a finite tangency budget

**Status:** a conventional mathematical derivation and a separate Lean component layer.
The point-count theorem below is **not yet a Lean theorem** and has not received
independent semantic review. No discriminant cutoff or saved certificate is changed.
The argument uses the existing derivative rows, not a new witness matrix.

Baseline: `main` at `c1dbf684536fd77d43aecdcab09b4e772a59597b`.
Matrix dependency: PR #6 at `72fdab43921ab4ca00c05cb11fd19fca7d4deee1`.
The earlier resultant mechanism is already present in
[`review/PHASE2_GPT-6.1-Sol.md`, N4](../review/PHASE2_GPT-6.1-Sol.md).
This note specializes the factor accounting to Ender's `J=S` regime. No novelty
or priority claim is made, and previous same-loop reviews are not independent witnesses.

## Verification snapshot

The code and tests at `561b2947aea42171af3534eca0dee54d4518ff34` passed
[run 39781264061](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39781264061),
job `119832824420`: source-endpoint correspondence, `lake build`, the compiled
axiom audit, and the complete control suite. The pinned environment is Lean 4.19.0
and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.
The new module has 14 explicit theorem declarations; this is inventory, not a
completion score. All nine matched mathematical pairs and four axiom-audit probes
passed, together with the inherited Gram controls and new finite jet controls.

The first draft's failed run `39780241294` is preserved: polynomial evaluation
needed an explicit sample-to-Complex coercion; the circle polynomial's nonzero
proof was replaced by a constant-term argument, removing unnecessary hypotheses.
No check was bypassed. Lean was executed in GitHub Actions, not the local working
container. The exact Python controls were also run locally, normally and under
`python -O`, with byte-identical output. One inherited tactic-style warning remains.

## 1. The object: a polynomial seen through directional jets

For a finite set of distinct complex numbers `P` and positive integers `R,S`, put

$$Q(Z,W)=\sum_{r<R,\ s<S}c_{r,s}Z^rW^s.$$

The actual row matrix samples

$$\mathcal J_{P,J}(Q)_{z,j}=(\partial_Z^j Q)(z,\bar z),\qquad 0\le j<J.$$

`W` is held fixed during differentiation. This is not differentiation along the
real path `z -> (z,conj z)`. For **real** coefficient vectors `c`, the existing
trace-Gram matrix satisfies

$$c^{\mathsf T}Gc=2\sum_{z\in P}\sum_{j<J}
 |(\partial_Z^j Q)(z,\bar z)|^2.$$

Consequently positive definiteness is equivalent to absence of a nonzero invisible
**real** coefficient vector. Complex jet injectivity is sufficient, not necessary.
For example the two rows `1,i` at the single sample `z=i`, `J=1`, are complex-linearly
dependent, but their real trace Gram matrix is `2 I_2` and has determinant `4`.

`JetKernel.lean` proves this kernel/energy bridge, the link to Mathlib's actual
iterated polynomial derivative, and controls. It does not assume the point-count
criterion in a structure field, an axiom, or a theorem parameter presented as closure.

## 2. Proposed replacement for the nonvanishing step

**Jet uniqueness criterion.** If

$$R,S\ge1,\qquad J\ge S,\qquad |P|>2(R-1)+(S-1),$$

then the rectangular complex derivative-row family is linearly independent.
In particular, the actual real trace-Gram matrix is positive definite and
`det G > 0`.

No horizontal-line count, angular symmetry, lattice hypothesis or exclusion of
the origin appears in this criterion. Ellipse point-count estimates are still
needed to verify the numerical condition for the original application.

The algebraic statement behind it is slightly more general: for pairs
`(z_i,w_i)` with **both coordinate projections injective**, a nonzero polynomial
of bidegree `(r,s)` can have all its `Z`-jets of orders `0,...,J-1` vanish at at most
`2r+s` of the pairs when `J>s`. The conjugate graph automatically has both
injectivity properties.

## 3. Proof of the algebraic zero estimate

Work over the complex numbers, hence in characteristic zero. Factor

$$Q=c\prod_\nu H_\nu^{e_\nu},\qquad c\ne0,\quad e_\nu\ge1,$$

into pairwise nonassociate irreducibles. Write
`a_nu=deg_Z H_nu`, `b_nu=deg_W H_nu`. Degree additivity gives

$$r=\sum_\nu e_\nu a_\nu,\qquad s=\sum_\nu e_\nu b_\nu.$$

### Vertical factors

An irreducible factor depending only on `W` is a scalar multiple of `W-beta`.
A pair with `w_i=beta` makes the specialized polynomial identically zero, so its
order in `Z` must **not** be treated as a finite root multiplicity. Remove such
pairs first. Injectivity of the `w_i` bounds their number by the number of distinct
vertical factors, which is at most their total weighted `W`-degree.

### Why one factor must have excessive contact

At every remaining pair, each specialization `H_nu(Z,w_i)` is nonzero. Otherwise
`W-w_i` divides all its coefficients and thus divides `H_nu`, contrary to its
nonvertical irreducibility. Let `m_nu,i` be its ordinary root multiplicity at `z_i`,
with multiplicity zero when it does not vanish.

Vanishing of the first `J` jets, in characteristic zero, implies

$$J\le\sum_\nu e_\nu m_{\nu,i}.$$

If every `m_nu,i <= b_nu`, the right side would be at most `s`, contradicting
`J>s`. Thus **every remaining invisible point belongs to a factor with**

$$m_{\nu,i}>b_\nu.$$

This weighted argument includes repeated factors; squarefreeness of `Q` is not
assumed. It is the reason the special regime `J>=S` is useful.

### Horizontal factors

When `b_nu=0`, irreducibility over the complex numbers forces
`H_nu` to be a scalar multiple of `Z-alpha`, with `a_nu=1`.
It can contain at most one sample pair because the `z_i` are distinct.
This is exactly where injectivity of the first projection is needed.

### Mixed factors: the resultant pays for tangencies

For an irreducible factor `H` of bidegree `(a,b)` with `a,b>=1`, let

$$E(W)=\mathrm{Res}_Z(H,\partial_ZH).$$

`H` is primitive as a polynomial in `Z` over `C[W]` and irreducible over `C(W)`.
Its `Z`-derivative is nonzero and has smaller `Z`-degree, so `E` is nonzero.
Its fixed-size Sylvester determinant has size `2a-1`; every entry has `W`-degree
at most `b`. Therefore

$$\deg E\le(2a-1)b.$$

At a pair where the nonzero specialization `H(Z,w_i)` has a root of multiplicity
`m`, both `H(Z,w_i)` and its derivative are divisible by `(Z-z_i)^(m-1)`.
The specialized Sylvester map

`(A,B) -> A H + B H_Z`, with `deg A<a-1`, `deg B<a`,

therefore has image in the subspace of polynomials of degree `<2a-1` divisible
by `(Z-z_i)^(m-1)`. This subspace has codimension `m-1`.
The specialized matrix has corank at least `m-1`.

Here is the required order argument, including leading-degree drops. Constant
invertible row operations over `C` make at least `m-1` rows of the specialized
matrix zero. The corresponding polynomial rows before specialization are each
divisible by `W-w_i`. Extracting one such factor per row shows

$$(W-w_i)^{m-1}\mid E(W).$$

This uses the fixed-size matrix and remains valid when specialization lowers
the leading `Z`-degree. It does not silently replace the specialized determinant
by a smaller resultant.

At every excessive-contact point, `m>b`, so `m-1>=b`. Distinct `w_i` then give

$$b\cdot\#\{i:m_i>b\}\le\deg E\le(2a-1)b,$$

hence at most `2a-1` such points for this mixed factor.

### Sum the budgets

Let `v` and `h` be the numbers of distinct vertical and horizontal irreducible
factors. Every invisible sample is either vertical, horizontal, or an
excessive-contact point of a mixed factor. A union bound gives

$$N\le v+h+\sum_{\nu\,\mathrm{mixed}}(2a_\nu-1)\le s+2r.$$

The second inequality uses degree additivity and `e_nu>=1`.
This proves the claimed zero estimate. It is deliberately conservative; no
optimality or sharpness of the numeric constant is asserted.

For the rectangular coefficient space, a nonzero coefficient vector gives a
nonzero polynomial with `r<=R-1`, `s<=S-1`. Since `J>=S>s`, more than
`2(R-1)+(S-1)` samples contradict the estimate. Complex jet injectivity follows;
restricting coefficients to the reals and using the exact energy identity gives
positive definiteness of the unchanged trace-Gram matrix.

## 4. Relation to the existing Ender parameters

`ledger/ender.txt` and `tools/ender.py` use `J=S` and certify `n>3R+S`.
Those inequalities imply the proposed uniqueness criterion for positive `R,S`.
Thus the candidate argument can replace the **nonvanishing** use of
`J>=L+M`, without changing the matrix, derivative cutoff, radius or inertness
range. It does not by itself remove geometric estimates used to bound `n` or
row sizes, or prove the determinant's integrality or prime-adic divisibility.

This note does not disable the old guards, rerun a threshold search, or promote a
new bound for `D`. That requires separate review and numerical verification.

## 5. Falsifiers and executed controls

The fixed experiment in `jet_uniqueness_controls.py` tests `R=1,...,8`,
`S=1,...,4`, `J=S`, and exactly `2(R-1)+(S-1)+1` sample points in three families:
real points, irregular Gaussian-integer points, and rational unit-circle points.
All 96 matrices had full row rank after exact reduction modulo the prime
`1000000009` with `i -> 430477711`. This proves full rank for those particular
characteristic-zero rational/Gaussian matrices, not the universal theorem.
Point and row order reversal preserved the ranks.

Dropping `J>=S` is concretely false: take `R=S=J+1` and

$$Q(Z,W)=(ZW-1)^J.$$

All jets of orders `<J` vanish on any number of distinct unit-circle points,
while `Q` is nonzero. Four exact controls with `J=1,2,3,4` detect this dependence.
The general univariate-specialization vanishing and nonzero-polynomial facts
are formalized in `JetKernel.lean`.

Four fixed polynomial families `W Z^a+Z^2+W`, `a=3,...,6`, check the delicate
specialization `W=0`: the leading degree drops, the root at `Z=0` becomes multiple,
and the fixed-size resultant retains sufficient vanishing order. The real-versus-complex
rank control gives real determinant `4` despite complex row rank `1`.
These finite resultant controls do not require or assert irreducibility of their inputs.

These checks share authorship with the candidate argument. They are adversarial
regressions, not an independent semantic review. No causal advantage of semantic
priming is established. Python checks use explicit failures, not removable asserts.

## 6. Exact formalization boundary and next gate

`JetKernel.lean` proves the energy/nullspace/PD equivalence, the actual formal
polynomial derivative correspondence, observation monotonicity, and the stated
counterexample controls. The determinant-positive corollary explicitly takes
jet uniqueness as a hypothesis; **it does not discharge that hypothesis**.

The proposed universal zero estimate, irreducible-factor bookkeeping, Sylvester
corank-to-order lemma, and degree budget have **not yet been connected in Lean**.
They remain named formalization obligations, not imported axioms.

Next bounded gate: encode the fixed-size Sylvester specialization lemma,
including degree loss and vertical-factor exclusions, then connect it to the
jet uniqueness criterion. Kill the proposed route if a qualifying characteristic-zero
rank defect or violated multiplicity budget is found. A modular rank defect alone
requires exact follow-up. Stop before updating a discriminant cutoff or asserting
the global class-number theorem.
