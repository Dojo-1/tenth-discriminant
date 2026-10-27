# One controlled lattice for an entire ideal class

**The odd-chart class-family bridge is now composed in Lean.** Assume
the actual quadratic field has class number at most two, with squarefree
D=3mod4. For each actual ideal class C, the theorem chooses one nonzero
integral ideal J, one actual integral basis and one normalized norm form

    Q(x,y)=a*x^2+b*x*y+c*y^2,
    0<a<=N(J)<=M(K),       4*a*c-b^2=D.

Here M(K) is the existing explicit Minkowski bound for the actual field.
No ideal, primitive vector, basis, form or coefficient bound is supplied
by the caller. These choices are made before all later sets and thresholds.

Why the coefficient is controlled: class number at most two makes each
class its own inverse. A bounded representative J has J^2=(v), providing
|Norm(v)|=N(J)^2. Choose a least-norm nonzero z in J instead. It has no
larger norm and is primitive in every integral basis: otherwise dividing
its coordinates by their gcd would give a smaller positive norm.

Bezout's identity then completes z to an actual integral basis through
a determinant-one integer operator. In this basis, the actual normalized
norm of the first vector is a. Cancelling N(J) in the norm identity gives
a<=N(J). The minimum z need not generate J squared; v supplied that bound.

The same J also lifts every ideal I of class C to an element satisfying
(w)=I*J, with exact norm multiplication and ideal recovery. This matters:
we have not switched representatives between the arithmetic and geometry.

For any finite U of actual elements of this J, with norm magnitudes at
most N(J)*t and nonzero second coordinates in the chosen basis, Lean proves

    card(U) <= 2*pi*t/sqrt(D) + 4*sqrt(M(K)*t/D).

This replaces the formerly uncontrolled coefficient in the error term
by a single field-dependent bound shared by the classes. It counts actual
ideal elements, using the same basis and form throughout.

What remains: count axis elements, combine the classes with the four-lift
prime multiplicity, and turn that into the excluded-prime budget B used
by the original determinant. The even chart, field-parameter transport
and a new numerical cutoff are separate obligations. This per-class
result alone does not close them. The h=1 cutoff stays 50 billion.

The [principal-class calibration](PRINCIPAL_BASIS_GUIDE.md) is also integrated
locally. Accepted sources are transported with import changes only; both
stopped attempts remain unchanged. [Exact verification](PHASE78_VERIFICATION.md)
separates local library/dependency checks from future exact-head CI and
independent human review. Nothing here announces a full classification.
