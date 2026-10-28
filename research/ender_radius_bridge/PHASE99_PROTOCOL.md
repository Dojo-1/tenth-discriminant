# Phase99: actual even prime-count to original-Gram weighted budget

Base a5cd1e3281c778ede1595c5065e29d0ca10834ef. Register before source/run.
Standalone full target: for positive squarefree d=1 or 2 modulo 4 with
actual class number h(EvenQuadraticField d)<=2, every finite set P of odd
primes <=L, L>=3, positive R,S and the EXISTING Ender radius guard (d<=d2),
prove on the SAME original rectangularTraceGram(ellipsePoints d rho):
 mass(P,R,S) <= log(product of original diagonal entries)
   + lossScale(R,S)*kernelCost(L,primeKernel,evenCountBound d)
   + R*S*(S-1)*log(d).
One new definition countBound: (2*pi*n/sqrt(4*d)
 +4*sqrt(actualM(EvenQuadraticField d)*n/(4*d))+1)/2.
Two main public theorems: remainder_prefix_bound and actual_gram_budget.
Use already generic SplitPrimeBudget.goodPrimes/splitRemainder/
mem_remainder_iff; do NOT duplicate that partition or use its odd-field
countBound/remainder_prefix_bound/actual_gram_budget. Derive remainder
prefix count from actual EvenClassAggregation.uniform_two_class_bound.
Compose generic PrimeDivisorLoss.excluded_budget_without_divisors.
No caller prefix bound/family/count/divisibility premise. Retain actual
field discriminant4*d versus original-Gram radicand d; no field switch.
Five controls: empty partition, Gaussian d1/p5 square remainder, d5/p5
parameter divisor excluded from remainder, p2 square root rejected by
Admissible, one-column valuation zero. Print all seven public statements,
countBound, both main axiom sets; namespace audit and fresh full budget
closure. Exclude all49Phase98inputs plus the three odd SplitPrimeBudget
countBound/remainder_prefix_bound/actual_gram_budget roots (52total).
Only propext, Classical.choice, Quot.sound. No actualM scalar candidate
or normalization, improved cutoff, classification or optimality claim.

At most3 full standalone Lean invocations,600seconds/8192MB per owned
process each,1200seconds cumulative; max2 statement/definition-type/
control-preserving proof repairs. Stop any internal/outer resource limit;
no weaker target, probes, heartbeat/recursion/limit increase or replay.
Freeze all seven public theorem types, one definition type/body and five
controls at first invocation. Full source/stdout/stderr/result each run;
archive failures and record exact repair. Production/root/tools/pins/CI/
certificates/prior protocols/raw/verifiers/reviews/ledgers frozen. No
production integration/root rebuild/audit/campaign/CI/reviewer/merge/
publication in this attempt. Saved verifier preserves prior files and
checks caps, hashes, unchanged types/definition/controls, exact52exclusions.
Update current README61/STATUS/FORMALIZATION/objective/reply and human
guide only after result is known; preserve negative results if rejected.
Argon pending until review arrives and version is identified.
