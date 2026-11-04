#!/usr/bin/env python3
"""Phase204-A prereg #136: full truncated local Smith profile, not det scalar."""
from ordinary_jet_filtration import gram

def profile(M,p,e=2):
    a=[[x%(p**e) for x in row] for row in M]
    lev=0;result=[]
    while a:
        q=p**(e-lev);n=len(a)
        hit=next(((i,j) for i in range(n) for j in range(n)
                  if a[i][j]%p),None)
        if hit is None:
            if lev==e-1:
                result.extend([e]*n);break
            assert all(x%p==0 for row in a for x in row)
            a=[[x//p for x in row] for row in a]
            lev+=1;continue
        i,j=hit;a[0],a[i]=a[i],a[0]
        for row in a:row[0],row[j]=row[j],row[0]
        inv=pow(a[0][0],-1,q)
        a=[[(a[r][s]-a[r][0]*inv*a[0][s])%q for s in range(1,n)]
           for r in range(1,n)]
        result.append(lev)
    return result

def controls(p,D):
    Q=[(0,0),(1,0),(1,1)];R=p+2;S=2
    low=gram(Q,D,R,S,p);full=gram(Q,D,R,S,p+2)
    assert all((a-b)%(p*p)==0 for x,y in zip(low,full)
               for a,b in zip(x,y))
    x=profile(low,p);y=profile(full,p)
    assert x==y and len(x)==R*S
    shifted=full[:]
    shifted=[row[:] for row in full]
    shifted[0]=[(a+b) for a,b in zip(shifted[0],shifted[1])]
    assert profile(shifted,p)==x
    transposed=[list(t) for t in zip(*full)]
    assert profile(transposed,p)==x
    print("LOCAL_SMITH",{"p":p,"D":D,"N":R*S,
          "truncated_exponents":x,
          "rank_mod_p":x.count(0),"rank_mod_p2_units":x.count(0),
          "same_after_depth_increment":True,
          "row_shear_and_transpose_invariant":True})
def main():
    controls(3,7);controls(5,3)
    a=profile([[1,0],[0,25]],5)
    b=profile([[5,0],[0,5]],5)
    assert a==[0,2] and b==[1,1] and a!=b
    print("NEGATIVE_EQUAL_DET",{"det":25,"profiles":[a,b]})
    print("PASS vector-valued local Smith filtration controls")
if __name__=="__main__":main()
