# Phase178 — test an actual-field bound at 377^4 without changing objects

**HYPOTHESIS / unverified formal theorem target. Do not announce a proof before every gate is green.**

The proposed strict inequality is
[
  |mathrm{disc}(K)| < 377^4 = 20,200,652,641
]
for any totally complex number field (K/mathbb Q) of degree two and
class number one.

This is deliberately the **actual field discriminant**, not the
original integer ordinary-jet trace-Gram determinant. We follow
the original maximal-order chart and field equivalence, exactly as
in the already verified 41,006,250,000 theorem.

The load-bearing comparison starts with one and only one integer
trace Gram (G_{m thin}(D)), evaluated on the original unmodified
thin ellipse and ordinary-(Z) jets. The original odd-prime
product and the **already proved** binary factor both divide this
same integer determinant under the original squarefree, mod-four,
class-number-one and inertness hypotheses. Its strict positivity
is a separate formal geometry result. The upper side is the
unchanged ordinary-jet analytic Hadamard inequality on this
very same thin Gram; the padded ellipse contributes only a cardinality
majorant.

Writing (u=log D), the intended normalized inequalities are

[
L(u)+rac{log 2}{4} le
 rac{logdet G_{m thin}}{R^2S}le U(u),
]
[
L(u)=rac{999997}{1000000}u-rac{5739}{1000},qquad
U(u)=rac45u-rac{1849}{2000},
]
with (uge23.7), for which the *formal affine gap*
(L(u)+rac{log2}{4}-U(u)>0.098) is strictly positive.

**The arithmetic and upper estimates MUST be kernel verified on the
identical source Gram; the positive scalar gap alone proves nothing
about fields.** In particular no old (450^4) premise may be
transported by fiat.

The steps are separately represented by:
- existing Phase166 original binary+odd same-Gram source theorem;
- Phase170 thin interpolation (merged);
- Phase171 radius/dimension (merged);
- Phase172 recovered normalized odd lower;
- Phase173 normalized binary quarter and strict scalar gap;
- Phase174 source Gram positivity and old padded cardinality majorant;
- Phase176 rederived padded analytic SCALAR upper;
- Phase177 source-exact thin determinant upper;
- this Phase178 old quadratic chart and actual field discriminant
  endpoint theorem.

### Promotion, regression and stop rules

Require pinned Lean 4.19.0+Mathlib exact-head focused and whole-library
compilation, source correspondence, allowed axioms, known-false
regression rejection and CodeQL. Reconstruct the key determinant
and field statements independently of the same agent-written source
(see issue #50) before making an external research claim.
A code build establishes *the formal statement* as written; it does
not by itself establish equivalence with a historical research
statement if the specification is wrong.

Stop and retain a falsifying artifact on ANY failed hypothesis,
changed support, determinant mismatch, reuse of a 450-domain theorem,
incorrect number-field chart, negative controls or unverified
source mapping. Only integrate after the precursor branch layers
are merged and the final exact-head audit passes.
