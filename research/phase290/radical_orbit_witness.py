#!/usr/bin/env python3
"""Phase290-D: local radical witness for each source orbit, no full adjugate needed.

Preregistered at ffac6a9 AFTER Phase290-C observed data.
All 700 original rows stay fixed; only six frozen principal rows tested.
"""
from noether_smith_wall import (
    D,LABELS,guard,params,gram,det,eval_ordinary,v_p
)
from primitive_wall_radical import primitive_kernel,rref
from orbit_discriminant_gradient import orbit_partition,adjugate,trace_product

def cofactor_ii(G,i):
    return det([[G[r][c] for c in range(len(G)) if c!=i]
                for r in range(len(G)) if r!=i])

def orbit_null_self_pairing(E,weights,v,p):
    assert len(E)==len(v)
    local=[sum(v[i]*E[i][c] for i in range(len(v)))
           for c in range(len(weights))]
    return sum(w*x*x for w,x in zip(weights,local))%p

def main():
    guard()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(51,140,5,5,359)
    added=[z for z in Q if abs(z[1])==2]
    assert len(added)==74
    orbits=orbit_partition(added)
    assert len(orbits)==37
    G=gram(D,Q,J,LABELS)
    adj=adjugate(G)
    parity=[(-1)**(r+s) for r,s in LABELS]
    observations={}
    for p,count,expected_kernel,expected_unit in (
            (5,37,[0,2,0,0,0,1],1),
            (7,32,[4,0,1,0,1,0],2)):
        _,pivots,okay=rref(G,[0]*len(G),p)
        assert okay and len(pivots)==len(G)-1
        v=primitive_kernel(G,p)
        assert v==expected_kernel
        assert all(sum(g*u for g,u in zip(row,v))%p==0 for row in G)
        assert len({parity[i] for i,u in enumerate(v) if u%p})==1
        index=next(i for i,u in enumerate(v) if u%p)
        gam=(cofactor_ii(G,index)*pow(v[index]*v[index],-1,p))%p
        assert gam!=0
        assert all(adj[i][j]%p==(gam*v[i]*v[j])%p
                   for i in range(len(G)) for j in range(len(G)))
        active=[]
        for representative,orbit in orbits:
            E,W=eval_ordinary(orbit,J)
            q=orbit_null_self_pairing(E,W,v,p)
            local=gram(D,orbit,J,LABELS)
            d=trace_product(adj,local)%p
            assert d==(gam*q)%p
            if q:active.append((representative,d))
        assert len(active)==count
        assert active[0][0]==(-18,-2) and active[0][1]==expected_unit
        observations[str(p)]={
            "primitive_null_vector":v,
            "kernel_row_parity":next(parity[i] for i,x in enumerate(v) if x%p),
            "rank_one_adjugate_scalar_mod_p":gam,
            "unit_source_orbit_witnesses":len(active),
            "all_orbits":len(orbits),
            "first_unit_source_orbit":[-18,-2],
            "first_full_adjugate_derivative_mod_p":active[0][1],
            "all_orbit_derivatives_replayed_without_orbit_adjugates":True,
        }
    assert v_p(det(G),5)==2 and v_p(det(G),7)==1
    print("PHASE290D_LOCAL_RADICAL_ORBIT_WITNESS",{
      "D":D,"actual_source_Q":len(Q),
      "original_unchanged_row_count":R*S,
      "principal_rows_tested":len(LABELS),
      "original_jets_preserved":J,
      "orbit_count":len(orbits),
      "p_local_source_evaluation_bilinear_witnesses":observations,
      "no_full_700_by_700_adjugate_or_prime_mass_added":True
    },flush=True)
    print("PASS Phase290-D rank-one mod-p radical witness on all 37 orbits",flush=True)

if __name__=="__main__":
    main()
