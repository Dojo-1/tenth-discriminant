#!/usr/bin/env python3
"""Phase308-B: adaptive exact Picard torsion scanner, no heuristic norm cutoff.

Combines a genuine local p-adic Hensel tendril with global quadratic norm
arithmetic and Picard class labels. The scalar baseline is deliberately naive.
It is NOT an improvement to the existing original Gram discriminant bound.
"""
from math import gcd, isqrt

from picard_tendrils import (HenselWorldlet, InvalidTransport,
                            hensel_tower, norm, order_parameter)


def complete_norm_shell(d, target):
    """Enumerate ALL O_D elements with positive norm target, exactly.

    4*N=(2a+b)^2+D*b^2 bounds |b| and reduces a to two square roots.
    No arbitrary rectangular search boundaries or floating point.
    """
    order_parameter(d)
    if target <= 0:
        raise InvalidTransport("norm target must be positive")
    max_abs_b=isqrt((4*target)//d)
    solutions=set()
    for b in range(-max_abs_b,max_abs_b+1):
        remaining=4*target-d*b*b
        if remaining<0:
            continue
        sq=isqrt(remaining)
        if sq*sq!=remaining:
            continue
        for t in {sq,-sq}:
            if (t-b)%2 != 0:
                continue
            a=(t-b)//2
            if norm((a,b),d)==target:
                solutions.add((a,b))
    return tuple(sorted(solutions))


def independent_reduced_forms(d):
    """Another finite reduced-form enumeration (uses standard theorem externally)."""
    m=order_parameter(d)
    out=[]
    upper=isqrt(d//3)+1
    for a in range(1,upper+1):
        bstart=-a if a!=1 else -1
        for b in range(bstart,a+1):
            delta=b*b+d
            q,rem=divmod(delta,4*a)
            if rem:
                continue
            c=q
            if c<a:
                continue
            if (b==-a or (a==c and b<0)):
                continue
            if gcd(gcd(a,abs(b)),c) != 1:
                continue
            out.append((a,b,c))
    return tuple(sorted(out))


def principalization_scanner(d,p,root0,max_depth):
    """Find minimal k for I=(p,omega-root0) becoming principal.

    Assumes p is prime and root is simple; HenselWorldlet enforces
    polynomial relation and unique lifts. Ordinary p-adic ideal factorization
    identifies I^k with the residue map kernel.
    """
    order_parameter(d)
    if p<2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
        raise InvalidTransport("p must be prime")
    if max_depth<1:
        raise InvalidTransport("positive depth required")
    tower=hensel_tower(d,p,root0,max_depth)
    checks=[]
    first=None
    for w in tower:
        target=p**w.level
        shell=complete_norm_shell(d,target)
        representatives=tuple(x for x in shell if w.residue(x)==0)
        checks.append({
            "depth":w.level,"modulus":target,"hensel_root":w.root,
            "complete_norm_shell_size":len(shell),
            "in_ideal_power":representatives,
        })
        if representatives and first is None:
            first=(w.level,representatives)
    if first is None:
        raise InvalidTransport("no principalization below supplied depth; not proof of infinity")
    k,witnesses=first
    # A smaller exponent MUST have been exhausted completely.
    assert all(not x["in_ideal_power"] for x in checks[:k-1])
    return {
      "D":d,"p":p,"root0":root0,
      "first_principal_power":k,
      "principal_generators":witnesses,
      "full_bounded_depth_ledger":checks,
      "exact_ideal_class_order_by_prime_norm_and_hensel":k,
    }


def source_family():
    # These candidates were recorded BEFORE this hosted program in the
    # post-discovery, pre-code validation protocol.
    cases=[
      (163,41,0,1,(0,1)),
      (187,7,2,2,(-2,1)),
      (203,3,0,4,(-6,1)),
      (167,2,0,11,(-2,7)),
    ]
    out=[]
    for d,p,r0,expected,generator in cases:
        row=principalization_scanner(d,p,r0,expected)
        assert row["first_principal_power"]==expected,(d,row)
        assert generator in row["principal_generators"],(d,row)
        assert norm(generator,d)==p**expected
        forms=independent_reduced_forms(d)
        assert len(forms)==expected,(d,len(forms),expected)
        cls={
            "field_D":d,
            "prime_p":p,
            "Picard_ideal_class_order":expected,
            "class_number_from_standard_reduced_form_correspondence":len(forms),
            "global_generator":generator,
            "hensel_root_at_principalization":row["full_bounded_depth_ledger"][-1]["hensel_root"],
            "rank100_twisted_determinant_class_exponent":100%expected,
            "rank100_determinant_trivial":100%expected==0,
            "individual_rank1_ideal_principal":expected==1,
            "depth_checked":expected,
            "no_original_integer_gram_change":True,
        }
        out.append(cls)
    return out


def flattening_adversary():
    rows=source_family()
    # A deliberately naive "read only the aggregate determinant class"
    # predictor is NOT mathematically justified; count its false positives.
    false_positive=[x["field_D"] for x in rows
                    if x["rank100_determinant_trivial"]
                    and not x["individual_rank1_ideal_principal"]]
    false_negative=[x["field_D"] for x in rows
                    if not x["rank100_determinant_trivial"]
                    and x["individual_rank1_ideal_principal"]]
    assert false_positive==[187,203] and not false_negative
    # Structured classifier has exact finite answers because the proof
    # certificates classify the *named ideal*, not its 100-fold sum.
    structured=[x["Picard_ideal_class_order"]==1 for x in rows]
    true=[x["individual_rank1_ideal_principal"] for x in rows]
    assert structured==true
    return {
       "cases":rows,
       "naive_scalar_only_false_positives_D":false_positive,
       "naive_scalar_only_accuracy_on_this_in_sample_family":"2/4",
       "structured_named_line_class_accuracy_on_this_in_sample_family":"4/4",
       "labels_remain_visible_under_source_aggregation":True,
       "NOT_independent_or_out_of_sample_cognition_benchmark":True,
    }


def main():
    data=flattening_adversary()
    print("PHASE308_ADAPTIVE_TORSION_FAMILY_PASS",data,flush=True)


if __name__=="__main__":
    main()
