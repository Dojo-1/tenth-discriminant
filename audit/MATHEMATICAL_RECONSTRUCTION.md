# Mathematical reconstruction

## 1. The classical statement and the Lean objects

For a positive squarefree integer \(d\), put \(K_d=\mathbb Q(\sqrt{-d})\). Its ring of integers has basis \(1,\sqrt{-d}\) if \(-d\not\equiv1\pmod4\), and basis \(1,(1+\sqrt{-d})/2\) otherwise. Therefore the *field* (maximal-order) discriminant is

\[
\Delta(K_d)=
\begin{cases}
-d,&d\equiv3\pmod4,\\
-4d,&d\equiv1,2\pmod4.
\end{cases}
\]

The input \(d\) is a squarefree radicand, not itself always the absolute fundamental discriminant. Every imaginary quadratic field has such a radicand, unique up to the usual square-class normalization. The radicands
\[
1,2,3,7,11,19,43,67,163
\]
map to the discriminants
\[
-4,-8,-3,-7,-11,-19,-43,-67,-163.
\]
This is the classical list of fundamental discriminants in the class-number-one theorem under review; the source's radicand list matches it under the maximal-order discriminant map.

The frozen source defines `ImaginaryQuadraticField d` as the root-adjoined quadratic chart for \(X^2+d\). Mathlib defines `NumberField.classNumber K` as the cardinality of the class group of the ring of integers \(\mathcal O_K\), and proves that class number one is equivalent to \(\mathcal O_K\) being a principal ideal ring. Thus the source type of Theorem A has the intended class-group meaning; it is not counting ideals in a nonmaximal order.

The public theorem A is still chart-specific as a Lean type. This is no defect for the classical classification: all imaginary quadratic fields can be represented by a positive squarefree radicand. The source separately makes this representation explicit for theorem B.

The reverse implication (the nine fields really have class number one) is not inferred from the sieve. For discriminant magnitude at most 8, the source invokes Mathlib's Minkowski/PID criterion. For the remaining five, it rules out ideals of prime norm 2 for 11 and 19, and of prime norm 2, 3, 5, or 7 for 43, 67, and 163; Minkowski then gives representatives in every ideal class small enough that those local exclusions force the ideal to be principal.

## 2. Arbitrary totally complex quadratic fields

Let \(K/\mathbb Q\) be a number field of degree two with no real infinite places. Its nontrivial automorphism is complex conjugation under a complex embedding. The repository's construction takes the anti-invariant part \(u=(x-\sigma x)/2\) of an element not fixed by conjugation. Then \(\sigma(u)=-u\), so \(u^2\in\mathbb Q\); its image under the complex embedding is purely imaginary, so \(u^2<0\). Clearing rational denominators and removing square factors produces a positive squarefree \(d\) and an element \(a\in K\) satisfying \(a^2=-d\). Since the degree is two, this yields \(K\simeq\mathbb Q(\sqrt{-d})\).

This construction does not use class number one. The discriminant and class number then pass through the algebra equivalence. Consequently theorem B's displayed field hypotheses genuinely cover arbitrary totally complex quadratic number fields; no chosen generator or special model is a public assumption.

## 3. From class number one to small-prime nonsquareness

Write \(D>0\), \(D\equiv3\pmod4\), squarefree, and use the integral basis \(1,\omega\), \(\omega=(1+\sqrt{-D})/2\), for \(\mathbb Q(\sqrt{-D})\). Suppose an odd prime \(p\) has a root \(z\) of \(z^2\equiv-D\pmod p\). The root defines a surjective ring map from the maximal order to \(\mathbb F_p\); its kernel has additive index, hence ideal norm, \(p\).

If the class number is one, this kernel is principal. A generator has absolute norm \(p\). In the chosen coordinates its norm is
\[
N(x+y\omega)=x^2+xy+\frac{D+1}{4}y^2,
\qquad
4N=(2x+y)^2+Dy^2.
\]
The norm is nonnegative, so absolute norm \(p\) means norm \(p\), not \(-p\). If \(y\ne0\), then \(4p\ge D\). If \(y=0\), then \(x^2=p\), impossible for a prime. Therefore no root exists when \(p<(D+1)/4\). The inequality must be strict. At \(D=163,p=41\), \(-D\equiv1\pmod{41}\) is a square; this is exactly the excluded endpoint \(p=(D+1)/4\). A prime divisor of \(D\) below the threshold is also ruled out by the same argument because it would give the root zero. The statement excludes \(p=2\), where the local polynomial behavior is different.

For odd \(p\), nonsquareness of \(-D\) is equivalent to irreducibility of \(X^2+D\) over \(\mathbb F_p\). Together with the odd-prime maximal-order chart (the possible index-two discrepancy is coprime to \(p\)), this is the inert-prime condition, not merely a statement that split primes are absent. A ramified \(p\mid D\) in the guarded range would give the root zero and is excluded as well.

## 4. The Gram determinant mechanism

The intended construction samples a rectangular family of bivariate monomials and their \(Z\)-derivatives at points in an ellipse. For a coefficient vector, the associated Gram quadratic form is a sum of squared absolute values of those jet evaluations. It is positive definite if no nonzero polynomial in the stated bidegree range can vanish to the required multiplicity at every sampled point.

The interpolation argument is a contact budget. For an irreducible factor of bidegree \((a,b)\), a Sylvester resultant with a fixed derivative is a nonzero polynomial in the conjugate coordinate, of degree at most \((2a-1)b\). Excessive contact at a fiber forces a root of that resultant. Summing multiplicities bounds the number of such fibers. Factoring a general polynomial and accounting for exceptional specializations yields the stated contact budget \(2r+s\). Hence a strict point-count inequality of the form \(2(R-1)+(S-1)<\#P\), with the derivative-depth conditions in the code, forces positivity.

There are two important distinct steps after this interpolation fact:

1. The analytic/real trace-Gram is identified with the cast of the actual integer-coordinate Gram. This is necessary to infer that the integer determinant is a positive, nonzero integer.
2. The inert-prime congruences are transported through a unitriangular polynomial-basis change. They must make a matching row and column divisible by the appropriate power of \(p\), with an integral middle matrix. A single divisible row and column would only give one power; the generic two-sided factor lemma explicitly requires both. Summing coordinate weights yields a determinant factor \(p^{2F(p)}\).

Thus the determinant's nonvanishing/positivity and its prime divisibility are not interchangeable. The source has separate lemmas for both, but their concrete interaction is the principal unclosed proof risk in this review.

The geometric input is an upper bound for the number of ellipse points using disjoint inward cells and area. Axis points require separate treatment: the source itself records a false “all points own a full inward cell” control, and uses an off-axis restriction. The prime-mass upper bound then uses Hadamard's inequality and diagonal bounds for the Gram. The lower bound comes from the determinant divisibility and factorial prime weights.

## 5. The 50-billion cutoff

The source's cutoff proof is a contradiction for \(D\ge50{,}000{,}000{,}000\), in the \(D\equiv3\pmod4\) case. It converts the class-number-one hypothesis into the guarded nonsquareness at every prime in its chosen range, applies the determinant lower bound, and compares it with the ellipse/Hadamard upper bound. Factorial-prime-mass estimates, tail controls, and recovered contributions at 3 and 5 give the production lower estimate
\[
0.999997\log D-5.739.
\]
The upper estimate in the source is
\[
0.8\log D-0.813.
\]
At \(\log D\ge24.6304\), the affine gap is at least
\[
(0.999997-0.8)\,24.6304-(5.739-0.813)
=0.0000061088>0.
\]
The source formalizes this separation using rational constants and `linarith`; it also provides a natural-number-to-real lower bound for \(\log D\). The strict positive margin is very small, so every coefficient, tail endpoint, guard, and cast matters. This review traced the source chain but did not independently verify every estimate or compile the theorem.

For radicands \(d\equiv3\pmod4\), the field discriminant magnitude is \(d\), so the contradiction gives \(d<50\) billion. For squarefree \(d\equiv1,2\pmod4\), a separate small-field argument forces class-number-one cases to \(d=1,2\), whose discriminants have magnitude \(4,8\). The arbitrary-field theorem transports the bound through the representation above.

## 6. How Theorem A differs from Theorem B's cutoff

The classification theorem does **not** simply apply the public 50-billion theorem and then sieve. Its current source chain uses a separate necessary radicand bound \(d<700{,}000{,}000{,}000\), supplied by `imaginaryQuadratic_classNumber_one_radicand_bound` in `QuadraticChartEquivalence.lean`; its large-\(d\) case invokes `FirstCertificate.odd_large_classNumber_ne_one`. The finite sieve is designed for that 700-billion interval. The 50-billion result is a separate, tighter discriminant theorem in `FiftyBillionCutoff.lean`, with its own cutoff assembly and a generic-field transport. The two routes share determinant/prime-mass ideas, but the code makes the finite classification's dependency explicit rather than deriving it from Theorem B.

## 7. The finite sieve

The classification has a first finite stage below one million and a second stage covering \([1{,}000{,}000,700{,}000{,}000{,}000)\). The class-number-one hypothesis gives \(d\equiv3\pmod8\) for the large range. Each odd prime contributes a forbidden residue condition \(t^2+d\equiv0\pmod p\). The initial wheel lifts exactly the residues satisfying the current nonsquare conditions; the proof constructs quotient/remainder witnesses, so the wheel is not merely a generated candidate list.

For the large interval the modulus is \(M=892{,}371{,}480\), and \(d=r+Mk\). For each additional prime \(p\), the encoded inverse \(a\) satisfies \(Ma\equiv1\pmod p\). The wide mask records the allowed quotient bits after this affine change of coordinates. The initial interval mask bounds the possible quotients by \(k<785\). The final source certificate checks all 11 seeds, while general lemmas show that every candidate in the interval would retain its quotient bit through every filter. If the certificate says each filtered seed has no set bit, this contradicts the retained bit. The finite computation is an ordinary Lean Boolean decision/proof certificate, not an external oracle, if the source proof is accepted by the kernel.

The independent Python script in this audit recomputes all 200 masks from the prime-root condition and verifies 92,964 deterministic quotient/root comparisons. It does not establish that the 11 seeds exhaust the wheel or that the formal all-fibers proof is correct. The latter remains source-audited, not replayed.
