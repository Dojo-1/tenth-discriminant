# What survives a compatible change of regime?

A scalar cutoff is the conclusion of an estimate. Our organising question
is what remains the same when we change the presentation of the objects,
observables and operators used to obtain that estimate.

## Transport the whole sampled object

The useful object is an integral lattice of observables L inside a real
vector space V, a jet-sampling map E:V→W, a positive inner product q on W,
and compatible reductions modulo primes. The Gram entries are
G_ij=q(E f_i,E f_j) for a chosen integral basis of observables.
A transport needs maps U_V,U_W satisfying

    E' U_V = U_W E,       q'(U_W x,U_W y)=q(x,y),       U_V L=L'.

The local reduction maps must commute too. In the transported basis these
identities preserve the actual Gram entries, hence the determinant and
its arithmetic obstruction. For jets, the differential operator must also
be transported: D'=U_V D U_V^{-1}. Each compatibility is a proof obligation.
The translation instance is now [checked standalone](PASSIVE_TRANSPORT_GUIDE.md);
the full abstract interface across all regimes is not formalized here.

| Structure or observable | What survives, with its condition |
| --- | --- |
| Actual number field, ring of integers, ideal classes, discriminant | Field isomorphism preserves the actual class number and discriminant. Checked here, including the arbitrary-field transport. |
| Original arithmetic Gram and prime-power obstruction | The proved integral matrix identifications and unimodular congruences concern the SAME integer. Arbitrary real/complex reparametrization alone does not establish integral compatibility. |
| Sample distinctness, jet separation and positivity | Survive the checked injective/affine transports with their point-count and derivative-depth guards. A new operator regime must preserve the relevant sampling map and positivity assumptions. |
| Lattice index | Cannot disappear under a change of presentation. The odd chart's index two and the even discriminant's factor four must be retained. |
| Coordinate Gram spectrum and Hadamard diagonal product | Depend on basis/metric choices. An intrinsic operator spectrum needs the domain metric transported as well; congruence alone preserves rank and inertia, not ordinary matrix eigenvalues. |
| Computational hardness | Requires computationally bounded, witness-preserving transports and a stated cost model. Our noncomputable algebraic equivalences do not supply those complexity bounds. |

## Our24→60 example identifies an incomplete transport

The checked example shifts the sample points while keeping the monomial
observables1,z fixed at their old origin. This is an ACTIVE change of the
sampled object, not a passive change of coordinates of the whole object.
Its determinant changes from24to60; the [Lean counterexample](../../lean/TenthDiscriminant/CoordinateTranslation.lean)
remains correct. It does not disprove fully compatible transport.

For a translation by c, a compatible passive change uses z'=z+c and
f_c(Z,W)=f(Z-c,W-conj(c)). Ordinary Z derivatives then satisfy

    (∂_Z^j f_c)(z+c,conj(z)+conj(c))=(∂_Z^j f)(z,conj(z)).

Thus transporting the observables as well as the points recovers the same
sampled jets and Gram. This full polynomial/ordinary-jet translation
interface is now checked standalone at110, including the SAME original
integer Gram. The old active-shift controls and exhausted budgets remain
unchanged; all three new110slots are consumed too.

## The missing phase is visible in a small calculation

For samples-1,0,1 and rows1,z, the complex Hermitian moment matrix H is
[[3,0],[0,2]]. After the active vertical shift, it is
[[3,-3i],[3i,5]]. Both determinants are6. But the original real trace-Gram
is2Re(H): its determinants are24and60. The imaginary cross term cancels
part of the Hermitian determinant; taking the real part discards it.
These Hermitian calculations are paper calculations, not new Lean results.

Keeping both real and imaginary channels restores a larger covariant
representation, but it changes the observable if we simply replace the
original determinant. For rows1,i at one sample, the real trace-Gram is
2I with determinant4, while the Hermitian matrix has rank1 and determinant0.
The [checked real/complex control](../../lean/TenthDiscriminant/JetKernel.lean)
already exposes this rank distinction. More channels cannot be substituted
without proving how the original positive integer is recovered.

## What counts as an obstruction

Rank loss, a nontrivial lattice index, a failure of the local reduction
diagram, and loss of a required positive form are structural obstructions.
A bad diagonal estimate or an untransported observable may instead be a
presentation artifact. Changing algebraic regimes also requires checking
which multiplication, associativity and divisibility laws the proof uses.
An embedding into a larger representation needs a faithful recovery map;
it is not automatically an equivalence of the arithmetic problem.

The translation instance of the commuting diagram is now checked for
actual polynomial observables, ordinary jets and the SAME integer Gram.
A claimed improvement must still be separated into an intrinsic
obstruction, a sharper estimate, or a change in the chosen observables.
[Published verification](PR38_MERGE_RECEIPT.md). No lower cutoff or
computational-hardness theorem is claimed by this guide.
