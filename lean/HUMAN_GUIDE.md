# Why the derivative Gram determinant is positive

**A proof to read, with a source map to check.** This guide explains the
interpolation theorem in ordinary mathematics. It is not a proof of the
class-number-one classification. The [claim map](FORMALIZATION.md) separates
completed components from the arithmetic and numerical links still missing.

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

This interpolation theorem does not define the imaginary quadratic class group,
prove small-prime inertness, establish Ender's quantitative ellipse count, identify
the integer Gram matrix, prove its prime-adic divisibility, certify the analytic
bounds or close the finite classification. It supplies one connected part of
that longer argument. See [FORMALIZATION.md](FORMALIZATION.md).

Put plainly: this proof says that **if** the intended ellipse supplies enough
distinct samples, then the exact derivative Gram matrix used by the arithmetic
argument is nonsingular. To turn that into a classification, the project still
has to prove that Ender's chosen ellipse meets the count, that its matrix is the
integer matrix whose prime divisibility is used, and that the analytic bounds
apply to that same determinant. A finished interpolation theorem cannot fill
those application-specific gaps by itself. The project-wide
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
**not** derive Ender's lower count, connect his chosen real-valued radius to
an integer-radius instance, or prove the determinant's arithmetic
divisibility. Those are the next application obligations. The full-classification
claim remains candidate mathematics, not a checked theorem.
