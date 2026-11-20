% Phase375 -- finite cross-policy transport counterworlds.
% This is a GNU Prolog falsification model, not cryptography or a field proof.
% Each v375* name represents a SEPARATE hypothetical policy successor,
% not multiple active snapshots for one ordinal in the production registry.

version(v374,374).
version(v375_compatible,375).
version(v375_fast_widened,375).
version(v375_changed_source,375).
version(v375_changed_scope,375).
version(v375_changed_plane,375).
version(v375_changed_clock,375).
version(v375_cost_increased,375).

% profile(Version,Arm,Source,Scope,Execution,NativeClock,Cost).
profile(v374,source_anchor,original,source_contract,local,meso,1).
profile(v375_compatible,source_anchor,original,source_contract,local,meso,1).
profile(v375_fast_widened,source_anchor,original,source_contract,local,fast,1).
profile(v375_changed_source,source_anchor,d203,source_contract,local,meso,1).
profile(v375_changed_scope,source_anchor,original,matrix_general,local,meso,1).
profile(v375_changed_plane,source_anchor,original,source_contract,human,meso,1).
profile(v375_changed_clock,source_anchor,original,source_contract,local,fast,1).
profile(v375_cost_increased,source_anchor,original,source_contract,local,meso,2).
profile(v374,d203_contrast,d203,matrix_general,local,fast,3).

tier_accept(fast,fast).
tier_accept(meso,fast).
tier_accept(meso,meso).
tier_accept(review,fast).
tier_accept(review,meso).
tier_accept(review,review).

valid_executor(local,_,_).
valid_executor(human,review,yes).

source_allowed(original,_).
source_allowed(d203,yes).

authorized(Version,Arm,Tier,Budget,AllowHuman,AllowContrast) :-
    profile(Version,Arm,Source,_,Execution,Native,Cost),
    Cost =< Budget,
    tier_accept(Tier,Native),
    source_allowed(Source,AllowContrast),
    (Execution \= human ; (AllowHuman=yes, Tier=review)).

% Original task identity and issuance conditions are NOT recomputed from
% the new policy. These are fixture facts, not externally fetched comments.
issued(task_meso,v374,source_anchor,meso,1,issuer_a).
issued(task_meso_budget2,v374,source_anchor,meso,2,issuer_a).
issued(task_fast_historical,v374,source_anchor,fast,9,issuer_a).

same_meaning(Old,New,Arm) :-
    profile(Old,Arm,Source,Scope,Exec,Native,_OldCost),
    profile(New,Arm,Source,Scope,Exec,Native,_NewCost).

candidate_migration(Task,Target,Approver) :-
    issued(Task,Original,Arm,Tier,Budget,Issuer),
    version(Original,V0),version(Target,V1),V0<V1,
    authorized(Original,Arm,Tier,Budget,no,no),
    authorized(Target,Arm,Tier,Budget,no,no),
    same_meaning(Original,Target,Arm),
    Approver \= Issuer.

% An explicit version label is not proof of a distinct authenticated key.
% This predicate is deliberately narrower than a signed attestation.

test(Name,Goal) :-
    (call(Goal) -> write('PASS '),write(Name),nl
    ;write('FAIL '),write(Name),nl,fail).

phase375_main :-
    test(old_source_fast_rejected,
         \+ authorized(v374,source_anchor,fast,9,no,no)),
    test(old_source_meso_allowed,
         authorized(v374,source_anchor,meso,1,no,no)),
    test(new_fast_policy_widens,
         authorized(v375_fast_widened,source_anchor,fast,9,no,no)),
    test(widening_not_retroactive,
         \+ candidate_migration(task_fast_historical,v375_fast_widened,external_auditor)),
    test(compatible_rename,
         candidate_migration(task_meso,v375_compatible,external_auditor)),
    test(unrelated_change_not_authority_loss,
         same_meaning(v374,v375_compatible,source_anchor)),
    test(source_drift_blocks,
         \+ candidate_migration(task_meso,v375_changed_source,external_auditor)),
    test(scope_drift_blocks,
         \+ candidate_migration(task_meso,v375_changed_scope,external_auditor)),
    test(executor_drift_blocks,
         \+ candidate_migration(task_meso,v375_changed_plane,external_auditor)),
    test(clock_drift_blocks_even_if_new_tier_eligible,
         \+ candidate_migration(task_meso,v375_changed_clock,external_auditor)),
    test(cost_increase_over_budget_blocks,
         \+ candidate_migration(task_meso,v375_cost_increased,external_auditor)),
    test(cost_increase_under_budget_can_be_certified,
         candidate_migration(task_meso_budget2,v375_cost_increased,external_auditor)),
    test(self_approval_blocks,
         \+ candidate_migration(task_meso,v375_compatible,issuer_a)),
    test(unknown_approver_is_not_claimed_authoritative,
         \+ candidate_migration(task_fast_historical,v375_compatible,unknown_auditor)),
    test(d203_contrast_not_original,
         \+ authorized(v374,d203_contrast,meso,9,no,no)),
    test(d203_contrast_optin_only,
         authorized(v374,d203_contrast,meso,9,no,yes)),
    test(source_scope_equality_is_not_clock_equality,
         \+ same_meaning(v374,v375_changed_clock,source_anchor)),
    write('PHASE375_PROLOG_VERSION_TRANSPORT_PASS (finite fixtures only)'),nl,
    halt(0).
