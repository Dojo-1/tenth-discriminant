# The prime lifts and the count now use the same ideals

**The compatibility bridge is checked locally in Lean.** One fixed actual
ideal family now supplies both the full per-class prime-point counts and
four selected distinct labelled points per admissible prime.

Why a new bridge was needed: the old multiplicity theorem chose its own
bounded ideal family. The controlled-basis theorem made a different
choice. Counting elements of one family cannot bound points constructed
in another without a proved transfer between them.

The new lifting interface works for ANY specified family J_C whose ideal
class is C inverse. If a residue kernel I has class C, then I*J_C is
principal. A generator z belongs to J_C and satisfies

    (z)=I*J_C,       |Norm(z)|=N(I)*N(J_C).

No new representative is selected during this step. Exact ideal recovery
remembers which kernel produced z.

For an odd prime not dividing D, the two square roots of -D produce
distinct residue kernels. Their generators and negatives yield four
distinct class-labelled points. If two labels agree, ideal recovery
still separates the kernels. Nonzeroness separates each sign pair.

Different primes cannot share a labelled point: the norm equations would
give p*N(J_C)=q*N(J_C), hence p=q because N(J_C)>0. Thus a finite set P of
admissible primes has a selected point set U with

    card(U)=4*card(P).

Now choose J_C from the actual controlled count theorem under h<=2 in
the squarefree odd chart. Each class is self-inverse, so those ideals
meet the lifting interface. For each class we retain its actual basis,
norm form, coefficient bound and full prime-point count, with axis
allowance0 in the principal class and2 otherwise. The SAME J_C supplies
the selected points above. The family is fixed before every finite P.

What remains is precise finite bookkeeping: form each class slice of U
as actual elements of J_C, apply its count, and sum those slice cards.
That has not yet been joined into a numerical prime-prefix bound B.
The earlier scalar accounting alone is insufficient. Weighted-budget,
even-chart and field transport, and a new cutoff remain separate.

Controls preserve the empty set, modulus-zero failure, characteristic-two
sign collapse and an actual ramified-root collapse. These explain the
guards rather than removing them. [Exact verification](PHASE80_VERIFICATION.md).
Local checks are distinct from external exact-head CI and human review.
No full classification is announced.
