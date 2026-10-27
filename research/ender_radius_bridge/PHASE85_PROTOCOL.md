# Phase85: sealed scalar feasibility test for the normalized h<=2 budget

Base1cf5f5ed564a7aad2e472dc00fac54812ffde55f. Register before code/execution.
One bounded numerical test, no Lean/source/tool/pin/certificate/gate changes.
Preserve all earlier proof attempts, protocols, manifests and verifier sources.
No publication/merge/reviewer/Tao or new cutoff claim.

## Frozen mathematical mapping

Use existing class-free scalar envelopes: FiftyBillionCutoff.fifty_normalized_lower
>=.999997logD-5.739, TunedAnalyticCutoff.normalized_upper<=.8logD-.813, under
their explicit D>=50b and earlier geometry guards. Their difference is
.199997logD-4.926. Same fixed R=floor(D/4),S=floor(R/25),L=R. The84 loss ratios
are lossScale/(R²S)=(R-1)/R<=1 and parameter divisor scale/(R²S)=(S-1)/R<=1/25.
For D>0,L>=3, L<=D, actual chartCost(D,L) is at most the conservative candidate
 H(D)=(4/sqrtD+1/sqrt(sqrtD))*(2+u*(1+u))+1/3, u=logD.
Derivation: pi<4,pi>3=>2sqrt(2/(3pi))<1; log3<=2; logL<=logD;
keep the constant payment separate. The H majorization and composition with
actual prime mass/upper_B are NOT yet a new checked Lean theorem.
Test m(D)=.159997logD-4.926-H(D). Positive is ONLY scalar feasibility, not proof
for every D>=endpoint, a field statement, classification or a new cutoff.
The sample powers2^N are scalar arguments and need not be squarefree/3mod4.

## Sealed design / controls

Exactly N=36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,80,96,128 (18points),
no adaptation/refinement/reroll. Python decimal only, no dependency installation.
Run all points at100 AND200decimal digits within the ONE registered invocation.
Basic arithmetic uses directed ROUND_FLOOR/ROUND_CEILING endpoint evaluation.
Built-in ln/sqrt are correctly rounded half-even (local Python docstrings),
enclose each endpoint result with next_minus/next_plus at the same precision.
Record intervals for logD, H and margin; classifications positive if lower>0,
negative if upper<0, otherwise unresolved.100digit interval must contain200digit
interval for every result; any failure stops, no changed precision/retry.
Controls before samples at eachprecision: rational1/3 enclosure; exactsqrt4
andlog1; ln4 contains2ln2; sign controls positive/negative/straddlingzero;
mutation control removing +1/3 must change H by enclosed1/3 (not silentlyomit).
All rational constants read as exactDecimal strings/fractions, no float arithmetic.

One run cap120seconds/8192MB, snapshot source/stdout/stderr/result. STOP on ANY
resource stop/control failure; no codefix/rerun under85. Output raw full18x2grid,
Python/libmpdec versions, timings and source hash. Record firstpositive sealedN
without claiming minimum/optimality, preserve every negative/unresolved sample.
Saved verifier checks hashes, grid, controls, interval nesting/signs, runtime,
and frozen84source/evidence. Do NOT rerun84rootfixedverifier after no production
change unless needed; no fullCI/old numerical campaigns/reviewer.

Explain the exact tested formula and remaining proof obligations to humans.
Update currentREADME/STATUS/FORMALIZATION/objectiveledger with distinct
Lean-checked84 versus numerical-feasibility85. README61lines; actual h1cutoff50b
unchanged. Nextattempt, if positive: separately preregister all-D monotonic
majorization and genuine prime-mass/diagonal/cutoff composition with a fresh
assumption audit; scalar helpers may be used only under their actual guards,
no class-number-one/cutoff theorem assumed.
