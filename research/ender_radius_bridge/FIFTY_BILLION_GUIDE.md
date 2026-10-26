# A50-billion cutoff from the same determinant

The new field theorem, full local build, fresh input exclusions, boundary
controls and axiom audit pass. [Verification](PHASE56_VERIFICATION.md)
records their scope. Exact-head CI and independent human review remain
separate; this guide explains the fixed argument.

Geometry and arithmetic still constrain one positive integer Gram
determinant. Geometry supplies the upper estimate. Existing prime-power
divisibility supplies the lower estimate. If the lower exceeds the upper,
class number one is impossible. Nothing about the determinant, ordinary
derivatives, row family or valuation exponents changes here.

The62.5-billion proof restored contributions at3 and5 that its simpler
uniform formula had omitted. It used only log3,log5>=1 to obtain a
normalized recovery>=.06. We can keep more information without adding a
prime or a derivative: log3>=1.09 and log5>=1.6.

The first follows from2^19<=3^12 and the existing rational log2 bound;
the second follows from the existing rational log5 certificate. These
are exact inequalities, not measured or floating-point logarithms.

## The row count with sharper weights

For p>0, every monomial row r>=pS contributes its full staircase, so

    2F(p)>=(R-pS)S(S-1).

When S>=100 and25S<=R<=26S, apply the formula at3 and5 and retain the
two different logarithm bounds. The recovered numerator is at least

    [1.09(R-3S)+1.6(R-5S)]S(S-1)
      >=55.98 S²(S-1)>=55.4202 S³.

The common scale R²S is at most676S³. Since .081*676=54.756<55.4202,
the normalized recovery is at least.081. The S=1 control still rejects
an unguarded positive gain. Neither the constant nor the guards are
claimed sharp. This count concerns degree weights, not derivative order.

## The radius still works

The fixed choices remain R=floor(D/4), S=floor(R/25), J=S and
rho=ceil(.52D^.75). We now prove the same geometric helper estimates
for D>=450^4=41006250000. The radius-admissibility slack is
t²(.024505t-10), positive at t=D^.25>=450. Ceiling, strict inertness,
ellipse count, positive scale and all retained error terms are checked.
The slightly weaker rho/R bound521/90000 still leaves the endpoint
correction below.001. The upper estimate is unchanged.

The chosen endpoint50 billion is larger than450^4 and equals2^10*5^11.
Existing log certificates give logD>=24.6304 there. Let u=logD. The
normalized bounds are now

    upper <= .8u-.813,
    recovered lower >= .999997u-5.739.

At u=24.6304 their difference is exactly.0000061088>0. At u=24.6 this
coarse comparison fails. The small positive margin is an exact rational
proof; it creates no floating-point precision obligation. It says nothing
about the best possible endpoint for this method.

## Returning to an actual field

The tail comparison, class-number-to-inertness bridge and actual-Gram
sandwich are the same as before. Conjugation supplies a positive squarefree
generator for an abstract totally complex degree-two field; the algebra
equivalence transports actual class number and actual discriminant.
The separate even case distinguishes radicand from field discriminant.
The new bound must exclude earlier cutoff and finite-answer roots in its
actual dependency closure, rather than assume their absence from imports.

The first bounded review remains tied to86abe21 and the62.5-billion proof.
It does not cover these new helper/gain changes. No new valuation, parity
gain, novelty, optimality, higher-class-number result, full-classification
announcement, human review, merge or submission to Tao is claimed.
