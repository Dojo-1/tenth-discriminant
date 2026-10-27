# Phase65: separate prime-divisor loss on the original determinant

Registered before new proof source or execution. Base9705cac06cab2a6a14f78795fd4778b2b5b9ce01. PR32 CI40416976865/job121901646441 is live; work locally on a separate branch, with no cancellation, restart, replacement push or transfer of success. Prior mathematical head70f9217 has terminal success recorded. No reviewer or merge authorization is inferred.

## Fixed target

Standalone research file Phase65PrimeDivisorLoss.lean imports the unchanged production root. Use the actual valuationWeight, ExcludedPrime.weight/mass, primeKernel, lossScale and kernelCost. No proxy matrix or weight.

1. For all natural R,S,p: 2*valuationWeight R S p <= R*S*(S-1).
2. For D>0 and any finite natural prime set T with every p dividing D: sum_T log(p) <= log(D), and
   mass T R S <= ((R*S*(S-1):Nat):Real)*log(D).
3. Set E=P\G, T=E.filter(p divides D), U=E\T. Under exactly the existing excluded_prime_budget_log_div guards (D>0,D<=D2,R>=1,S>=1,L>=3,G subset P,P prime and odd,P<=L,G nonsquare and the same Ender radius), require prefixCount U n<=B n only for3<=n<=L. Prove on the actual original ellipse Gram:
   mass P R S <= log(product diagonal actualGram)
                  +lossScale R S*kernelCost L primeKernel B
                  +((R*S*(S-1):Nat):Real)*log(D).
No supplied bound on T, aggregate excluded mass or determinant premise. Arbitrary G means U consists of non-divisor excluded primes; do not call U all split primes without an additional coverage theorem.

Fixed compiled controls: S=1 has zero valuation weight; T={3,5},D=15 has product15 and the actual mass bound; empty T has zero mass; D=1 permits no prime divisors; dropping divisibility fails for D=1,T={3},R=4,S=2 because mass>0 while the proposed right side is zero. Include #check/#print axioms of the full target and compiled namespace audit. Standard three axioms only; no sorry, new axioms, answer-list or class-number assumption.

## Budget and preservation

At most3 full standalone Lean invocations,600seconds/8192MB each,1200seconds cumulative; at most2 repairs with unchanged public target statements, guards and controls. Stop after any target resource stop. Snapshot source/stdout/stderr/result for every attempt. No target weakening or hidden rerun. Import/API source inspection is allowed; no separate Lean probe that evades the budget. After acceptance, inspect public types and audit from the same invocation; saved-evidence integrity checks are not proof reruns. Do not rerun prior campaigns. No production root/source/pin/tool/certificate/gate change in this cycle; integration would require a separate registration.

## Meaning and limits

The new result removes parameter-prime-divisor contributions from the open count. It does not identify parameter divisors with ramified field primes, supply the ideal-class/form dictionary or four-representation multiplicity, supply arithmetic B, improve a numerical cutoff or prove classification/novelty/independent review. Preserve any failed/incomplete attempt. Explain the product/log bound and exact partition in a short human guide. Publish only after the live PR32 run is terminal and its exact-head result is recorded; do not interrupt it. The full goal remains open.
