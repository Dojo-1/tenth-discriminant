# Phase105: two-dimensional coordinate and literal-shift compatibility

Basebe1c0e36b9eea47a846277383253318063e717e0; separate local branch
codex/coordinate-shift-compatibility. Register before source/Lean run.
PR36head staysbe1c0e3 during its ownCI40700006963/job122856935607; do not
push this new math into that run. USER requests BOTH coordinate maps and
literal lattice shifts, explicit invariants, maximum effort, no copycat
method. This is a new full proof bridge, not a new numerical cutoff.

Five definitions: shift(v) asZ^2equiv p->p+v,inversep-v; orderPoint(D,p)
inZ[T]/(T^2+D);embedding(D) fromactual rational quadratic quotient toC
sending root to pairEvalD(0,1);integralPoint viaexistingactualorder map;
oddCoordinates(x,y)=(x-y,2y). Definition types and mathematicaldata fixed.
Only proof components of shift inverse laws/embedding root validation may
be repaired; executable/data formulas cannot change.

25main public types: shift_zero,shift_comp,shift_inverse,pairEval_shift,
pairEval_sub,metric_translation,orderPoint_to_field,embedding_root,
integralPoint_eval,integralPoint_shift,integralPoint_norm,
coordinate_norm_commutes,even_coordinates_bijective,
actual_integer_norm_commutes,odd_coordinate_matrix,odd_coordinate_shift,
odd_coordinate_norm,odd_order_norm_commutes,shifted_points,shifted_card,
shifted_ellipse_membership,shifted_gram_cast,shifted_valuation,
shifted_posDef,coordinate_translation_bridge.

Full commuting selected-lattice/order/actualfield/complex diagram, actual
norm=complexnormSq, full actualevenmaximalring coordinatebijection under
positive/squarefree/mod1or2guards, explicit odd sublattice index2 matrix
and norm identity viaexistinghalf-order norm. Literal2Dshift group laws,
cardinality and centeredmetric/ellipse transport; original shiftedinteger
Gram cast equals original realGram on actual shiftedcomplexpoints, SAME
row order/ordinaryZderivatives/factor2. Preserve generic odd nonsquare
prime valuation exponent and strict Gram positivity under actualpointcount.
The final bridge derives all these parts internally, no callercoordinate/
norm/cast/cardinality/divisibility/PD premise; preserve ordinary guards.

Four frozen controls: actual Gramdet24 for Q={(-1,0),(0,0),(1,0)},D1,J1,
R2,S1 versusdet60 afterverticalshift(0,1),with3points exceedingthe strict
count threshold; D0coordinatecollapse; odd-coordinate matrixdet2!=1;
both-axis nontrivialshiftcomposition. NO blanket realtraceGram determinant
invariance is assumed. These are intended theorems/counterexamples, not
measured results until fulltarget passes. No cutoffgain is claimed.
All29publictheorem types and4controls frozen at firstinvocation; max2
proof-only repairs,including specified proof fields, no weaker statement.

Same58excludedroots as104 PLUS threeEvenTwoClasscutoffs,EvenMinkowski
actual_minkowski/normalized_actual_gram_budget/scalar_actual_gram_budget,
EvenSplitPrimeBudget.actual_gram_budget,EvenClassAggregation prime_prefix/
uniform_two_class bounds,EvenPrimeFamily.controlled_family (68total).
Fresh closures for coordinate_translation_bridge,odd_order_norm_commutes,
shifted_gram_counterexample;all29types/5definitions/finalbridgeaxioms and
namespaceaudit;standard3axioms only. Use existing algebra/norm/Gram/
pointcount/Frobenius theorems, notanyclass-numbercutoff or numericalpilot.

Max3full standaloneLean invocations600s/8192MB perownedprocess,
1200scumulative. Stop anyinternal/outerresource stop;no probes/weaker
target/heartbeat/recursion/limitincrease/replay. Fullsource/stdout/stderr/
result eachrun;preserve failures/repairs. Production/root/tools/pins/CI/
certificates/priorprotocols/raw/verifiers/reviews/ledgers/failures frozen.
No productionintegration/rootbuild/audit/numericexperiment/Taopost/new
reviewagent here. PR36CI/authorizedmerge mayfinish separately with its
head unchanged;no success transfer to105. Savedverifier fixedtypes/
defdata/controls,exactrepairs/68exclusions/axioms/budgets/raw/frozenfiles.
Updatehuman/currentREADME61/STATUS/FORMALIZATION/objectives/reply after
resultknown. Futurelowercutoff experiment needs its own preregistration.
Goalactive;arbitraryfieldtransport/independentreview remainopen;Argonpending.
