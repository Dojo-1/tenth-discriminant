# A smaller bound, with the same arithmetic integer

**The 48-billion actual-field theorem is integrated unchanged into the Lean
library.** Module build, complete build, fresh dependency checks and the
whole-library audit passed on their first invocations. [PR42](https://github.com/Dojo-1/tenth-discriminant/pull/42) merged at
`0bde1bf58893f1adf66bfded5eaf1a0f270c6dce` after pinned CI and security
passed. Source, tested merge and actual merge have the same tree.

For every imaginary quadratic number field of class number one, Lean proves
that its actual absolute discriminant is below 48,000,000,000. The theorem
requires no supplied generator, earlier cutoff or known list of fields.
The bound improves 50 billion by 4%. It remains much larger than bounds
from other approaches; no optimality, novelty or classification claim.

The geometric freedom is to change polynomial observations by an integer
matrix of determinant 1. The integral row lattice and determinant survive,
as do every prime divisor and the ranks between frames modulo each prime.
Real positivity retains the original point-count/depth guards. Individual
row norms can change, and real rank need not survive reduction modulo a
prime. These distinctions are checked rather than inferred from a picture.

Centering the radial quantity ZW lowers a UNIFORM geometric ceiling.
Every ordinary derivative term, the origin and integer rounding remain.
The sufficient 0.010 scale gain now bounds the SAME original determinant.
Class-number arithmetic forces prime powers into that integer; factorial
estimates bound their logarithmic mass from below. The fixed 48-billion
endpoint makes that lower bound exceed the new upper bound.

[Read the human proof](FORTY_EIGHT_BILLION_GUIDE.md) ·
[Exact integration evidence](PHASE121_VERIFICATION.md) ·
[Standalone theorem evidence](PHASE120_VERIFICATION.md).

All 56 written public theorem types/proof bodies, 6 data definitions and
private helpers are unchanged. Three production modules and three root
imports expose the result. The whole audit has 5,584 logical declarations,
4,772 theorems and17,029 runtime auxiliaries (recorded separately), covering
202 reachable modules. There are 134 added logical declarations and zero
removals: 132 from the accepted bodies plus two generated equation theorems.

The stronger 0.013 estimate remains paper. Earlier failed/stopped attempts
are preserved. The older AI review of the 50-billion proof does not cover
this new argument; independent human semantic review remains open.
