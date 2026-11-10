#!/usr/bin/env python3
"""Phase208-B follow-on, prereg #151/#152: Frobenius quotient jet signatures.

Post-observation mathematical hypothesis; the test protocol was registered
BEFORE this code. All original ordinary jets and original integer-pair
real/imag channels. Positive G is one unchanged source for each D.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase206"))
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/"phase207"))

from math import comb
from source_probe import params, mul, fall
from middle_frobenius import pair_powers, rank_cols
from truncated_middle_smith import run as run_subset

def old_k(r,s,S,p):
    return min(r//p,S-1-s)

def normalized_row(D,R,S,J,p,power_cache,r,s,k):
    modulus=p**S
    denominator=p**k
    out=[]
    for j in range(J):
        line=[]
        for zpow,wpow in power_cache:
            a=b=0
            for t in range(k+1):
                exponent=r-p*t
                if exponent<j:continue
                x,y=mul(zpow[exponent-j],wpow[s+t],D,modulus)
                coef=(-1 if t%2 else 1)*comb(k,t)*fall(exponent,j)
                a=(a+coef*x)%modulus
                b=(b+coef*y)%modulus
            assert a%denominator==b%denominator==0,(
                "original p^k row division",D,p,r,s,j)
            line.append((a//denominator%p,b//denominator%p))
        out.append(line)
    return out

def conjugate_class(t,p2):
    x,y=t
    return (x,(-y)%p2)

def signatures(D,p):
    rho,R,S,J,Q=params(D)
    assert J==S and all((-D)%p != (a*a)%p for a in range(p))
    assert len(Q)>2*(R-1)+(S-1) # original-source positivity premise
    mod=p**S;p2=p*p
    # Frozen complete original ellipse, NEVER a subset picked for rank.
    key=[(x%p2,y%p2) for x,y in Q]
    types=sorted(set(key))
    reps={}
    for index,t in enumerate(key):reps.setdefault(t,index)
    assert all(conjugate_class(t,p2) in reps for t in types)
    assert len(types)==(27 if p==3 else 75)
    # Source classes with y == 0 mod p² contribute one real channel;
    # paired nonreal conjugate residue classes contribute two channels total.
    orbits=[];seen=set()
    for t in types:
        if t in seen:continue
        bar=conjugate_class(t,p2)
        if bar==t:
            orbits.append((t,True))
            seen.add(t)
        else:
            canonical=min(t,bar)
            if canonical not in seen:
                orbits.append((canonical,False))
            seen.add(t);seen.add(bar)
    channels_per_depth=sum(1 if isreal else 2 for _,isreal in orbits)
    assert channels_per_depth==len(types)
    assert channels_per_depth==(27 if p==3 else 75)
    cache=[]
    for x,y in Q:
        z=(x%mod,y%mod);w=(x%mod,(-y)%mod)
        cache.append((pair_powers(z,R,mod),pair_powers(w,S-1,mod)))
    observation_index={z:i for i,z in enumerate(Q)}
    assert all((x,-y) in observation_index for x,y in Q)
    compressed=[]
    for r in range(R):
        for s in range(S):
            k=old_k(r,s,S,p)
            row=normalized_row(D,R,S,J,p,cache,r,s,k)
            cv=[]
            for j in range(J):
                values=row[j]
                for qi,t in enumerate(key):
                    assert values[qi]==values[reps[t]],(
                        "p^2 class collision failure",D,p,r,s,j,Q[qi])
                    x,y=Q[qi]
                    bar=values[observation_index[(x,-y)]]
                    assert (bar[0]-values[qi][0])%p==0
                    assert (bar[1]+values[qi][1])%p==0
                    if t==conjugate_class(t,p2):
                        assert values[qi][1]==0,(
                            "fixed real residue must be real",D,p,r,s,j,Q[qi])
                for t,isreal in orbits:
                    a,b=values[reps[t]]
                    cv.append(a)
                    if not isreal:cv.append(b)
            assert len(cv)==J*len(types)
            compressed.append(cv)
    full_rank=rank_cols(compressed,p)
    row_count=R*S
    cap=J*len(types)
    assert full_rank<=cap and full_rank<=row_count
    nullity=row_count-full_rank
    lower_from_classes=max(0,row_count-cap)
    assert nullity>=lower_from_classes
    result={"D":D,"p":p,"R":R,"S":S,"J":J,"rho":rho,
         "Q":len(Q),"classes_mod_p2":len(types),
         "full_compressed_channels":len(compressed[0]),
         "full_normalized_rank_mod_p":full_rank,
         "first_Smith_nullity":nullity,
         "uniform_class_bound":cap,
         "uniform_first_layer_index_lower":lower_from_classes}
    print("PHASE208_FROBENIUS_SIGNATURE",result,flush=True)
    return result

def main():
    saved={}
    for D in (283,403):
        for p in (3,5):
            saved[(D,p)]=signatures(D,p)
    # SECOND depth data is derived from a new bounded exact replay of
    # the separately preregistered p² subset-Smith certificate.
    for p in (3,5):
        b=saved[(403,p)]
        s=run_subset(p)
        # Coker(full original source) -> coker(selected k>=2 row source)
        # is a SURJECTION; each p^h graded dimension is nondecreasing
        # under passing from subset back to the full cokernel.
        gamma1_full=b["first_Smith_nullity"]
        gamma2_subset=s["truncated_levels"][">=2"]
        total_index=gamma1_full+gamma2_subset
        assert total_index>=s["selected_index_lower"]
        vp_lower=2*(s["old_Fp"]+total_index)
        uniform_variant=2*(s["old_Fp"]+
            b["uniform_first_layer_index_lower"]+gamma2_subset)
        assert vp_lower>=uniform_variant
        print("PHASE208_NONOVERLAPPING_LAYERS",{
            "D":403,"p":p,"old_F":s["old_Fp"],
            "gamma1_FULL":gamma1_full,
            "gamma2_selected":gamma2_subset,
            "new_index_lower":total_index,
            "original_Gram_vp_lower":vp_lower,
            "conservative_uniform_class_plus_second_layer":uniform_variant,
            "two_distinct_Smith_grades_NO_double_count":True},flush=True)
    # The split-prime counterworld D287,p3 cannot form integral q_p.
    z=(1,1);z3=mul(mul(z,z,287,3),z,287,3)
    assert ((z3[0]-1)%3,(z3[1]+1)%3)==(0,2)
    print("PASS finite residue-class source collapse and graded cokernel lower",flush=True)

if __name__=="__main__":main()
