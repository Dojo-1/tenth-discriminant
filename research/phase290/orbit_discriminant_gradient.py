#!/usr/bin/env python3
"""Phase290-C: exact 37-dimensional inversion-orbit determinant gradient.

Preregistered at 8a11277 before code. Six original D563 ordinary-jet
rows, full old source and 74 outer points, no new p-adic mass claim.
"""
from noether_smith_wall import (
    D,LABELS,guard,params,gram,det,eval_ordinary,
    gram_direct,plus,eye,mm,symmetry,v_p
)
from primitive_wall_radical import det_poly,derivative

def orbit_partition(points):
    allpts=set(points)
    assert len(allpts)==74
    reps=sorted({min(q,(-q[0],-q[1])) for q in points})
    assert len(reps)==37
    orbits=[]
    seen=set()
    for q in reps:
        orbit=[q,(-q[0],-q[1])]
        assert orbit[0]!=orbit[1]
        assert all(v in allpts for v in orbit)
        assert not any(v in seen for v in orbit)
        orbits.append((q,orbit))
        seen.update(orbit)
    assert seen==allpts
    return orbits

def adjugate(A):
    n=len(A)
    assert n==6
    adj=[]
    for i in range(n):
        row=[]
        for j in range(n):
            # adj[i,j] is the (j,i) cofactor, over exact integers.
            M=[[A[r][c] for c in range(n) if c!=i]
               for r in range(n) if r!=j]
            row.append(((-1)**(i+j))*det(M))
        adj.append(row)
    dd=det(A)
    target=[[dd*x for x in row] for row in eye(n)]
    assert mm(A,adj)==target
    assert mm(adj,A)==target
    return adj

def trace_product(A,B):
    return sum(A[i][j]*B[j][i] for i in range(len(A))
               for j in range(len(A)))

def main():
    guard()
    rho,R,S,J,Q=params(D)
    assert (rho,R,S,J,len(Q))==(51,140,5,5,359)
    base=[z for z in Q if abs(z[1])<=1]
    outer=[z for z in Q if abs(z[1])==2]
    assert len(base)==285 and len(outer)==74
    G0=gram(D,base,J,LABELS)
    Delta=gram(D,outer,J,LABELS)
    Gplus=gram(D,Q,J,LABELS)
    assert plus(G0,Delta)==Gplus
    assert v_p(det(Gplus),5)==2 and v_p(det(Gplus),7)==1
    orbits=orbit_partition(outer)
    assert all(rho*rho>=4*D+q[0]*q[0] for q,_ in orbits)
    assert all(abs(q[0])<=18 and abs(q[1])==2 for q,_ in orbits)
    assert rho*rho<4*D+19*19

    sum_orbit=[[0]*6 for _ in range(6)]
    tangent=[]
    adj=adjugate(Gplus)
    pgrade=[(-1)**(r+s) for r,s in LABELS]
    for representative,orbit in orbits:
        E,W=eval_ordinary(orbit,J)
        symmetry(E,W,orbit,J)
        local=gram_direct(E,W)
        assert local==gram(D,orbit,J,LABELS)
        assert all(local[i][j]==0 for i in range(6)
                   for j in range(6) if pgrade[i]!=pgrade[j])
        sum_orbit=plus(sum_orbit,local)
        tangent.append((representative,trace_product(adj,local)))
    assert sum_orbit==Delta

    poly=det_poly(G0,Delta)
    fprime=derivative(poly,1)
    assert sum(x for _,x in tangent)==fprime
    assert fprime%5==4 and fprime%7==5
    assert poly[0]==det(G0) and sum(poly)==det(Gplus)
    assert all(Gplus[i][j]==0 for i in range(6)
               for j in range(6) if pgrade[i]!=pgrade[j])
    witnesses={}
    for p in (5,7):
        nonzero=[(q,value%p) for q,value in tangent if value%p]
        assert nonzero,("gradient vanished despite diagonal unit",p)
        q,der=nonzero[0]
        assert 4*D+q[0]*q[0]<=rho*rho
        witnesses[str(p)]={
            "nonzero_orbit_directions":len(nonzero),
            "total_orbit_directions":len(orbits),
            "first_lexicographic_unit_direction":[q[0],q[1]],
            "first_unit_partial_mod_p":der,
            "first_orbit_norm_micro_wall":4*D+q[0]*q[0],
            "diagonal_partial_sum_mod_p":fprime%p,
            "formal_simple_root_hensel_at_all_ones":True,
        }
    assert det([[1,1],[1,-1]])==-2
    print("PHASE290C_ORBIT_GRADIENT",{
        "D":D,"original_source_rows_unchanged":R*S,
        "actual_principal_rows_tested":len(LABELS),
        "old_Q":len(base),"new_orbit_points":len(outer),
        "central_inversion_orbits":len(orbits),
        "micro_wall_condition":"rho^2 >= 4D+x^2",
        "integer_orbit_gram_sum_equals_full_wall":True,
        "exact_adjugate_identity":True,
        "total_orbit_partials_equal_independent_Leibniz_derivative":True,
        "p5_p7_formal_local_hypersurface_witnesses":witnesses,
        "binary_no_half_projection":True,
        "not_full_700_row_or_actual_field_theorem":True,
    },flush=True)
    print("PASS Phase290-C 37-orbit source-exact prime-local discriminant gradient",flush=True)

if __name__=="__main__":
    main()
