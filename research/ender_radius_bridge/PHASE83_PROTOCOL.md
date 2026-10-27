# Phase83: close the actual finite weighted-kernel estimate

Base a4a6fe1b32dbc8bf182e160155c0bec6e69ba0ae. Register before source or Lean execution.
Standalone Phase83ClosedKernel.lean imports frozen root82 and pinned harmonic bounds.
No production/root/tools/pins/certificates/gates changes. Earlier failures and evidence
including82 runner discrepancy remain unchanged. No publication/merge/reviewer/Tao.

## Fixed mathematical target

For L>=3, prove the positive linear operator kernelCost on decreasing f=log(n)/n
is monotone in pointwise prefix bounds on3..L. Prove EXACT affine identity for any
real alpha,beta and any f:
 K_L(alpha*n+beta)=alpha*(3*f(3)+sum_{k=4}^L f(k))+beta*f(3).
The constant must remain separate, never replaced by a growing linear allowance.
Using pinned harmonic_le_one_add_log prove sum_{4..L}log(k)/k<=log(L)*(1+log(L)).
For real M>=0,D>0,n>=3 prove sqrt(M*n/D)<=n*sqrt(M/(3D)).
Define linearSlope(D,M)=pi/sqrt(D)+2sqrt(M/(3D)),
 closedCost(D,M,L)=linearSlope(D,M)*(log3+logL*(1+logL))+log3/6.
Derive the actual countBound(D,n)<=linearSlope(D,M(K))*n+1/2,
with actual ClassFiber.normBound K nonnegative proved from its definition.
Then prove kernelCost L primeKernel (countBound D)<=closedCost D M(K) L,
for D=3mod4 and L>=3, D>0 derived, not supplied.
Finally compose82 actual_gram_budget with nonnegative lossScale, retaining EVERY
actual squarefree/actualh<=2/oddprimes/finitebound/Ender-radius guard and SAMEoriginal
Gram to replace its finite kernel by this explicit closedCost. No supplied
count/Minkowski-discriminant identity/oldh1cutoff/classification/margin assumptions.
No weaker fallback or numerical claim. M(K)-to-D, even/field transport and cutoff open.

Controls: affine L3 endpoint exactly (no sum); alpha0 pays constant only;
constant count contributes f3 once at everyL>=3; closed endpoint L3 nonnegative.
Print allpublictypes/defs, primeKernel/kernelCost, root axioms and namespace audit.
Fresh transitive root check copied from82 same34forbidden inputs; record closure.

## Bounded execution

At most3 standalone target invocations600seconds/8192MB each,1200seconds cumulative,
at most2 statement-preserving repairs. Stop after ANY internal or outer resource
stop; no old-target replay, heartbeat/recursion/limit increase, probes or weakened
statements. One invocation includes all helpers, composition, controls, reporting
and dependency exclusion check. Snapshot source/stdout/stderr/result each attempt.
Preflight names/reporting/34exclusions beforefirst run. On success no further83run;
verify saved evidence and frozen82 verifier, no full root/audit rerun because source
is standalone. Preserve negative attempts exactly. Explain the bound to humans;
keep README61lines and cutoff50billion; no externalCI/humanreview claim.
