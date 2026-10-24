# Phase 32: actual field discriminant and a first positive class-number bridge

Base 6a16da7a14670da793103cf908847d6e2109845d. Previous goal turn made
verified progress: universal wheel coverage and necessary candidate list
below one million passed full pinned CI 40130787539/security 40130786275;
merge/head/local trees matched a5fd0ef8d66ddb2214acf700a3626ea861681f51.
Live refresh confirms zero divergence, PR28 OPEN/DRAFT/UNMERGED and only
the inherited untracked lake manifest. No subagents. Global goal remains active.

## Choice of next bridge

Full classification needs both complete upper-middle exclusion and positive
class-number equalities for the nine fields. Scaling the current direct
kernel sieve is a separate computational bottleneck; it is not solved here.
The pinned library already supplies Minkowski's small ideal representative
and a PID criterion for small field discriminant. Applying them requires the
actual NumberField.discr, not a conventional parameter named as if proved.

Prove the missing identity for every positive squarefree radicand d:

    NumberField.discr (ImaginaryQuadraticField d)
      = if (d:Int)%4=3 then -(d:Int) else -4*(d:Int).

Use the already proved maximal-order ring equivalences and their integral
bases. A reusable two-dimensional trace-pairing lemma should compute the
discriminant s^2-4*t in basis (1,u) with u^2=s*u-t. Transport actual integral
bases, not arbitrary rational bases. The odd chart uses s=1,t=(d+1)/4;
the even chart s=0,t=d. The checked field equivalence joins them.

Then prove the actual absolute field discriminant equals
absoluteDiscriminantParameter d, and obtain its existing 700000000000 bound
under actual class number one. This is not a numerical improvement.

As the fixed positive-class-number attempt, use the pinned small-discriminant
PID/Minkowski criterion to prove actual class number one for d=1,2,3,7.
The degree-two signature identity bounds the complex-place count by one;
the existing pi>3 bound should make absolute discriminant <=8 sufficient.
Do not claim the other five positive cases, upper-middle exclusion or full
classification. If the bridge cannot close, preserve the exact failure and
state the missing premise rather than presenting it as supplied.

## Controls and scope

Keep positivity, squarefreeness and all chart guards explicit. Check the
trace-zero order at d=3 has basis discriminant -12 whereas the actual field
has discriminant -3: an arbitrary order basis is not a maximal integral basis.
Check actual absolute discriminants 4,8,3,7 for the four positive targets.
Check d=11 is outside this <=8 criterion, not thereby a negative class-number
claim. Retain all previous necessary-list and endpoint controls.

Use kernel-checked proofs; no native_decide, new axioms, inherited
classification theorem or Heegner-method input. Default proof budgets and
existing 8192 MB owned-process monitor apply. Preserve every terminal failed
build/resource stop; any bounded elaboration repair must be recorded without
weakening the mathematical target. Do not run or modify the frozen full
campaign, production tools, old ledgers, cutoff, dependency pins or gates.

## Delivery

Commit this protocol before proof edits. Keep the trace-pairing calculation
and actual-field transport human readable. Update current README/STATUS/
FORMALIZATION and objective accounting with proved versus open items separate.
Run full root build, source correspondence, compiled axiom audit, signature
checks and inherited adversarial controls; require complete unchanged pinned
Linux CI on the published exact tree. Report decomposed local checks as such.
Update only draft PR28, with no merge or Tao post. Independent human review,
optimization, full finite classification and other open objectives stay open.
