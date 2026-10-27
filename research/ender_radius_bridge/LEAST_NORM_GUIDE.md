# A least-norm vector cannot be an integer repeat

**Checked locally in Lean for actual ideals in the squarefree odd
maximal-order chart.** This closes the primitivity step left after
[class squaring](CLASS_SQUARE_GUIDE.md). The separate [basis-completion interface](BASIS_COMPLETION_GUIDE.md) is now
checked; their chosen class-family composition remains open.

An element of an ideal is primitive when it is not a nontrivial integer
multiple of another element of that ideal. Its coordinates then have
gcd one in every integral basis. This property belongs to the element
and the lattice; it does not depend on our choice of coordinates.

Choose a nonzero ideal element whose algebraic norm magnitude is least
among all nonzero elements of that ideal. This minimum exists because
the norm magnitudes are positive integers. Lean uses well-ordering of
the natural numbers, without a numerical search or compactness argument.

Suppose its coordinates in any basis are (m,n)=d(u,v), with d the
positive coordinate gcd. The element w=u*e0+v*e1 belongs to the same
ideal by the integer module operations, and z=d*w. It is nonzero.
The actual quadratic norm satisfies

    |Norm(z)| = d^2*|Norm(w)|.

Minimality says |Norm(z)|<=|Norm(w)|. Since |Norm(w)|>0, cancellation
gives d^2<=1. Therefore d=1. The proof works for any basis supplied
after the minimum has been chosen.

Class number at most two supplies the bound on this minimum. First
choose the existing bounded representative J for each class. Class
squaring supplies v in J with |Norm(v)|=N(J)^2. The least-norm element
z therefore satisfies

    |Norm(z)| <= N(J)^2,       N(J) <= M(K).

The minimum z may differ from v. We do not assert (z)=J^2; that ideal
identity belongs to v. The new theorem retains the bound, minimality,
nonzeroness and primitivity in every actual basis of J.

The scaling proof uses the actual ambient integer-basis norm identity.
It avoids the chosen normalized-form witness assembly that exhausted
the [stopped basis attempt](CONTROLLED_BASIS_ATTEMPT.md). That source
and its failure remain unchanged. The new proof is not a repaired run.

Controls check scalars zero and -2, the nonprimitive pair (4,6), and
the actual element 1 in the D=7 unit ideal: it has coprime coordinates
in every integral basis. Two failed control-proof assemblies and the
passing third run are all preserved in the [verification](PHASE76_VERIFICATION.md).

The separate basis-completion theorem now supplies those two steps from
this primitive/norm interface. Composing the actual chosen class family
and integrating the accepted sources still require a separate check. This standalone proof is outside production
CI; class-wide counts, even-chart transport and a new cutoff remain open.

Current integration: [Phase78](PHASE78_VERIFICATION.md) composes the accepted
principal/least-norm/basis sources into one controlled actual class-family
count. Its local checks pass; external exact-head CI and aggregate B remain
separate. Earlier standalone scope statements above describe their checkpoints.
