% Phase372 — bounded Prolog adversarial run/attempt/job lineage controls.
% Actual Phase371 data: run family 44809412040 has attempt 1 and attempt 2.
% This is a finite governance model, NOT a real verifier, signer, or theorem.
%
% A history/attempt event has fields:
% execution(Id, Run, Attempt, Job, Head, Started, RunSuccess, JobSuccess, Marker).
% Timestamps are lexicographically ordered UTC integers for this fixed case.

head(b07bb172).
issued(phase371_source, b07bb172, 20261120201440, source_contract).
execution(first,44809412040,1,136541801767,b07bb172,
          20261120201340,yes,yes,not_issued).
execution(second,44809412040,2,136542423196,b07bb172,
          20261120201448,yes,yes,source_verified).
execution(false_green,44753105275,1,136345755487,b07bb172,
          20261120201000,yes,yes,uncaught_exception).
execution(duplicate_job,44809412040,3,136542423196,b07bb172,
          20261120201548,yes,yes,source_verified).
execution(wrong_head,44809412040,3,136542423197,stale_head,
          20261120201548,yes,yes,source_verified).
execution(failed_job,44809412040,4,136542423198,b07bb172,
          20261120201648,yes,no,source_verified).
execution(missing_marker,44809412040,5,136542423199,b07bb172,
          20261120201748,yes,yes,none).

same_family(A,B) :-
    execution(A,R,_,_,_,_,_,_,_),
    execution(B,R,_,_,_,_,_,_,_).

same_execution(A,B) :-
    execution(A,R,T,J,H,_,_,_,_),
    execution(B,R,T,J,H,_,_,_,_).

distinct_execution(A,B) :-
    same_family(A,B),
    \+ same_execution(A,B).

strictly_after_issue(Task,E) :-
    issued(Task,H,Issued,_),
    execution(E,_,_,_,H,Started,_,_,_),
    Started > Issued.

candidate(Task,E) :-
    strictly_after_issue(Task,E),
    execution(E,_,Attempt,_,_,_,yes,yes,source_verified),
    Attempt > 0.

% The execution key is (run family, attempt, job, head).
% A second task may credit a distinct attempt only if separately issued
% and with a fresh job ID. "same family" is not equality of executions.
duplicate_job(A,B) :-
    execution(A,_,_,Job,_,_,_,_,_),
    execution(B,_,_,Job,_,_,_,_,_), A \= B.

% The system must detect a true prior consumption rather than mere
% membership in the same GitHub run family.
consumed_execution(second).
eligible_new_execution(E) :-
    execution(E,_,_,_,_,_,_,_,_),
    \+ consumed_execution(E),
    \+ (consumed_execution(C), duplicate_job(C,E)).

% Fixed historical facts. They are not representative random workloads.
untrusted_ci_run(44753105275).
cannot_promote_number_theory(source_contract).
cannot_promote_number_theory(prolog_exact).

test(Name,Goal) :-
    ( call(Goal) -> write('PASS '),write(Name),nl
    ; write('FAIL '),write(Name),nl,fail ).

phase372_main :-
    test(same_run_family_1_2, same_family(first,second)),
    test(attempts_distinct, distinct_execution(first,second)),
    test(not_same_execution, \+ same_execution(first,second)),
    test(initial_preissue_rejected, \+ candidate(phase371_source,first)),
    test(rerun_after_issue_accepted, candidate(phase371_source,second)),
    test(different_head_rejected, \+ candidate(phase371_source,wrong_head)),
    test(job_failure_rejected, \+ candidate(phase371_source,failed_job)),
    test(missing_marker_rejected, \+ candidate(phase371_source,missing_marker)),
    test(false_green_rejected, \+ candidate(phase371_source,false_green)),
    test(second_consumed_cannot_recredit, \+ eligible_new_execution(second)),
    test(recycled_job_rejected, \+ eligible_new_execution(duplicate_job)),
    test(different_attempt_not_identical, \+ same_execution(second,duplicate_job)),
    test(known_false_green_marked, untrusted_ci_run(44753105275)),
    test(source_guard_not_field_authority, cannot_promote_number_theory(source_contract)),
    test(prolog_not_field_authority, cannot_promote_number_theory(prolog_exact)),
    write('PHASE372_PROLOG_GOVERNANCE_PASS (finite witness, not field theorem)'),nl,
    halt(0).
