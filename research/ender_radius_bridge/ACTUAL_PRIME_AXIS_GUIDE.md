# The missing row costs two points, except in the principal class

**Checked locally in Lean on actual ideal elements.** The per-class
prime-norm count now includes the zero row; the caller no longer has
to exclude those elements.

In the chosen actual basis, normalized norm is

    Q(x,y)=a*x^2+b*x*y+c*y^2.

On the zero row y=0, this is a*x^2. If it equals a prime p, prime
factorization forces a=p and x=1 or -1. Thus the whole zero row can
contain at most two prime-normalized elements, even when we consider
many primes at once. Injective coordinates make this a bound on actual
elements of J, not merely a picture of the quadratic form.

In the principal class we can do better. Keep the SAME bounded ideal J,
but use the calibrated basis obtained by multiplying the ambient basis
by a generator of J. Its normalized coefficient is a=1. A square cannot
be prime, so this class has no prime-normalized elements on the zero row.

For each actual class C under h<=2 in the squarefree odd chart, the theorem
now chooses one bounded ideal and one controlled actual basis before all
finite sets and thresholds. It preserves lifting of every ideal of that
class into the same J, and proves for any finite set U of prime-normalized
elements with norm magnitudes<=N(J)*t:

    card(U) <= 2*pi*t/sqrt(D) + 4*sqrt(M(K)*t/D)
               + (0 if C is principal, otherwise 2).

No off-axis guard is supplied. The nonprincipal basis has0<a<=N(J)<=M(K);
the principal basis has a=1. Both are actual bases of the selected ideals.

If we can join the class counts to four distinct labelled representatives
per eligible prime, the total axis allowance is2(h-1), at most h for h<=2.
The scalar accounting for that inequality was checked earlier. The new
theorem supplies the ACTUAL per-class counts that accounting needs.
The class-wide four-lift aggregation on these same chosen ideals still
requires its own proof; matching counts on different ideal families would
not close it.

The a=3 control retains both axis points; a=1 and the actual zero element
are excluded from prime-normalized axis witnesses. Coordinate negation
preserves the sign-pair structure. The failed first source assembly and
passing second run are both saved. [Verification](PHASE79_VERIFICATION.md).

This standalone result is outside production CI. Aggregate B, even/field
transport and a new cutoff remain open. No classification is announced.

Current integration: [Phase80](COMMON_FAMILY_GUIDE.md) now supplies the
SAME controlled ideal family with both full per-class counts and the
four selected prime lifts. Class-slice summation to B is still separate.
