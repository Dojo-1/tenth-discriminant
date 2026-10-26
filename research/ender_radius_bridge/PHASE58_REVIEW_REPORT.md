# Phase58 first native bounded adversarial review

## Registration, identity, timing and verdict

Reviewer: `/root/final_cutoff_review`, one fresh-context model agent. No children, reroll, source/proof/gate changes, Git mutations, or external-chat messages. This is the first native report, written once with create-new semantics before returning a verdict. It must remain byte-for-byte unchanged; corrections require another artifact.

- Registration commit: `610f750d36eb05f81c92d0421c997a6189bd2d35`, verified as current HEAD.
- Frozen mathematical commit: `63be64b4ba3ff9795f552dd34bc415f6ea3acb25`.
- Frozen tree: `1ee8bbcc0ff6f7362c96262af1231e439b9b1fcd`, verified with Git.
- Dispatch: `2026-10-26T17:50:40.685250Z`, supplied by the parent and corroborated by PHASE58_DISPATCH.json.
- Exact task-receipt time was not separately clocked: CANNOT-VERIFY its exact timestamp. Receipt was after dispatch and before the first explicit reviewer clock observation, `2026-10-26T17:52:49.5647668Z`. The first tool action was reading the protocol and brief; its first execution failed with helper_sandbox_lock_failed and the escalated read succeeded.
- Report preparation timestamp: `2026-10-26T17:58:41.9033399+00:00`; elapsed from registered dispatch: `481.218` seconds, inside the inclusive 1,800-second cap. Creation/hash receipt is returned separately after the single write.
- `git diff 63be64b4ba3ff9795f552dd34bc415f6ea3acb25 HEAD -- lean tools .github` and the working-source diff were empty. Unrelated existing .agent changes and untracked files were observed and untouched. The parent concurrently added its own source-hash inventory; that is not this reviewer's work.

**Verdict: no concrete FATAL, GAP or SLOPPY mathematical finding identified within these six obligations.** The local calculations in obligations 1, 2, 3 and 6 were re-derived, with inherited apparatus explicitly separated below. Obligations 4 and 5 are source-traced, not complete re-proofs. **Lean/CI NOT RERUN.** Fresh kernel checking and fresh compiled input-closure exclusion are CANNOT-VERIFY in this execution. This qualified absence of findings is not whole-library certification, full classification, novelty, optimality, human review or model-family independence.

## 1. Sharper existing 3/5 recovery — RE-DERIVED

Sources: StrongSmallPrimeRecoveryGain.lean:9-85; SmallPrimeRecoveryGain.lean:11-38; SmallPrimeRecovery.lean:9-113; LogEnclosure.lean:14-96,161-168,211-222; UniformRadiusFamily.lean:59-65.

The positive odd-power log series has prefix P_N(z)=sum(2*z^(2k+1)/(2k+1)) and remainder bound 2*z^(2N+1)/((2N+1)*(1-z^2)). Recomputed with exact fractions: at N=5,z=1/3, prefix `4297606/6200145` and prefix+remainder `189094979/272806380` lie in [0.6931,0.6932]. Since 2^19=524288 <=531441=3^12, monotonicity and the positive-power log identity give log3 >=19*0.6931/12=131689/120000 >1.09. For log5, binary reduction 5=2^2*(5/4) uses z=1/9 for 5/4. The N=8 lower prefix is `710786490865530496/441636478343022105`, exceeding 1.609 and hence 1.6. The analytic series soundness is inherited/source-traced; its rational instantiations were recomputed here.

For p>0 and r in [pS,R), r/p>=S, so sum_{t<S} min(r/p,t)=S(S-1)/2. This yields 2F(p)>=(R-pS)S(S-1), with truncated natural subtraction valid even when the interval is empty. Under S>=100,25S<=R<=26S, both R-3S and R-5S, and S-1, cast to ordinary real differences legitimately. Weighted addition gives

    2*(1.09 F(3)+1.6 F(5))
      >= (2.69R-11.27S)*S*(S-1)
      >=55.98*S^2*(S-1)
      >=55.4202*S^3.

The positive scale is R^2*S<=676*S^3. The requested gain costs only .081*676=54.756<55.4202. Thus 2*small35Mass/scale>=.081. The code guards every subtraction and denominator used for this deduction. At S=1 both F terms vanish, correctly rejecting the unguarded positive gain.

No new valuation or exponent appears. SmallPrimeRecovery explicitly inserts 3 and 5 into the >=7 retained-prime set, proves disjointness, and embeds the union into the original odd production-prime set. The max-clipped small-prime proxy is bounded by the retained sum before adding these two terms. This rules out double counting, including the potentially delicate clipping step.

## 2. Geometry at 450^4 — RE-DERIVED local changes; inherited count/interpolation SOURCE-TRACED

Compared both changed files against 86abe21 with Git. Sources: TunedRadiusFamily.lean:11-161; TunedAnalyticCutoff.lean:10-192; UniformRadiusFamily.lean:35-39,75-86; EllipseUpperCount.lean:182-184,276-322; EllipseCellArea.lean:120-181; LatticeEllipse.lean:77-126,160-191; NormalizedComparison.lean:9-38.

Write t=D^(1/4)>=450, so D=t^4 and sqrt(D)=t^2. Exactly 450^4=41006250000. R=floor(D/4), S=floor(R/25), J=S. Floor remainders give all changed dimensions: R>=100000000, S>=500000, 10R<=251S, R<=10000S, D/5<=R<=D/4, and S<=R/25. In particular R=25S+r with 0<=r<=24 makes 10R<=251S immediate for S>=240. The lower log floor ratio uses R>=.249D and the inherited log(1000/249)<=1.4 certificate; the upper uses R<=D/4. The newly introduced geometry log bound follows from 450^4=2^4*3^8*5^8 and the available rational lower logs, giving at least 24.3644>24.

rho=ceil(.52*t^3) satisfies .52*t^3<=rho<.52*t^3+1<=.521*t^3. The last step remains valid at t=450 and increases with t. Hence rho>0, rho<R using R>=t^4/5. The odd-case strict inertness uses D=3 mod4 to prove floor(D/4)<(D+1)/4 as an integer inequality. It is not an inclusive endpoint convention; the D=163,R=41 rejected control is appropriate.

Radius admissibility is checked independently of the affine budget: 3R+S<=.76D and .495^2*3.14=.7693785>.76 imply sqrt((3R+S)*sqrt(D)/pi)<=.495*t^3. Remaining slack is

    .52*t^3-1.001*.495*t^3-10*t^2
      =t^2*(.024505*t-10).

At t=450 its second factor is 4109/4000>0. This verifies the radius theorem's changed threshold. The inherited EllipseCellArea theorem discharges the area premise and gives strict card>3R+S, then interpolation gives positive definiteness and a positive actual integer determinant. I did not re-prove the entire interpolation/measure apparatus.

The upper count keeps Y=floor(rho/sqrt(D))<=rho/sqrt(D) and n=pi*rho^2/sqrt(D)+2rho+2Y+1. Using rho<=.6t^3, pi<4, n<=1.44t^4+1.2t^3+1.2t+1<=4t^4 for t>=450. No ceiling/floor term is removed. The log-radius certificate log(.521)<=-.65 follows from log(1.042)<=.042 and the log2 bound. Also logD/R<=1/9000 follows from logD<=2(sqrt(D)-1), R>=D/5 and sqrt(D)>=90000.

The changed rho/R bound is .521*5/450=521/90000. Together with logD/R<=1/9000 it gives (rho+log(R/rho))/R <=531/90000<.01, because 0<=log(R/rho)<=logD. With 2(S-1)<=R/10, the endpoint correction remains <=.001. The sample-count logarithm is <=.00025, retaining log8 and R>=100000000.

After dividing by the positive R^2*S, put a=S/R in [0,.04]. The other two normalized terms are bounded by

    (1-a)*(.75u-.65)+2a*(u-2.38).

The coefficient 1.25u-4.11 is positive for u>=24, so a<=.04 gives <=.8u-.8144. Adding .00125 gives .8u-.81315<=.8u-.813. This checks every changed geometric-helper role, the positive scale and the retained .001 correction, rather than relying on endpoint affine separation alone.

## 3. Fixed 50-billion endpoint — RE-DERIVED

Sources: FiftyBillionCutoff.lean:10-72; TunedRadiusFamily.lean:95-104; AspectRatioLowerEnvelope.lean:79-87; Mathlib/Data/Complex/ExponentialBounds.lean:62.

50,000,000,000=2^10*5^11. The actual inherited Mathlib bound is log2>0.6931471803; log5>=1.609. Thus logD>=24.630471803>24.6304 at and above this endpoint. The exact rational check also passed with the slightly weaker 0.693147180 bound.

The raw lower envelope is inherited/source-traced: .999997*logR-4.419, and logR>=u-1.4 gives at least .999997u-5.820 (the computed loss is only 5.8189958). Adding the .081 recovered gain yields .999997u-5.739. Subtracting the upper envelope yields

    (.999997-.8)*u-4.926.

Its slope is positive. At u=24.6304 its exact value is 1909/312500000=.0000061088>0. At u=24.6 the value is -30369/5000000=-.0060738, so the rejected-control theorem says only that these coarse estimates fail to separate there. It does not assert existence of a field, a sharp threshold, or failure of the underlying determinant method.

## 4. Actual Gram sandwich and excluded inputs — SOURCE-TRACED

Sources: FiftyBillionCutoff.lean:45-72; PrimeTail.lean:116-164; PrimeMassLower.lean:42-61,96-181,401-439; SmallPrimeRecovery.lean:34-113; UniformPrimeMassCertified.lean:56-77; PrimeMassAssembly.lean:48-204; EnderUpperB.lean (ordinary diagonal bounds, upper expression and final two ellipse comparisons); IntegerTraceGram.lean:60-171; TraceGram.lean:15-24; RectangularRowAction.lean:17-34; RectangularGramFactor.lean:223-281; RectangularValuation.lean (exponent sum and determinant factor); ClassNumberInertBridge.lean:25-76; SmallPrimeBridge.lean:66-75; InertFrobenius.lean:120-128.

Under class number one, the maximal-order quotient/norm bridge gives the nonsquare local condition at every odd prime below R, using the strict cutoff. Frobenius, the actual ordinary-jet row action and the integral two-sided unimodular factor give p^(2F(p)) dividing the SAME integerRectangularTraceGram(ellipsePairs D rho,D,J=S,R,S) determinant. Distinct primes permit multiplication of their factors. Chosen-radius geometry makes the determinant positive, so divisibility implies the product<=det. The integer-to-real cast is entrywise and determinant-preserving, using injective complex sampling for D>0. Hadamard gives det<=product(diagonal). Logarithms are applied with positive arguments.

Definitions retain ordinary Z derivatives r.descFactorial(j)*Z^(r-j)*conj(Z)^s, with the conjugate factor constant, j<=r else zero. Both integer and complex pairings retain 2*Re(v*conj(w)); integerPairTrace=2*(a_x*b_x+D*a_y*b_y). Rows retain r=i/S,s=i%S, and the original finite sample indexing is retained rather than replaced by residue-image samples.

The exact direction chain is:

    recovered(tailBudget) <= recovered(actualTail)
      <= production(actualTail) <= exactOddPrimeMass
      <= log(product(actual diagonal)) <= upperB.

The first inequality uses actualTail<=tailBudget and antitonicity in the tail: larger loss budgets weaken the lower bound. Recovery adds a tail-independent term, preserving that direction. The finite actual tail is discharged by PrimeTail; clipping is bounded by nonnegative actual masses, not assumed branch behavior. The separately established strict upperB<recovered(tailBudget), with positive scale, contradicts this chain.

Inherited results not re-proved here: principal-ideal/maximal-order norm bridge; universal Frobenius law and jet-power divisibility; unimodular basis determinant; interpolation and geometric measure proofs; factorial analytic estimate; prime-table coverage, all row certificates and their sum; analytic tail comparison. Their interfaces and relevant source applications were inspected, not exhaustively re-proved.

Compiled exclusions: read Phase56InputCheck.lean in full. It traverses the compiled root closure, rejects each of 25 named old-cutoff/classification/finite-answer/fixed-ratio declarations, unresolved or unsafe reached constants, and axioms outside propext/Classical.choice/Quot.sound. It tests the odd 50b root, the canonical discriminant root and the abstract-field root. The saved Phase56 input stdout reports respectively 55475,55810,58604 reached, none of the 25 forbidden inputs; its result JSON records exit 0. This is historical SOURCE-TRACED evidence, not my execution or a proof that every imaginable forbidden semantic formulation was enumerated. Imports alone are not used as evidence of exclusion.

Phase56/57 build and audit result JSONs report exit 0; both requested audit stdout paths are absent locally, so their complete namespace-audit textual output was not verified here. Phase57 input stdout/result are present and were read. The parent's pinned CI40367229446 SUCCESS is supplied parent evidence, NOT checked or rerun by this reviewer. No claim of whole-library audit completion follows from this review.

## 5. Actual-field transport — SOURCE-TRACED, normalization algebra checked

Sources: ImaginaryQuadraticRepresentation.lean:11-184; QuadraticGeneratorBridge.lean:11-37; QuadraticChartEquivalence.lean:96-113,136-137; QuadraticDiscriminant.lean:84-134; EvenClassNumber.lean:19-52; FiftyBillionCutoff.lean:81-117.

For arbitrary totally complex degree-two K, complex conjugation gives a nonidentity involution sigma compatible with an embedding phi. A nonzero anti-invariant u=(x-sigma(x))/2 has sigma(u)=-u. Quadratic Galois automorphisms are {1,sigma}, so u^2 belongs to the rational fixed field. phi(u) is nonzero purely imaginary, hence u^2=r<0 with r rational. This construction uses no class-number-one assumption and supplies the generator rather than requesting one.

Put q=-r=A/B>0. Then z=B*u satisfies z^2=-AB. Factoring positive AB=b^2*d with b,d>0 and d squarefree gives a=z/b with a^2=-d. This clearing-denominators/square-class algebra is correct. The quotient root map from ImaginaryQuadraticField(d) to K is injective and, by equal rational dimension two, surjective; it becomes an actual algebra equivalence.

Class-number-one transport uses PID equivalence for the actual rings of integers, not a stipulated class-group number. Discriminant transport uses NumberField.discr_eq_discr_of_algEquiv. The canonical actual discriminant equals -d for d=3 mod4 and -4d otherwise, obtained from maximal-order bases. Thus a mere radicand bound would not suffice in the even branch. Here the norm-two obstruction proves even class-number-one radicands are 1 or 2, giving actual absolute discriminants 4 or 8. The odd branch uses the new cutoff, and the even branch uses this separate obstruction.

Exact public claim: for every type K with Field K, NumberField K, NumberField.IsTotallyComplex K, rational finrank=2, and NumberField.classNumber K=1, `(NumberField.discr K).natAbs < 50000000000`. No caller-supplied root, generator, pre-existing cutoff or finite-answer premise appears. I source-traced the algebraic/Galois/maximal-order foundations; I did not reconstruct all Mathlib or local ideal-theoretic proofs.

## 6. Exact guarded staircase — RE-DERIVED

Sources: Arithmetic.lean:48; StaircaseExact.lean:8-85; PrimeMassLower.lean:96-112,467-478; NumericalWeights.lean:139-147; Phase57InputCheck.lean.

For p>0, min(floor(r/p),t+1)-min(floor(r/p),t) equals 1 exactly when p(t+1)<=r. Thus C(t+1)-C(t)=max(R-p(t+1),0). Lean's natural subtraction correctly expresses this before a threshold-fit assumption is made. When pt<=R, every increment through t is unsaturated and summation gives 2C(t)=t*(2R-p(t+1)); Nat.cast_sub uses precisely the required fit guard.

Under p(S-1)<=R this identity applies to all t<S, giving

    2F = 2R*sum(t) - p*sum(t(t+1)),
    sum(t)=S(S-1)/2,
    sum(t(t+1))=S(S-1)(S+1)/3,
    6F=S(S-1)*(3R-p(S+1)).

The final polynomial is over the reals. S=0 and S=1 are valid zero cases even though real S-1 differs from truncated natural subtraction at zero; the source induction treats zero separately. For p=0,R=4,S=2 the original weight is 0 but the polynomial 24. For R=1,S=3,p=2 it is 0 versus -30. These reject deletion of each guard. At R=8,S=2,p=2, F=6 and 6F=36. The older quotient-guarded floor formula would give F=4 if used without its guard, and its negative-control theorem remains intact. No contradiction arises because the hypotheses differ.

I also ran 4678 exact finite guarded cases (R=0..50,S=0..15,p=1..15); all matched. This is an extra finite control, not a universal proof. The general derivation and Lean induction were examined separately. The new theorem counts the pre-existing weight, is not consumed by the 50b proof, and introduces no extra exponent, parity gain or cutoff.

## Commands, actual execution and limitations

All shell calls explicitly used the absolute repository working directory:

`C:\Users\HAL900\Documents\Codex\2026-10-23\referenced-chatgpt-conversation-this-is-an-2\work\tenth-discriminant`.

Actual identity/change commands included:

```powershell
git status --short
git rev-parse HEAD
git rev-parse '63be64b4ba3ff9795f552dd34bc415f6ea3acb25^{tree}'
git diff 86abe21 63be64b4ba3ff9795f552dd34bc415f6ea3acb25 -- lean/TenthDiscriminant/TunedRadiusFamily.lean lean/TenthDiscriminant/TunedAnalyticCutoff.lean
git diff --exit-code 63be64b4ba3ff9795f552dd34bc415f6ea3acb25 HEAD -- lean tools .github
git diff --exit-code -- lean/TenthDiscriminant lean/TenthDiscriminant.lean
```

Source inspection used `rg --files`, `rg -n`, `rg -l`, `Get-Content` (whole files or explicit `-TotalCount`/`Select-Object -Skip ... -First ...` windows), line-number rendering, `Get-FileHash -Algorithm SHA256`, `Test-Path`, and `Get-Date -AsUTC -Format o`. The source locations cited above identify actual reviewed material. The tool transcript retains exact queries/windows. Some attempted filename probes did not exist (ProductionComparison, PrimeComparison, LatticeEnvelope, EnderUpper, EllipseLowerCount, and a scripts directory); some wildcard path probes failed under Windows. These errors were corrected by discovering the actual filenames with rg. They supplied no mathematical evidence. The missing audit stdout was not silently treated as present.

A read-only Python payload was actually executed as a PowerShell here-string piped to `python -`, with no file creation. Its essential exact checks were:

```python
from fractions import Fraction as Q

def pref(n,z):
    return sum((2*z**(2*k+1)/Q(2*k+1) for k in range(n)), Q(0))
def rem(n,z):
    return 2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
p2=pref(5,Q(1,3)); u2=p2+rem(5,Q(1,3))
p5=2*pref(8,Q(1,3))+pref(8,Q(1,9))
u5=2*(pref(8,Q(1,3))+rem(8,Q(1,3)))+pref(8,Q(1,9))+rem(8,Q(1,9))
assert Q(6931,10000)<=p2<=u2<=Q(6932,10000)
assert Q(1609,1000)<=p5<=u5<=Q(161,100)
assert 2**19<=3**12
assert 19*Q(6931,10000)/12>=Q(109,100)
assert 10*Q(693147180,10**9)+11*Q(1609,1000)>=Q(246304,10000)
assert Q(277101,5000)>Q(81,1000)*676
margin=(Q(999997,1000000)-Q(4,5))*Q(246304,10000)-Q(5739,1000)+Q(813,1000)
control=(Q(999997,1000000)-Q(4,5))*Q(246,10)-Q(5739,1000)+Q(813,1000)
assert margin==Q(61088,10**10)>0 and control<0
assert 450**4==41006250000 and 2**10*5**11==50000000000
assert Q(13,25)-Q(1001,1000)*Q(495,1000)==Q(24505,1000000)
assert Q(24505,1000000)*450-10>0
assert Q(495,1000)**2*Q(314,100)>=Q(19,25)
assert Q(521,1000)*450**3>=Q(13,25)*450**3+1
assert Q(521,90000)+Q(1,9000)<Q(1,100)
assert Q(1,4000)+Q(1,1000)-Q(65,100)-Q(411,100)*Q(1,25)<=-Q(813,1000)
assert Q(4,5)==Q(3,4)+Q(5,4)*Q(1,25)
assert Q(999997,1000000)*Q(14,10)+Q(4419,1000)<Q(5820,1000)
def f(R,S,p):
    return sum(min((r//p if p else 0),t) for r in range(R) for t in range(S))
checked=0
for R in range(51):
    for S in range(16):
        for p in range(1,16):
            if p*max(S-1,0)<=R:
                assert 6*f(R,S,p)==S*(S-1)*(3*R-p*(S+1))
                checked+=1
assert f(4,2,0)==0 and 2*(2-1)*(3*4)==24
assert f(1,3,2)==0 and 3*2*(3-2*4)==-30
assert f(8,2,2)==6
old=Q(3,2)*sum(r//2 for r in range(8))-Q(1,2)*sum((r//2)**2 for r in range(8))
assert old==4
```

Actual output included `EXACT_RATIONAL_CHECKS_PASS`, margin `1909/312500000`, 24.6 control `-30369/5000000`, radius slack factor `4109/4000`, and `staircase_guarded_finite_cases=4678`. No Lean build, proof driver, dependency audit, negative-controls runner or CI was executed by this reviewer. Those remain **Lean/CI NOT RERUN**. No general mathematical claim is inferred from finite testing alone.

## Hashes and preservation

Protocol SHA256: `8fb3ac95bcab6e972af6fef2dcb36f91534fff0934b2a5da388d8a92cede292b`.
Brief SHA256: `22c305eab20c6cbce0a135829df248eb813027cd30b979378358f5e9db754fef`.

Working source-byte SHA256 values, with paths relative to lean/TenthDiscriminant:

- `StrongSmallPrimeRecoveryGain.lean`: `b1cdd93d240331030eb809dbb3d524ee2e4730c0ec88c0ed7a49ff540ea2b632`
- `TunedRadiusFamily.lean`: `a1e904b7d332221ee50163406af28676f954589c88155e6df713e770ab55ff73`
- `TunedAnalyticCutoff.lean`: `d8a2da0463bfb050bfe89f90b51e4d238dece6205469fcd14de28b1737e0baa3`
- `FiftyBillionCutoff.lean`: `9abb0bd01eacf4a7acfb4d7d7aa85fd47e7a4a8a45847416be410ea0262ab2cf`
- `StaircaseExact.lean`: `1e478e54b1f4c249757e4cfdd64afdac4e884bd566f8163e171fef8f73f79815`
- `ImaginaryQuadraticRepresentation.lean`: `57975c7b9af10af5bf72a4629b5a32377c99030dce2bc17f1c91a2bc06b72843`
- `PrimeMassAssembly.lean`: `bc9d6cb4ae9fa30d845018262070a2e668c15bda2711433b2dc252db90fc5a61`
- `SmallPrimeRecovery.lean`: `0714650366b6b6283abd556d3e6d9828ddf75cc395e8cbdd2ac70e030e5508b5`
- `PrimeTail.lean`: `de884de9eeeb381759ceb04487bb3f0c4af7b36833fd2a4656feeb87745c9f99`
- `QuadraticDiscriminant.lean`: `648de6c85cc846c563befcd5e2d0dd99160f38b22c47c0d4c3120396de193d4e`
- `QuadraticGeneratorBridge.lean`: `0754b22f7080bfe28e4b4af815de3df4e2a38743b7e8a2afe41b246cf1799bdb`
- `EvenClassNumber.lean`: `b3901088570ac80c2c4fbd2a3189af3d54518a4e2b74d3d775324ad2cd2a033e`

The report's SHA256 is computed after this single create-new write and delivered outside this file, avoiding a self-referential hash. Only this report was written by this reviewer. All limitations and CANNOT-VERIFY statements above are part of the immutable first report.