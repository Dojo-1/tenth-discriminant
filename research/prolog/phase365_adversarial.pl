% Phase365: bounded GNU Prolog adversarial controls for the SAME original Gram.
% Evidence scope: source-contract model + finite integer counterworlds ONLY.
% Not a Lean checker, a proof of a uniform bound, or a class-number solver.
% Source terms must also pass scripts/phase365_lean_anchor_guard.py.

source_sig(phase362_upper, gram(q_thin,d,s,r,s,ordinary_z_fixed_w,trace_2_2d,row_major)).
source_sig(phase363_lower, gram(q_thin,d,s,r,s,ordinary_z_fixed_w,trace_2_2d,row_major)).
source_sig(phase362_positive, gram(q_thin,d,s,r,s,ordinary_z_fixed_w,trace_2_2d,row_major)).
source_sig(fake_padded, gram(q_padded,d,s,r,s,ordinary_z_fixed_w,trace_2_2d,row_major)).
source_sig(fake_hasse, gram(q_thin,d,s,r,s,hasse_z_fixed_w,trace_2_2d,row_major)).
source_sig(fake_j_change, gram(q_thin,d,extra_j,r,s,ordinary_z_fixed_w,trace_2_2d,row_major)).
source_sig(fake_metric, gram(q_thin,d,s,r,s,ordinary_z_fixed_w,trace_unit,row_major)).
source_sig(fake_row_order, gram(q_thin,d,s,r,s,ordinary_z_fixed_w,trace_2_2d,column_major)).

same_source(A, B) :-
    source_sig(A, SA), source_sig(B, SB), SA == SB.

% This is a declared dependency graph of Phase364, not an extracted Lean proof.
requires(phase364_field, odd_even_field_chart).
requires(phase364_field, phase364_odd).
requires(phase364_odd, phase362_upper).
requires(phase364_odd, phase363_lower).
requires(phase364_odd, phase362_positive).
requires(phase364_odd, phase361_scalar).
requires(phase362_upper, source_gram).
requires(phase363_lower, source_gram).
requires(phase362_positive, source_gram).
requires(phase363_lower, joint_binary_odd_mass).
requires(joint_binary_odd_mass, original_integral_rows).
requires(joint_binary_odd_mass, squarefree_odd_chart).
requires(phase364_field, quadratic_field_equivalence).
requires(odd_even_field_chart, quadratic_field_equivalence).
requires(cycle_a, cycle_b).
requires(cycle_b, cycle_a).

seen(X, [H|_]) :- X == H, !.
seen(X, [_|T]) :- seen(X,T).

backtrace(A, B, Path) :- walk(A, B, [A], Path).
walk(A, B, Seen, [A,B]) :-
    requires(A, B), \+ seen(B, Seen).
walk(A, B, Seen, [A|Rest]) :-
    requires(A, Mid), \+ seen(Mid, Seen),
    walk(Mid, B, [Mid|Seen], Rest).

% Exact real-axis toy restriction of original ordinary-Z derivative, S=1.
% Source Q consists of distinct real (x,0) lattice points; all imaginary
% coefficients vanish, leaving the original 2*a*b trace contribution.
falling(R, K, 0) :- K > R, !.
falling(_, 0, 1) :- !.
falling(R, K, F) :-
    K > 0, K =< R,
    R1 is R-1, K1 is K-1,
    falling(R1,K1,F1), F is R*F1.

power_int(_, 0, 1) :- !.
power_int(X, N, P) :-
    N > 0, N1 is N-1,
    power_int(X,N1,P1), P is X*P1.

ordinary_jet(R, J, _, 0) :- J > R, !.
ordinary_jet(R, J, X, Value) :-
    J =< R, falling(R,J,F), N is R-J,
    power_int(X,N,P), Value is F*P.

sum_j(J, J, _, _, _, 0) :- !.
sum_j(K, J, X, R, T, Total) :-
    K < J, ordinary_jet(R,K,X,A), ordinary_jet(T,K,X,B),
    K1 is K+1, sum_j(K1,J,X,R,T,Rest),
    Total is A*B+Rest.

sum_q([], _, _, _, 0).
sum_q([X|Xs], J, R, T, Sum) :-
    sum_j(0,J,X,R,T,Here),
    sum_q(Xs,J,R,T,Rest), Sum is Here+Rest.

gram_entry(Q, J, R, T, G) :-
    J >= 1, sum_q(Q,J,R,T,Raw), G is 2*Raw.

gram_2(X,Y,G00,G01,G11) :-
    Q = [X,Y],
    gram_entry(Q,1,0,0,G00),
    gram_entry(Q,1,0,1,G01),
    gram_entry(Q,1,1,1,G11).

det_2(X,Y,Det) :-
    X =\= Y,
    gram_2(X,Y,A,B,C), Det is A*C-B*B.

det_3(Q, J, Det) :-
    Q = [X,Y,Z], X =\= Y, X =\= Z, Y =\= Z,
    gram_entry(Q,J,0,0,A),
    gram_entry(Q,J,0,1,B),
    gram_entry(Q,J,0,2,C),
    gram_entry(Q,J,1,1,E),
    gram_entry(Q,J,1,2,F),
    gram_entry(Q,J,2,2,I),
    Det is A*(E*I-F*F)-B*(B*I-F*C)+C*(B*F-E*C).

v_p(N, P, V) :- N > 0, P > 1, v_p_loop(N,P,V).
v_p_loop(N,P,V) :-
    Rem is N mod P,
    ( Rem =:= 0 -> N1 is N // P,
      v_p_loop(N1,P,V0), V is V0+1
    ; V = 0 ).


% True non-real integer-pair operations, not a Euclidean scalar proxy.
% These mirror IntegerTraceGram.lean: pairMul, pairConj, pairPow,
% r.descFactorial j, ordinary Z differentiation holding W fixed.
pair_mul(D,z(A,B),z(C,E),z(R,I)) :-
    R is A*C-D*B*E, I is A*E+B*C.
pair_conj(z(A,B),z(A,NB)) :- NB is -B.
pair_scale(F,z(A,B),z(R,I)) :- R is F*A, I is F*B.
pair_pow(_,_,0,z(1,0)) :- !.
pair_pow(D,Z,N,P) :-
    N > 0, N1 is N-1,
    pair_pow(D,Z,N1,P0),
    pair_mul(D,P0,Z,P).
pair_trace(D,z(A,B),z(C,E),T) :-
    T is 2*(A*C+D*B*E).

integer_ordinary_jet(_,R,_,J,_,z(0,0)) :-
    J > R, !.
integer_ordinary_jet(D,R,S,J,Z,Out) :-
    J =< R,
    falling(R,J,F), N is R-J,
    pair_pow(D,Z,N,P), pair_conj(Z,C),
    pair_pow(D,C,S,W),
    pair_mul(D,P,W,Raw), pair_scale(F,Raw,Out).

lattice_sum_j(K,K,_,_,_,_,0) :- !.
lattice_sum_j(K,J,D,Z,row(R,S),row(T,U),Total) :-
    K < J,
    integer_ordinary_jet(D,R,S,K,Z,A),
    integer_ordinary_jet(D,T,U,K,Z,B),
    pair_trace(D,A,B,Here),
    K1 is K+1,
    lattice_sum_j(K1,J,D,Z,row(R,S),row(T,U),Rest),
    Total is Here+Rest.

lattice_sum_q([],_,_,_,_,0).
lattice_sum_q([Z|Zs],D,J,Row1,Row2,Total) :-
    lattice_sum_j(0,J,D,Z,Row1,Row2,Here),
    lattice_sum_q(Zs,D,J,Row1,Row2,Rest),
    Total is Here+Rest.

lattice_original_gram_entry(Q,D,J,Row1,Row2,Value) :-
    J >= 1,
    lattice_sum_q(Q,D,J,Row1,Row2,Value).

nonreal_conjugate_observer :-
    Q=[z(0,1)], D=3, J=2,
    lattice_original_gram_entry(Q,D,J,row(0,0),row(0,0),A),
    lattice_original_gram_entry(Q,D,J,row(0,0),row(1,1),B),
    lattice_original_gram_entry(Q,D,J,row(1,1),row(1,1),C),
    A =:= 2, B =:= 6, C =:= 24,
    Det is A*C-B*B, Det =:= 12.

% Holding the W factor FIXED is observable: z*z=-3 while z*conj(z)=+3.
nonreal_sign_falsifier :-
    pair_mul(3,z(0,1),z(0,1),z(-3,0)),
    pair_mul(3,z(0,1),z(0,-1),z(3,0)),
    nonreal_conjugate_observer.


% Two-clock discriminator: for fixed real source, adding ordinary-jet
% observations increases the *positive-semidefinite* Gram in Loewner order,
% but p-adic determinant valuations need not increase.
increment_entry(Q,J1,J2,R,T,Delta) :-
    J2 > J1, gram_entry(Q,J1,R,T,A), gram_entry(Q,J2,R,T,B),
    Delta is B-A.

archimedean_padic_clock_split :-
    Q=[1,6,11],
    increment_entry(Q,1,2,0,0,0),
    increment_entry(Q,1,2,0,1,0),
    increment_entry(Q,1,2,0,2,0),
    increment_entry(Q,1,2,1,1,6),
    increment_entry(Q,1,2,1,2,72),
    increment_entry(Q,1,2,2,2,1264),
    Minor is 6*1264-72*72, Minor =:= 2400, Minor > 0,
    increment_entry(Q,2,3,0,0,0),
    increment_entry(Q,2,3,1,1,0),
    increment_entry(Q,2,3,1,2,0),
    increment_entry(Q,2,3,2,2,24),
    det_3(Q,1,A), det_3(Q,2,B), det_3(Q,3,C),
    A < B, B < C,
    v_p(A,5,6), v_p(B,5,2), v_p(C,5,0).

% Bounded search, not universal inference.
clock_counterexample(J1,J2,V1,V2) :-
    between(1,3,J1), between(1,3,J2), J1 < J2,
    det_3([1,6,11],J1,D1), det_3([1,6,11],J2,D2),
    v_p(D1,5,V1), v_p(D2,5,V2), V1 > V2.

selected_minor_counterexample(E1,E2,Selected,Gram) :-
    between(1,3,E1), between(1,3,E2),
    Selected is E1*E1,
    Gram is E1*E1 + E2*E2,
    Gram > Selected.

% U=[[1,0],[-1,1]]: only integral unimodular row changes are
% a genuine Gram congruence, not an arbitrary coordinate substitution.
moving_row_frame_control :-
    gram_2(1,6,A,B,C),
    H00 is A,
    H01 is B-A,
    H11 is C-2*B+A,
    H00 =:= 4, H01 =:= 10, H11 =:= 50,
    Before is A*C-B*B, After is H00*H11-H01*H01,
    Before =:= After, Before =:= 100.

% Two distinct modular prime roles: p extracts, q may witness rank.
two_prime_role_control :-
    P = 3, Q = 5,
    DetE = 3,
    0 =:= DetE mod P,
    0 =\= DetE mod Q,
    DetGram is 36,
    0 =:= DetGram mod (P*P).

% A p^2 Gram factor need not appear in each raw matrix entry.
raw_entry_obstruction :-
    det_2(1,6,Det),
    gram_2(1,6,_,OffDiagonal,_),
    0 =:= Det mod 25,
    0 =\= OffDiagonal mod 5.

% Matched source size need not imply matched determinant valuations.
equal_cardinality_unequal_valuation :-
    det_2(0,5,D5), det_2(0,1,D1),
    D5 =:= 100, D1 =:= 4,
    v_p(D5,5,2), v_p(D1,5,0).

test(Name, Goal) :-
    ( call(Goal) ->
        write('PASS '), write(Name), nl
    ; write('FAIL '), write(Name), nl, fail ).

run_tests :-
    test(upper_lower_source_match,
        same_source(phase362_upper,phase363_lower)),
    test(positive_upper_source_match,
        same_source(phase362_positive,phase362_upper)),
    test(reject_padded_gram,
        \+ same_source(phase362_upper,fake_padded)),
    test(reject_hasse_jet,
        \+ same_source(phase362_upper,fake_hasse)),
    test(reject_changed_derivative_clock,
        \+ same_source(phase362_upper,fake_j_change)),
    test(reject_changed_trace_metric,
        \+ same_source(phase362_upper,fake_metric)),
    test(reject_changed_row_order,
        \+ same_source(phase362_upper,fake_row_order)),
    test(trace_back_from_field_to_arithmetic,
        backtrace(phase364_field,original_integral_rows,
          [phase364_field,phase364_odd,phase363_lower,
           joint_binary_odd_mass,original_integral_rows])),
    test(reject_cycle_in_backtrace,
        \+ backtrace(cycle_a,nonexistent,_)),
    test(original_two_point_qfive,
        det_2(0,5,100)),
    test(original_two_point_qunit,
        det_2(0,1,4)),
    test(shifted_source_row_unimodular,
        moving_row_frame_control),
    test(p_squared_factor_without_raw_entry,
        raw_entry_obstruction),
    test(fixed_sample_clock_j1,
        det_3([1,6,11],1,500000)),
    test(fixed_sample_clock_j2,
        det_3([1,6,11],2,784400)),
    test(fixed_sample_clock_j3,
        det_3([1,6,11],3,799664)),
    test(archimedean_psd_vs_padic_clock_drop,
        archimedean_padic_clock_split),
    test(clock_valuations_6_2_0,
        (det_3([1,6,11],1,A), v_p(A,5,6),
         det_3([1,6,11],2,B), v_p(B,5,2),
         det_3([1,6,11],3,C), v_p(C,5,0))),
    test(find_clock_counterexample,
        clock_counterexample(1,2,6,2)),
    test(two_distinct_prime_roles,
        two_prime_role_control),
    test(original_nonreal_conjugate_trace,
        nonreal_conjugate_observer),
    test(nonreal_sign_countercontrol,
        nonreal_sign_falsifier),
    test(selected_minor_is_not_gram_upper,
        selected_minor_counterexample(1,1,1,2)),
    test(same_sample_cardinality_not_same_factor,
        equal_cardinality_unequal_valuation),
    write('PHASE365_BOUNDED_PROLOG_PASS (not a field theorem)'), nl.

main :- (run_tests -> halt(0) ; halt(1)).
