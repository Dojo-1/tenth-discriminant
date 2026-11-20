% Phase373 — clock-authority square, GNU Prolog finite adversarial model.
% The policy uses Phase368's *nested* scheduling phases, not 1 clock == 1 phase.
% This is a finite policy projection, not an authenticated Github reader.

source(original, original_integer_pair_gram).
source(contrast_d203, maximal_order_d203).

arm(source_anchor, source_world, original, local).
arm(prolog_counterworld, logic_world, original, local).
arm(lean_formalization, lean_world, original, local).
arm(external_field_review, reviewer_world, original, human).
arm(d203_contrast, phase306_world, contrast_d203, local).

native_clock(source_world, meso).
native_clock(logic_world, fast).
native_clock(lean_world, meso).
native_clock(reviewer_world, review).
native_clock(phase306_world, fast).

% Scheduling tiers expose increasing collections of native clocks.
capability(fast,fast).
capability(meso,fast).
capability(meso,meso).
capability(review,fast).
capability(review,meso).
capability(review,review).

plane_ok(local, github_ci).
plane_ok(human, independent_review).

% Human review cannot be transformed into a GitHub-CI source guard.
eligible(A,Phase,Plane) :-
    arm(A,W,original,Exec),
    native_clock(W,Native),
    capability(Phase,Native),
    plane_ok(Exec,Plane),
    (Exec \= human ; Phase = review).

% An issue is allowed only on its ORIGINAL policy snapshot.
manifest(v368_original,sha_v368).
issue(history371,source_anchor,fast,v368_original,20261120201440).
issue(new373,source_anchor,meso,v368_original,20261120201440).
issue(prolog_meso,prolog_counterworld,meso,v368_original,20261120201440).
issue(review_task,external_field_review,review,v368_original,20261120201440).
issue(wrong_version,source_anchor,meso,nonexistent,20261120201440).
issue(preissued,source_anchor,meso,v368_original,20261120201450).

execution(history371,github_ci,20261120201448,original).
execution(new373,github_ci,20261120201448,original).
execution(prolog_meso,github_ci,20261120201448,original).
execution(review_task,independent_review,20261120201500,original).
execution(wrong_version,github_ci,20261120201448,original).
execution(preissued,github_ci,20261120201448,original).

authorizable_task(Task) :-
    issue(Task,A,Phase,Version,_),
    manifest(Version,_),
    execution(Task,Plane,_,S),
    arm(A,_,S,_),
    eligible(A,Phase,Plane).

causally_creditable(Task) :-
    authorizable_task(Task),
    issue(Task,_,_,_,Issued),
    execution(Task,_,Started,_),
    Issued < Started.

% Exact positive affine clock change preserves + reflects strict order.
affine_t(Scale,Offset,T,V) :-
    integer(Scale),Scale>0,integer(Offset),
    V is Scale*T+Offset.

strict_clock_transport(Scale,Offset,A,B) :-
    A < B,
    affine_t(Scale,Offset,A,FA),
    affine_t(Scale,Offset,B,FB),
    FA < FB.

% A monotone but constant transport is NOT strict and cannot carry causality.
flat_map(0,_Clock,0).
constant_clock_collapses :-
    0 < 1,
    flat_map(0,0,X),
    flat_map(0,1,Y),
    X=:=Y.

% The same signer may state execution facts, but cannot self-grant a policy.
policy_issued_by(scheduler).
execution_verified_by(gh_readonly_auditor).
field_authorized_by(independent_human).
not_self_promoted :-
    policy_issued_by(A),execution_verified_by(B),
    A \= B,
    \+ field_authorized_by(B).

test(Name,Goal) :-
    (call(Goal)->write('PASS '),write(Name),nl
    ;write('FAIL '),write(Name),nl,fail).

phase373_main :-
    test(source_native_meso,native_clock(source_world,meso)),
    test(fast_source_rejected,\+ eligible(source_anchor,fast,github_ci)),
    test(meso_source_eligible,eligible(source_anchor,meso,github_ci)),
    test(review_tier_source_eligible,eligible(source_anchor,review,github_ci)),
    test(meso_includes_fast_prolog,eligible(prolog_counterworld,meso,github_ci)),
    test(fast_prolog_eligible,eligible(prolog_counterworld,fast,github_ci)),
    test(proof_fast_rejected,\+ eligible(lean_formalization,fast,github_ci)),
    test(proof_meso_eligible,eligible(lean_formalization,meso,github_ci)),
    test(human_review_only,eligible(external_field_review,review,independent_review)),
    test(human_review_not_ci,\+ eligible(external_field_review,review,github_ci)),
    test(d203_source_not_same,\+ eligible(d203_contrast,fast,github_ci)),
    test(historical_real_execution_not_eligible,\+ authorizable_task(history371)),
    test(new_source_authorized,authorizable_task(new373)),
    test(new_source_causally_creditable,causally_creditable(new373)),
    test(prolog_meso_authorized,causally_creditable(prolog_meso)),
    test(review_human_authorized,causally_creditable(review_task)),
    test(wrong_manifest_rejected,\+ authorizable_task(wrong_version)),
    test(preissue_execution_rejected,\+ causally_creditable(preissued)),
    test(strict_affine_forward,strict_clock_transport(7,31,0,1)),
    test(strict_affine_reversal_rejected,\+ strict_clock_transport(-1,31,0,1)),
    test(flat_map_collapse_detected,constant_clock_collapses),
    test(no_self_promotion,not_self_promoted),
    write('PHASE373_CLOCK_AUTHORITY_PASS (finite policy projection only)'),nl,
    halt(0).
