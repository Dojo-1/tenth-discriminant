# Why the derivative Gram determinant is positive

**A proof to read, with a source map to check.** This guide explains the
interpolation theorem in ordinary mathematics. It is not a proof of the
class-number-one classification. The [claim map](FORMALIZATION.md) separates
completed components from the arithmetic and numerical links still missing.
For the shorter conceptual route, start with the
[mathematical spine](MATHEMATICAL_SPINE.md).

## The theorem in one paragraph

Choose a finite set P of distinct complex numbers, positive integers R and S,
and an integer J >= S. Take every monomial Z^r W^s with 0 <= r < R and
0 <= s < S. Observe its first J ordinary Z-derivatives at (z, conjugate(z))
for every z in P, keeping W fixed while differentiating. Form the real
trace-Gram matrix of these observations. If P has more than
2(R-1)+(S-1) points, that actual matrix is positive definite. Its determinant
is strictly positive and at most the product of its diagonal entries.

In symbols, with G defined below,

$$
J\ge S,\qquad |P|>2(R-1)+(S-1)
\quad\Longrightarrow\quad
G\succ0,\qquad 0<\det G\le\prod_i G_{ii}.
$$

This is a sufficient condition, not a necessary or optimal threshold. There is
no lattice, symmetry, angular-distribution or nonzero-point hypothesis.

**Public entry point:**
[`rectangularTraceGram_det_bounds`](TenthDiscriminant/Interpolation.lean).
For a subset of distinct monomial labels, use
`JetAssembly.traceGramMatrix_det_pos_of_point_count` in
[`JetCountGram.lean`](TenthDiscriminant/JetCountGram.lean).

## 1. What is the matrix?

A row is labelled by (r,s), and a column by a point z and derivative order j.
The complex entry is

$$
v_{r,s}(z,j)=
\begin{cases}
(r)_j z^{r-j}\bar z^{s},&j\le r,\\
0,&j>r,
\end{cases}
\qquad (r)_j=r(r-1)\cdots(r-j+1).
$$

The empty product (r)_0 is 1. These are ordinary derivatives, not derivatives
divided by j!. The observation at the origin is not discarded; zero to the zeroth
power has its usual polynomial value 1.

For row labels i and k, define

$$
G_{ik}=2\mathrm{Re}
\sum_{z\in P}\sum_{j=0}^{J-1}v_i(z,j)\overline{v_k(z,j)}.
$$

Writing the complex row coordinates as A+iB gives
G=2(AA^T+BB^T). Thus G is positive semidefinite even with repeated rows or no
observations. Positive semidefinite alone does not imply a positive determinant.

For real coefficients c_i, form the genuine bivariate polynomial
Q(Z,W)=sum_i c_i Z^(r_i) W^(s_i). Its observation energy is

$$
c^T Gc=2\sum_{z\in P}\sum_{j<J}
\left|(\partial_Z^j Q)(z,\bar z)\right|^2.
$$

Consequently, strict positivity is an observation-separation question:
can a nonzero bounded-degree Q have all these observations equal to zero?
Distinct monomial labels matter: they let us recover c from Q. The rectangular
API proves their quotient/remainder enumeration is injective for the caller.

Source: [`TraceGram`](TenthDiscriminant/TraceGram.lean),
[`GramMatrix`](TenthDiscriminant/GramMatrix.lean), and
[`JetKernel`](TenthDiscriminant/JetKernel.lean). The ordinary Hadamard upper
bound is in [`GramHadamard`](TenthDiscriminant/GramHadamard.lean).

## 2. Count exceptional parameters, not equations

Work temporarily over any characteristic-zero field K. Let F in K[W][Z] be
nonzero, with r=deg_Z F and s=deg_W F. Sample distinct parameter values w,
with an injective coordinate map z=z(w).

Call a sampled parameter exceptional when either

* F(Z,w) is the zero polynomial; or
* F(Z,w) is nonzero and has root multiplicity at z(w) greater than s.

Let B(F) be that finite exceptional set. The zero-polynomial case is separate:
it must not be assigned a finite order of vanishing. Lean gives
`rootMultiplicity` a total natural-number value, so this separation is essential.

The central counting statement is

$$
|B(F)|\le 2r+s.
$$

The proof starts with irreducible factors and then uses a product rule. It
never assumes that a general F is squarefree.

## 3. Why an irreducible mixed factor has a contact budget

Let H be irreducible with exact positive Z-degree a and positive W-degree b.
Use the fixed (2a-1)-square coefficient matrix whose columns are

$$
H,ZH,\ldots,Z^{a-2}H,
\qquad H_Z,ZH_Z,\ldots,Z^{a-1}H_Z.
$$

When a=1 the first block is empty. Let E(W) be its determinant.

Three facts do the work.

**E is not the zero polynomial.** Over the fraction field K(W), a vector in
this actual matrix's kernel gives AH+BH_Z=0, where deg A<a-1 and
deg B<a. Irreducibility, Gauss's lemma and characteristic zero give coprimality
of H and H_Z. Therefore H divides B; the degree window forces B=0 and then
A=0. The square matrix has trivial kernel. The implementation proves its
coefficient correspondence and reflects the nonzero determinant back to K[W].
Primitivity is derived from irreducibility and positive Z-degree, not assumed.
It also rules out identically zero specializations of H.

**A contact of order m>=1 uses at least m-1 zeros of E.** Translate the Z
coefficient basis to Taylor coordinates at the contact point. Both specialized
column blocks are divisible by (Z-z)^(m-1), so their first m-1 coefficients
vanish. The translation matrix has determinant one. Each resulting zero row
at W=w supplies a factor W-w, hence

$$
(W-w)^{m-1}\mid E(W).
$$

Keep the original global matrix size. For F=WZ^2+Z+1 its fixed determinant is
W(4W-1), which vanishes at W=0. Rebuilding a smaller resultant after specializing
to Z+1 would give 1. Both calculations are valid for different constructions;
they cannot be substituted for each other here.

**E has finite W-degree.** Every matrix entry has W-degree at most b.
Each determinant term is a product of 2a-1 entries, so

$$
\deg_W E\le(2a-1)b.
$$

At distinct parameters with m>b, each contact uses at least b units of this
degree. There can therefore be at most 2a-1 such parameters. Cancellation of b
is legitimate because b>0. Pure-variable factors are handled separately below.

Source: [`DeterminantMultiplicity`](TenthDiscriminant/DeterminantMultiplicity.lean),
[`SylvesterLocal`](TenthDiscriminant/SylvesterLocal.lean),
[`SylvesterNonzero`](TenthDiscriminant/SylvesterNonzero.lean),
[`SylvesterIrreducible`](TenthDiscriminant/SylvesterIrreducible.lean),
[`SylvesterDegree`](TenthDiscriminant/SylvesterDegree.lean),
[`ContactBudget`](TenthDiscriminant/ContactBudget.lean), and
[`IrreducibleContact`](TenthDiscriminant/IrreducibleContact.lean).

## 4. The short assembly: one product rule

For nonzero F and G,

$$
B(FG)\subseteq B(F)\cup B(G).
$$

To see this, consider a parameter outside the two factorwise exceptional sets.
Both specializations are nonzero. Their root multiplicities add and are at
most deg_W F and deg_W G respectively. Their product's multiplicity is
therefore at most deg_W(FG). It is not exceptional.

A factor depending only on W contributes at most its W-degree in zero fibers.
A factor depending only on Z contributes at most its Z-degree in roots, since
z(w) is injective. A mixed irreducible contributes at most 2a-1, hence at most
2a+b. Constant units cause no difficulty.

Factor induction, the union bound and additivity of both degrees on nonzero
products now give |B(F)|<=2 deg_Z F+deg_W F for every nonzero F. Repeated factors
are multiplied in repeatedly: their multiplicities are not thrown away. This
is the reason the implementation does not need a large explicit factor list.

The source lemma to read is `bad_mul_subset`, followed by
`badParameters_card_le` in [`FactorJetBudget.lean`](TenthDiscriminant/FactorJetBudget.lean).
[`BivariateDegree.lean`](TenthDiscriminant/BivariateDegree.lean) defines the
actual W-degree by an exact coordinate exchange and proves degree additivity.

## 5. Vanishing observations exceed that budget

Suppose J>deg_W F and all derivatives of orders 0,...,J-1 vanish at every
sampled point. A zero specialization is already exceptional. For a nonzero
specialization, ordinary derivative vanishing in characteristic zero implies
root multiplicity at least J, so that parameter is exceptional too.

Thus every sample lies in B(F). More than 2 deg_Z F+deg_W F samples are
impossible for a nonzero F. The only alternative is F=0.

For the actual observations, put w=conjugate(z). Conjugation is injective and
its own inverse, so both sampled coordinates retain distinctness. A polynomial
from the rectangular monomial grid has degrees at most R-1 and S-1. Our
hypotheses J>=S and |P|>2(R-1)+(S-1) therefore force Q=0.

Distinct row labels recover every coefficient c_i=0. The energy identity then
gives positive definiteness and a positive determinant of the original G.
Hadamard supplies the upper bound for that same matrix.

## 6. Small examples that protect the meaning

| Example | What it prevents us from saying |
|---|---|
| P={0}, R=S=J=1 gives G=[2]. | The origin contributes nothing; the trace factor can be dropped. |
| Two identical constant rows give determinant zero. | Semidefiniteness alone gives nonsingularity. |
| Rows 1,Z at P={i}, J=1 give G=2I. | Complex linear dependence is equivalent to real Gram singularity. |
| Q=(ZW-1)^J is invisible to orders below J on the unit circle. | The derivative-depth condition can be removed for arbitrary point sets. |
| F=Z^2-W has E=-4W. | A nonzero determinant polynomial is nonzero at every parameter. |
| In characteristic p, the ordinary Z-derivative of Z^p-W is zero. | The characteristic-zero jet argument transfers unchanged to small characteristic. |

A failed sufficient count condition does not prove singularity. Multiplicity
and degree refer to actual polynomials, not to sampled numerical estimates.

## 7. The Lean notation, decoded

| Lean expression | Mathematical meaning |
|---|---|
| `Polynomial (Polynomial K)` | K[W][Z]: inner variable W, outer variable Z |
| `F.natDegree` | Z-degree, with the convention natDegree(0)=0 |
| `JetAssembly.wDegree F` | W-degree from exact variable exchange; also zero at F=0 |
| `Polynomial.C q` | q(W), constant with respect to Z |
| `q.map Polynomial.C` | q(Z), with coefficients constant in W |
| `JetAssembly.specialize F w` | F(Z,w), still a polynomial in Z |
| `Polynomial.derivative` | Derivative in the outer variable Z |
| `Finset` | A finite set: duplicate entries cannot increase its cardinality |
| `Fin (R*S)` | Exactly R*S row indices, enumerated by quotient and remainder |
| `PosSemidef` / `PosDef` | Nonnegative / strictly positive quadratic form |

Natural-number subtraction truncates at zero. The proof keeps positivity and
nonzero hypotheses wherever a degree or multiplicity argument needs them.

## 8. What this does not yet prove

This interpolation theorem alone does not define the imaginary quadratic class
group, prove small-prime inertness, count Ender's ellipse, identify the integer
Gram matrix, prove prime-adic divisibility, certify the analytic bounds or close
the finite classification. Later work supplies the count on paper (§9) and the
matrix identification in Lean (§10), then an exact residue detector (§11).
The remaining links are not consequences of interpolation alone. See
[FORMALIZATION.md](FORMALIZATION.md).

Put plainly: this proof says that **if** the intended ellipse supplies enough
distinct samples, then its exact derivative Gram matrix is nonsingular. The
geometric count now supplies that premise in an unformalized area argument;
the integer-coordinate bridge identifies the same matrix, and the residue
bridge detects divisibility by a chosen modulus. Neither statement by itself
proves Ender's uniform prime-adic lower bound; a later
[paper argument](../research/uniform_inert_valuation/PROOF.md) supplies its
rectangular basis mechanism, but that instantiation is not in Lean. The
analytic bounds and finite classification also remain to be connected. The project-wide
[Tao-objective audit](../TAO_OBJECTIVE_AUDIT.md) records this boundary without
collapsing it into a percentage-complete claim.

The attached identity framing motivates the question of observation separation.
No Picard-groupoid equivalence or geometric metaphor is an extra proof premise.
The scalar Gram determinant and a module's determinant line are different objects.

A kernel-checked proof establishes its encoded statement under its actual
hypotheses. Human review must still examine the definitions, the intended
application and the remaining links. This guide and the proof scripts share
authorship; a human readability study or independent semantic review has not
been performed.

## 9. The concrete ellipse bridge

The new [`LatticeEllipse.lean`](TenthDiscriminant/LatticeEllipse.lean) makes
the sample set concrete for **positive natural D** and **natural integer
radius rho**. It enumerates pairs in the square −rho≤x,y≤rho and keeps those
with x²+D y²≤rho². Why is this the whole ellipse? Since D≥1, the inequality
forces both x²≤rho² and y²≤rho²; hence neither coordinate can lie outside
that square. This is proved, not assumed.

Map (x,y) to z=x+i y√D. Its real part recovers x; because D>0, √D>0 and its
imaginary part recovers y. Thus distinct pairs cannot collapse to one complex
point. The stored complex set has exactly the same cardinality as the integer
pair set. `latticePoint_normSq` verifies that the integer inequality is the
complex norm inequality. The boundary is inclusive, and a small checked
example D=rho=1 retains origin and the four unit-axis points.

The payoff is deliberately conditional:

$$
J\ge S,\quad R,S\ge1,\quad
|\mathcal E_{D,\rho}|>2(R-1)+(S-1)
\quad\Longrightarrow\quad
0<\det G\le\prod_iG_{ii}.
$$

Here G is precisely `rectangularTraceGram` on `ellipsePoints D rho`; no new
Gram matrix is substituted. The formal theorem takes the integer-pair count
as a premise and transports it by the proved cardinality equality. It does
**not by itself** derive Ender's lower count, formalize his radius guard, or
prove the determinant's arithmetic divisibility. The next paragraph supplies
the count on paper and §10 supplies the matrix identity in Lean. The area and
radius instantiation are not Lean-checked; **general** inert-prime divisibility
remains open in Lean (a fixed pilot is proved in §11 and a uniform paper
proof is linked below). The
full-classification claim remains candidate mathematics.

A separate [geometric proof](../research/ender_radius_bridge/PROOF.md) now
settles the count on paper. The idea is to partition the plane into cells of
width 1 and height √D. Each cell center is within √D of every point in the
cell. Ender's radius includes ten spare √D units; a smaller disk therefore
fits inside cells centered at ellipse points, and its area exceeds
`(3R+S)√D`. Lean checks the finite-set monotonicity needed to carry this
endpoint result across an interval, but does not yet check the area argument.

## 10. The same Gram matrix in integer and complex coordinates

The arithmetic calculation uses a pair `(a,b)` for `a+b√(-D)`, while the
interpolation proof uses the complex point `a+i b√D`. These are two
coordinates for the **selected lattice** `ℤ[√(-D)]`; it need not be the full
ring of integers of the quadratic field. Define pair multiplication by

$$
(a,b)(c,d)=(ac-Dbd,ad+bc),\qquad \overline{(a,b)}=(a,-b).
$$

The map `ι_D(a,b)=a+i b√D` preserves multiplication and conjugation. Its
integer trace pairing is

$$
B_D((a,b),(c,d))=2(ac+Dbd)
=2\operatorname{Re}\bigl(\iota_D(a,b)\overline{\iota_D(c,d)}\bigr).
$$

That equality is the key geometric invariant: the weighted Euclidean pairing
does not change when we pass from lattice coordinates to the complex plane.
Lean proves it, then transports every ordinary derivative row through `ι_D`,
including the `j>r` zero case. Summing over one finite set of distinct pairs
and the same derivative orders gives **entrywise equality** after casting the
integer matrix to the reals. The row labels remain `(i/S,i%S)`, so its
determinant casts to the determinant of the *existing* real matrix—not a new
matrix with a convenient bound. See [`IntegerTraceGram.lean`](TenthDiscriminant/IntegerTraceGram.lean).

A small asymmetric check explains why entries matter. At `D=3`, one sample
`(0,1)`, rows `1, ZW`, and derivative orders `j=0,1`, the integer matrix is
`[[2,6],[6,24]]`, with determinant `12`. Replacing the evaluation factor
`\bar z` by `z` while leaving the derivative rule unchanged changes the
off-diagonal entry to `-6` while leaving that determinant unchanged. A
determinant-only comparison could miss the wrong derivative semantics.

The generic equality concerns a supplied **finite set of distinct pairs**.
The verifier's historical ellipse generator uses a half-integer-scaled radius,
whereas `ellipsePairs D rho` uses integer `rho`; this bridge does not identify
those two generators or certify the saved numerical campaign. Most importantly,
integer entries alone do not imply the **general** inert-prime valuation bound.
The [uniform paper proof](../research/uniform_inert_valuation/PROOF.md)
supplies an explicit basis change; its concrete Lean instantiation and the
class-number classification remain open.

## 11. Local and global arithmetic views of one Gram matrix

Here “global” means the integral lattice, not an assertion about every place
of a number field. There are two useful views of the *same* integer Gram
matrix. For `D>0`, the pair `(a,b)` is exactly the coordinate description of
`a+b√(-D)` in the selected order `ℤ[√(-D)]`. Multiplication, conjugation,
the norm, and the factor-two trace pairing agree in these charts; see
[`QuadraticCoordinates.lean`](TenthDiscriminant/QuadraticCoordinates.lean).
For some `D`, this selected order is smaller than the full ring of integers.
This is the useful *first* Cayley–Dickson-style doubling: conjugation and a
quadratic norm have concrete operations that the proof uses. Quaternionic or
octonionic doublings add no needed operator to this determinant calculation.

For an integer `m>0`, reduce each pair coordinate modulo `m` and carry out
the same multiplication, conjugation, **ordinary** derivative and trace
pairing in `(ℤ/mℤ)²`. The local matrix is computed independently from these
residue operations. Its sum still runs over the original points: if two
different integer points become the same residue, they contribute twice.
Entrywise equality with the reduced integer matrix gives

$$
G_m = G_{\mathbb Z}\bmod m,\qquad
\det G_m = (\det G_{\mathbb Z})\bmod m,\qquad
\det G_m=0\ \Longleftrightarrow\ m\mid\det G_{\mathbb Z}.
$$

These are the two directions of the bridge: reduce a concrete global matrix
to make local calculations, then lift *a proved local vanishing statement*
back to an integer divisibility statement. The complex matrix in §10 and the
residue matrix both originate from the integer one; there is no map from
complex numbers to `ℤ/mℤ` in this argument. See
[`ResidueTraceGram.lean`](TenthDiscriminant/ResidueTraceGram.lean).

Two exact controls prevent attractive mistakes. The asymmetric matrix in §10
has determinant `12`, so its local determinants are `0` modulo `3` and `2`
modulo `5`. For the constant row sampled at `(0,0)` and `(3,0)`, the global
Gram entry is `4`, hence `1` modulo `3`; replacing the two samples by the
*set* of their residues would wrongly give `2`. Both controls are Lean-checked.

For the registered `D=19`, `p=3` pilot, `X²+19` becomes `X²+1` modulo `3`,
which has no root. The quotient `𝔽₃[t]/(t²+1)` has nine elements;
conjugation agrees with the cube map. Thus `Z³-W` evaluates to a multiple of
`3` at every lattice point,
and its ordinary derivatives of orders `1,2,3` are `3Z²,6Z,6`; higher
derivatives vanish. The checked theorem
`inertPilotJet_dvd_three` proves coordinatewise divisibility for *every*
point and derivative order. This is a fixed toy case, not an inert-prime
theorem for arbitrary `D,p,R,S`.

Why is the determinant step subtler? If the row `Z³-W` replaces the canonical
`Z³` row, the matching Gram column changes too. To obtain `9 | det G`, one
needs an *integral* middle matrix in
`T G Tᵀ = diag(3) K diag(3)`. Separate divisibility of the selected row and
column does not suffice: the `1×1` matrix `[3]` has both but its determinant
is not divisible by `9`. [`GramDivisibility.lean`](TenthDiscriminant/GramDivisibility.lean)
proves this determinant implication under the explicit two-sided factorization.
[`InertPilot.lean`](TenthDiscriminant/InertPilot.lean) constructs that
factorization for the canonical eight-row matrix and proves `9 | det G` for
*every* finite `Q` and cutoff `J`. The ellipse `Q=ellipsePairs 19 5`, `J=2`
has 21 points; the checked count criterion also proves its determinant is
strictly positive. As a falsifier, `D=2`, `p=3`, `Z=√(-2)` gives
`Z³-W=-Z`, which is not coordinatewise divisible by `3`; this too is a
checked control. The [registered protocol](../research/local_global_gram/PROTOCOL.md)
records the test and its boundary. The general Ender valuation now has a
[paper proof](../research/uniform_inert_valuation/PROOF.md): replace each
`Z^rW^s` by `Z^(r-pk)W^s(Z^p-W)^k`, where
`k=min(⌊r/p⌋,S-1-s)`. The replacement stays within the rectangle and is
unitriangular; every jet receives `p^k`, so the determinant receives
`p^(2Σk)=p^(2F(p))`. Lean checks the abstract unimodular determinant
step, the exact exponent sum, and the [ordinary-jet power](TenthDiscriminant/JetPower.lean):
all transformed `H^k` jets have both coordinate factors `p^k` under
their explicit order-zero congruence. Phase 7 below now identifies the
unitriangular basis change with the actual Gram. Phase 8 below derives
the Frobenius premise from odd-prime nonsquareness of `-D` in the selected
residue order. The class-number
classification is still open.

There is now an explicit [integer binomial matrix](TenthDiscriminant/RectangularBasisMatrix.lean)
for this basis, with a Lean proof that it is lower triangular and has
determinant `1`. The previously missing entrywise identity—its action on
the **existing** integer derivative rows—is now proved in Phase 7 below.

## 12. An operator on examples, and the limit of its orbit

Fix `D` and `p`. Call a lattice sample `a=x+y√(-D)` **locally valid** when
both integer coordinates of `a^p-conjugate(a)` are divisible by `p`.
This is precisely the premise of the ordinary-jet lemma, not the assertion
that `D` has class number one. Conjugation is an exact operator on valid
samples:

$$
a^p\equiv\bar a\pmod p
\quad\Longrightarrow\quad
(\bar a)^p=\overline{a^p}\equiv a
=\overline{\bar a}\pmod p.
$$

Applying it twice returns `a`. Thus the orbit generated by this proven
operator is at most `{a,bar a}`; for the non-real `D=19,p=3` pilot it has
two distinct members. Lean checks the integer-pair multiplication identity,
power identity, coordinatewise divisibility and its composition with the
all-orders one-factor jet theorem in
[`LocalOperators.lean`](TenthDiscriminant/LocalOperators.lean).

Other possible operators have different guards. Changing `D` or `a` within
their residues modulo `p` should preserve this *local* congruence, but this
is only a proposed next lemma, not a checked result here. Adjoining valid
samples retains a pointwise jet statement, provided the original sample
indices and their multiplicities are kept. The binomial change of basis
has determinant one and its action on the actual derivative rows is proved
in Phase 7. Composing local operators nevertheless explores a residue fiber;
it does not reach a class-number classification, a radius count, or an
analytic cutoff. Those are separate predicates requiring their own bridges.

## 13. Why the rectangular bridge now commutes

The hard equality is small enough to say without Lean syntax. Label a row by
`(r,s)` and put `k=min(⌊r/p⌋,S-1-s)`. The binomial theorem gives

$$
Z^{r-pk}W^s(Z^p-W)^k
=\sum_{t=0}^{k}(-1)^t\binom{k}{t}Z^{r-pt}W^{s+t}.
$$

Every displayed monomial is **already** a row of the original rectangle.
The checked coefficient matrix uses exactly these integers. Evaluation,
ordinary differentiation in `Z` (holding `W` fixed), and the coordinate
map into `ℤ[√(-D)]` commute with that finite linear combination. Thus the
matrix acts on the *original* jet table, not on an invented replacement.
This is [the row-action theorem](TenthDiscriminant/RectangularRowAction.lean).

Suppose now that `a^p-conjugate(a)` has both coordinates divisible by `p`
for **every** integer pair `a`. The ordinary-jet power lemma puts `p^k`
in every transformed jet of row `(r,s)`. Write `U` for the checked
determinant-one binomial matrix, `G` for the actual integer Gram, and
`D_p=diag(p^k)`. Bilinearity of the *same factor-two trace* then gives an
integer matrix `K` with

$$ UGU^{\mathsf T}=D_p K D_p. $$

No point is discarded if two samples coincide modulo `p`. Taking
determinants yields `p^(2Σk) | det G`; the checked sum identity says
`Σk=F(p)`. Both the [integral factor](TenthDiscriminant/RectangularGramFactor.lean)
and this exact conditional determinant implication are now Lean theorems,
for arbitrary finite samples, grid and derivative cutoff, including empty
grids. Phase 8 below supplies the local hypothesis that makes it fire,
under an explicit odd-prime nonsquare guard. The chosen-radius area
argument and subsequent analytic/class-number links remain separate.

## 14. One local generator controls every lattice point

Reduce the selected order modulo an odd prime `p`. Write `t` for the pair
`(0,1)`; its multiplication is the repository's existing rule, so
`t²=-D`. If `-D` is **not a square** in `𝔽_p`, Euler's criterion gives
`(-D)^((p-1)/2)=-1`. Since `p=2((p-1)/2)+1`,

$$ t^p=t(t^2)^{(p-1)/2}=t(-D)^{(p-1)/2}=-t. $$

Every residue pair is `x+yt`. Characteristic `p` and Fermat's identity
in `𝔽_p` now yield

$$ (x+yt)^p=x^p+y^pt^p=x-yt. $$

The new [residue-ring chart](TenthDiscriminant/QuadraticResidueRing.lean)
is proved injective and respects the **existing** residue-pair
multiplication and powers. Thus this equality returns to both original
coordinates; a zero residue is exactly integer divisibility by `p`.
[InertFrobenius.lean](TenthDiscriminant/InertFrobenius.lean) checks that
transport and applies §13 to obtain the exact determinant exponent for
every finite original sample set. It checks `D=19,p=3` as a nonsquare
and `D=2,p=3` as a square counter-control.

The local condition is deliberately sharper than an unqualified word
“inert”: for a nonmaximal selected order, a prime dividing its conductor
needs special care. The theorem assumes odd prime and nonsquare `-D`
*in this coordinate ring*. We have not proved that the global
class-number-one hypothesis supplies these guards at every prime used by
Ender, nor formalized the geometric area and analytic comparison. These
are now the visible global-to-local and determinant-to-cutoff gaps.

## 15. The small-prime gate, without hiding the class group

There is a short argument at the boundary of the formal proof. For
`D ≡ 3 (mod 4)`, the relevant principal norm form is

$$N(x,y)=x^2+xy+\frac{D+1}{4}y^2,
\qquad 4N(x,y)=(2x+y)^2+Dy^2.$$

If `y ≠ 0`, this forces `N(x,y) ≥ (D+1)/4`. If `y=0`, its norm is a
square, so cannot equal a prime. Hence a prime `p<(D+1)/4` cannot be
represented by this form. Lean checks both cases. It also checks that
`X²+D` has no root modulo `p` exactly when `-D` is nonsquare, and that
this is equivalent to irreducibility of `X²+D` over `𝔽_p`.

The *missing sentence* is: **why would a root modulo `p` give a
principal element of norm `p`?** In a class-number-one imaginary
quadratic field, the intended answer passes through a prime ideal of
norm `p`, principality, and identification of its generator's norm
with the displayed form. The abstract ideal/class-group move is
formalized in §16, but its field-specific input remains open.
[SmallPrimeBridge.lean](TenthDiscriminant/SmallPrimeBridge.lean)
names it `SmallPrimeNormLifting` and proves only the implication

$$\text{small prime + norm lifting}
\Longrightarrow X^2+D\text{ irreducible mod }p
\Longrightarrow p^{2F(p)}\mid\det G.$$

The strict inequality matters. At `D=163,p=41`, the form represents
`41` as `N(0,1)`; the theorem deliberately says nothing at equality.
At `D=15,p=3`, zero is a residue root and Lean proves the lifting
premise is false. These are boundary checks, not a classification or a
new analytic cutoff.

## 16. What class number one actually buys

The previous section deliberately left “principal” as an assumption.
We can now prove the middle ideal-theoretic move for **any number field**
`K`, without yet claiming it applies to our particular root. Suppose
there is a ring map `f : 𝓞_K → 𝔽_p`. It is onto: each element of
`𝔽_p` is the image of an integer. Its kernel `I` therefore has
quotient `𝓞_K/I ≅ 𝔽_p`, so the ideal norm of `I` is `p`.

Mathlib identifies class number one with the assertion that every
ideal of `𝓞_K` is principal. Thus `I=(a)` for some algebraic integer
`a`. The principal-ideal norm formula gives

$$p=N(I)=N((a))=|N_{K/\mathbb Q}(a)|.$$

This entire implication is checked in
[PrincipalIdealBridge.lean](TenthDiscriminant/PrincipalIdealBridge.lean),
including a concrete `K=ℚ,p=3` control. The absolute value is
necessary for a general number field. It becomes the positive norm in
our imaginary quadratic application only after we identify that field
and its integral coordinates.

Two arrows still need formal proofs: a root of `X²+D` modulo odd `p`
must supply the ring map from the **maximal** order, and every algebraic
integer obtained this way must have coordinates `(x,y)` whose norm is
the displayed `N(x,y)`. The latter also fixes the sign. Until those
arrows are checked, the Phase 9 lifting premise is not discharged and
the class-number classification remains open.

## 17. From a residue root to an actual quotient map

Let `D ≡ 3 (mod 4)` and write `c=(D+1)/4`. Put
`ω=(1+√(-D))/2`. Its defining relation is

$$\omega^2-\omega+c=0.$$

For an odd prime `p`, suppose `z²=-D` in `𝔽_p`. Then
`t=(1+z)/2` satisfies the same relation: multiply
`t²-t+c` by `4` to obtain `(2t-1)²+D=z²+D=0`.
Because `4` is invertible, the relation itself is zero. The universal
property of the quotient ring therefore gives a **surjective ring map**

$$\mathbf Z[T]/(T^2-T+c)\longrightarrow\mathbf F_p,
\qquad T\longmapsto t.$$

Lean checks the integer coefficient identity, the odd-prime division,
the polynomial-root calculation, the ring map, its value on `T`, and
surjectivity in [HalfOrderResidue.lean](TenthDiscriminant/HalfOrderResidue.lean).
This makes one of §16's arrows concrete, but for the explicit order
`ℤ[ω]`, **not yet** for Mathlib's maximal integer ring `𝓞_K`.
The field-specific remaining work is to identify those rings under
the fundamental-discriminant hypotheses and show that the algebraic
norm in that identification equals `x²+xy+cy²`. Only then can §16
feed §15 without an extra premise. At `D=15,p=3`, the quotient map
exists while the lifting premise fails; this is a useful guard against
dropping class number one.

## 18. The two-dimensional norm chart

There is no mystery in the quadratic form once the order is written
with basis `1,T`. Set `c=(D+1)/4`; the relation `T²=T-c` gives

$$
(x+yT)\cdot1=x+yT,
\qquad
(x+yT)\cdot T=-cy+(x+y)T.
$$

So the two columns of multiplication by `x+yT` are `(x,y)` and
`(-cy,x+y)`. Its determinant is

$$\det\begin{pmatrix}x&-cy\\y&x+y\end{pmatrix}
=x^2+xy+cy^2.$$

[HalfOrderNorm.lean](TenthDiscriminant/HalfOrderNorm.lean) checks the
relation in the actual quotient, the nontrivial second-column
identity, and this exact integer determinant (including `c=4` for
`D=15`). The formula is therefore a genuine multiplication chart,
not a numerically fitted expression. One formal sentence is still
missing: Mathlib's `Algebra.norm` of `x+yT` must equal the determinant
of this matrix under the order's power basis. A second, logically
separate sentence must identify the explicit order with the maximal
integer ring of the intended quadratic field. Neither is silently
assumed; until both are proved, §16 does not discharge §15's premise.
