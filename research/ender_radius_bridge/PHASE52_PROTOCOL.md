# Phase52: recover the omitted exact3/5 contribution in the uniform proxy

Base published10b684c (review/doc head); mathematical sources69010f4.
CI40229150685 is live, security40229148012 passed. No push/cancel/restart
while that run is live. Both authorized reviewer cycles are completed;
no additional agent is authorized by this protocol.

Source inspection before this registration found that the certified uniform
small-prime proxy retains primes>=7, while the production small-prime
budget contains all odd primes up to10000. Thus3 and5 are already omitted
from the proxy, not newly lost by unclipped negative contributions.
The target recovers their exact existing valuations, not stronger exponents.

Fixed target: define recoveredPrimeMassLower as certifiedPrimeMassLower
plus2*(F(R,S,3)*log3+F(R,S,5)*log5). Prove it is bounded by the SAME
enderPrimeMassLower R S10000 I for R>=2,S>=1, through a disjoint prime
partition and clipping without double counting. Prove the proxy improvement
is strict for R>=4,S>=2. Include the R=4,S=2 gain2log3 control and a
zero-gain control at R=3,S=2. No unconditional strict-gain statement.

Keep every determinant weightF, original derivative convention, sample
construction, production expression, pin and workflow unchanged. The proof
must identify the retained>=7 budget before adding back3 and5; an inequality
to the full small-prime sum alone cannot justify adding them again. No new
inertness assumption is supplied: connecting production to the actual Gram
still uses the existing guarded class-number/prime bridge.

Budget: at most3 target builds (initial and2 local elaboration repairs),
600 seconds/8192MB per process,1200 seconds cumulative. A resource stop
ends the cycle. Preserve every failed source and raw record before repair.
No numerical pilot, parameter search, inherited-proof changes or fallback
success. New module plus root import only; after acceptance, whole root,
public signature/control/standard-axiom check and source correspondence.
Future publication-head pinned CI is separate.

Human scope: this is a strictly stronger certified proxy under the stated
dimension guards, not a new prime valuation or numeric discriminant cutoff.
Any affine-envelope estimate for the recovered terms, lower-radius guard
or new threshold requires a later separately registered proof. No full
classification, novelty, optimality, higher-class-number, merge or Tao post.
