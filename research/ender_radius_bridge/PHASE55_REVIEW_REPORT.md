# Phase55: first bounded adversarial review of the recovered cutoff

## Identity, scope and outcome

Reviewed mathematical target `86abe21f1ca023f9f62f99d1f785cdb361d86010`, tree `7383bdcc0fa035bc83628420785813240b0e535e`. The checkout HEAD during review was protocol commit `2a943fd1572bd57f50023c6033ecbcd87e4e12f4`. Git confirmed the tree identifier and no difference from the frozen target in `lean/TenthDiscriminant/`. The reviewed README, STATUS, lean/FORMALIZATION, TAO_OBJECTIVES_CURRENT and Phase54InputCheck also have no differences from that target. Later documentation such as MATHEMATICAL_SPINE is not being silently identified with the mathematical target.

Dispatch marker: 2026-10-26 16:12:55 UTC. Source reading began immediately afterward. Finalization is timestamped below by the write operation, well before the 16:42:55 UTC deadline. This is one fresh-context AI review, with no child agent, reroll, model override, proof repair, parameter search, heavy build, deployment or external message. The only reviewer-created file is this report. Concurrent parent task-state/dispatch files and the pre-existing untracked lake manifest were observed; I did not edit them.

**No FATAL or GAP contradiction was established in the six checked joints.** This is a bounded conclusion, not full certification. New finite algebra and endpoint estimates were re-derived as described below. The inherited determinant, arithmetic, maximal-order and interpolation apparatus was traced in source, not reproved wholesale. Saved compiled-check records were inspected and their integrity verifier was executed; Lean and CI were not rerun. No human or model-family independence, novelty, optimality, higher-class-number theorem or full-classification announcement follows.

The protocol and review brief were read first. Mathematical sources were read before RECOVERED_CUTOFF_GUIDE and PHASE54_VERIFICATION. Earlier semantic review reports were not used as evidence of mathematical correctness.

## 1. Recovery without double counting — RE-DERIVED locally; inherited valuation SOURCE-TRACED

Sources: `SmallPrimeRecovery.lean:9-110`, `Arithmetic.lean:48`, `PrimeMassLower.lean:35-62,287-331`, `UniformPrimeMassCertified.lean:12-74`, `TraceGram.lean:15-25`, `IntegerTraceGram.lean:60-144`, `RectangularGramFactor.lean:268-284` and `ClassNumberInertBridge.lean`'s `rectangularTraceGram_valuation_of_classNumber_one`.

Write A for the certified small-odd proxy, T for the nonnegative retained prime >=7 sum, and M for F(3)log3+F(5)log5. The source establishes A<=T by termwise uniform valuation bounds and rational prime-log enclosures. The production odd-prime sum contains the disjoint set {3,5} union retained>=7. Every omitted term is nonnegative. Thus max(A,0)+M<=T+M<=the production small sum. Padded primes p>=R add zero weight, so the padding identity does not create a new factor. The certified tail lies below the production tail because the certified factorial-small upper bound is larger and S-1/2>=0; applying max(_,0) preserves that direction. Multiplying both parts by two yields recovered<=the SAME production expression for every real I, R>=2 and S>=1. It is not an argument that adds M to a bound already using it.

The exact weight is sum over r<R,t<S of min(floor(r/p),t). The row derivative is r-descending-factorial(j) z^(r-j) conjugate(z)^s, zero for j>r; conjugate(z) is held constant. Its Gram is twice the real pairing summed over j<J and the same samples. Integer-to-complex equality is entrywise and then determinant equality. The recovered proof changes none of these definitions. The exponent 2F(p) is an inherited determinant divisor, traced through the Frobenius basis factor and class-number norm-lifting bridge, not newly inferred from the recovery calculation.

Smallest relevant failure modes: counting 3 or 5 again inside T; or inferring max(A,0)+M<=production from A+M<=production without a nonnegative retained bound. Both are explicitly prevented. The controls R=3,S=2 (no recovery) and R=4,S=2 (exactly 2log3) agree with the finite ranges. I have not independently re-proved all ordinary-jet divisibility lemmas.

## 2. Saturated rows and 3/50 — RE-DERIVED

Sources: `SmallPrimeRecoveryGain.lean:11-125`, `NormalizedComparison.lean:10-15`, `Arithmetic.lean:48`.

For p>0 and pS<=r<R, floor(r/p)>=S; hence min(floor(r/p),t)=t for 0<=t<S. There are exactly R-pS such rows when R>=pS and none otherwise. Their sum is (R-pS)S(S-1)/2; the Nat subtraction and S-1 remain legitimate even for empty/zero ranges. This proves 2F(p)>=(R-pS)S(S-1). The division guard p>0 matters: p=0,R=4,S=2 gives the false 8<=0, as the source control records.

With S>=100 and 25S<=R<=26S, both R-3S and R-5S can be cast to real subtraction. Adding the bounds gives 2(F3+F5)>=(2R-8S)S(S-1)>=42S^2(S-1)>=41.58S^3. The source derives log3,log5>=1 from rational log2 bounds and 8<=9,4<=5. Therefore 2M>=41.58S^3. The comparison scale R^2 S<=676S^3, and (3/50)*676=40.56<41.58 (slack 1.02S^3), proving the advertised gain. Scale positivity follows from the same guards.

Here t is a monomial-degree/weight coordinate, not the ordinary derivative index j. No claim about sharp guards follows. S=1 gives F(p)=0 and disproves an unguarded positive gain at R=25. That control does not show S>=100 is necessary, nor does p=0 show optimality for positive p. The raw-to-recovered step uses raw<=certified and a positive common scale; clipping cannot invalidate it.

## 3. Entire endpoint geometry and logs — RE-DERIVED for widened estimates; inherited count theorem SOURCE-TRACED

Sources: `TunedRadiusFamily.lean:10-160`, `TunedAnalyticCutoff.lean:10-191`, `UniformRadiusFamily.lean:10-15,35-39,59-85`, `AspectRatioLowerEnvelope.lean:11-91`, `EllipseUpperCount.lean:182,276-328`, `EllipseCellArea.lean:120-181`, `NormalizedComparison.lean:16-37`.

I compared both tuned source files to `bd2a207`. The family remains R=floor(D/4), S=floor(R/25), rho=ceil(.52 t^3), t=D^(1/4). The helper premise is weakened from 100 billion to 500^4; the old log25.3 and old-cutoff theorem remain separate. The new log24.8 lemma and changes of its uses are explicit. The old theorem caller is repaired only by deriving its weaker helper premise.

For every D>=500^4=62,500,000,000, t>=500, R and S exceed the stated coarse bounds 10^8 and 500000. Integer remainders give 25S<=R<25S+25, hence R<=26S and 10R<=251S here. Also D/5<=R<=D/4 and S<=R/25. For D congruent to3 mod4, write D=4k+3: R=k<k+1=(D+1)/4. The rejected inclusive endpoint at D=163,R=41 is a real obstruction; the actual choice is R=40.

Ceiling adds less than one; .001t^3>=125000, so .52t^3<=rho<=.521t^3 holds comfortably at the endpoint. Then rho<R since R>=t^4/5 and .521<t/5. For radius admissibility, 3R+S<=.76D. Using pi>3.14, (.495)^2*pi>.76, so the square-root term is <=.495t^3. The remaining slack is (.52-1.001*.495)t^3-10t^2=t^2(.024505t-10)>=2.2525t^2>0 at t>=500. Thus the chosen-radius positivity/interpolation guard is retained, not extrapolated from affine arithmetic.

The exact padded count is pi*rho^2/t^2+2rho+2Y+1 with Y=floor(rho/t^2). The source safely weakens rho to .6t^3; this gives n<=1.44t^4+1.2t^3+1.2t+1<4t^4 for t>=500. Positivity and all log arguments are explicit. The source's coarser log/R bound uses logD<=2(sqrtD-1), R>=D/5 and sqrtD>=90000; hence logD/R<=1/9000. Further rho/R<=2.605/t<=.00521 and 0<=log(R/rho)<=logD. Thus log(2nS)/R<=(3+2logD)/R<=1/4000, and the retained endpoint correction is <=(1/10)(.00521+1/9000)<.001. No correction was discarded.

Writing x=S/R in [0,1/25] and u=logD, the main normalized upper terms are bounded by (1-x)(.75u-.65)+2x(u-2.38), plus .00025+.001. The coefficient 1.25u-4.11 is positive for u>=24.8. Substitution x<=.04 gives .8u-.81315<=.8u-.813. The lower aspect-ratio bound gives .999997 logR-4.419; logR>=u-1.4 implies >=.999997u-5.8189958>=.999997u-5.820.

Finally D0=2^8*5^12. The weaker rational log2>=.6931 and log5>=1.609 already give 8*.6931+12*1.609=24.8528>24.8. The source uses a stronger Mathlib log2 certificate and the checked log5 enclosure, so the required logarithm bound follows for all D>=D0. I traced, but did not re-prove, the analytic soundness of the rational-log checker, the ellipse area/count construction, and the full positivity/interpolation theorem.

Minimal falsifiers checked: dropping the rounding guard fails at D=1; inclusive inertness fails at 163,41; treating floor(R/25) as R/25 exactly loses remainder control. None is used in the new proof. Boundary examples are not evidence of sharpness.

## 4. Actual determinant and inequality directions — RE-DERIVED composition; determinant apparatus SOURCE-TRACED

Sources: `RecoveredAnalyticCutoff.lean:10-63`, `UniformPrimeMassCertified.lean:59-74`, `SmallPrimeRecovery.lean:93-110`, `PrimeTail.lean:116-167`, `PrimeMassLower.lean:411-444`, `PrimeMassAssembly.lean:44-178`, `IntegerTraceGram.lean:127-159`.

Let U be enderUpperB(R,S,S,rho,n), C=R^2 S>0, B the tailBudget and I the exact enderTailIntegral(10000). Since I<=B and the certified proxy is antitone in its tail argument, recovered(B)<=recovered(I): the added 2M is independent of I. Recovery then gives recovered(I)<=production(I); the inherited finite-prime/tail and actual-Gram argument gives production(I)<=U. All use the identical R,S,J=S,rho and ellipse count. R<=10000S is supplied by dimensions; the strict prime cutoff, squarefreeness, class number one, positive dimensions and chosen radius are passed explicitly with D1=D=D2 and Y the exact vertical floor.

Conversely the estimates give U/C<=.8u-.813<.999997u-5.760<=recovered(B)/C. The lower-minus-upper gap is .199997u-4.947, increasing with u. At 24.8 it is exactly .0129256>0; at 24.7 it is -.0070741. Positive scaling yields U<recovered(B)<=recovered(I)<=production(I)<=U, a contradiction. The log24.7 rejection only concerns these coarse affine estimates.

The source-traced sandwich uses distinct odd prime powers dividing the positive integer ellipse Gram determinant; its cast equals the real Gram determinant and Hadamard bounds that same determinant. Product-divisibility requires distinct primes, not multiple witnesses for the same prime. The factor two is retained throughout. A minimal failure would be reversing tail monotonicity or cancelling C without positivity; neither occurs. I did not independently establish the complete inherited local Frobenius, ideal-norm or jet-interpolation stack.

## 5. Actual-field conclusion and input closure — RE-DERIVED transport logic; compiled execution SOURCE-TRACED

Sources: `RecoveredAnalyticCutoff.lean:72-109`, `ImaginaryQuadraticRepresentation.lean:11-184`, `QuadraticGeneratorBridge.lean:11-37`, `QuadraticChartEquivalence.lean:74-112`, `EvenClassNumber.lean:18-52`, `QuadraticDiscriminant.lean:119-135`, `research/ender_radius_bridge/Phase54InputCheck.lean`, and its saved Phase54 input stdout/result.

The odd chart is identified by an explicit rational algebra equivalence with the trace-zero canonical field. Actual class number one is transported via the ring-of-integers equivalence/PID characterization. The separate even chart proves a norm-two equation; for squarefree d>2 it is impossible, so class number one forces d=1 or 2. This is not an inference from the odd analytic cutoff. The actual canonical discriminant is -d in the odd chart and -4d otherwise: a radicand bound alone would not bound the even discriminant by the same constant. The proof correctly uses d in {1,2} in that branch, giving absolute discriminant 4 or 8.

For abstract K, conjugation supplies a nonidentity involution. A nonzero anti-invariant u=(x-sigma x)/2 has u^2 fixed by all automorphisms. Degree two supplies quadratic Galoisness and the rational fixed field, not just uniqueness of the nonidentity automorphism. Its embedding is purely imaginary and nonzero, so u^2 is negative rational. Clearing a positive rational's denominator and removing the positive square factor gives a positive squarefree d with a^2+d=0. The canonical-field homomorphism is injective and, by equal rational dimension two, surjective. The resulting AlgEquiv transports the actual class-number-one premise and actual discriminant. No generator is supplied by the caller and no class-number assumption constructs it.

I inspected the compiled closure-check source: CollectAxioms traverses the actual root, checks visited constants against 21 explicit forbidden old-cutoff/classification/finite-answer/fixed-ratio names, rejects unresolved/unsafe constants and permits only propext, Classical.choice and Quot.sound. Saved stdout records 55469,55804,58598 reached constants for the odd/canonical/abstract roots. The integrity verifier passes and ties these records/checker/source bytes to the preserved evidence. The new source calls none of the older bound wrappers; its imports contain some old bounds but imports alone are not proof use.

Limit: I did not rerun that compiled traversal, audit all 58598 constants, or prove completeness of the 21-name denylist against every conceivable differently named classification theorem. Thus archived execution is SOURCE-TRACED; independent fresh compiled acceptance is CANNOT-VERIFY in this review. This limitation is not a discovered circularity. A minimal decisive falsifier would be an actual reached old-cutoff/finite-answer root or a discriminant transport that only transported d; the inspected paths and saved records supply neither.

## 6. Public scope and preserved failures — SOURCE-TRACED

Sources: README.md:5-55 and its explicitly historical section; STATUS.md:3-22; lean/FORMALIZATION.md:1-38; TAO_OBJECTIVES_CURRENT.md:1-38; PHASE54_VERIFICATION.md; PHASE54_RESULTS.json; preserved first-build result/logs/sources, interrupted root stdout/stderr, and Phase54InputCheck saved stdout.

The current public theorem description matches the actual type: totally complex rational degree-two K, actual class number one, actual absolute field discriminant <62,500,000,000. It distinguishes local acceptance from exact-head CI and independent human review, says Phase51 predates the new additions, and does not announce novelty, optimality, all challenge objectives, higher class numbers or new full classification. The existing canonical-family classification is described separately; the new cutoff does not borrow it. Historical old-cutoff/open-gap statements are labelled as history rather than used as current evidence.

The failed first Phase54 target build, its three source snapshots, and interrupted root logs remain present. The incomplete root lacks a terminal result and is expressly not counted as success. The integrity check verifies five terminal records, first-build failure then success, exact guard repair, all archived hashes, exact helper generalization and prior evidence correspondence. I inspected the failure result (exit 1,66.1649854s), the interrupted log tail without completion, and the saved signature/closure outputs. I did not verify live CI or remote publication state, and infer no CI success from local records. No public overclaim requiring a FATAL/GAP/SLOPPY finding was established within these checked passages.

## Checks performed, assumptions and exclusions

Executed from the repository root in PowerShell, using read-only escalation after the normal helper failed with `helper_sandbox_lock_failed`:

- `git rev-parse HEAD`
- `git rev-parse '86abe21f1ca023f9f62f99d1f785cdb361d86010^{tree}'`
- `git status --short`
- `git diff 86abe21f1ca023f9f62f99d1f785cdb361d86010 -- lean/TenthDiscriminant`
- `git diff bd2a207 86abe21 -- lean/TenthDiscriminant/TunedRadiusFamily.lean lean/TenthDiscriminant/TunedAnalyticCutoff.lean`
- `git diff --exit-code 86abe21f1ca023f9f62f99d1f785cdb361d86010 -- research/ender_radius_bridge/Phase54InputCheck.lean README.md STATUS.md lean/FORMALIZATION.md TAO_OBJECTIVES_CURRENT.md`
- `python -B research/ender_radius_bridge/verify_phase54_results.py` — PASS, evidence integrity only.
- Targeted `rg -n`, `rg --files` and `Get-Content` source/evidence reads recorded above.

No Lean build, numerical experiment, parameter search or browser/CI query was run. The mathematical calculations above are explicit re-derivations, not fabricated empirical measurements. Inherited Mathlib algebra/Galois/discriminant facts, rational-log soundness, certified prime constants, local Frobenius divisibility, maximal orders/ideal norms, and global jet positivity are assumed at their inspected theorem interfaces. Some were followed through immediate proofs, not recursively re-established to axioms.

Tool failures were preserved in this conversation: initial sandbox launch failure; unquoted PowerShell `^{tree}` parsing produced an invalid revision before correction with single quotes; a brace-style path caused a PowerShell parse error; initial guesses for FORMALIZATION/Phase54InputCheck/EvenDiscriminant paths failed and were corrected by file discovery. These were read-only lookup errors, not proof failures. No report reroll followed them.

This report is the first final report and must remain byte-for-byte preserved. Any later correction belongs in a separate record. A bounded absence of findings is not an end-to-end certification of the development.

Finalized: 2026-10-26 16:18:37 UTC.
