% Phase376 — bounded GNU Prolog witness/revocation counterworlds.
% No actual cryptographic verification or authenticated clock runs here.

credential(issuer, key_a, issue_task, 1).
credential(issuer_alias, key_a, policy_migration, 1).
credential(approver, key_b, policy_migration, 1).
credential(guardian, key_c, revoke_key, 1).
credential(successor, key_d, policy_migration, 5).

revocation(key_b, 4).
revocation(key_a, 4).

active_at(Key, Tick) :-
    credential(_, Key, _, Registered),
    Tick >= Registered,
    \+ (revocation(Key, Cutoff), Tick >= Cutoff).

has_role(Actor, Role, Tick) :-
    credential(Actor, Key, Role, _),
    active_at(Key, Tick).

independent_keys(ActorA, ActorB) :-
    credential(ActorA, KeyA, _, _),
    credential(ActorB, KeyB, _, _),
    KeyA \= KeyB.

% Historical records belong to old policy and cannot be manufactured
% retroactively just because a new version changes permissions.
issued_under(task_source_meso, policy374, source_anchor, meso, issuer, 1).
issued_under(task_source_fast, policy374, source_anchor, fast, issuer, 1).
issued_under(task_d203, policy374, d203_contrast, meso, issuer, 1).

allowed(policy374, source_anchor, meso).
allowed(policy375, source_anchor, meso).
allowed(policy375, source_anchor, fast).

meaning(policy374, source_anchor, original_trace_gram).
meaning(policy375, source_anchor, original_trace_gram).
meaning(policy374, d203_contrast, maximal_order_d203).
meaning(policy375_drift, source_anchor, maximal_order_d203).

semantically_compatible(Old,New,Arm) :-
    meaning(Old,Arm,M),
    meaning(New,Arm,M).

historically_issued(Task) :-
    issued_under(Task,Old,Arm,Tier,Issuer,Issued),
    allowed(Old,Arm,Tier),
    has_role(Issuer,issue_task,Issued).

new_approval(Task,Target,Approver,Tick) :-
    issued_under(Task,Old,Arm,Tier,Issuer,Issued),
    Issued < Tick,
    allowed(Old,Arm,Tier),
    allowed(Target,Arm,Tier),
    semantically_compatible(Old,Target,Arm),
    has_role(Issuer,issue_task,Tick),
    has_role(Approver,policy_migration,Tick),
    independent_keys(Issuer,Approver).

% A signed, trusted revocation would need external authentication.
% Here the revocation facts are only fixture declarations.
valid_revocation(Target,By,Effective,Observed) :-
    credential(Target,TargetKey,_,_),
    has_role(By,revoke_key,Observed),
    independent_keys(Target,By),
    credential(_,TargetKey,_,_),
    Effective =:= Observed.

historic_approval_record(task_source_meso,policy375,2).

test(Name,Goal) :-
    (call(Goal)->write('PASS '),write(Name),nl
    ;write('FAIL '),write(Name),nl,fail).

phase376_main :-
    test(issuer_active_before_revocation, has_role(issuer,issue_task,2)),
    test(approver_active_before_revocation, has_role(approver,policy_migration,2)),
    test(approval_before_revocation, new_approval(task_source_meso,policy375,approver,2)),
    test(approver_revoked_at_cutoff,\+ has_role(approver,policy_migration,4)),
    test(issuer_revoked_at_cutoff,\+ has_role(issuer,issue_task,4)),
    test(revocation_blocks_new_migration,\+ new_approval(task_source_meso,policy375,approver,4)),
    test(historical_record_not_erased,historic_approval_record(task_source_meso,policy375,2)),
    test(approver_before_enrollment_rejected,\+ has_role(successor,policy_migration,4)),
    test(new_key_active_after_registration,has_role(successor,policy_migration,5)),
    test(revoked_issuer_still_blocks_new_approver,\+ new_approval(task_source_meso,policy375,successor,6)),
    test(self_alias_not_independent,\+ independent_keys(issuer,issuer_alias)),
    test(distinct_names_not_sufficient,issuer \= issuer_alias),
    test(independent_three_keys,independent_keys(approver,guardian)),
    test(guardian_revocation_fixture,valid_revocation(approver,guardian,4,4)),
    test(backdated_revocation_rejected,\+ valid_revocation(approver,guardian,3,4)),
    test(future_revocation_rejected,\+ valid_revocation(approver,guardian,5,4)),
    test(guardian_cannot_self_revoke,\+ valid_revocation(guardian,guardian,4,4)),
    test(historical_fast_origin_still_unauthorized,\+ historically_issued(task_source_fast)),
    test(policy_widening_not_retroactive,\+ new_approval(task_source_fast,policy375,approver,2)),
    test(d203_not_source_transport,\+ semantically_compatible(policy374,policy375_drift,source_anchor)),
    write('PHASE376_PROLOG_REVOCATION_PASS (finite symbolic worlds only)'),nl,
    halt(0).
