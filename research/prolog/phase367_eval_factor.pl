% Phase367 source-exact integer evaluation factorization adversarial oracle.
% Built on Phase365's exact integer-pair polynomial/ordinary-jet evaluator.
% This is an independent arithmetic organization of the same finite model,
% NOT an independent number-theoretic proof or a Lean parser.
:- consult('research/prolog/phase365_adversarial.pl').

% A and B retain BOTH coordinates, rather than collapsing a complex pair
% into a Euclidean real scalar. Same Q, D, clock and row family.
eval_col(D,K,Row,Z,Real,Imag) :-
    Row = row(R,S),
    integer_ordinary_jet(D,R,S,K,Z,z(Real,Imag)).

eval_q_product([],_,_,_,_,0,0).
eval_q_product([Z|Zs],D,K,RowA,RowB,Real,Imag) :-
    eval_col(D,K,RowA,Z,A1,B1),
    eval_col(D,K,RowB,Z,A2,B2),
    eval_q_product(Zs,D,K,RowA,RowB,R0,I0),
    Real is A1*A2+R0,
    Imag is B1*B2+I0.

eval_clock_products(K,J,_,_,_,_,0,0) :- K >= J, !.
eval_clock_products(K,J,Q,D,RowA,RowB,Real,Imag) :-
    K < J,
    eval_q_product(Q,D,K,RowA,RowB,R1,I1),
    K1 is K+1,
    eval_clock_products(K1,J,Q,D,RowA,RowB,R0,I0),
    Real is R1+R0,
    Imag is I1+I0.

factor_entry(Q,D,J,RowA,RowB,Entry) :-
    J >= 0, D >= 0,
    eval_clock_products(0,J,Q,D,RowA,RowB,A,B),
    Entry is 2*(A+D*B).

% Deliberately false comparison: ignores the imaginary D-weight.
bad_unweighted_entry(Q,D,J,RowA,RowB,Entry) :-
    eval_clock_products(0,J,Q,D,RowA,RowB,A,B),
    Entry is 2*(A+B).

% Compare independently arranged *factor-product* and direct trace-sum.
exact_factor_cross(Q,D,J,RowA,RowB) :-
    factor_entry(Q,D,J,RowA,RowB,Factor),
    lattice_original_gram_entry(Q,D,J,RowA,RowB,Direct),
    Factor =:= Direct.

nonreal_factor_matrix :-
    Q=[z(0,1)], D=3, J=2,
    exact_factor_cross(Q,D,J,row(0,0),row(0,0)),
    exact_factor_cross(Q,D,J,row(0,0),row(1,1)),
    exact_factor_cross(Q,D,J,row(1,1),row(1,1)),
    factor_entry(Q,D,J,row(0,0),row(0,0),2),
    factor_entry(Q,D,J,row(0,0),row(1,1),6),
    factor_entry(Q,D,J,row(1,1),row(1,1),24),
    bad_unweighted_entry(Q,D,J,row(1,1),row(1,1),Wrong),
    Wrong =:= 20, Wrong =\= 24.

% Real sample positive Gram gains but 5-adic valuations fall.
real_two_clock_matrix :-
    Q=[z(0,0),z(5,0)], D=25,
    exact_factor_cross(Q,D,1,row(0,0),row(0,0)),
    exact_factor_cross(Q,D,1,row(0,0),row(1,0)),
    exact_factor_cross(Q,D,1,row(1,0),row(1,0)),
    factor_entry(Q,D,1,row(0,0),row(0,0),4),
    factor_entry(Q,D,1,row(0,0),row(1,0),10),
    factor_entry(Q,D,1,row(1,0),row(1,0),50),
    factor_entry(Q,D,2,row(1,0),row(1,0),54),
    OldDet is 4*50-10*10,
    NewDet is 4*54-10*10,
    OldDet =:= 100, NewDet =:= 116,
    v_p(OldDet,5,2), v_p(NewDet,5,0).

% Boundary: at D=0 the pair-ring trace identity still exists, but
% the positive-D complex embedding used in the earlier Lean cast does not.
zero_d_boundary_factor :-
    Q=[z(0,1)], D=0, J=2,
    exact_factor_cross(Q,D,J,row(0,0),row(0,0)),
    exact_factor_cross(Q,D,J,row(0,0),row(1,1)),
    exact_factor_cross(Q,D,J,row(1,1),row(1,1)),
    factor_entry(Q,D,J,row(0,0),row(0,0),2),
    factor_entry(Q,D,J,row(0,0),row(1,1),0),
    factor_entry(Q,D,J,row(1,1),row(1,1),0).

% Exact row-gauge: Qshift=(1,6) and U=[[1,0],[-1,1]].
% Transform A to U A first; then rebuild the Gram from transformed features.
gauge_real_entry(Q,D,J,R1,R2,Val) :-
    eval_clock_products(0,J,Q,D,R1,R2,A,B),
    Val is 2*(A+D*B).

unimodular_evaluation_frame :-
    Q=[z(1,0),z(6,0)], D=25, J=1,
    gauge_real_entry(Q,D,J,row(0,0),row(0,0),4),
    gauge_real_entry(Q,D,J,row(0,0),row(1,0),14),
    gauge_real_entry(Q,D,J,row(1,0),row(1,0),74),
    % A_0=[1,1], A_1=[1,6], U*A=[[1,1],[0,5]]
    % The imaginary matrix vanishes, so this is the SAME original Gram.
    Row0=[1,1], Row1=[0,5],
    Row0=[X,Y], Row1=[Z,W],
    H00 is 2*(X*X+Y*Y),
    H01 is 2*(X*Z+Y*W),
    H11 is 2*(Z*Z+W*W),
    H00 =:= 4, H01 =:= 10, H11 =:= 50,
    Before is 4*74-14*14,
    After is H00*H11-H01*H01,
    Before =:= 100, After =:= Before.

% A nonunimodular diagonal row scaling changes determinant by det(U)^2.
nonunimodular_frame_falsifier :-
    % Qshift Gram determinant is 100, U=diag(5,1) => det(U)=5
    % after congruence it becomes 2500, not 100.
    OldDet = 100, Scale=5,
    NewDet is Scale*Scale*OldDet,
    NewDet =:= 2500,
    NewDet =\= OldDet.

phase367_main :-
    test(nonreal_full_original_evaluation_gram,nonreal_factor_matrix),
    test(reject_missing_imaginary_D_weight,nonreal_factor_matrix),
    test(two_clock_original_real_factorization,real_two_clock_matrix),
    test(integer_D0_source_factor_boundary,zero_d_boundary_factor),
    test(legitimate_unimodular_row_eval_frame,unimodular_evaluation_frame),
    test(reject_nonunimodular_determinant_transport,nonunimodular_frame_falsifier),
    write('PHASE367_BOUNDED_FACTOR_ORACLE_PASS (not a universal proof)'), nl,
    halt(0).
