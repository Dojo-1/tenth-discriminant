"""Phase390: bounded INDEPENDENT-STRUCTURE reconstruction of Phase360's source.

Pure integer arithmetic; does not import the Lean Gram implementation.
Two computations of each W-fixed ordinary derivative:
  source chart x+y*sqrt(-D), Z[sqrt(-D)] and
  maximal chart u+v*omega, omega=(1+sqrt(-D))/2, omega^2=omega-c.

The physical sample set is held fixed under T(x,y)=(x-y,2y).
Replacing it with ALL maximal-order samples is a deliberately killed
representation change, not a legitimate coordinate transformation.
This does NOT prove the large-D odd-prime Gram valuations or field bound.
"""
from math import isqrt

def mul_source(D,a,b):
    return (a[0]*b[0]-D*a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def mul_max(D,a,b):
    c=(D+1)//4
    return (a[0]*b[0]-c*a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]+a[1]*b[1])

def power(mul,D,z,n):
    x=(1,0)
    for _ in range(n):x=mul(D,x,z)
    return x

def falling(r,j):
    z=1
    for i in range(j):z*=r-i
    return z

def derivative(D,r,s,j,z,kind):
    if j>r:return (0,0)
    if kind=="source":
        mul=mul_source
        conjugate=(z[0],-z[1])
    elif kind=="maximal":
        mul=mul_max
        conjugate=(z[0]+z[1],-z[1])
    else:raise ValueError("unknown chart")
    a=power(mul,D,z,r-j)
    b=power(mul,D,conjugate,s)
    x=mul(D,a,b);f=falling(r,j)
    return(f*x[0],f*x[1])

def trace(D,a,b,kind):
    if kind=="source":
        return 2*(a[0]*b[0]+D*a[1]*b[1])
    if kind=="maximal":
        return (2*a[0]*b[0]+a[0]*b[1]+a[1]*b[0]
                +((D+1)//2)*a[1]*b[1])
    raise ValueError("unknown chart")

def source_points(D,radius):
    output=[]
    ymax=isqrt(radius*radius//D)
    for y in range(-ymax,ymax+1):
        xmax=isqrt(radius*radius-D*y*y)
        output.extend((x,y) for x in range(-xmax,xmax+1))
    return output

def maximal_points(D,radius):
    assert D%4==3
    c=(D+1)//4
    output=[]
    vmax=isqrt(4*radius*radius//D)
    for v in range(-vmax,vmax+1):
        h=4*radius*radius-D*v*v
        for u in range((-isqrt(h)-v)//2-1,
                       (isqrt(h)-v)//2+2):
            if u*u+u*v+c*v*v<=radius*radius:
                output.append((u,v))
    return output

def chart(xy):
    x,y=xy
    return(x-y,2*y)

def gram(D,R,S,J,points,kind):
    assert D>0 and D%4==3
    rows=[(r,s) for r in range(R) for s in range(S)]
    n=len(rows)
    out=[[0]*n for _ in range(n)]
    for j in range(J):
        for z in points:
            a=[derivative(D,r,s,j,z,kind) for r,s in rows]
            for i in range(n):
                for k in range(i,n):
                    out[i][k]+=trace(D,a[i],a[k],kind)
    for i in range(n):
        for k in range(i):out[i][k]=out[k][i]
    return out

def det_bareiss(A):
    a=[r[:] for r in A];n=len(a)
    if not n:return 1
    sign=1;prev=1
    for k in range(n-1):
        if not a[k][k]:
            for i in range(k+1,n):
                if a[i][k]:
                    a[k],a[i]=a[i],a[k]
                    sign=-sign
                    break
            else:return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def full_gram_chart_test(D,rho,R=3,S=2,J=2):
    original=source_points(D,rho)
    same=[chart(z) for z in original]
    all_maximal=maximal_points(D,rho)
    assert set(same)<set(all_maximal)
    g=gram(D,R,S,J,original,"source")
    mapped=gram(D,R,S,J,same,"maximal")
    substituted=gram(D,R,S,J,all_maximal,"maximal")
    assert g==mapped
    assert g!=substituted
    for z in original:
        for r in range(R):
            for s in range(S):
                for j in range(J):
                    a=derivative(D,r,s,j,z,"source")
                    b=derivative(D,r,s,j,chart(z),"maximal")
                    assert chart(a)==b
    return {"D":D,"rho":rho,"points_source":len(original),
            "points_full_order":len(all_maximal),
            "original_det":det_bareiss(g),
            "substituted_det":det_bareiss(substituted),
            "same_physical_samples_equal":True,
            "enlarged_source_changes_gram":True}

def exact_ellipse_count_at_fourth_root(t):
    D=t**4;R=D//4;S=R//25
    rho=(11*t**3+24)//25
    n=len(source_points(D,rho)) if rho<1000 else 0
    # Slice the enormous source without constructing billions of points.
    ymax=isqrt(rho*rho//D)
    n=sum(2*isqrt(rho*rho-D*y*y)+1 for y in range(-ymax,ymax+1))
    need=2*(R-1)+(S-1)
    return {"root":t,"D":D,"R":R,"S":S,"thin_radius":rho,
            "original_ellipse_points":n,
            "interpolation_requirement":need,"strict_margin":n-need}

def prime(n):
    return n>=2 and all(n%p for p in range(2,isqrt(n)+1))

def strict_prime_boundary(D):
    """Prime c=(D+1)/4 is NOT inert, because omega has norm c.

    The polynomial X^2-X+c has distinct roots 0 and 1 modulo c.
    A strict p<c cutoff is essential; equality can be split.
    """
    c=(D+1)//4
    assert prime(c) and D==4*c-1
    norm=lambda u,v:u*u+u*v+c*v*v
    assert norm(0,1)==c
    assert (0*0-0+c)%c==(1*1-1+c)%c==0
    return {"D":D,"boundary_prime":c,"boundary_split":True,
            "p_less_than_c_cannot_be_replaced_with_p_le_c":True}

def valuation(n,p):
    if n==0:raise ValueError("zero has no finite p-adic valuation")
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v

def predicted_binary_exponent(R,S):
    # Phase331 simultaneous row-frame exponent, not two products.
    return R*S+2*(S*sum(r//4 for r in range(R))
                   +R*sum(s//4 for s in range(S)))

def predicted_local_odd_exponent(R,S,p):
    # Phase323 valuationWeight plus ONE selected horizontal p^2 gain.
    vertical=sum(min(r//p,s)for r in range(R)for s in range(S))
    horizontal=R*sum(s//(p*p) for s in range(S)) if p in (3,5,7,11,13,17,19,23,29,31,37,41) else 0
    return 2*(vertical+horizontal)

def local_source_valuation_pilot():
    D=163;rho=18;R=S=J=6
    Q=source_points(D,rho)
    original=gram(D,R,S,J,Q,"source")
    transported=gram(D,R,S,J,[chart(z)for z in Q],"maximal")
    assert original==transported
    det=det_bareiss(original)
    if det<=0:raise AssertionError("not a positive full trace Gram")
    actual={p:valuation(det,p)for p in (2,3,5)}
    required={2:predicted_binary_exponent(R,S),
              3:predicted_local_odd_exponent(R,S,3),
              5:predicted_local_odd_exponent(R,S,5)}
    assert required=={2:84,3:30,5:10}
    assert actual=={2:216,3:36,5:21}
    assert all(actual[p]>=required[p]for p in required)
    return {"D":D,"R":R,"S":S,"J":J,"rho":rho,"Q_cardinality":len(Q),
            "actual_valuations":actual,"theorem_required_exponents":required,
            "scope":"FINITE_NONVACUOUS_ORIGINAL_GRAM_ONLY"}

def run():
    examples=((3,4),(7,5),(11,6),(19,7),(43,8),(163,15))
    data=[full_gram_chart_test(D,rho) for D,rho in examples]
    controls=[strict_prime_boundary(D) for D in (7,11,19,43,67,163)]
    counts=[exact_ellipse_count_at_fourth_root(t) for t in (301,302)]
    pilot=local_source_valuation_pilot()
    return {"local_matched_valuation_pilot":pilot,"commit_under_audit":"e720d2679e9292e101a39afd8f1b7720863e42f5",
            "status":"BOUNDED_EXACT_ARITHMETIC_NOT_AN_INDEPENDENT_FIELD_PROOF",
            "source_chart_oracles":data,"strict_prime_cutoff_controls":controls,
            "exact_endpoint_ellipse_counts":counts,
            "unresolved":"Production p-adic source valuation and field-semantic review"}

if __name__=="__main__":
    import json
    print(json.dumps(run(),indent=2))
