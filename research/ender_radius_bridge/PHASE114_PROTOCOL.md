# Phase114: symbolic full radial-block bridge

Registered before new Lean source or invocation. Base evidence commit
b9bf8c5d07a394b969a49a562b7a2b6e7768da66 on codex/radial-weight-blocks.
The Phase113 resource stop remains terminal: no replay, repair or rescaling.
This is a distinct symbolic theorem attempt, not another numerical campaign.

## Full acceptance target (all required)

1. General finite REAL positive-semidefinite Fischer inequality: for any
finite partition f:n -> k, det A <= product_b det(A restricted to f=b).
No supplied block inequality, invertibility, strict positivity, nonempty
blocks or vanishing cross-block entries. Prove the dependent-Sigma version
and reindex by sigmaFiberEquiv. Empty and singular matrices are included.
2. For every finite complex P and ordinary derivative depth J, prove the
full equal-angular-weight cross identity for arbitrary r,s,t,u with
r+u=t+s (not just adjacent rows):
 traceGramEntry P J r s t u =
 2 sum_(j<J) if j<=r and j<=t then
   (r.descFactorial j)*(t.descFactorial j)*normMoment P (r+u-j) else 0.
This includes origins, negative integer weights, zero/extra derivative
columns, arbitrary nonsymmetric P, and the existing factor two.
3. Define the rectangular row weight as INTEGER r-s. Group ALL actual rows
by those weights, not truncated Nat subtraction or overlapping pairs.
Prove every actual principal block equals its ordinary-jet moment matrix,
and det(rectangularTraceGram P J R S) <= product of those moment determinants.
4. For original G=integerRectangularTraceGram Q D J R S, compose its real
cast and existing positive-definiteness / odd-prime nonsquare valuation:
 0<G.det and (p:Int)^(2*valuationWeight R S p) divides G.det, and
 (p:Real)^(2*valuationWeight R S p) <= (G.det:Real)
   <= product of actual radial moment block determinants.
Only guards: D>0, prime p!=2, nonsquare -D mod p, R>=1,S>=1,J>=S,
2*(R-1)+(S-1)<Q.card. No supplied compatibility, rank, independence,
divisibility, determinant inequality, class number, cutoff or classification.

Auxiliary blockwise REAL orthogonal changes of basis preserve det A and
PSD; they need NOT preserve the integer lattice. Arithmetic stays on G.
No Hermitian replacement, angular averaging, rotational symmetry, new
valuation exponent or claim that this alone lowers a cutoff.

## Fixed controls and dependency gates

Lean controls in the SAME source/invocation: zero-dimensional determinant1;
singular all-one2x2 block inequality (det0 versus singleton product1);
nonzero cross-weight entry at P={1},J=1 between (0,0),(1,0) (value2);
negative-weight nonadjacent pair (0,2),(2,4) at P={1},J=3 (cross2,
second diagonal14), distinguishing lost extra jets; origin cross for
(0,0),(2,2),J=3 equals0 but first diagonal2; existing real/Hermitian
control (real determinant4, Hermitian determinant0).
Freeze all public theorem TYPES, definition BODIES and control data at
first invocation. Max two proof-only repairs; private lemmas may be added.
No partial-success substitution if the full bridge fails.
Print all public theorem types and namespace axiom audit. Fresh final
bridge closure must reject the same70 forbidden roots in Phase110 source,
and permit only propext, Classical.choice, Quot.sound, with no unresolved
or unsafe logical inputs. Imported old cutoff declarations may exist in
the environment, but must not occur in fresh proof dependency closures.

## Budget, isolation and evidence

At most THREE full standalone Lean invocations, max600s and8192MB per
owned process,1200s cumulative; stop permanently on any outer or internal
resource limit, including default heartbeat/recursion limits. No probes,
raised limits, hidden checks or repaired/replayed earlier phases.
Use pinned Lean4.19.0 and PRIMARY lean cache in ../tenth-discriminant/lean;
source remains in this separate worktree, explicit relative path recorded.
Freeze primary checkout and every preexisting tracked file except current
reader documentation and task-local .agent state. No production source,
root import, tools, pins, workflows, earlier evidence/protocols changed.
Preserve each source/stdout/stderr/result and exact command/cwd/hash before
repairs. Keep fixed-type/definition snapshots and verify final source
against them; preserve failed sources even if later attempts pass.
After terminal outcome: raw archive, saved evidence verifier, short human
proof guide, and current README/STATUS/FORMALIZATION/objective ledger/reply
updates. Keep README and current ledger61lines. No new cutoff claim.
No full root build, integration, CI, reviewer, publication, merge or Tao
posting in this cycle: successful source still requires separate integration.
