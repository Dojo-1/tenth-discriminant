# Phase162 — A binary lower bound from the original ordinary jets

*1 November 2026. Original source object: the integer-pair ordinary-\(Z\)-jet Gram with \(W\) held fixed and trace metric \(2,2D\). This document separates an explicit mathematical derivation [P-paper], exact finite tests [M], limited Lean proof status [P when CI confirms], and the still-unproved uniform field-endpoint comparison [H].*

Our arithmetic lower bound already contains all eligible **odd** inert primes. Phase155–156 also introduced the valid \(2\)-adic **jet-factorial capacity**. The present construction is different: a **sample-independent unimodular integer row basis** produces a larger binary divisor on the *same determinant*, without relying on a characteristic-subset optimization.

## The one polynomial we need

Let \(\mathcal O_D=\mathbb Z[\sqrt{-D}]\), the **selected integer-pair order**, not necessarily the maximal order. For \(z=x+y\sqrt{-D}\), put \(a=x^2-Dy^2\). Exact multiplication gives

$$
z^4-z^2=\bigl(a(a-1)-4Dx^2y^2\bigr)+
  2xy(2a-1)\sqrt{-D}.
$$

Both integer coordinates are even: the first contains two consecutive factors, the second contains an explicit factor two. Therefore

$$
\boxed{F(z):=z^4-z^2\in 2\mathcal O_D
\quad\text{for every }D,x,y\in\mathbb Z.}
$$

Even more importantly, **all positive ordinary derivatives of \(F(Z)=Z^4-Z^2\) have even integer coefficients**:

$$
F'(Z)=4Z^3-2Z,\quad F''(Z)=12Z^2-2,\quad
F'''(Z)=24Z,\quad F^{(4)}(Z)=24
$$

and higher derivatives vanish. Thus *every* ordinary derivative of \(F\), including order zero when evaluated at any integer-pair point, lies in \(2\mathcal O_D\).

This derivative-level statement is the decisive improvement over an ordinary pointwise Frobenius congruence. A tempting smaller \(Z^2-Z\) **fails**: at \(z=\sqrt{-3}\), its imaginary coordinate is odd. In fact \(F\) has **minimal degree among monic integer polynomials whose reduction mod 2 has zero formal derivative and which vanish on all selected integer-pair points**: derivative zero forces a polynomial \(h(Z^2)\) mod 2; evaluation at \(Z=0,1\) forces \(h(0)=h(1)=0\), hence \(\deg h\ge2\) and \(\deg F\ge4\). This is optimality within that precisely stated class, *not* global optimality of all lower-bound constructions.

## A unimodular row basis; no new Gram

Let \(R,S\ge1\), \(M=RS\), and \(J=S\) as in production. Index the original rows by \(0\le r<R,\ 0\le s<S\). Define \(k_r=\lfloor r/4\rfloor\) and replace the row monomial by

$$
P_{r,s}(Z,W)=Z^{r-4k_r}\bigl(Z^4-Z^2\bigr)^{k_r}W^s.
$$

The expansion

$$
P_{r,s}(Z,W)=\sum_{t=0}^{k_r}
  (-1)^t {k_r\choose t}Z^{r-2t}W^s
$$

contains the old row \(Z^rW^s\) with coefficient one, and every other term has a strictly smaller row-major index. Thus it defines a **unitriangular integral matrix** \(U\) with \(\det U=1\).

The ordinary Leibniz rule is an *integral* sum of products of derivatives. Every one of the \(k_r\) factors \(F\) contributes a factor two, regardless of which ordinary derivatives strike it; the other monomial and the fixed \(W^s\) contribute integral coordinates. Hence every original transformed jet channel in row \((r,s)\) is divisible by \(2^{k_r}\), **without dividing by \(j!\)** or substituting a Hasse jet. Both real and imaginary integer channels have this same factor.

Consequently there exists an integer matrix \(C_Q\) and diagonal \(A=\operatorname{diag}(2^{k_r})\), with each \(k_r\) repeated \(S\) times, such that

$$
UE_Q=AC_Q,\qquad B_Q=2\widetilde B_Q,
\qquad \widetilde B_Q=\operatorname{diag}(1,D,1,D,\dots)
$$

with the appropriate real-only omissions. In particular,

$$
UG_QU^{\mathsf T}
=A\,C_Q(2\widetilde B_Q)C_Q^{\mathsf T}A.
$$

Taking determinants and using \(\det U=1\) gives an **integer identity**, not merely an inequality:

$$
\boxed{
\det G_Q=2^{\Lambda(R,S)}
       \det(C_Q\widetilde B_Q C_Q^{\mathsf T}),\qquad
\Lambda(R,S)=RS+2S\sum_{r=0}^{R-1}\left\lfloor{r\over4}\right\rfloor .
}
$$

Thus \(2^{\Lambda(R,S)}\mid \det G_Q\) for **every** finite integer-pair observation set \(Q\), even an undersampled one with determinant zero. The log lower bound requires \(\det G_Q>0\), which must be shown separately. The row argument works for any fixed ordinary derivative range \(J\); the displayed \(J=S\) matches the existing prime-mass proof.

The exponent has the closed form, for \(R=4q+t\), \(0\le t<4\),

$$
\Lambda(R,S)=RS+2S\bigl(2q(q-1)+tq\bigr).
$$

In fact there is an **exact normalized identity**. With \(t=R\bmod4\),

$
\boxed{4\Lambda(R,S)=S\bigl(R^2+t(4-t)\bigr).}
$

Consequently for all \(R,S\ge1\),

$
\boxed{\Lambda(R,S)\log2/(R^2S)\ge(\log2)/4
  \approx0.1732868.}
$

Equality holds whenever \(4\mid R\). This is an exact discrete consequence of the unitriangular binary row certificate, not an asymptotic extrapolation. The new binary exponent and the previous Phase156 factorial exponent **must not be added**: both are valuations at two. Use their maximum until an independent joint strengthening is proved.

## A two-variable refinement, using the real sampling relation [P-paper / M]

The polynomial \(H(Z,W)=Z^2-W^2\) has a second useful property. At our actual observations \(W=\bar z\),

$
H(z,\bar z)=4xy\sqrt{-D}\in2\mathcal O_D,
$

and all positive **ordinary partial-\(Z\)** derivatives are even:
\(\partial_ZH=2Z\), \(\partial_Z^2H=2\), and higher derivatives vanish.
No conjugate differentiation is introduced.

For each row \(0\le r<R,\ 0\le s<S\), choose

$
b_{r,s}=\min(\lfloor r/2\rfloor,\lfloor(S-1-s)/2\rfloor),
\qquad
a_{r,s}=\lfloor(r-2b_{r,s})/4\rfloor .
$

Use the row polynomial

$
\boxed{\ P_{r,s}=Z^{r-4a_{r,s}-2b_{r,s}}\,
 F(Z)^{a_{r,s}}H(Z,W)^{b_{r,s}}W^s .\ }
$

Its exact expansion is

$
P_{r,s}=\sum_{t=0}^{a_{r,s}}\sum_{u=0}^{b_{r,s}}
(-1)^{t+u}\binom{a_{r,s}}t\binom{b_{r,s}}u
Z^{r-2t-2u}W^{s+2u}.
$

The leading coefficient is one, and all other terms have smaller \(Z\)-degree and remain inside the original \(R\times S\) rectangle, so the change-of-basis matrix is integral unitriangular. Every ordinary jet of this row is divisible by \(2^{a_{r,s}+b_{r,s}}\), by the same integral Leibniz argument. This yields the **stronger** paper-level divisor

$
\boxed{
2^{\Lambda_{\mathrm{mix}}(R,S)}\mid\det G_Q,\quad
\Lambda_{\mathrm{mix}}=RS+
2\sum_{\substack{0\le r<R\\0\le s<S}}
(a_{r,s}+b_{r,s})\ge\Lambda(R,S).
}
$

The choice of \(b\) is maximal within this two-factor row family: when \(b\) increases by one, \(b+\lfloor(r-2b)/4\rfloor\) never decreases. This does **not** establish global optimality among all integer polynomial bases. The new mixed factor is an alternative **stronger 2-primary certificate**, not an independent divisor to multiply with the univariate \(2^\Lambda\).

At \(R=30,S=5\), the floors are \(1130\to1242\), a further **112** guaranteed binary exponents in the very same \(150\)-row Gram. At \(R=8,S=4\), \(64\to80\). The [source-matched verifier](phase162_binary_null_lower.py) expands the row polynomials exactly, preserving ordinary derivatives and trace channels, and tests these claims for \(D=2,3,19,163\). The full mixed-row factorization is **not yet formalized in Lean** and no uniform numerical field bound follows.

## A third generator, from the conjugate coordinate [P-paper / M]

We can do slightly better without introducing a new observation or a new derivative. Because the original derivative holds \(W\) fixed, the polynomial \(F(W)=W^4-W^2\) has **zero positive-order partial-\(Z\)** derivatives, while \(F(\bar z)\in2\mathcal O_D\) at every integer-pair point.

Put \(c_s=\lfloor s/4\rfloor\). Keep the \(a_{r,s},b_{r,s}\) above and change the row to

$
P^\star_{r,s}=
Z^{r-4a-2b}\,
W^{s-4c_s}\,
F(Z)^a\,
\bigl(Z^2-W^2\bigr)^b\,
F(W)^{c_s}.
$

The leading monomial is exactly \(Z^rW^s\), with coefficient one. Its other terms have lower \(Z\)-degree or, at equal \(Z\)-degree, lower \(W\)-degree. All exponents are inside the original rectangle because \(4a+2b\le r\), \(4c_s\le s\), and \(s+2b<S\). The integral change of rows is again unitriangular. The ordinary jets contain \(2^{a+b+c_s}\), so

$
\boxed{
2^{\Lambda_3(R,S)}\mid\det G_Q,\qquad
\Lambda_3=RS+
2\sum_{r=0}^{R-1}\sum_{s=0}^{S-1}
\bigl(a_{r,s}+b_{r,s}+\lfloor s/4\rfloor\bigr).
}
$

There is an exact incremental relation
\(\Lambda_3=\Lambda_{\mathrm{mix}}+
2R\sum_{s<S}\lfloor s/4\rfloor\). For \(R=30,S=5\):
\(\Lambda_3=1302\), compared with the two-variable \(1242\) and
univariate \(1130\). For \(R=2500,S=100\) the three exponents are
\(156250000\), \(162294200\), \(168294200\), respectively. This is a
source-compatible *paper* derivation with independent finite row tests, not
a Lean-checked all-\(R,S,Q\) theorem. No new field cutoff is inferred.

## A useful overlap cancellation: one further binary certificate [P-paper / M]

Instead of introducing an unrelated fourth rule, cancel the leading monomials
of the first two null polynomials:

$
\boxed{K(Z,W)=Z^2(W^2-1)=F(Z)-Z^2(Z^2-W^2).}
$

This exact integer identity reveals a **new leading monomial**
\(Z^2W^2\) even though \(K\) is already in the ideal generated by
\(F(Z)\) and \(Z^2-W^2\). At a sampled point \(z=x+y\sqrt{-D}\) with
\(a=x^2-Dy^2\),

$
K(z,\bar z)=\bigl(a(a-1)+4Dx^2y^2\bigr)-2xy\sqrt{-D}\in2\mathcal O_D.
$

The positive ordinary partial-\(Z\) derivatives are
\(2Z(W^2-1),\,2(W^2-1),\,0,\ldots\), all even. Thus \(K\) has the same
all-jets binary-null property as the other three polynomials.

Within the **four declared generators** \(F(Z)\), \(Z^2-W^2\), \(F(W)\)
and \(K\), choose for each \((r,s)\) nonnegative exponents
\((a,b,c,d)\) maximizing \(a+b+c+d\) subject to

$
4a+2b+2d\le r,\qquad 4c+2d\le s,\qquad s+2b<S.
$

The row polynomial
\(Z^{r-4a-2b-2d}W^{s-4c-2d}F(Z)^a(Z^2-W^2)^bF(W)^cK^d\)
is monic in \(Z^rW^s\); all other monomials occur earlier in the
original row-major rectangle. Its ordinary jets retain \(2^{a+b+c+d}\).
Therefore another paper-level determinant divisor is

$
\boxed{
2^{\Lambda_4(R,S)}\mid\det G_Q,\quad
\Lambda_4=RS+2\sum_{r<R,s<S}
\max_{\substack{a,b,c,d\ge0\\
4a+2b+2d\le r,\;4c+2d\le s,\;s+2b<S}}
(a+b+c+d).
}
$

At \(R=30,S=5\), the successive same-source binary floors are
\(1130,1242,1302,\boxed{1358}\). A [separate exact-source finite
test](phase162_null_syzygy.py) checks this four-generator row action at
\(D=2,3,4,19,163\). This establishes neither global optimality of the
differential-null ideal nor a completed Lean proof of the determinant
factorization. The method is intended to *discover* useful leading-term
relations, not accumulate hard-coded metaphors.

## Finite evidence against the original source [M]

The [executable controls](phase162_binary_null_lower.py) import the Phase159 evaluator, already cross-checked against Phase147, retaining **ordinary derivatives**, the exact \(2,2D\) metric and unchanged integer-pair order. They explicitly build every transformed row and check integer divisibility, including the root-selection support and multiple small examples.

| Source configuration | Phase156 factorial floor \(\beta_2\) | Phase162 universal floor \(\Lambda\) |
| --- | ---: | ---: |
| \(D=19,R=8,S=4\), large real sample | 32 on a sufficiently oversampled complete sample | **64** |
| \(D=163,R=30,S=5\), 31 effective characteristic roots | **430** | **1,130** |
| \(D=163,R=30,S=5\), 30 roots, central deletion | **450** | **1,130** |

The stronger two-variable certificate is **1,242** for both D163 supports (the respective factorial capacities remain 430/450). For the 30-root square support, Phase159 independently measured \(v_2(\det G)=3,200\), so 1,130 is a nontrivial but **not sharp** lower certificate. Adding or deleting roots changes the determinant; these certificates apply to **each named original Gram separately**.

The control suite also checks that \(F(z)\) is coordinatewise even across multiple \(D,x,y\), that *all positive ordinary derivative coefficients* of \(F\) are even, that \(Z^2-Z\) fails, and that undersampling still requires a separate rank witness. A large finite test does not prove the universal divisibility; the derivation above is the proposed proof, awaiting complete Lean formalization.

## Joining the existing odd-prime lower bound

The checked source theorem \`RadialCutoff.prime_mass_log_lower_of_det_pos\` already gives, under class-number-one, squarefree-\(D\), congruence and prime-window hypotheses, the odd-prime divisor

$$
P_{\rm odd}=\prod_{\substack{p<R\\ p\ \mathrm{odd\ prime}}}
p^{\,2F_{R,S}(p)}
\quad\bigm|\quad \det G_Q.
$$

Since \(\gcd(2^{\Lambda},P_{\rm odd})=1\), the two independent factors multiply:

$$
\boxed{2^{\Lambda(R,S)}P_{\rm odd}\mid\det G_Q}
$$

and, **only if \(\det G_Q>0\)**,

$$
\boxed{\Lambda(R,S)\log2+
\mathrm{exactOddPrimeMass}(R,S)\ \le\ \log\det G_Q.}
$$

No odd prime is counted twice, and the entire derivation concerns **the same integer trace Gram**. The [Lean binary-prime bridge](../../lean/TenthDiscriminant/BinaryPrimeMassBridge.lean) expresses exactly this coprime combination but takes the binary divisibility as an **explicit hypothesis** until the complete source-level row factor is formalized.

## What may actually improve

For the production aspect ratio \(R\approx25S\), the *binary* contribution normalized by \(R^2S\) approaches \(\frac14\log2\approx0.1733\). This is substantially larger than the earlier Phase156 conservative factorial-capacity bound. But the Hadamard upper, interpolation positivity, radius counts and odd-prime mass must all be applied **with their original hypotheses and exact constants**. Merely adding 0.1733 to a speculative numerical cutoff margin is not a field theorem.

One also must not re-use the factor \(2^{RS}\) as an independent gain after changing the trace-metric normalization: all comparisons must keep the source metric or shift both upper and lower consistently.

**The next formal obligations** are narrow: (i) compile the integer-coordinate null-value lemma, (ii) prove the uniform ordinary-jet row factorization \(UE_Q=AC_Q\) in Lean, (iii) discharge the \`hbinary\` hypothesis in the coprime mass theorem, and (iv) compare the augmented lower with the *same-source* existing analytic upper across a fully verified parameter range. The first two mathematical derivations are source-local; the last is a genuinely global arithmetic/geometric research problem.

The established actual-field theorem remains **47 billion**, subject to the existing independent semantic-reconstruction obligation. Phase162 does not claim a stronger endpoint. No priority or independent-referee claim is made for the polynomial construction or its AI-assisted finite evidence.
