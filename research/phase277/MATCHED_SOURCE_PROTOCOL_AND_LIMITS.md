# Phase277 — matched inert/split local pairing on the original D=283 Gram

**11 November 2026; provenance:** the question and multiframe research strategy are user-originated. The numerical ranks were first observed in a model-authored local exploratory calculation, *before* this note. Consequently these assertions are POST-HOC REPRODUCTION TARGETS, not prospective independent predictions. The present new contribution is a source-typed regression with a split-prime and wrong-metric negative control, not a newly proved analytic number theory theorem.

## Frozen source

D=283 (squarefree, 283≡3 mod4), rho=31, R=70, S=J=2,
complete Q={(x,y)∈Z²:x²+283y²≤31²}, |Q|=169. There are 140
original row-major monomials Z^r W^s and 676 integer-coordinate
columns (ordinary ∂_Z^j derivatives, j=0,1, W held fixed).
The ORIGINAL trace metric is B=diag(2,566,2,566,...). The source
is G=E B Eᵀ, not a substituted Euclidean or Hasse Gram.

The field is NOT assumed to have class number one. In fact, its split
prime 7<283/4 violates the inertness necessary for class number one.
This is an intentionally hostile control, not an exceptional field claim.

## What was previously known

Phase206/208 already constructed these original D283 and D403 source
families, proved the p-local *old Frobenius* row normalization for inert
p3,p5, and measured additional evaluation-index defects on these
finite specimens. Phase205 (D19, a DIFFERENT same-source geometry
with R8,SJ4) already showed that split p5 has a nonzero fully saturated
residual Gram valuation (4), and split p7 has zero, while inert p3 has
residual valuation 1. Therefore "positive residual valuation iff inert"
is already contradicted by the archive and must not be revived.

This Phase277 panel adds a **same D283, same Q, same E** split-prime
negative comparator p7 and explicit correct trace metric/wrong metric
and discarded high ordinary jet controls.

## Frozen local operators

For an odd INERT prime p in {3,5}, set

  k_(r,s)=min(floor(r/p), 1-s) in {0,1},
  F_(r,s)=Z^(r-pk)W^s (Z^p-W)^k.

This is the repository's old certified integral, unitriangular
Frobenius row frame with W held fixed during ordinary Z differentiation.
For every original point and derivative coordinate, divide the row
by p^k ONCE, then reduce modulo p. Call the resulting 140x676 matrix C0.

The old already-counted source mass is F_p=sum_(r,s) k_(r,s):
F_3=67 and F_5=65. These values are not newly discovered divisors.
At the SPLIT p=7, the inert Frobenius factorization is illegal:
use k=0 and C0=E mod7, F_7=0. All three p avoid p|2D, so the
ambient trace metric B modp is nondegenerate.

Let r_p=rank_Fp C0, q_p=rank_Fp(C0 B C0ᵀ), and

  delta_p = r_p-q_p.

This is exactly the dimension of the radical of the original metric
restricted to the UNSATURATED row image im C0ᵀ over Fp. It does
NOT equal the radical of the fully p-adically SATURATED evaluation
lattice, because r_p<140 at all three primes.

## Reproduced finite results (not uniform in D or p)

| p | chi_{-283}(p) | old Fp | rank C0 | rank(C0BC0ᵀ) | delta(image) | evaluation defect 140-r |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | -1 (inert) | 67 | 36 | 10 | 26 | 104 |
| 5 | -1 (inert) | 65 | 60 | 32 | 28 | 80 |
| 7 | +1 (split) | 0 | 28 | 28 | 0 | 112 |

Interpretation: two inert primes carry nonzero radicals of the
UNSATURATED normalized row-image pairing. The split prime does not
on THIS source. This does **not** imply inertness is necessary or
sufficient for primitive residual Smith depth; the D19 fully
saturated split-prime counterexample from Phase205 already prohibits
that generalization.

## Independent controls and discriminating defects

- The executable derives normalized rows using integer-pair modular
  exponentiation and explicit ordinary derivatives, while a separate
  original integer-jet oracle from Phase204 checks first/middle/last
  rows, high derivatives, and complete original points selected before
  performing the assertions.
- Two implementations of finite-field elimination (NumPy-vectorized
  and scalar Python) agree on the 140x140 Gram ranks.
- Reversing all columns and their corresponding trace weights preserves
  G; a nontrivial invertible row shear preserves rank C0 and Gram rank.
- DISCARDING j=1 changes rank(C0) to (18,30,14) at (p3,p5,p7),
  exactly half the full-source ranks. It is not a valid production
  simplification.
- Replacing B=diag(2,566) by the FALSE Euclidean diag(2,2)
  changes the split p7 Gram rank from 28 to 26. One must not silently
  identify these metrics. The inert ranks happen not to move in these
  particular cases; that cannot justify the substitution.

All constraints use p-units in the original metric. The split comparator
is not a surrogate "null" with a changed D, Q, radius or jet order.


## Inert-prime no-double-counting theorem killer (exact 2-row control)

This is an **abstract lattice counterexample with the same positive
trace-metric shape**, NOT an original ordinary-jet evaluation E. It
refutes a proposed universal *algebraic* inference from UNSATURATED
image-pairing radicals to additional p-valuation, even at inert p.

Take D=7, p=3 (inert), B=diag(2,14,2,14), and

    C0 = [[1,0,1,1],[3,0,0,0]],
    Cprim = [[1,0,1,1],[1,0,0,0]],
    Delta = diag(1,3),  C0=Delta*Cprim.

Then the original-shaped positive trace pairing gives

    G0=C0 B C0^T=[[18,6],[6,18]],   detG0=288=3^2*32.
    H =Cprim B Cprim^T=[[18,2],[2,2]], detH=32 (3-adic unit).

Mod 3: rank C0=1, rank G0=0, and the *unsaturated image* pairing
radical has dimension 1. Yet rank Cprim=2, rank H=2, and **primitive
residual valuation is exactly 0**. Its full v3(detG0)=2 is exhausted
by twice the single p-adic evaluation-index exponent. The tempting
but invalid formula v3(detG0)>=2(n-rank C0)+(rank C0-rank G0)
would predict 3 and is **false**.

This small example is an adversarial control, not evidence about a
production determinant. Precisely because even an inert trace-metric
model kills the universal addition rule, **the Phase277 (26,28)
unsaturated radicals must not be promoted to uncounted valuation
factors** without constructing the primitive Smith-normalized Cprim
for the SAME production source and checking non-overlap.

## Non-double-counting and open theorem

No number in delta_p can be appended to the existing Frobenius or
evaluation-index lower bound as an independent p-adic exponent.
The original Frobenius Fp was consumed once in creating C0.
The deficit 140-rp captures *additional evaluation-index* constraints
but C0 is not primitive; a p-local Smith iteration must first saturate
the evaluation image to C_prim before one can assign primitive
residual pairing factors.

Exact p-adic structure (classical, given full rank over Qp):
U E=Delta C_prim with U invertible over Zp and C_prim modp full row rank,
and H_prim=C_prim B C_primᵀ, hence

  v_p(det(E B Eᵀ)) =
    2 sum_i v_p(Delta_ii) + v_p(det H_prim).

The first summand already includes the old Fp and any newly found
evaluation-index mass; the second captures a genuinely distinct
restricted-pairing residual. Even then, its extra valuation might have
already appeared implicitly in an existing proof. The source comparison,
normalization and non-overlap must be audited BEFORE claiming new mass.

**Candidate H:** on the growing **production** source (R=floor D/4,
S=J=floor R/25, original thin Q(D)), is there a nonnegative, source
certified *uncounted* residual prime mass of order R²S log D?
The present D283 finite rank results DO NOT support such a uniform
asymptotic statement. A fixed collection of primes with only O(R²S)
residual valuation would contribute only O(1) after normalizing by
R²S and cannot fix the conductor-scale logarithmic gap.

**Kill rule:** if the primitive full Smith normalization erases the
candidate radical, or a matched split-prime control explains the
same effect, reject inert-specific residual-pairing gain. Stop before
new geometry unless it yields a source-identical and numerically
discriminating invariant. Prior art Phases205–208 and semantic review
#50 remain explicit.

**Merge boundary:** scoped finite regression and documentation only.
A passing workflow establishes executable reproducibility (M), not
independent peer review, source-to-field validation, a new discriminant
cutoff or an exclusion of Siegel zeroes.
