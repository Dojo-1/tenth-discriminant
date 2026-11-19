# E37 — FINITE-RANK GRAM DIVISIBILITY THROUGH HONEST INTEGRAL FRAMES

*19 November 2026 · n-row proof candidate stacked on E36.*

## Object and evidence boundaries

The source matrix is always the actual integerRectangularTraceGram Q D J R S
from TenthDiscriminant.IntegerTraceGram. Its original rows, ordinary Z
derivatives (W fixed), factor-two positive trace, and sample support Q
may not be silently changed.

The E36 matched null demonstrated that the same observed terminal Gram
may arise from two incompatible histories: a unimodular change on
G_shift (original det100), or a nonunimodular rescaling on G_unit
(original det4). E37 makes the frame certificate explicit.

## Theorem A — arbitrary rank, algebraic sufficiency

For square integer matrices G,U,H of arbitrary finite rank n,
an integer diagonal d_i and a valid frame
    det(U) = +1 or det(U) = -1,
a complete integer Gram congruence
    U G U^T = diag(d_i) H diag(d_i)
implies
    (product_i d_i)^2 divides det(G).

The proof uses the exact determinant multiplicativity over Z,
det(U^T)=det(U), and det(diag(d))=product_i d_i.
It works without requiring real, Euclidean, positive,
diagonalizable or invertible G.

For d_i=p^(e_i), this is the advertised factor p^(2 sum_i e_i).
The source file currently states the equivalent squared product.

## Theorem B — actual original rectangular Gram

Replace G by the **complete original**
integerRectangularTraceGram Q D J R S of dimension n=R*S.
If the exact integer congruence certificate is supplied,
the same divisor follows. No auxiliary minor is introduced.

This is still CONDITIONAL on constructing the certificate
for a particular original Q; it is not an automatic
prime-mass improvement.

## Theorem C — transparent source-jet interface

Let E be an integer evaluation matrix, B an integer
coefficient trace metric, and F an integer row quotient.
A valid source certificate explicitly includes:

    E B E^T = integerRectangularTraceGram Q D J R S,
    U E = diag(d) F,
    det(U)=+1 or det(U)=-1.

Then the original determinant inherits (product_i d_i)^2.

Crucially, a proposed E is **not silently deemed**
to be the actual original ordinary-jet matrix. The displayed
identity to the existing original Gram must be established
from all original source samples and derivative slots.

The file proves the algebraic implication for arbitrary
finite m and n, but does NOT yet construct a general
canonical indexed E_Q with columns covering every original
(j,q,real/imag) witness and prove this identity.

## Verification and genuine null controls

- Positive finite case: E36 Qshift with
  G=[[4,14],[14,74]], U=[[1,0],[-1,1]],
  d=(1,5), H=[[4,2],[2,2]].
  Exact integral U G U^T=diag(d)Hdiag(d), detU=1.
- Negative finite case: E36 fake V=[[1,0],[0,5]],
  detV=5, produces the same terminal matrix from a
  different original G with determinant4. V is **not**
  IntegerUnimodular and cannot invoke the theorem.
- No source resampling, real/rational isometry, changed
  jet operation, changed trace sign or selected minor
  is permitted.
- New theorem remains H until exact-head Lean,
  allowed axioms and full source audit pass.
- Even if code passes, the complete thin-ellipse
  E_Q/B identity and nontrivial row-extraction
  certificate are separate H obligations.
- E37 does not improve 307^4 or prove ETH/P vs NP,
  arithmetic valuation for all quadratic fields,
  or a sheaf/holonomy complexity obstruction.

## Immediate next theorem

Construct a canonical, complete E_Q using column slots
(j,q,real/imag) of the original integerDerivativeRow and
B=diag(2,2D), exactly once for each sample/derivative pair.
Prove E_Q B E_Q^T = original integerRectangularTraceGram.

Then derive integral row operations from actual sampled
arithmetic witnesses on the **thin** source, and measure
whether any p-adic factor exceeds the existing certified
same-Gram lower bound. The field-level source-to-discriminant
interpretation remains separately subject to independent review.

*Algebraic sufficient condition != verified arithmetic source premise.*
