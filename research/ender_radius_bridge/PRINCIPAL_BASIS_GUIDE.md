# The principal class has no prime points on the axis

**Checked locally in Lean for actual ideals in the odd maximal-order chart.**
This supplies the principal-class basis choice that the generic coordinate
theorem deliberately left open. It gives no new numerical cutoff.

The hypothesis ClassGroup.mk0(J)=1 concerns this particular ideal J.
It says J is principal. It does not say the number field has class number
one, or that its whole ring of integers is a PID.

Choose a nonzero generator g of J. Multiply the existing ambient basis
(1,omega) by g. This is an actual integral basis of J, constructed using
Mathlib's basisSpanSingleton and transported through the ideal equality.

Multiplication by g changes every norm by the same factor:

    Norm(g*(x+y*omega)) = Norm(g)*Norm(x+y*omega).

Here Norm(g)=N(J), with positive norm in the imaginary quadratic chart.
Dividing by N(J) cancels the factor. Thus the normalized form is exactly

    Q_J(x,y)=x^2+x*y+((D+1)/4)*y^2.

The leading coefficient is1. This works for proper principal ideals as
well: in D=7, the ideal(2) has norm4, and that factor4 cancels from the
normalized form. The positive control is not restricted to the unit ideal.

On the zero row y=0, this form is x^2. If an actual element had
|Norm(z)|=p*N(J) for prime p, norm positivity and cancellation would give
x^2=p. The square of an integer cannot be prime. Therefore every such
normalized-prime-norm element has nonzero second coordinate in this basis.

For any finite set U of these actual elements with norm magnitude<=N(J)*t,
where t is natural, the checked geometric count now applies to ALL of U:

    card(U)<=2*pi*t/sqrt D+4*sqrt(t/D).

The caller supplies no off-axis assumption. The basis is chosen before
all primes, finite sets and thresholds. This is the actual principal-class
zero-row saving behind the two-class bookkeeping.

The control with coefficient3 and form3x^2+xy+1001y^2 still has prime value3
at(1,0) and(-1,0). A generic basis/form cannot silently inherit the a=1
axis saving; choosing the calibrated basis is part of the proof.

Other classes still need controlled bases and quantitative leading bounds.
The even chart, class-wide usable arithmetic B and field-parameter transport
remain open. [Exact verification](PHASE73_VERIFICATION.md). This standalone
result is outside production CI; no new cutoff or classification is claimed.
