#!/usr/bin/env python3
"""Phase304-A: matched h1 / non-h1 maximal-order p5 Frobenius signature.

Preregistered 6bc1cfa4 BEFORE this implementation/results. Uses genuine
O_K half-integral (p,q) points, same norm<=441 and R40/J1; also
tests native source_probe params separately. Smith oracle frozen Phase303-F.
No false h1 inference or changed discriminant cutoff.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
for part in ("phase206","phase303","phase304"):
    sys.path.insert(0,str(ROOT/"research"/part))
from source_probe import params
from independent_half_integer_replay import independent_dvr_smith

P,K,MOD=5,16,5**16
D_LIST=(163,167,187)
FROZEN={
  "research/phase303/independent_half_integer_replay.py":
    "b6f2d242277f396538296c4ac061308cba03ff81",
  "research/phase206/source_probe.py":
    "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6"
}

def guard():
    for path,sha in FROZEN.items():
        actual=subprocess.check_output(
          ["git","rev-parse","HEAD:"+path],cwd=ROOT,text=True).strip()
        assert actual==sha,("frozen old helper changed",path,actual)

def mul(x,y,D):
    a,b=x;c,d=y
    u=a*c-D*b*d
    v=a*d+b*c
    assert u%2==0 and v%2==0
    return (u//2,v//2)

def norm4(x,D):
    a,b=x
    return a*a+D*b*b

def trace_hermitian(x,y,D):
    a,b=x;c,d=y
    q=a*c+D*b*d
    assert q%2==0
    return q//2

def norm_points(D,cut):
    assert D>0 and D%4==3
    m=4*cut
    radius=isqrt(m)
    q_bound=isqrt(m//D)
    Q=[]
    for q in range(-q_bound,q_bound+1):
        p_bound=isqrt(m-D*q*q)
        for p in range(-p_bound,p_bound+1):
            if (p-q)%2==0:
                Q.append((p,q))
    assert len(Q)==len(set(Q))
    assert all(norm4(z,D)<=m for z in Q)
    assert all(norm4((p,q_bound+1),D)>m
               for p in range(-radius,radius+1))
    even=[z for z in Q if z[1]%2==0]
    return Q,even

def power_grid(Q,D,R):
    grid=[]
    for z in Q:
        powers=[(2,0)]
        for r in range(1,R):
            powers.append(mul(powers[-1],z,D))
        grid.append(powers)
    return grid

def big_gram(grid,D,R):
    H=[[0]*R for _ in range(R)]
    for i in range(R):
        for j in range(i,R):
            q=sum(trace_hermitian(point[i],point[j],D)
                  for point in grid)
            H[i][j]=H[j][i]=q
    return H

def omega_pairing(x,y,D):
    a,b=x;c,d=y
    return 2*a*c+a*d+b*c+((D+1)//2)*b*d

def independent_omega_oracle(grid,H,D,R):
    # Standalone half-integral powers ALREADY constructed; now map
    # exact data into maximal-order omega coords and independently
    # contract with the Bomega bilinear form.
    om=[ [((p-q)//2,q) for p,q in line] for line in grid ]
    for i in range(R):
        for j in range(i,R):
            value=sum(omega_pairing(line[i],line[j],D)
                      for line in om)
            assert value==H[i][j],("cross-coordinate trace mismatch",D,i,j)
    return om

def mod5_rank(M):
    A=[[int(x)%P for x in line]for line in M]
    if not A:return 0
    rows,cols=len(A),len(A[0])
    r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        iv=pow(A[r][c],-1,P)
        A[r][c:]=[(x*iv)%P for x in A[r][c:]]
        for i in range(r+1,rows):
            mult=A[i][c]
            if mult:
                for j in range(c,cols):
                    A[i][j]=(A[i][j]-mult*A[r][j])%P
        r+=1
        if r==rows:break
    return r

def source_spectrum(Q,D,R,cut,arm,require_frobenius=True):
    assert R>=25
    grid=power_grid(Q,D,R)
    H=big_gram(grid,D,R)
    omega=independent_omega_oracle(grid,H,D,R)
    levels,profile=independent_dvr_smith(H)
    assert len(levels)==R and max(levels)<K
    residue={(int(z[0])%P,int(z[1])%P) for z in
             ((p-q)//2 for p,q in [])} if False else {
                (((p-q)//2)%P,q%P) for p,q in Q}
    Eval=[]
    for r in range(R):
        row=[]
        for line in omega:
            a,b=line[r]
            row.extend((a%P,b%P))
        Eval.append(row)
    erank=mod5_rank(Eval)
    grank=mod5_rank(H)
    raw={"D":D,"arm":arm,"cut":cut,"R":R,
         "original_jet_count":1,
         "full_maximal_Q":len(Q),
         "distinct_F25_residue_classes":len(residue),
         "F5_monomial_evaluation_rank":erank,
         "F5_Gram_rank":grank,
         "v5_det_original_Gram":sum(levels),
         "original_Gram_Smith_histogram":profile,
         "all_exact_big_integer_trace_Gram_cells_dual_basis_checked":R*R,
         "exact_Frobenius_divided_row_count":R-25,
         "sample_residue_multiplicity_mod5_histogram":
            dict(sorted(Counter(n%5 for n in
                  Counter((((p-q)//2)%5,q%5) for p,q in Q).values()).items()))}
    if require_frobenius:
        # Frobenius z^25=z for any residue in O_K/5=F25:
        # original row difference r vs r-24 divisible 5 in
        # *BOTH* integral maximal order coordinates.
        primitive=[]
        for r in range(R):
            row=[]
            for line in omega:
                a,b=line[r]
                if r>=25:
                    c,d=line[r-24]
                    assert (a-c)%5==(b-d)%5==0
                    row.extend((((a-c)//5)%5,((b-d)//5)%5))
                else:
                    row.extend((a%5,b%5))
            primitive.append(row)
        prim_eval_rank=mod5_rank(primitive)
        prim_gram=[[0]*R for _ in range(R)]
        for i in range(R):
            for j in range(i,R):
                p=0
                for k in range(0,len(primitive[i]),2):
                    x=(primitive[i][k],primitive[i][k+1])
                    y=(primitive[j][k],primitive[j][k+1])
                    p+=omega_pairing(x,y,D)
                prim_gram[i][j]=prim_gram[j][i]=p%P
        prim_rank=mod5_rank(prim_gram)
        top25=mod5_rank([row[:25] for row in prim_gram[:25]])
        raw.update({
          "actual_r25_to_last_F25_divisions_full_coordinate_checks":
             (R-25)*len(Q)*2,
          "primitive_evaluation_rank_mod5":prim_eval_rank,
          "primitive_Gram_rank_mod5":prim_rank,
          "primitive_top25_Gram_rank_mod5":top25,
          "Frobenius_unit_primitive_criterion_pass":
             prim_rank==R and top25==25,
        })
        if prim_rank==R and top25==25:
            assert profile=={0:25,2:R-25},(
              "Frobenius primitive unit proof vs Smith mismatch",
              D,R,profile)
            assert sum(levels)==2*(R-25)
    return raw

def h1_false_certificate(D):
    if D==163:
        assert (-D)%8==5
        return {"field_D":D,"h1_status":"classical h1 prior art",
                "all_small_prime_splits_blocked":True}
    if D==167:
        assert (-D)%8==1
        p=2
    elif D==187:
        p=7
        assert (-D)%7==2 and 2 in {x*x%7 for x in range(7)}
    else:raise ValueError(D)
    bound=(D+1)//4
    assert p<bound
    # Norm a²+ab+bound*b² = (a+b/2)²+D*b²/4.
    # For b!=0 minimal norm >= bound, for b0 square.
    assert all((a*a+a*b+bound*b*b)!=p
               for a in range(-20,21)for b in range(-3,4))
    return {"field_D":D,"h1_status":"PROVABLY false by split prime",
            "split_prime_that_must_be_principal_if_h1":p,
            "principal_prime_norm_lower_threshold":bound,
            "split_prime_norm_contradiction":True}

def root_hensel_to_common_unramified(D):
    if D==163:return {"D":D,"alpha":1,"modulus":MOD}
    # u_D↦alpha*u_163, alpha²*163≡D mod5^16.
    # Both -D nonresidues mod5. Unit ratio has square root.
    assert (-D)%P in (2,3)
    assert (-163)%P==2
    assert (163*4-D)%5==0
    alpha=2
    for k in range(1,K):
        old=P**k
        nxt=P**(k+1)
        roots=[alpha+d*old for d in range(P)
               if (163*(alpha+d*old)**2-D)%nxt==0]
        assert len(roots)==1
        alpha=roots[0]
    assert (163*alpha*alpha-D)%MOD==0
    inv4=pow(4,-1,MOD)
    for a in range(-2,3):
        for b in range(-2,3):
            left=(a*a+D*b*b)*inv4%MOD
            right=(a*a+163*(alpha*b)**2)*inv4%MOD
            assert left==right
    return {"field_D":D,"alpha_mod5pow16":alpha,
            "same_unramified_local_quadratic_algebra_at5":True,
            "norm_conjugation_transport_tested":25}

def main():
    guard()
    results=[]
    for D in D_LIST:
        assert D%4==3 and all(D%(q*q) for q in range(2,isqrt(D)+1))
        assert (-D)%5 in (2,3)
        field=h1_false_certificate(D)
        local=root_hensel_to_common_unramified(D)
        matched,even=norm_points(D,441)
        assert D!=163 or (len(matched),len(even))==(225,109)
        a=source_spectrum(matched,D,40,441,"matched_full")
        b=source_spectrum(even,D,40,441,"matched_even")
        if D==163:
            assert a["original_Gram_Smith_histogram"]=={0:25,2:15}
            assert b["original_Gram_Smith_histogram"]=={
                0:15,2:8,3:7,4:10}
            assert (a["v5_det_original_Gram"],
                    b["v5_det_original_Gram"])==(30,77)
            assert (a["Frobenius_unit_primitive_criterion_pass"],
                    b["Frobenius_unit_primitive_criterion_pass"])==(True,False)
        rho,R,S,J,Qold=params(D)
        assert S==J==1 and R in (40,41,46)
        native,native_even=norm_points(D,rho*rho)
        nat=source_spectrum(native,D,R,rho*rho,"native_full")
        assert D!=163 or (rho,R)==(21,40)
        same=a["original_Gram_Smith_histogram"]=={0:25,2:15}
        results.append({
           "field":field,"local_Z5_isometry":local,
           "fixed_norm441_same_R40_full":a,
           "fixed_norm441_even_suborder_control":b,
           "actual_original_params_policy":{
               "rho":rho,"R":R,"S":S,"J":J,
               "integer_order_Q":len(Qold)},
           "native_policy_actual_maximal_full":nat,
           "same_fixed_original_40row_signature_as_D163":same,
           "if_nonh1_and_same_signature_retires_class_number_specificity":
               D==163 or not same
        })
        print("PHASE304A_MATCHED_FIELD_RESULT",{
           "D":D,"h1_status":field["h1_status"],
           "local_Z5_iso":local,
           "matched_Q":len(matched),
           "matched_F5_Gram_rank":a["F5_Gram_rank"],
           "matched_smith":a["original_Gram_Smith_histogram"],
           "matched_v5":a["v5_det_original_Gram"],
           "matched_Frobenius_primitive_unit":
             a["Frobenius_unit_primitive_criterion_pass"],
           "native_R":R,
           "native_full_Smith":nat["original_Gram_Smith_histogram"],
           "native_full_v5":nat["v5_det_original_Gram"],
           "same_class_one_signature":same
        },flush=True)
    controls=[x for x in results if x["field"]["field_D"]!=163]
    source_nonh1_same=[x["field"]["field_D"] for x in controls
                      if x["same_fixed_original_40row_signature_as_D163"]]
    print("PHASE304A_CLASS_ONE_SIGNATURE_FALSIFICATION_GATE",{
       "predeclared_fixed_fields":list(D_LIST),
       "actual_163_h1_control":results[0]["field"],
       "provably_nonh1_controls":[x["field"]for x in controls],
       "nonh1_fields_with_exact_h1_D163_Gram_signature":
           source_nonh1_same,
       "retire_naive_p5_Gram_signature_characterizes_h1":
           bool(source_nonh1_same),
       "if_no_match_does_not_establish_class_number_sufficiency":True,
       "same_p5_local_algebra_not_same_finite_source":True,
       "no_original_field_discriminant_bound_change":True,
       "all_exact_source_results":results
    },flush=True)
    print("PASS Phase304-A matched genuine maximal orders h1 vs non-h1 controls",flush=True)

if __name__=="__main__":
    main()
