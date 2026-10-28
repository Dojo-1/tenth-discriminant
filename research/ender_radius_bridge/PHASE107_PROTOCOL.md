# Phase107: actual even-field transport and all-parity h<=2 bound

Base38d799e38145d6676f89d8aaa638bd8ae94c1ffc; separate branch
codex/even-field-transport. Register before new source/Lean invocation.
Phase106 local integration passed; its own CI40707296487 is CANCELLED
at25m (all controls finalPASS printed, no successful job completion).
PR37 remains draft/unmerged. Do not rerun that CI or standalone105,
change workflow/limits, or transfer past checks to this new proof.

Five public main statements, zero definitions:
even_chart_of_even_parameter: squarefree d with Even(absoluteDiscriminantParameter d)
forces dInt%4=1or2; no actual field premise needed.
arbitrary_even_discriminant_bound: any actual number field K, degreeRat2,
IsTotallyComplex, actual classNumber<=2 and Even(actual absdiscr) implies
actual absdiscr<2^52; no caller generator, chosen chart, isomorphism,
maximal-order identification, norm budget or canonical class-number premise.
arbitrary_discriminant_bound: same actual field hypotheses, no parity
hypothesis, implies actual absdiscr<2^52.
parity_refined_discriminant_bound: same hypotheses give the odd implication
absdiscr<2^50 AND the even implication absdiscr<2^52.
classNumber_gt_two_of_large_discriminant: same actual field/degree,
actual absdiscr>=2^52 implies actual classNumber>2.

Four fixed controls: absoluteDiscriminantParameter2=8; parameter3=3;
4*2^50=2^52 and unequal2^50;3mod4 excluded from even chart. No finite
class-number classification, improved h1 cutoff or novelty assertion.
All nine complete mathematical types/control data frozen at first run.
At most2 proof-only repairs, no definitions or weakened hypotheses/types.

Allowed existing proof components: internally construct squarefree root
and actual field equivalence; generic field_classNumber_eq without PID;
actual field discriminant formula; EvenTwoClass.even_discriminant_bound.
For the all-parity/refined/large-discriminant statements, explicitly reuse
OddFieldTwoClass.arbitrary_odd_discriminant_bound in the odd branch.
Do not falsely advertise this final composition as independent of the
already-proved odd h<=2 bound. No external method/code imported.

Fresh transitive checks: even bound uses exactly58 exclusions from104
plus CoordinateTranslation.coordinate_translation_bridge and
CoordinateTranslation.shifted_gram_counterexample (60total). All-parity
bound and large-discriminant contrapositive use exactly35 h1/classification/
finite-answer exclusions from88 plus those same2 coordinate roots (37total).
Namespace audit; all9types and axioms for3fresh roots; standard propext,
Classical.choice,Quot.sound only; unresolved/unsafe/forbidden rejected.

Max3full standalone invocations600s/8192MB perownedprocess,
1200s cumulative. Stop internal/outer resource stop, no probes/replay,
weaker target or raised heartbeat/recursion/resource limits. Preserve
full source/stdout/stderr/result perrun and all failures/repairs.
Freeze production/root, tools,pins,CI,earlier protocols/raw/verifiers,
reviews,ledgers,numerical certificates and historical failures. No root
build/whole-library audit/integration/publication/CI/reviewer/Tao post here.
Update current readerdocs/README61/STATUS/FORMALIZATION/objective/reply,
new short human guide and saved evidence verifier after result known.
