# Phase73: actual principal-class basis calibration and prime-axis removal

Register before source/execution. Basee77a446aaed709c04afe38b1dc846e4a8f6386cc. PR35 CI40426517803/job121933520286 is live; separate local branch, no push over/cancel/restart/status transfer. Preserve all earlier sources/raw, especially stopped69 (no rerun/repair/limit increase). No merge/reviewer.

## Fixed actual target

In the actual squarefree odd maximal-order chart D mod4=3, for EVERY nonzero integral ideal J whose actual ClassGroup.mk0 J=1, construct one actual integral basis e with
 IdealCoordinates.FormData D J e 1 1 ((D+1)/4).
This means the ACTUAL normalized algebraic norm is x^2+xy+((D+1)/4)y^2, not merely an arbitrary positive coefficient. Use a generator of this ideal and Mathlib Ideal.basisSpanSingleton, transport to J, norm multiplicativity and the actual positive norm=ideal norm identity. Do not assume the field class number is one or give a PID instance for its entire ring. The class-identity hypothesis concerns only J.

On the SAME constructed e, prove every actual element z:J with norm magnitude=p*N(J) for prime natural p has nonzero second coordinate. Then derive the actual full finite prime-norm point count for any U:J and natural t with those prime-norm properties and norm magnitude<=N(J)*t:
 card(U)<=2*pi*t/sqrtD+4*sqrt(t/D).
The caller supplies no off-axis guard, supplied basis/form or zero-axis count. Derive exclusion by exact coordinate reconstruction, positive ideal-norm cancellation and prime not-square arithmetic. Basis choice precedes all primes/U/t.

Fixed controls: actual unit ideal in D=7 admits the calibrated a=1 form; actual proper principal ideal(2) has norm4 and admits that same calibrated normalized form; zero element cannot satisfy prime-normalized norm; the uncalibrated integer form a=3,b=1,c=1001 has prime zero-row value3 at x=+-1, demonstrating why a=1 matters. Print the complete principal-class root and FormData/axiom list, with full namespace audit allowing only standard3 axioms.

## Bounded execution/preservation

Standalone research file imports unchanged production root plus pinned Ideal.Basis if required. At most3 full invocations,600seconds/8192MB each,1200seconds cumulative; at most2 repairs preserving target/control statements and guards. Stop after any resource stop including deterministic Lean heartbeat exhaustion. Default limits unchanged; no separate probe, easier abstract-form fallback, global class-number-one shortcut or hidden rerun. Snapshot exact source/stdout/stderr/result each attempt. After acceptance inspect printed type/axioms/audit from that invocation, then saved-evidence integrity only. No old campaign replay or production/root/tool/pin/certificate/gate changes in this cycle.

## Meaning/limits

This closes the principal-class coordinate calibration and actual prime-axis exclusion. It does not give a quantitative leading bound for other classes, a primitive/short-vector basis, even chart, class-wide usable B, field/ramification transport or new cutoff. No classification/novelty/human-review/upstream claim. Explain multiplication by a generator and cancellation of its norm as the operative symmetry. Publish only after exact PR35 CI is terminal and recorded, preferably combined with a coherent follow-up; no automatic merge/reviewer. Broader goal remains open.
