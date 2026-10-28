# Phase113: full angular-weight blocks on the same arithmetic Gram

Register before implementation/execution. Base7913eba8ac3ec0bcf765036ba5cebd8f0197463f.
Separate checkout/branch codex/radial-weight-blocks; PR40's tested branch
codex/control-priority-policy MUST remain7913eba while CI40759337480 runs.
No source/root/controller/pin/workflow change or extra CI dispatch here.

## Fixed object and hypothesis

Use the original factor-two REAL ordinary-derivative trace-Gram. Group
rectangular rows(r,s) by INTEGER weight r-s. If r+u=t+s, their cross entry is
  2 sum_{j<J,j<=r,j<=t} (r)_j(t)_j M_(r+u-j),
M_n=sum_(x,y in P)(x*x+D*y*y)^n. Both conjugate channels are retained.
No angular averaging, sample rotation symmetry or Hermitian replacement.
Each diagonal keeps ALL its own derivative columns.

The product of actual principal block determinants is a Fischer upper bound
on the SAME original determinant, refined relative to the old disjoint-pair
and diagonal products. This known matrix inequality and general moment
identity are paper mathematics here, not new Lean theorems. Keep arithmetic
lower product from ACTUAL odd inert primes only, with exact weight
sum_(r<R,s<S)min(r//p,s). Do not assume every prime<=R is inert.

## Sealed finite corpus and endpoint

Exactly12cases: D in[19,43,163], R in[40,80,160,320], S=floor(R/25).
Use the EXISTING annulus18D<=x*x+D*y*y<=36D, distinct integer points,
y in[-6,6], and J=max(points per horizontal line)+number of lines.
Reuse is intentional; this is not held-out generalization. Rank guard is
J>=L+M and card(P)*J>2RS+J(R+S). If it fails, record NO CERTIFICATE,
not singularity, and perform no advertised determinant certification.
Keep all failed/unresolved cases. No parameter/radius/point-set search.

For guarded cases calculate exact diagonal product H, old safe-pair product
B2 and full weight-block product BK. Require0<BK<=B2<=H and actual inert
product<=BK. Record normalized logarithmic gains versus H and B2, and the
remaining gap above the actual inert product, at80and160decimal digits.
Leading1024bits suffice for log diagnostics; discarded positive relative
tail<2^-1023. Diagnostics are NOT Arb intervals or Lean certificates.
Store exact integers in signed base64 big-endian encoding, moments, all
block determinants and products. Do not serialize huge decimal integers.
No full campaign Gram matrix, full determinant or Smith form.

Primary feasibility gate, fixed BEFORE data: all THREE D cases at R160
must satisfy the rank guard and normalized gain log(H/BK)/(R^2*S)>=.02
at both precisions. Within1e-60of the threshold is UNRESOLVED, never PASS.
Other cases report scaling/failures only. A passing gate justifies a future
uniform-estimate proof attempt; it is NOT a lower cutoff or asymptotic law.
Sampling here is fixed-D annular data, not the production all-D radius.

## Adversarial controls in the SAME invocation

Independently assemble seven small full Gram matrices using frozen
mul/powers/gram AST functions from tools/verify_exact.py (base blob checked;
no driver/import execution). Cohorts: D7 asymmetric[(0,0),(2,1),(-1,2),(3,-1)]
and D19 grid{x=0,1,2;y=0,1}, each R4/S3/J1,2,6; plus D1 unit pair
[(1,0),(-1,0)],R3/S3/J1 singular control. Compare every within-block entry,
full determinant versus block/diagonal products, including negative weights,
origins and nonadjacent rows. D1 is an algebra control, not field discriminant1.
Reject wrong factor2, wrong moment exponent, missing extra diagonal jet,
nonmatching weights/Nat-subtraction collisions, overlapping/missing groups
and assumed orthogonality between different weights. Check determinant
base cases(empty,scalar,zero-pivot swap,singular). Compare weight formula
against frozen G_sum/g/F_exact AST functions on a fixed small grid.

## Budget and evidence

ONE combined controls+campaign invocation,180s/8192MB per owned process.
No repairs, repeats, partial probes, larger grid or resource increases after
any failure/stop. Preserve source/data-jsonl/stdout/stderr/native result
including partial rows. New pure-standard-library script and one-shot
runner only; all previous tracked files/evidence frozen. No Lean execution,
new reviewer, merge or Tao posting. A saved verifier checks protocol ancestry,
source/raw hashes, fixed grid/guards/gate/outcomes and frozen base Git blobs.
After results, add a short human guide and update current reader documents
on THIS branch, keeping README/current ledger61lines and the unchanged
50b h1 cutoff. Raw negative results and old19/43/163campaign remain intact.
The next proof/integration/publication needs a separate registered cycle.
