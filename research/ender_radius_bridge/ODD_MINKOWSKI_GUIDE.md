# The field-size term becomes a function of the discriminant

The odd-chart weighted determinant bound no longer contains an unknown
field-dependent Minkowski term. Lean now derives its exact value:

    M(K) = (2/pi)*sqrt(D).

Here K is the actual field with generator satisfying
u^2-u+(D+1)/4=0, D is squarefree, and D=3 mod4. Squarefreeness matters:
the integral basis must describe the full ring of integers, not a smaller
order. This is why a discriminant calculation for a convenient polynomial
alone would not suffice.

Three facts determine the answer.

1. **Degree two.** The field has two rational dimensions.
2. **One conjugate pair.** A real image of u would force
   (2u-1)^2+D=0 with D>0. No real number can satisfy that equation.
   Both embeddings are therefore complex, forming one conjugate pair.
3. **Actual discriminant -D.** The existing maximal integral-basis theorem
   identifies the discriminant of the field itself.

Mathlib's Minkowski expression then simplifies to

    (4/pi)^1 * (2!/2^2) * sqrt(abs(-D)) = (2/pi)*sqrt(D).

Conjugation is doing concrete work: one complex pair fixes the exponent
of 4/pi. Degree two fixes the factorial ratio. Maximality fixes the
quantity inside the square root. All three must refer to the same field.

Substitution into the checked closed-kernel bound gives the explicit cost

    alpha_D = pi/sqrt(D) + 2*sqrt(((2/pi)*sqrt(D))/(3*D))
    C_D(L) = alpha_D*(log(3)+log(L)*(1+log(L))) + log(3)/6.

The integrated theorem proves, on the SAME original derivative Gram,

    prime mass <= log(product of Gram diagonal)
                  + R*(R-1)*S*C_D(L) + R*S*(S-1)*log(D).

It retains actual class number<=2, finite odd-prime bounds and the explicit
Ender-radius guard. It assumes no counting function, coverage assertion,
Minkowski identity, earlier cutoff or known list of fields.

This closes the odd-chart field-size substitution. It is not a numerical
contradiction: parameters and a strict margin still need proof. The even
chart and transport to an arbitrary field also remain separate. The
class-number-one cutoff stays50billion; no classification is announced.

[Exact verification](PHASE84_VERIFICATION.md) records target attempts,
integration checks and their limits. External CI and independent human
review must not be inferred from local Lean checks.
