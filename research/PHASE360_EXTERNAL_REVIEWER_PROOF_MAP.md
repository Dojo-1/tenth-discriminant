# Phase360 — external reviewer proof map (20 November 2026)

**Status:** Lean-checked at the separate Phase357, Phase358 and Phase359 heads; the new Phase360 combined head must pass its own pinned full-root and transitive-axiom audit. **No independent number-theoretic referee report exists.** This packet does not request priority or assert novelty versus classical quadratic class-number-one results.

## Statement being audited

For any field K with [Field K], [NumberField K], [NumberField.IsTotallyComplex K], Module.finrank Rat K = 2 and NumberField.classNumber K = 1, the encoded theorem target says

$$
|\operatorname{disc}(K)| < 302^4 = 8\,318\,169\,616.
$$

Declaration: TenthDiscriminant.Threshold302.totallyComplex_degree_two_classNumber_one_discriminant_bound_302 (Phase359Field302Candidate.lean).

## Exactly one auxiliary Gram, not the discriminant

Fix any natural D >= 302^4 in the odd, squarefree maximal-order chart, with D mod 4 = 3. Use the original definitions:

$$
R(D)=\lfloor D/4\rfloor,\qquad
S(D)=\lfloor R(D)/25\rfloor,\qquad
t(D)=D^{1/4},\qquad
\rho_{\rm thin}(D)=\lceil 11t(D)^3/25\rceil.
$$

Full original sample carrier, not a sub-sampling or a selected minor:

$$
Q_D=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le \rho_{\rm thin}(D)^2\}.
$$

Let E be the **ordinary** Z-derivative evaluation operator **holding W fixed** with jet order J=S and the original row-major rectangular monomial family (R,S). Let B be the original integer trace pairing with weights 2 and 2D. The auxiliary integer Gram is

$$
G_D=E_{Q_D} B_D E_{Q_D}^{T}
=\operatorname{integerRectangularTraceGram}(Q_D,D,S(D),R(D),S(D)).
$$

Its determinant is **not** the number-field discriminant. Its normalized log is

$$
g_D=\log(\det G_D)/\operatorname{comparisonScale}(R(D),S(D)).
$$

The padded ellipse radius rho(D) = ceil(13 t(D)^3/25) may furnish an upper bound on the NUMBER of source samples. The padded Gram itself cannot substitute for G_D.

## Five proof seams to reconstruct or refute

**1. Positive determinant and exact source.** Phase354OriginalGram14.lean proves the unchanged Q_D has enough interpolation samples and det G_D>0 already for D>=14^4. Phase358SourcePositivity302.lean transports this to 302^4 and proves the padded-cardinality majorant without replacing the Gram.

**2. The original analytic upper.** Phase356Radius302.lean replaces the FALSE 307-domain guard R>=76t^3 (false at exactly t=302) by the checked weaker 75t^3 guard. Phase358UpperScalars302.lean recovers the padded upper scalar -815/1000. Phase358ThinUpper302.lean calls TightRadialSaving.normalized_integer_upper_tight on the literal unchanged Q_D, which contributes -23/2000; the already proved 17/20 radius contraction contributes -27/200. Thus the target upper statement is

$$
g_D\le U(D)=\frac45\log D-\frac{1923}{2000}.
$$

Reviewer: verify the original Hadamard hypotheses and every normalization/source identity, not just the rational constant addition.

**3. The original arithmetic lower.** Phase357JointLower302.lean uses Phase331.joint_binary_odd_log_of_pos on the SAME Q_D and positive G_D; the existing joint-unimodular binary exponent and odd-prime source lower are combined with the existing horizontal 3/5/ten-prime contributions, with no Phase332 speculative mixed gain. Under D squarefree, D mod 4 =3 and classNumber(QuadraticField(((D+1)/4)))=1, the encoded lower is

$$
\begin{aligned}
L(D)={}&\frac{999997}{1000000}\log D-\frac{57193}{10000}
+\frac14\log2\\
&+\left(\frac{4659}{625000}-\frac{16895455}{625000D}\right)\\
&+\left(\frac{6931}{1000000}-\frac2{R(D)}\right)
+\left(\frac{873747}{250000000}-\frac{40}{R(D)}\right)
\le g_D.
\end{aligned}
$$

Reviewer: reconstruct why **each exact ordinary-Z derivative row** yields the claimed integral p-adic divisibility, why the row transformation is unimodular, and why binary and odd-prime factors are not double-counted. This is a genuinely critical independent-semantic gate.

**4. Scalar contradiction.** Phase355Scalar302.lean checks the rational log enclosure and claims for every D>=302^4:

$$
U(D)<L(D),
$$

with a conservative separation margin greater than 318967/250000000 under the frozen error bounds. Consequently the preceding same-g inequalities cannot simultaneously hold. At D=301^4 the unchanged scalar formulas do NOT have this strict separation: keep this negative control and do not weaken the threshold by substitution.

**5. Transport to the actual field.** Phase359Field302Candidate.lean starts with the odd chart, passes through squarefree_mod_four_cases, quadraticChartEquiv, imaginaryQuadratic_discr_natAbs and even_classNumber_ne_one, then uses exists_squarefree_root_of_totallyComplex_degree_two, imaginaryQuadraticEquivOfRoot, and NumberField.discr_eq_discr_of_algEquiv. Independently check which quadratic order each chart represents, exactly when the discriminant is D or 4D, and whether field isomorphism transports the right class-number and absolute-discriminant hypotheses.

## Complete comparison for one and the same D

$$
L(D)\le
\frac{\log\det G_D}{\operatorname{comparisonScale}(R(D),S(D))}
\le U(D)<L(D).
$$

The contradiction is meaningful only if all three inequalities name **the same Q_D, G_D, D, R, S, J, B and normalization** and have no undeclared or displaced hypotheses.

## Explicit correction and falsification ledger

- **R:** the old radius assertion R>=76t^3 cannot be used at 302.
- **M:** bounded complete-ellipse oracles do not establish a universal theorem.
- **P relative to encoding:** source geometry, radius, scalar gap, lower and upper have separately passed pinned exact-head Lean checks with standard permitted axioms.
- **H until fresh root CI:** this Phase360 combined branch's exact source-to-field closure.
- **H independent semantics:** no mathematical referee has checked the p-adic exponents or the odd/even maximal-order chart on paper.
- **No theorem promotion:** the improved 302^4 research threshold is NOT merged into public main and should not be externally described as independently proved.

## What would constitute useful external review?

A short independent derivation of the exact source Gram valuation and field transport; OR a single explicit counterexample to any stated sublemma/normalization/prime exponent; OR a missing-hypothesis report with a corrected lemma. Code compilation alone, especially by the same research workflow, does not satisfy the issue #50 review gate.

Reference: https://github.com/Dojo-1/tenth-discriminant/issues/50
