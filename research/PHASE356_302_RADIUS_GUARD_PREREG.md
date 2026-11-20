# Phase356 — 302⁴ original-radius obstruction and replacement

**2026-11-20 (Madrid); preregistered before the Lean file.** Research-only.

## Original objects, no substitutions

- (D) is a natural parameter; (t=D^{1/4}) is the existing `fourthRoot D`.
- (R(D)=\lfloor D/4\rfloor), (S(D)=\lfloor R/25\rfloor).
- The SAME padded radius `rho D = ceil((13/25)*t^3)` and SAME thin radius `thinRadius D = ceil((11/25)*t^3)`.
- The target upper determinant remains the unchanged original full `integerRectangularTraceGram (ellipsePairs D (thinRadius D)) D (S D) (R D) (S D)`.

## Prediction

The Phase342 lemma `R >= 76*t³` is FALSE at `D=302^4`: exactly `R=75.5*t³`. Any naive weakening of the 307-domain theorem to 302 using this lemma is invalid.

Prove **instead** for every `D>=302^4`:

1. `t>=302` and `rho D <= 521/1000*t³`, same original rounding convention.
2. `75*t³ <= R D` uniformly, including arbitrary integers not perfect fourth powers. Use `D<=4R+3`, `t-300>=2`, `3<=2*t³`.
3. `rho/R <= 521/75000`. This weaker ratio is still enough for `521/75000+1/9000 < 1/100`.
4. `thinRadius/rho<=17/20` persists at 302; hence the original strong radius-saving comparison can be instantiated once the remaining 302 numeric guards are discharged.
5. Negative theorem: `R((302)^4)<76*302³`, positive theorem `75*302³<=R((302)^4)`.

## Kill condition and exclusions

- If **any** Lean proof fails, repair or demote; do not turn these into axioms.
- Check the half-integer fourth-root vicinity, not only `D=302^4`.
- No claim that the analytic **upper bound** (Phase347) or arithmetic **lower bound** (Phase348) holds at 302 yet; those use additional 307-only guards and must be re-derived on the same Gram.
- No field-discriminant promotion: public `main` remains separate, research 307 statement remains separate, issue #50 remains open.
- The 14⁴ geometry and 302⁴ scalar lines are independent and remain accessible in PRs #259/#261 and #260.

## Evidence ledger

- P at the natural-integer endpoint for 76-cube failure, once Lean built;
- H until full-root compile/axiom check of the uniform 75-cube bound;
- M for additional exact-integer large-D tests; field implication H.
