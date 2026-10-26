# Phase69: actual ideal coordinates, integral norm form and exact discriminant

Register before new source/execution. Base34f277531d8c160b05a14fac7a9482b8fbd6e141. Phase68 all3target invocations consumed: do not rerun it. PR33 CI40419910108/job121911466303 is live; work locally with no push over/cancellation/restart/status transfer. No merge/reviewer.

## Complete fixed target

For squarefree natural D congruent to3 mod4 and actual K=QuadraticField((D+1)/4), construct an actual integral basis of O_K by transporting the existing halfOrderBasis through halfOrderEquivRingOfIntegers. For EVERY nonzero integral ideal J of O_K, construct a Basis(Fin2,Int,J), not a supplied basis/norm-form premise. Prove there exist integer a,b,c with a>0 and4ac-b^2=D, such that for ALL integer x,y:
 Norm_Int(x*basis0+y*basis1)=N(J)*(a*x^2+b*x*y+c*y^2).
Prove actual integer norm nonnegativity and positivity for nonzero elements, preserving the actual norm rather than defining a replacement. Use actual ideal-norm divisibility for coefficient integrality, and Ideal.natAbs_det_basis_change for the exact discriminant, not a supplied determinant identity. The actual basis supplies injective integer-pair coordinates and reconstructs every element.

Compose with the unchanged production QuadraticRows.off_axis_area_bound to bound any finite set U of elements of J with norm magnitude<=N(J)*t (natural t) and nonzero second basis coordinate:
 cardU <=2*pi*t/sqrtD+4*sqrt(a*t/D).
The basis/form are chosen before U and t. No supplied coordinate-count/area/discriminant hypothesis, arbitrary replacement matrix or non-prime-point fallback. The constant a is the proved positive integral leading coefficient of this actual normalized norm form, not yet bounded above uniformly in D.

Fixed controls: D=7 ambient order has actual norm x^2+xy+2y^2; shearing its second basis vector by the first gives x^2+3xy+4y^2 with discriminant7; actual principal ideal(2) has ideal norm4 and scalar-coordinate norm4*(x^2+xy+2y^2); origin singleton at t=0 falsifies dropping the off-axis guard. Print full actual ideal-form and actual off-axis-count target types/axioms and audit the whole new namespace with standard3 axioms only.

## Budget and preservation

Standalone source imports unchanged production root. At most3 complete Lean invocations,600seconds/8192MB each,1200seconds cumulative; at most2 repairs preserving public target types/guards/controls and quantifier order. Stop after any target resource stop. No separate Lean probe, weakened supplied-basis/discriminant endpoint or hidden rerun. Snapshot source/stdout/stderr/result every attempt; preserve failures/incomplete outcomes. API/source inspection allowed. After acceptance inspect printed types/axioms/audit from that invocation, then saved-evidence integrity only. No prior campaign rerun or production/root/tool/pin/certificate/gate changes. No scope expansion to a quantitative leading-coefficient theorem in this cycle.

## Interpretation

This attempts to close the actual ideal-to-normalized-binary-form and per-ideal geometric count bridge in the odd chart. A uniformly controlled leading coefficient, class-wide analytic B, even chart and arbitrary-field-discriminant/ramification transport remain separate. Do not infer a new cutoff, classification, novelty, independent review or Mathlib acceptance. Explain coefficient divisibility and determinant/index cancellation in a short human proof. Publish only after live PR33 exact CI is terminal and recorded, combining dependent research into a coherent follow-up; no automatic merge. Broader goal remains open.
