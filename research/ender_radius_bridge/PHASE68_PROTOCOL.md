# Phase68: actual residue ideals and finite four-representation multiplicity

Register before new proof source/execution. Base564321005e8c9a34e5541dce8205e0e29b21caf7. PR33 CI40419910108/job121911466303 is live; work on separate local branch without pushing over, cancelling, restarting or transferring its status. No merge or reviewer.

## Fixed complete target

Standalone research source imports the unchanged production root. For an actual number field K, choose a family J_C of nonzero integral ideals, mk(J_C)=C^-1 and the existing checked normBound K, BEFORE primes/residue maps. Two distinct residue kernels of maps O_K->ZMod p (p>0) must yield a finite set of exactly4 distinct labelled elements (C,z), with z!=0,z in J_C and abs(norm z)=p*Norm(J_C). Use actual ClassFiber recovery and sign symmetry, not a supplied count/multiplicity premise. Membership in a class must not be erased when counting. The family must be shared across all primes.

For the actual odd maximal-order chart K=QuadraticField((D+1)/4), with squarefree natural D and D mod4=3, construct the TWO residue maps from roots z and -z of z^2=-D. Prove their kernels differ under odd-prime p and p not dividing D, rather than assuming that pair. Use the existing halfOrderEquivRingOfIntegers and halfOrderResidueMap; do not replace the order or assume it maximal/principal. Show value separation implies kernel separation using integer residue scalars.

For EVERY finite natural prime set P with all p odd, p not dividing D and IsSquare(-D:ZMod p), construct one such family J_C and a finite labelled-element set U with
 card(U)=4*card(P),
 and every (C,z) in U has z!=0,z in J_C, and actual norm magnitude p*Norm(J_C) for some p in P. Different primes' sets must be proved disjoint by cancelling the positive ideal norm. No class-number-one/two, supplied ideal-pair, aggregate count or norm-form-coordinate premise. Generic family choice precedes all residue maps/primes; the finite theorem composes that family, not per-prime replacement lattices.

Fixed compiled controls: actual D=7,P={11} (root2) gives4 labelled elements; empty prime set gives0; ramified D=15,p=3 root0 coincides with its negative and gives identical actual residue maps; characteristic2 root1 equals its negative, so the odd-prime guard is necessary for this construction. Print the generic family and complete finite target types/axioms and audit the full new namespace with only standard3 axioms.

## Bounded execution and preservation

At most3 complete standalone Lean invocations,600seconds/8192MB each,1200seconds cumulative; at most2 proof repairs preserving all public target statements/guards/controls and family quantifier order. Stop after any target resource stop. No separate Lean probe, easier per-prime fallback, weakening to supplied-pair/abstract-count assumptions or hidden rerun. Snapshot exact source/stdout/stderr/result each time. Preserve every failure/incomplete record. Source/API inspection permitted. After acceptance inspect printed full types and audit from that invocation; saved-evidence integrity checks do not rerun Lean. No prior campaign rerun or production/root/pin/tool/certificate/gate changes this cycle.

## Scope

This is a finite actual arithmetic multiplicity theorem for the odd maximal-order chart. Its elements are labelled by ideal class; do not describe them as four points in one common lattice. It does not choose an integral basis, prove normalized norm-form coefficients/discriminant/leading-coefficient bound, identify the parameter with arbitrary field discriminants, give the even chart, supply usable arithmetic B or improve any cutoff. Keep norm magnitude for the generic field. No classification/novelty/human-review/upstream claim. Explain why labels, recovery, signs and prime separation give the count. Publish only after the live exact PR33 CI is terminal and recorded; broader goal remains open.
