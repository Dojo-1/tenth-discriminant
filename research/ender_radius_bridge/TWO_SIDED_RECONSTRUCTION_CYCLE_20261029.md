# Registered cycle: independent two-sided Gram reconstruction

**Registered:** 29 October 2026. Base main: 0bde1bf58893f1adf66bfded5eaf1a0f270c6dce.
**Branch:** audit/independent-two-sided-gram-20261029.

## Frozen identity and acceptance

The object is the integer, ordinary-derivative, factor-two trace-Gram determinant G of the ORIGINAL rectangular polynomial rows and ORIGINAL selected sample pairs. Its determinant is not the field discriminant. The selected order Z[sqrt(-D)] differs from the maximal order in the odd fundamental-discriminant chart; the even-chart actual absolute field discriminant carries the factor four.

Primary obligation: independently reconstruct the explicit integer unitriangular row change U, the diagonal p-power matrix P, and a genuinely INTEGRAL middle Gram K satisfying U G U^T = P K P. Prove the exact exponent p^(2F(p)) with F(p) = sum_(r<R,t<S) min(floor(r/p), t), not by separate unproved row/column divisibilities.

Independence control: a separately written pure-Python integer-pair oracle computing original jets, G, U, transformed jets, K, and exact matrix/determinant identities. Test the D=19,p=3 pilot and a second inert prime; test split-prime, divided derivative, and active/passive translation counterexamples. Arithmetic equality is exact, without floating-point approximations.

This is an explanation/audit cycle, NOT an attempted new discriminant cutoff. No changes to existing Lean statements, proof bodies, prior errors, failed/stopped attempts, earlier CI controls, current 48-billion theorem, or main. **Zero Lean proof-repair slots** are allocated in this cycle. Any later Lean elaboration needs a separate frozen specification, at most two declared proof-only repair slots, and full acceptance of the intended actual-field theorem (not merely its logarithm certificate).

Stop on any mismatch: a bad sample identity, lost factor two, failure of coordinatewise row divisibility under the stated guard, nonintegral middle K, or missing same-sample correspondence. Do not rescue such a failure through geometric terminology.

## Evidence separation

- Main at the registered base reports an actual-field 48-billion theorem; its complete local 202-module audit and the two successful same-head GitHub Actions runs are versioned evidence, not human-independent mathematical reconstruction.
- The earlier 173-module inventory is a different historical scope. The inspected main review directory did not contain a completed standalone Argon semantic report. The user describes a failed 47.5-billion attempt; the present inspection has NOT found a specific primary artifact that would authorize changing its status. Leave it and other failed rounds untouched.
- Arithmetic basis/jet sources: lean/TenthDiscriminant/IntegerTraceGram.lean, RectangularBasisMatrix.lean, RectangularRowAction.lean, JetPower.lean, RectangularGramFactor.lean, GramDivisibility.lean and RectangularValuation.lean.
- Field/prime sources: InertFrobenius.lean, ClassNumberInertBridge.lean and QuadraticFieldChart.lean.
- Geometry: RadialOperator.lean, RadialDetBound.lean, RadialCutoff.lean. Current verification: research/ender_radius_bridge/PHASE121_VERIFICATION.md.

A complete cycle here means only that the **independent finite explanation and witness** can be reproduced. It does not mean a failed higher theorem has become proved.
