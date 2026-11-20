% Phase368: bounded GNU Prolog governance checker, not a field theorem.
% No consult/1, no self-signed proof promotion, no unbounded search.

source(original301, ordinary_integer_pair_gram).
source(d203, maximal_omega_order).

world(source_original, original301, meso).
world(formal_lean, original301, meso).
world(finite_prolog, original301, fast).
world(field_chart, original301, review).
world(d203_fabric, d203, meso).
world(external_reviewer, original301, review).

triad(matrix_bridge,source_original,formal_lean,finite_prolog).
triad(field_review,source_original,field_chart,external_reviewer).

valid_triad(Name) :-
    triad(Name,A,B,C), A \= B, B \= C, A \= C,
    world(A,_,_), world(B,_,_), world(C,_,_).

% Source-preserving integral row gauge and observation-clock extension are
% DIFFERENT typed transports, even with the same integer source.
transport(unimodular_frame,original301,original301,exact,none).
transport(clock_successor,original301,original301,lossy,observation_columns_change).
transport(d203_to_301,d203,original301,forbidden,coefficient_category_mismatch).

safe_for_det_valuation(T) :-
    transport(T,S,D,exact,none), S == D.

same_source_closure(World,Scope) :-
    world(World,original301,_), Scope == encoded_matrix_lemma.

% A distinct outside reviewer is required for field-chart *semantic review*.
% This predicate alone cannot authenticate a human or certify any mathematics.
external_semantic_review(Author,Validator,field_301,external_record) :-
    Author \= Validator, Validator == independent_human.

can_close_encoded_proof(lean_kernel,encoded_matrix_lemma).
can_close_field_semantics(independent_human,field_301,external_record).

% Recorded historical CI audit: false green must never count as evidence.
replay_record(44753105275,success,marker_missing,exception_present).
replay_record(44753393399,success,marker_present,no_exception).
trusted_test_record(Id) :-
    replay_record(Id,success,marker_present,no_exception).

assert_goal(Name,Goal) :-
    ( call(Goal) -> write('PASS '),write(Name),nl
    ; write('FAIL '),write(Name),nl,fail).

phase368_main :-
    assert_goal(matrix_three_way_obligation,valid_triad(matrix_bridge)),
    assert_goal(review_three_way_obligation,valid_triad(field_review)),
    assert_goal(unimodular_row_frame_safe,safe_for_det_valuation(unimodular_frame)),
    assert_goal(clock_not_row_gauge,\+ safe_for_det_valuation(clock_successor)),
    assert_goal(d203_not_301,\+ safe_for_det_valuation(d203_to_301)),
    assert_goal(prolog_cannot_close_field,
       \+ can_close_field_semantics(prolog_exact,field_301,external_record)),
    assert_goal(lean_cannot_self_certify_field,
       \+ can_close_field_semantics(lean_kernel,field_301,external_record)),
    assert_goal(refuse_self_reviewer,
       \+ external_semantic_review(author_a,author_a,field_301,external_record)),
    assert_goal(allow_distinct_review_request,
       external_semantic_review(author_a,independent_human,field_301,external_record)),
    assert_goal(reject_false_green_44753105275,
       \+ trusted_test_record(44753105275)),
    assert_goal(accept_corrected_test_44753393399,
       trusted_test_record(44753393399)),
    assert_goal(forbid_d203_as_same_source,
       \+ same_source_closure(d203_fabric,encoded_matrix_lemma)),
    write('PHASE368_GUARD_PASS (typed governance only)'),nl,
    halt(0).
