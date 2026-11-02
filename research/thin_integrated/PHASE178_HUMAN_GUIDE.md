# Tenth Discriminant — the 377⁴ theorem, for a human reader

*State of the formalization, 2 November 2026. Lean-checked; not independently reviewed by a mathematician.*

## The claim we actually encoded

For a number field \(K/\mathbb Q\) that is totally complex, of degree two, and has class number one, the checked declaration

[\`Threshold377.totallyComplex_degree_two_classNumber_one_discriminant_bound_377\`](../../lean/TenthDiscriminant/ActualField377.lean)

states that its **actual** absolute field discriminant satisfies

\[
|\operatorname{disc}(K)|<377^4=20{,}200{,}652{,}641.
\]

This is a formal theorem about the *field discriminant*, not the auxiliary determinant used in the proof. The classical nine imaginary quadratic class-number-one fields were already known: this experiment does not claim to classify them anew or improve upon all existing mathematical bounds.

## Why an auxiliary integer determinant enters

For a squarefree parameter \(D\), the odd quadratic chart uses the usual maximal-order bridge. Fix precisely the existing integer observation ellipse and rectangular monomial dimensions:

\[
Q_D=\operatorname{ellipsePairs}\!\left(D,
  \left\lceil\frac{11}{25}D^{3/4}\right\rceil\right),\qquad
R=\lfloor D/4\rfloor,\quad S=\lfloor R/25\rfloor.
\]

The row evaluations use ordinary \(Z\)-derivatives of \(Z^rW^s\), with \(W\) held fixed. The original integer matrix and trace pairing define

\[
G_D=\operatorname{integerRectangularTraceGram}(Q_D,D,S,R,S),
\quad c_D=R^2S.
\]

The trace pairing retains the original weights \(2,2D\). It is *not* a replacement by Hasse derivatives, a synthetic Gram, or a switch to the larger padded ellipse. Geometry and arithmetic will compare exactly \(\log\det(G_D)/c_D\).

## The two pressures on one integer

First, [Phase170](https://github.com/Dojo-1/tenth-discriminant/pull/89) gives the thin-ellipse interpolation count at \(D\ge377^4\). [Phase174, integrated with the lower and binary lemmas in PR #94](https://github.com/Dojo-1/tenth-discriminant/pull/94), proves source-Gram positivity. This allows us to take \(\log\det G_D\) legitimately.

On the **arithmetic side**, the guarded class-number-one hypothesis and original prime-valuation proof give the already established odd-prime product *and one existing binary factor* dividing \(\det G_D\). Phase172 rederives the odd-only normalized lower at this smaller range; Phase173 normalizes the binary exponent. Using \(u=\log D\), the resulting lower is

\[
L(u)+\frac14\log 2
\ \le\ \frac{\log\det G_D}{c_D},
\qquad
L(u)=\frac{999997}{1000000}u-\frac{5739}{1000}.
\]

The binary term is **not** an auxiliary prime newly inserted into the proof; it comes from the original \(2\)-adic row action and is counted just once.

On the **real geometric side**, [Phase171](https://github.com/Dojo-1/tenth-discriminant/pull/90) rederives the original radius-to-dimension bound, [Phase176](https://github.com/Dojo-1/tenth-discriminant/pull/95) bounds the old-radius *scalar* analytic expression, and [Phase177](https://github.com/Dojo-1/tenth-discriminant/pull/96) applies the same original ordinary-jet Hadamard bound directly to \(G_D\):

\[
\frac{\log\det G_D}{c_D}
\ \le\ U(u),\qquad
U(u)=\frac45u-\frac{1849}{2000}.
\]

The padded ellipse is used only to majorize the **number** of observations. Its own determinant is never equated to or substituted for \(\det G_D\).

## The strict contradiction and return to the field

[Phase169](https://github.com/Dojo-1/tenth-discriminant/pull/88) proves the valid numerical guard \(\log D\ge23.7\) at \(D\ge377^4\) (rather than incorrectly recycling \(\log D\ge24\)). The repository's certified \(\log2\ge0.6931\) implies

\[
L(u)+\frac14\log 2-U(u)\ge0.0987039>0
\qquad (u\ge23.7).
\]

Thus the two displayed inequalities cannot both hold for the **same positive \(G_D\)** under the hypothetical class-number-one arithmetic premises. [Phase178's Lean declaration](../../lean/TenthDiscriminant/ActualField377.lean) makes the contradiction and then uses the original odd/even maximal-order field charts and field equivalence to obtain the actual-field statement.

## Exactly what has, and has not, been verified

[PR #97](https://github.com/Dojo-1/tenth-discriminant/pull/97) passed focused Lean and the [exact-head whole-library, source-correspondence, permitted-axiom and known-false-negative checks](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41508959650) before merging. The chain of formal declarations is checked relative to its definitions and permitted axioms, and the original D=7 source examples provide bounded regressions.

Those tests and explanations were largely produced within one AI-assisted authoring lineage. **They are correlated evidence, not independent mathematical confirmation.** A mathematician still needs to reconstruct from the intended classical objects: the maximal order and class-number condition; the original ordinary-jet and trace metric; the inert-prime and binary divisibility under exactly the same observation set; the real determinant upper; the log and denominator signs; and finally the transport to \(|\operatorname{disc}(K)|\).

That work is tracked in [Independent semantic review #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). A precise missing hypothesis, counterexample or source mismatch would narrow or overturn the mathematical interpretation without erasing the valid *formal* CI record.

The older [41.00625-billion human derivation](HUMAN_GUIDE_CURRENT.md) remains a useful predecessor, not the final endpoint in the current repository.