# One field family; both parity cases; an effective bound

## The precise result

For every positive squarefree integer d, Lean proves

    classNumber(Q(sqrt(-d))) = 1  implies  d < 700000000000.

The actual encoded field is `ImaginaryQuadraticField d`, an alias for
`AdjoinRoot (X^2+C (d : Rat))`. The bound is directly about Mathlib's
`NumberField.classNumber` of that field, not a Boolean test or a piecewise
replacement for class number. The declaration is
`imaginaryQuadratic_classNumber_one_radicand_bound` in
[QuadraticChartEquivalence.lean](../../lean/TenthDiscriminant/QuadraticChartEquivalence.lean).
Its only assumptions are positivity, squarefreeness and actual class number one.

This closes the parity gap in the effective radicand bound. **It is not the
class-number-one classification:** the finite odd range below the bound
is not yet classified in Lean. No improved constant, novelty, independent
human review, Mathlib-upstream suitability or Tao submission is claimed.

## Why the two cases differ

Use d for the squarefree radicand, as in Tao's post. Earlier files use D
for the absolute fundamental-discriminant convention: D=d for d=3 mod 4,
and D=4d otherwise. Do not interchange those symbols without the factor four.

The integer rings have different natural generators:

| Radicand class | Integer generator | Integer coordinates |
|---|---|---|
| d=3 mod 4 | omega=(1+sqrt(-d))/2 | x+y*omega |
| d=1 or 2 mod 4 | theta=sqrt(-d) | x+y*theta |

Squarefreeness excludes d=0 mod 4. The first chart uses the
[checked determinant cutoff](ODD_CUTOFF_GUIDE.md). The second needs no large
determinant: the prime 2 supplies an obstruction for every d>2.

## The even-discriminant argument in five steps

1. Write a field element as a+b*theta with rational a,b. Its actual trace
   is 2a; its actual norm is a^2+d*b^2. These formulas come from the matrix
   of multiplication in the basis (1,theta).
2. Integral trace and norm imply 2a=m and 2b=n for integers m,n. The earlier
   squarefree denominator lemma supplies the second assertion. Since
   4 divides m^2+d*n^2, squares modulo 4 force both m and n even when
   d=1 or 2 mod 4. Hence a,b are integers. This proves that Z[theta] is the
   **actual maximal integer ring**, not merely an order inside it.
3. Modulo 2, send theta to d mod 2. The relation theta^2+d=0 holds in F2.
   Thus the actual integer ring maps onto F2; its kernel has ideal norm 2.
4. Class number one makes that ideal principal. The existing general norm
   theorem then supplies an algebraic integer of norm magnitude 2.
   The positive norm x^2+d*y^2 removes the absolute-value ambiguity, giving

       x^2+d*y^2=2.

5. For d>2, y nonzero already contributes more than 2. For y=0, x^2=2 is
   impossible in integers. Thus class number one forces d=1 or d=2 in
   this chart. The norm-two examples (x,y)=(1,1) for d=1 and (0,1) for d=2
   are retained. Those controls do not themselves prove class number one.

The mod-4 guard matters: for d=3, (1+theta)/2 has integral trace and norm,
but its coordinates are not integers. It is a checked counterexample to
using the trace-zero order as maximal without the congruence guard.

## Joining charts without changing the field

For d=3 mod 4, the two rational quotient fields are explicitly equivalent:

    theta -> 2*omega-1,    omega -> (1+theta)/2.

Lean checks the polynomial relations and both inverse identities. The
equivalence restricts to an equivalence of their actual integer rings.
The PID property, and hence class number one, transports along it.
Therefore the Phase28 odd cutoff applies to the **same** trace-zero field
used in the even argument. There is no numerical premise or unproved field
identification left in the radicand-bound statement.

The supplementary `absoluteDiscriminantParameter` uses the conventional
formula d or 4d and is also bounded by 7e11 under class number one. This
phase does not prove a separate identity with Mathlib's `NumberField.discr`;
the principal radicand cutoff requires no such identity.

## What changed, and what did not

The [protocol](PHASE29_PROTOCOL.md) was committed before proof edits. This
was a proof-bridge attempt, with exact algebraic controls, not another
numerical campaign. No production certificate, radius, threshold, tool,
dependency pin or inherited audit gate changed. No new Heegner/classification
input was used. Failed cast/simplification attempts and elaboration limits
are preserved; the final maps use explicit coefficient evaluation and
generic generator lemmas under the default proof budget.

The source layers are [coordinates](../../lean/TenthDiscriminant/EvenOrderCoordinates.lean),
[field and trace/norm](../../lean/TenthDiscriminant/EvenQuadraticField.lean),
[maximal order](../../lean/TenthDiscriminant/EvenMaximalOrder.lean),
[prime-two argument](../../lean/TenthDiscriminant/EvenClassNumber.lean), and
[field equivalence and cutoff](../../lean/TenthDiscriminant/QuadraticChartEquivalence.lean).

From `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`, and
`lake env lean ../research/ender_radius_bridge/Phase29SignatureCheck.lean`.
Exact published-tree CI belongs in the PR's final verification record.
Local wrapper deadlines remain separate from individual/remote passes.

Next: connect and verify the finite odd classification, obtain independent
semantic review, and keep the remaining Tao-objective accounting honest.
