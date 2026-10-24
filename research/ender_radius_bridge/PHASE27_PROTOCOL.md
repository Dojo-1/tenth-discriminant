# Phase 27: reusable prime-mass envelopes, not duplicated interval tables

Base: `44ee9ca40b8619ef242f3a3415a630e7d9270215`. Prior turn was progress:
the first bounded class-number exclusion is checked, published draft PR 28,
and passed pinned CI 40115806920 with identical branch/merge trees. Refresh
the branch and preserve the generated untracked lake manifest. No live proof
process remains at registration. Overall global-bound objective stays active.

## Mathematical target

For arbitrary natural R,S,P,Q with R>=2, S>=1, Q>=3, prove reusable estimates
on the existing production masses, not a replacement matrix. Write
V=R(R-1)/2, W=R(R-1)(2R-1)/6 and a=S-1/2. For primes p:

* floorSum(R,p) >= V/p-R (retain the floor-error term);
* factorialPowerSum(R,p) <= V/(p-1) (retain all prime powers);
* valuationWeight(R,S,p) >= a*(V/p-R)-W/(2*p^2).

Let A=sum_{p<=P} log(p)/(p-1); on retained primes Q<=p<=P let
B=sum log(p)/p, C=sum log(p)/p^2, E=sum log(p). Prove

    factorialSmallMass(R,P) <= V*A
    smallOddValuationMass(R,S,P) >= a*V*B-a*R*E-W*C/2.

Retaining Q>=3 excludes prime 2. Every omitted actual odd-prime term must be
proved nonnegative. Treat empty retained sets and small R correctly. Derive
a clipped uniform lower envelope below the unchanged enderPrimeMassLower,
then connect it to the already checked actual-Gram comparison under the
existing class-number/radius/range/padding guards. No new analytic premise
may be hidden in notation. Do not assert the global cutoff from an envelope.

## One fixed certificate pilot

Keep Q=7, P=10000, eight log terms and scale 10^12, with the same 1229 prime
labels and log enclosures already checked in the first-interval development.
Generate untrusted integer rounded bounds for A,B,C,E by cross multiplication,
not a trusted rational/primality oracle. Reuse checked prime coverage and
log bounds. Prove finite totals on bounded chunks, then compose symbolically.
Run one exact-rational observational pilot for the SAME first interval:
R=175000000000, S=8750000000, rho=408406701, padding=488. Attempt to recover
its existing budgets (1324*10^20 and 7995*10^29), without changing them.
If the conservative envelope fails, preserve that negative result rather
than tuning Q,P or the interval. No parameter search or new cutoff campaign.

The purpose is a theorem uniform in R,S and reusable fixed constants, not
another isolated proof of the already closed interval. Other intervals,
unbounded closure, even cases and finite classification remain separate.

## Controls, resources and delivery

Require controls rejecting omission of the floor-error term, omission of the
quadratic loss, and removal of S>=1 or the retained-prime exclusion as
applicable. Check rounding inequalities with supplied integers and exact
proofs; no native decision, added axioms, modified pins or trusted output.
Use existing 8192-MB owned-process cap and record every terminal failure.
If normalization is too large, partition the identical fixed checks into
bounded chunks/at most four modules; do not weaken targets or change inputs.

Run full root build, source correspondence, compiled axiom audit, matched
apparatus and inherited negative controls via pinned CI on the exact published
commit/tree. Preserve local parent deadlines separately from individual and
remote passes. Update README/STATUS/FORMALIZATION and a short human guide;
keep current Tao-objective verdicts distinct from candidate claims.
Only update draft PR 28, do not merge or post to Tao, and claim no novelty,
optimization, global bound or classification from this reusable bridge.
