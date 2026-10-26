# Phase62: prime-axis factorization and the two-class constant

Register before proof source/execution. Base b4cff273f620ead13fc60097222fac01cce4ab67. PR30 Phase61 CI40403267176/job121854391609 is live; no restart, cancellation, replacement push or status transfer. This is a separate local branch/cycle, not a rerun of the exhausted Phase61 builds or timed-out control suite. Old sources/budgets/results remain frozen. No reviewer or merge authorized.

## Fixed target

For a natural leading coefficient a, integer x and natural prime p, prove
(a:Int)*x^2=p iff a=p and x=1 or x=-1. Derive that the zero row of the actual binary form ax^2+bxy+cy^2 represents primes at at most two integer x, and none when a=1. For an arbitrary finite coordinate set U, formalize the filtered prime-axis cardinal bound<=2 and principal cardinal=0. Prove by prime factorization (a square factor in a prime must be1), not a bounded numerical search.

Prove conditional finite aggregation: a nonempty finite family has a distinguished principal member. Suppose its prime-representation counts q_i are bounded by A+beta_i plus0 for that member or2 for every other member. If the family has at most2 members and4*N<=sum q_i, prove N <= (h*A+sum beta_i+h)/4, with h its cardinal. The +h/4 constant matches the old H/4 when h<=H=2, after any required nonnegative coefficient enlargement. This algebra DOES NOT supply the per-form nonzero-row bound, representation multiplicity, a class-group/form dictionary, a bound B, or a numerical h<=2 cutoff.

Fixed controls: a=3 gives exactly the two axis points+-1 in U={-1,0,1}; a=1 gives none for arbitrary U; preserve the D=12011 form interpretation. Explain the paper route for the nonzero rows using completion of square, interval count<=length+1 and a decreasing-width integral. State clearly which steps are not Lean-checked; do not relabel the earlier per-form failure as an aggregate refutation or the old campaign as newly certified.

## Limits and evidence

Research-only Phase62PrimeAxis.lean, importing the pinned production library; no production/root/tool/pin/CI-gate changes. Whole fixed target, controls and standard-three-axiom namespace gate must compile together. At most3 complete builds,300seconds/8192MB each,600seconds cumulative, at most2 proof repairs with unchanged types/guards. Stop after any target resource stop; preserve every source/stdout/stderr/result. No hidden rerun, parameter sweep, numerical campaign or weaker substitute. Build runner must snapshot the source and enforce caps. No local Phase61 control rerun.

APIs and the counterexample were seen before registration. This is a mathematical repair attempt, not a blinded test. On failure preserve the precise unresolved obligation. On success claim only the prime-axis theorem and conditional two-class accounting. Keep the human explanation short and README unchanged. Publish only after recording Phase61's terminal exact-head CI result, on a separate reviewable delivery if appropriate.
