# Phase47: normalized generators for abstract imaginary quadratic fields

Baseline2def0702450e9b3fd526a85a70a11439653fcd97. Previous goal turn made
progress: the explicit-root/degree-two constructor, transported actual bounds
and fixed squarefree-guard control were published with local checks. Exact
baseline CI40203394568 remains live; security40203392082 passed. Finish
and record the same CI run before any newer push, with no restart/cancellation.

## Full fixed target, not a replacement by a conditional wrapper

For an arbitrary actual number field K, with rational degree two and the
pinned Mathlib NumberField.IsTotallyComplex property, prove that some
positive squarefree natural d and a in K satisfy a^2+d=0. Neither a
generator, isomorphism, cutoff nor class-number premise is supplied.

Use a primitive rational power basis, expand its monic quadratic minimal
polynomial, complete the square, and show its discriminant is negative:
a nonnegative discriminant would give a real root and a real embedding of
the entire field, contradicting total complexity. Clear the positive
rational denominator, extract the square factor using the pinned natural
squarefree decomposition, and divide the generator by that factor.

Compose this result with Phase46 to prove the actual absolute field
discriminant below100000000000 from degree two, total complexity and actual
class number one only. No new constant, old cutoff, finite classification,
known Heegner list or numerical premise. Do not assert full classification.

## Fixed budget and acceptance

One module target,600s/8192MB per owned process,1200s cumulative, at most
three generic elaboration repairs after the first attempt. No retry after
a resource stop or increased cap. Preserve every failure and failed source
snapshot. A mathematical failure stays a gap; do not weaken the universal
target to a provided-root/isomorphism hypothesis to obtain PASS. No sorry,
extra axiom, native_decide, unsafe shortcut, changed pin or audit gate.
No new numerical pilot, parameter search or extra reviewer agent.

After acceptance, root build/import coverage/escapes, source correspondence,
fresh public signatures, compiled input checks and full namespace audit.
The normalization theorem must exclude NumberField.classNumber, all old
classification/certificate/cutoff inputs and the newer100b bound wrappers.
The resulting actual-field cutoff may deliberately use the accepted100b
core and Phase46 transport, but must exclude the16 old Phase43 inputs.

Prove total complexity for the canonical positive-d family without class
number input, then instantiate the abstract field cutoff at d=1,2,19 using
the already checked positive class-number cases as controls only. Preserve
root/cutoff proof-input separation. Print the standard field hypotheses;
no representation premise should remain on the new actual-field bound.

The prior AI review predates this new normalization proof and is not
transferred to it. Update the current human guide/README/STATUS/FORMALIZATION
and objective ledger with the actual accepted scope or exact surviving gap.
Keep all prior campaigns, proofs, certificates, pins and CI gates unchanged.
New publication-head pinned CI remains a separate required record. No merge
or Tao post; no novelty, optimality, human-review or broad-goal-completion claim.
