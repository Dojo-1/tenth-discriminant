# Phase118: sufficient quantitative ordinary-jet estimate

Base ab5558ff7b482a6bec185b37115b6faf57a82c28. Separate research branch
codex/radial-jet-majorant, secondary checkout. PRIMARY publication head
MUST remain ab5558f while PR41CI40853123367 runs. No primary source/root
change, new CI dispatch, old trial replay or stopped113/114repair.
Register before new Lean source or invocation.

## Fixed scientific target: SAME48b endpoint via a simpler sufficient bound

The stronger.013hypergeometric estimate in115remains PAPER, unchanged.
This cycle aims at a different elementary estimate that still supports the
SAME fixed48bendpoint; no endpoint/parameter search or numerical experiment.
For r,s,j natural,h real>=0,j<=r, define the FULL Leibniz coefficient
 B(r,s,j,h)=sum_(k=0..s) choose(s,k)(j)_k(r-s)_(j-k)h^(s-k).
Prove universally
 B <= (r)_j*(h+j/(r-j+1))^s,
using (r-j+1)^k <= (r-(j-k))_k and exact descending-factorial splitting.
Retain all terms, including zero factors from k>j and higher derivatives.
Prove the actual ordinary derivative formula for (X*Cw-Cb)^s, all orders,
and the full Leibniz/pointwise norm bound for the ACTUAL RadialOperator
polynomial, not a surrogate coefficient chosen for easier estimates.

For integer rho>=5,a=floor(rho^2/2),all complex z with normz<=rho,
prove |normSqz-a|<=(13/25)rho^2. For every r,s,j<=r prove old radial
majorant norm(jet)<= (r)_j*rho^(r+s-j), including r<s and origin.
Prove all jets j>r vanish. For S>=1,s<S,j<S,r>=9S, prove the sharper
 norm(jet)<= (13/20)^s * (r)_j*rho^(r+s-j).
No divided derivatives, sample symmetry, dropped Leibniz columns,
new integer Gram, new p-adic exponent, supplied independence, positive
determinant or supplied quantitative inequality.

Prove log(20/13)>=43/100 using fixed existing sound rational log checker
with N2,x20/13,k0,lo43/100,hi44/100 (default Lean resources unchanged).
Prove for S>=100,25S<=R<=26S the normalized savings from rows r>=9S
are at least1/100: (R-9S)S(S-1)log(20/13)>=(R^2S)/100.
Prove the fixed scalar separation at logD>=24.5813, with upper.8logD-.823
and recovered lower.999997logD-5.739; exact margin.0001862561>0.
This is a sufficient bound for48b, not a proof of the stronger.013claim.
The full original-Gram logarithmic aggregation, actual-field cutoff,
production integration and pinned CI remain required after this target.

## Fixed controls and acceptance

SAME-source controls: j=r=1,s1,h13/25 givesB=1 (reject naiveh^s);
s=0 givesB=(r)_j in the guarded j<=r range; origin Q11(a3) value-3
and first jet at1,w1 equals1; second ordinary jet Q21(a3,w1) equals2;
rho5rounding a12 leaves13/25>1/2; S1aggregate gain0; endpoint comparison
with logD24.58 FAILS under the fixed coarse envelopes+gain.01 (preserve
this negative endpoint control, no retroactive tuning).
Freeze all public mathematical types and data definition bodies at first
call; up to2proof-only repairs/private helper additions, no weaker types,
erased controls or partial-success substitution. Check every public type,
namespace audit and fresh closures for coefficient, actual norm gain and
scale gain, excluding all70old116roots and permitting only standard3axioms.
The actual operator/proofs in production remain byte-exact.

## Budget and stop rule

At most3full standalone Lean calls,600s/8192MB perownedprocess,1200s
cumulative. Default heartbeat/recursion limits unchanged; STOP permanently
on any inner/outer resource stop, with no remaining-slot use/probes/repair.
No numerical trial and no standalone116/117replay. Execute new research
source from PRIMARY lean cwd/cache pinned to ab5558f, explicit secondary
source path; freeze PRIMARY tracked files and all earlier SECONDARY files
except current readers/.agent state. Preserve each source/stdout/stderr/
result before repairs; preserve every failed attempt and exact diff.
After terminal result save raw archive/read-only verifier and short human
scope guide. Update currentREADME61/STATUS/FORMALIZATION/ledger61/reply
on this SECONDARY branch only. Do not change or push PR41head. No root
build/integration/CI/publication/newreviewer/Taopost in this cycle. Published
cutoff remains50b until a full new actual-field theorem and CI pass.
