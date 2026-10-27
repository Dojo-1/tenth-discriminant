# Phase66: a fixed norm lattice for each actual ideal class

Registered before new source/execution. Base2dd80eb233833e33f01fb87dca2e10fc06ca77d0; preserve Phase65 source/raw/results. Local branchcodex/prime-divisor-loss while PR32 CI40416976865/job121901646441 runs. No push over live CI, restart, merge or reviewer.

## Fixed actual arithmetic target

For any actual number field K and any C:ClassGroup(O_K), choose ONE nonzero integral ideal J, with mk0(J)=C^-1 and the existing Mathlib Minkowski bound on its absolute norm:
 (4/pi)^(nrComplexPlaces K) * (degree! / degree^degree * sqrt(abs(discr K))).
For EVERY nonzero integral ideal I in class C, prove existence of z:O_K such that:
 z!=0; z belongs to J; span{z}=I*J;
 abs(field norm z)=absNorm(I)*absNorm(J);
 for every integral ideal I', I'*J=span{z} implies I'=I.
No supplied principal-ideal-ring, class-number-one, small-ideal existence or norm representation assumption. Use the pinned library's exists_ideal_in_class_of_norm_le, inverse-class principalization and nonzero-ideal cancellation.

Then define the actual nonzero residue ideal from any ring map f:O_K->ZMod p with p>0, using the existing proved residueKernel_absNorm, not an assumed kernel norm. For a FIXED class C, the same chosen J must serve EVERY such p,f whose residue ideal has class C. Prove z in J, nonzero, span{z}=ker(f)*J, abs(norm z)=p*absNorm(J), with exact ideal recovery. The choice of J must precede p/f; no per-prime replacement lattice.

Fixed controls: (i) actual rational ring-of-integers quotient to ZMod3 instantiates the full residue theorem with no class-number hypothesis; (ii) negation preserves membership, nonzero status, principal ideal and norm magnitude; (iii) nonzero J is necessary for recovery, since multiplication by zero ideal is not injective (over O_Q); (iv) zero modulus has zero kernel norm, so the positive-modulus guard cannot be silently dropped from the nonzero-residue-ideal construction. Check/print both full target types/axioms and audit the new namespace in the accepted invocation.

## Bound and preservation

At most3 full standalone invocations,600seconds/8192MB each,1200seconds cumulative; at most2 proof repairs preserving target types/guards/controls and the fixed-class quantifier order. Stop after any target resource stop. No separate Lean probe, easier specialization or hidden rerun. Snapshot exact source/stdout/stderr/result each time; preserve failure/incomplete evidence. Source/API inspection is permitted. After acceptance inspect the printed public types and standard-three-axiom namespace audit from that invocation, and run saved-evidence integrity checks only. No prior campaign rerun or production/root/tool/pin/certificate/gate changes.

## Interpretation

This is an actual ideal-class-to-element norm bridge with a fixed lattice and a recovery operator. It does not yet choose a Z-basis, derive binary-form coefficients/discriminant/leading-coefficient bound, prove two distinct unramified prime ideals or four-representation multiplicity, identify ramification, supply arithmetic B or improve a cutoff. In arbitrary number fields norm magnitude is essential; do not silently replace it by a positive norm. No classification/novelty/human-review/upstream claim. Explain the inverse-class, norm multiplication and cancellation argument to humans. Publish only after the live PR32 run is terminal and recorded; broader goal remains open.
