# Phase63: actual off-axis quadratic points bounded by row-width integral

Registered before proof source/execution. Base74d02d305cabc4bde1a46ed066bff3ad12f3e9da. Separate local branch/cycle. PR31 CI40407136985/job121867685012 is live; no cancel/restart/replacement push or status transfer. PR30 exact b4 full Linux CI/security success remains recorded, local Windows timeout preserved; merge approval pending, no merge authorized. No reviewer authorized.

## Fixed target

Let a,b,c,t be real, a>0, D=4ac-b^2>0, t>=0. For any finite U of integer pairs, assume every point satisfies Q(x,y)=a*x^2+b*x*y+c*y^2<=t and y!=0. Put Y=sqrt(4at/D), w(s)=sqrt(4at-D*s^2)/a. Prove

    (U.card:Real) <= 2*integral(s=0..Y,w(s)) + 2*Y.

This is the actual finite off-axis point count, not a supplied count bound or a change of Gram matrix. The integral is deliberately unevaluated: no pi coefficient is claimed Lean-checked in this cycle. The later area evaluation, prime multiplicity, class dictionary, ramified budget, arithmetic B and any h<=2 cutoff remain obligations.

Required internal steps: integer interval card<=length+1, completion of square and exact row intervals, height bound from Q<=t, finite positive-row fiber count, decreasing-width sum<=integral using existing Mathlib AntitoneOn.sum_le_integral, extension to real height, and reflection(x,y)->(-x,-y) to combine both halves. All definitions, actual full count and controls must compile together for acceptance; a positive-row-only or abstract-supplied-count fallback is not success.

Fixed controls: unit-circle a=c=t=1,b=0 has the two off-axis points(0,+-1) satisfying the theorem; empty input; at t=0 the origin is a counterexample if the y!=0 guard is dropped. No numerical parameter search/campaign. The source remains research-only Phase63NonzeroRows.lean, outside production/root/CI; pins/tools/old proofs/README unchanged.

## Limits

At most3 complete Lean builds,600seconds/8192MB each,1200seconds cumulative; at most2 proof repairs with fixed statements/guards. Stop after any target resource stop. Snapshot every source/raw stdout/stderr/result before repair. Standard-three-axiom namespace gate, no sorry/native_decide/custom-axiom escape. No rerun of the exhausted Phase61 build/control campaign or accepted Phase62 target. The paper derivation and Mathlib APIs were inspected before registration; not a blinded experiment. Preserve an incomplete full target if it fails, with precise missing arrows. Publish only after recording PR31's terminal exact-head CI result; no automatic merge.
