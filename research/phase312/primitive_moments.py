#!/usr/bin/env python3
"""Phase312: reconstruct the true D203 50-divided primitive source from
residue z plus epsilon(z)=(z^5-conjugate(z))/5 modulo5, THEN compress its
entire Hermitian trace Gram through 3x3 moments in each of 25 residue bins.

Nothing is inferred from residue counts ALONE about primitive lifts.
Original ordinary Z jets hold W fixed; this is crucial for K_a derivatives.
"""
from collections import defaultdict
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
for p in ("phase304","phase307","phase311","phase312"):
    sys.path.insert(0,str(ROOT/"research"/p))
import highjet_d203_original as pilot
from source_saturation import original_fifty_row_saturation
from inert_trace_radicals import rank_f5
from fermat_lift import epsilon,eta,conjugate,mul,add,scale,sub,power

D=203;P=5;R=50;S=J=2;N=100


def field_matmul(Aa,Ab,Ba,Bb):
    """Matrix product over O_D/5O_D=F25 using omega^2=omega-51."""
    m=(D+1)//4
    return ((Aa@Ba-m*(Ab@Bb))%5,
            (Aa@Bb+Ab@Ba+Ab@Bb)%5)


def residue_jet_coefficients(z):
    """For each jet and source row, three F25 coefficients of
    (1, epsilon, conjugate(epsilon)). Shape: (2,100,3,2).
    """
    z=(z[0]%5,z[1]%5)
    w=conjugate(z,5)
    zp=[(1,0)]
    for k in range(1,55):
        zp.append(mul(zp[-1],z,D,5))
    coeff=np.zeros((J,N,3,2),dtype=np.int64)
    def put(j,i,k,value):
        coeff[j,i,k]=tuple(int(t)%5 for t in value)
    for r in range(R):
      for s in range(S):
        i=2*r+s
        if s==0 and r>=5:
            # (Z^r-Z^(r-5)W)/5.
            put(0,i,1,zp[r-5])
            put(1,i,0,zp[r-1])
            if r>5:
                put(1,i,1,scale(r-5,zp[r-6],5))
        elif s==1 and r>=45:
            # (Z^(45+a) W-2Z^(26+a)+Z^(2+a))/5.
            a=r-45
            put(0,i,1,scale(-1,zp[45+a],5))
            put(1,i,0,scale(-1,zp[49+a],5))
            put(1,i,1,scale(-a,zp[44+a],5))
            put(1,i,2,scale(-2,zp[a],5))
        else:
            v=zp[r]
            if s==1:v=mul(v,w,D,5)
            put(0,i,0,v)
            if r>0:
                v=zp[r-1]
                if s==1:v=mul(v,w,D,5)
                put(1,i,0,scale(r,v,5))
    return coeff


def feature(z):
    e=epsilon(z,D)
    assert eta(z,D)==conjugate(e,5)
    return ((1,0),e,conjugate(e,5))


def field_dot(coeff,features):
    out=(0,0)
    for c,u in zip(coeff,features):
        out=add(out,mul(tuple(int(x) for x in c),u,D,5),5)
    return out


def moments_for_class(points):
    """M=sum u u^* where u=[1,epsilon,bar(epsilon)] column."""
    U=np.asarray([feature(z) for z in points],dtype=np.int64)
    a,b=U[:,:,0],U[:,:,1]
    abar,bbar=(a+b)%5,(-b)%5
    Ma,Mb=field_matmul(a.T,b.T,abar,bbar)
    assert Ma.shape==Mb.shape==(3,3)
    # Hermitian: M^* = M (this does NOT imply all entries are F5).
    assert np.array_equal(Ma,(Ma+Mb).T%5)
    assert np.array_equal(Mb,(-Mb).T%5)
    return Ma,Mb


def primitive_moment_certificate():
    pilot.guard()
    rho,r,s,j,_=pilot.params(D)
    assert (rho,r,s,j)==(24,R,S,J)
    q=tuple(pilot.qmax(rho))
    assert len(q)==263
    E=pilot.evaluate_original_jets(q,R,S,J,25)
    assert E.shape==(100,1052)
    changed,prim,selected=original_fifty_row_saturation(E)
    assert len(selected)==50
    original_prim=np.asarray(prim,dtype=np.int64)%5

    bins=defaultdict(list)
    for z in q:bins[(z[0]%5,z[1]%5)].append(z)
    assert len(bins)==25

    coeffs={z:residue_jet_coefficients(z) for z in bins}
    checked=0
    for qi,z in enumerate(q):
        c=coeffs[(z[0]%5,z[1]%5)]
        u=feature(z)
        for jet in range(J):
            col=2*(jet*len(q)+qi)
            for i in range(N):
                pred=field_dot(c[jet,i],u)
                got=tuple(original_prim[i,col:col+2])
                assert pred==got,(
                    "Fermat-quotient primitive jet prediction failed",
                    i,jet,z,pred,got)
                checked+=2
    assert checked==105200

    # Full primitive Gram by independent untouched source metric oracle.
    direct=pilot.original_trace_gram(original_prim,len(q),J,5)
    assert direct.shape==(N,N)
    sums_a=np.zeros((N,N),dtype=np.int64)
    sums_b=np.zeros((N,N),dtype=np.int64)
    class_moments={}
    for z,points in sorted(bins.items()):
        Ma,Mb=moments_for_class(points)
        class_moments[z]=(Ma,Mb)
        C=coeffs[z]
        for jet in range(J):
            Aa,Ab=C[jet,:,:,0],C[jet,:,:,1]
            Ta,Tb=field_matmul(Aa,Ab,Ma,Mb)
            # Conjugate transpose of the polynomial coefficient matrix.
            Ba,Bb=(Aa+Ab).T%5,(-Ab).T%5
            Ha,Hb=field_matmul(Ta,Tb,Ba,Bb)
            sums_a=(sums_a+Ha)%5
            sums_b=(sums_b+Hb)%5

    assert not np.any(sums_b),(
        "full conjugation-closed primitive moment matrix not F5-fixed")
    compressed=(2*sums_a)%5
    assert np.array_equal(compressed,direct),(
        "higher-lift moment compression differs from ORIGINAL primitive Gram")
    assert rank_f5(direct)==63

    # Conjugation transports the moment tensor after swapping epsilon
    # and conjugate(epsilon) feature channels.
    swap=[0,2,1]
    conjugate_pairs=0
    for z,(Ma,Mb) in class_moments.items():
        zz=conjugate(z,5)
        Ca,Cb=class_moments[zz]
        assert np.array_equal(Ca,(Ma+Mb)[np.ix_(swap,swap)]%5)
        assert np.array_equal(Cb,(-Mb)[np.ix_(swap,swap)]%5)
        conjugate_pairs+=1

    # A genuine original observation pair with equal mod5 residue but
    # different first Fermat-quotient layer. Both belong to Q263.
    assert (1,0) in q and (6,0) in q
    assert (1%5,0)==(6%5,0)
    assert epsilon((1,0),D)==(0,0)
    assert epsilon((6,0),D)==(4,0)
    F5row=2*5
    jet0=lambda z:original_prim[F5row,2*q.index(z):2*q.index(z)+2]
    assert tuple(jet0((1,0)))==(0,0)
    assert tuple(jet0((6,0)))==(4,0)

    return {
      "original_D":D,"original_Q":len(q),
      "same_original_source_shape":list(E.shape),
      "source_rows_p_divided":len(selected),
      "all_primitive_value_and_ordinary_jet_omega_coordinates_reconstructed":checked,
      "actual_F25_residue_bins":len(bins),
      "hermitian_3x3_moment_matrices":len(class_moments),
      "moment_primitive_Gram_cells_checked":int(direct.size),
      "primitive_Gram_rank_F5":rank_f5(compressed),
      "Fermat_feature_moments":["n","sum_eps","sum_conj_eps",
                                "sum_eps_squared","sum_conj_eps_squared",
                                "sum_eps_times_conj_eps"],
      "conjugation_moment_tensor_relations_checked":conjugate_pairs,
      "same_residue_1_and_6_distinct_primitive_F5row":True,
      "primitive_finite_radical_still_needs_higher_5adic_digits_for_exact_v5":True,
      "no_uniform_class_number_one_claim":True
    }


def main():
    print("PHASE312_PRIMITIVE_FERMAT_MOMENT_PASS",
          primitive_moment_certificate(),flush=True)

if __name__=="__main__":
    main()
