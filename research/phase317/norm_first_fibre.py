#!/usr/bin/env python3
"""Phase317-A: exact first nonrational norm-D+1 fibres.

For D=4m-1>3, O'=Z[sqrt(-D)] has N(x+y sqrt(-D))=x²+D*y².
At N=D+1=4m:
  y=±1,x=±1 gives 4 nonrational solutions;
  y=0 gives 2 MORE iff m is a square (x=±2sqrt(m));
  |y|>=2 is impossible.
Thus 4+2*isSquare(m) elements, regardless of class number.

The standard external class-group argument says if fundamental D has
h(-D)=1 then m must be prime: a proper prime divisor p|m gives a
ring map O_K -> F_p, omega -> 0, hence ideal norm p. Under h1 it
must be principal, contradicting the N<m rational-square lemma.

D187 is an intentional non-h1 field with PRIME m47 and STILL four
generators, so this norm fibre alone is not a class-one detector.
D35 with SQUARE m9 has six; D203 with composite NONSQUARE m51 has
four. No new discriminant cutoff.
"""
from math import isqrt
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase308"))
from adaptive_torsion_family import independent_reduced_forms

H1=(7,11,19,43,67,163)
NEGATIVE=(35,187,203)


def prime_by_integer_divisors(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def is_square(n):
    return isqrt(n)**2==n


def original_norm_fibre(D):
    if D<=3 or D%4!=3:
        raise ValueError("D fundamental imaginary odd discriminant form requires D>3, D%4=3")
    m=(D+1)//4
    N=D+1
    R=isqrt(N)
    Y=isqrt(N//D)
    solutions=tuple(sorted(
        (x,y) for y in range(-Y,Y+1) for x in range(-R,R+1)
        if x*x+D*y*y==N
    ))
    expected={(-1,-1),(-1,1),(1,-1),(1,1)}
    if is_square(m):
        q=2*isqrt(m)
        expected|={(-q,0),(q,0)}
    assert set(solutions)==expected
    assert len(solutions)==4+2*is_square(m)
    assert len(solutions)%2==0
    assert all((-x,-y) in expected for x,y in expected)
    signed=set()
    for z in solutions:
        negative=(-z[0],-z[1])
        signed.add(min(z,negative))
    assert len(signed)==len(solutions)//2

    forms=independent_reduced_forms(D)
    h=len(forms)
    if D in H1:
        assert h==1
        assert prime_by_integer_divisors(m),(
            "class-one fundamental field composite m contradicts classical ideal argument",D,m)
        assert len(solutions)==4
    elif D in NEGATIVE:
        assert h>1
    return {
        "D":D,"m":m,
        "class_number_by_reduced_forms":h,
        "m_prime":prime_by_integer_divisors(m),
        "m_square":is_square(m),
        "m_composite_nonsquare":m>1 and not prime_by_integer_divisors(m) and not is_square(m),
        "exact_norm_Dplus1":N,
        "integer_solutions":solutions,
        "signed_generator_classes":len(signed),
        "all_four_nonrational_points_present":True,
        "extra_two_rational_if_and_only_if_m_square":True,
        "h1_implies_m_prime_tested_if_applicable":D in H1,
        "four_generator_fibre_not_h1_specific":True,
    }


def full_fibre_certificate():
    rows=[original_norm_fibre(D) for D in H1+NEGATIVE]
    byD={row["D"]:row for row in rows}
    assert len(rows)==9
    assert all(byD[D]["m_prime"] and len(byD[D]["integer_solutions"])==4 for D in H1)
    assert byD[187]["class_number_by_reduced_forms"]>1
    assert byD[187]["m_prime"] and len(byD[187]["integer_solutions"])==4
    assert byD[35]["m_square"] and len(byD[35]["integer_solutions"])==6
    assert byD[203]["m_composite_nonsquare"] and len(byD[203]["integer_solutions"])==4

    # An explicit proof witness at D35 that the rational branch cannot
    # be erased without the no-square hypothesis.
    assert (-6,0) in byD[35]["integer_solutions"]
    assert (6,0) in byD[35]["integer_solutions"]
    return {
        "all_fundamental_field_controls":rows,
        "h1_primality_is_classical_conditional_paper_argument":True,
        "six_vs_four_formula_independent_of_class_number":True,
        "not_a_class_number_one_detector":True,
        "no_uniform_new_Gram_valuation_claim":True,
    }


def main():
    print("PHASE317_EXACT_NORM_DPLUS1_FIBRE_PASS",
          full_fibre_certificate(),flush=True)


if __name__=="__main__":
    main()
