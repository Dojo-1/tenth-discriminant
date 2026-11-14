#!/usr/bin/env python3
"""Phase277: same-source D403 first-layer matched inert/split controls.

Original integer ordinary-Z jets of Z^r W^s; W fixed in differentiation.
D=403, rho=40, R=100, S=J=4, complete Q219; 400x1752 original E.
At p7 inert: extract ONCE the existing (Z^p-W)^k Frobenius row factor.
At p11 split: DO NOT divide by Frobenius powers.
Factorials j! are p-units since j<4<7,11.

Truncated Smith results and first-image pairing radicals are NOT full
primitive-pairing valuations. The companion script saturates the source.
"""
from math import comb
import numpy as np

D,R,S,J,RHO=403,100,4,4,40

def points():
    return [(x,y) for x in range(-RHO,RHO+1)
            for y in range(-RHO,RHO+1) if x*x+D*y*y<=RHO*RHO]

def pair_mul(a,b,mod):
    return np.array([(a[0]*b[0]-D*a[1]*b[1])%mod,
                     (a[0]*b[1]+a[1]*b[0])%mod],dtype=np.int64)

def pair_powers(q,maxexp,mod):
    n=len(q)
    real=np.asarray([z[0] for z in q],dtype=np.int64)%mod
    imag=np.asarray([z[1] for z in q],dtype=np.int64)%mod
    powers=np.zeros((maxexp+1,n,2),dtype=np.int64)
    powers[0,:,0]=1
    for e in range(1,maxexp+1):
        a=powers[e-1,:,0]
        b=powers[e-1,:,1]
        # Mod each product before multiplying by D; no int64 overflow at 11^9.
        u=(a*real)%mod
        v=(b*imag)%mod
        powers[e,:,0]=(u-D*v)%mod
        powers[e,:,1]=((a*imag)%mod+(b*real)%mod)%mod
    return powers

def gram_from_rows(C,p,weight_D=D):
    n,m=C.shape
    assert m%(2*J)==0
    weights=np.tile(np.array([2,2*weight_D],dtype=np.int64),m//2)%p
    return (C@((C*weights)%p).T)%p

def rank_mod(A,p):
    A=np.array(A%p,dtype=np.int64,copy=True)
    n,m=A.shape
    row=0
    for col in range(m):
        if row==n:break
        piv=np.flatnonzero(A[row:,col])
        if len(piv)==0:continue
        k=row+int(piv[0])
        if row!=k:A[[row,k]]=A[[k,row]]
        A[row]=(A[row]*pow(int(A[row,col]),-1,p))%p
        factors=A[row+1:,col].copy()
        nz=np.flatnonzero(factors)
        if len(nz):
            idx=nz+row+1
            A[idx]=(A[idx]-factors[nz,None]*A[row])%p
        row+=1
    return row

def falling(r,j):
    f=1
    for k in range(j):f*=r-k
    return f

def build(p,inert,precision=1):
    Q=points()
    assert len(Q)==219
    n=len(Q)
    maxk=min((R-1)//p,S-1) if inert else 0
    modulus=p**(maxk+precision)
    powers=pair_powers(Q,R-1,modulus)
    wpowers=powers[:S+maxk,:,:].copy()
    wpowers[:,:,1]*=-1
    wpowers%=modulus
    rows=np.zeros((R*S,J*n*2),dtype=np.int64)
    klist=[]
    for r in range(R):
      for s in range(S):
        k=min(r//p,S-1-s) if inert else 0
        klist.append(k)
        for j in range(J):
            v=np.zeros((n,2),dtype=np.int64)
            for i in range(k+1):
                a=r-p*k+p*i
                b=s+k-i
                if a<j:continue
                coeff=((-1)**(k-i))*comb(k,i)*falling(a,j)
                pair_a=powers[a-j]
                pair_b=wpowers[b]
                product=np.column_stack((
                    ((pair_a[:,0]*pair_b[:,0])%modulus-
                     D*((pair_a[:,1]*pair_b[:,1])%modulus))%modulus,
                    ((pair_a[:,0]*pair_b[:,1])%modulus+
                     (pair_a[:,1]*pair_b[:,0])%modulus)%modulus))
                v=(v+coeff*product)%modulus
            assert np.all((v%(p**k))==0),(p,r,s,j,k)
            rows[r*S+s,j*n*2:(j+1)*n*2]=((v//(p**k))%(p**precision)).reshape(-1)
    return rows,np.asarray(klist,dtype=np.int64),Q

def independent_source_oracle(p,inert,C2,Q):
    """Separate truncated dual-number product; not a human independent review."""
    from math import factorial
    chosen=[(0,0),(7,0),(14,1),(21,0),(49,0),(70,2),(99,0),(99,3)]
    inspected=0
    for r,s in chosen:
        k=min(r//p,S-1-s) if inert else 0
        mod=p**(k+2)
        powz=pair_powers(Q,max(r,p),mod)
        z=np.array([[x%mod,y%mod] for x,y in Q],dtype=np.int64)
        w=np.array([[x%mod,(-y)%mod] for x,y in Q],dtype=np.int64)
        def mulv(a,b):
            return np.column_stack((
                ((a[:,0]*b[:,0])%mod-D*((a[:,1]*b[:,1])%mod))%mod,
                ((a[:,0]*b[:,1])%mod+(a[:,1]*b[:,0])%mod)%mod))
        base=[(comb(r-p*k,j)*powz[r-p*k-j])%mod
              if j<=min(r-p*k,J-1) else np.zeros_like(z) for j in range(J)]
        u=[(powz[p]-w)%mod]+[(comb(p,j)*powz[p-j])%mod for j in range(1,J)]
        for _ in range(k):
            nxt=[]
            for j in range(J):
                acc=np.zeros_like(z)
                for i in range(j+1):acc=(acc+mulv(base[i],u[j-i]))%mod
                nxt.append(acc)
            base=nxt
        wpow=pair_powers(Q,s,mod)[s].copy()
        wpow[:,1]*=-1
        wpow%=mod
        for j in range(J):
            deriv=mulv(base[j],wpow)*factorial(j)%mod
            assert np.all((deriv%(p**k))==0)
            independent=(deriv//(p**k))%(p*p)
            got=C2[r*S+s,j*len(Q)*2:(j+1)*len(Q)*2].reshape((-1,2))
            assert np.array_equal(independent,got),(p,r,s,j,k)
            inspected+=len(Q)*2
    return inspected

def p2_smith(A,p,expected_r0):
    """Exact levels 0,1,>=2 over Z/p^2; final band is NOT exactly 2."""
    q=p*p
    A=np.array(A%q,dtype=np.int64,copy=True)
    n,m=A.shape
    k=0
    while k<n:
        hit=None
        for i in range(k,n):
            columns=np.flatnonzero(A[i,k:]%p)
            if len(columns):hit=(i,k+int(columns[0]));break
        if hit is None:break
        i,j=hit
        if i!=k:A[[i,k]]=A[[k,i]]
        if j!=k:A[:,[k,j]]=A[:,[j,k]]
        inv=pow(int(A[k,k]),-1,q)
        tail=A[k+1:,k]
        nz=np.flatnonzero(tail)
        if len(nz):
            rows=nz+k+1
            factors=(tail[nz]*inv)%q
            A[rows,k+1:]=(A[rows,k+1:]-factors[:,None]*A[k,k+1:])%q
            A[rows,k]=0
        k+=1
    assert k==expected_r0,(k,expected_r0)
    assert np.all((A[k:,k:]%p)==0)
    r1=rank_mod(A[k:,k:]//p,p) if k<n else 0
    assert 0<=r1<=n-k
    return {'0':k,'1':r1,'>=2':n-k-r1}

def smith_controls():
    for p in (7,11):
        A=np.diag([1,p,p*p,1]).astype(np.int64)
        a=p2_smith(A,p,2)
        assert a=={'0':2,'1':1,'>=2':1}
        B=A.copy()
        B[0]+=B[1]
        B[:,1]+=B[:,0]
        assert p2_smith(B,p,2)==a

def split_frobenius_counterexample(p):
    assert p==11
    for x,y in points():
        a=np.array([x%p,y%p],dtype=np.int64)
        z=np.array([1,0],dtype=np.int64)
        for _ in range(p):z=pair_mul(z,a,p)
        w=np.array([x%p,(-y)%p],dtype=np.int64)
        if np.any((z-w)%p):
            return (x,y),tuple(int(v) for v in ((z-w)%p))
    raise AssertionError('invalid split Frobenius division was not rejected')

def run():
    smith_controls()
    Q=points()
    assert len(Q)==219
    assert (-D)%7 not in {k*k%7 for k in range(7)}
    assert (-D)%11 in {k*k%11 for k in range(11)} and D%11!=0
    assert J-1<7 and J-1<11
    result={}
    expected={
        7: dict(F=530,evalrank=331,gramrank=305,
                smith={'0':331,'1':5,'>=2':64},index_lb=133,
                shallowrank=252),
        11:dict(F=0,evalrank=132,gramrank=132,
                smith={'0':132,'1':66,'>=2':202},index_lb=470,
                shallowrank=99)
    }
    for p,inert in [(7,True),(11,False)]:
        C,k,Q=build(p,inert,precision=2)
        assert C.shape==(400,1752)
        evalrank=rank_mod(C,p)
        controls=independent_source_oracle(p,inert,C,Q)
        smith=p2_smith(C,p,evalrank)
        H=gram_from_rows(C,p)
        gramrank=rank_mod(H,p)
        shallow_indices=[i for i in range(2*J*len(Q)) if i//(2*len(Q))<3]
        shallow_rank=rank_mod(C[:,shallow_indices],p)
        wrong_metric_rank=rank_mod(gram_from_rows(C,p,weight_D=1),p)
        want=expected[p]
        assert (int(np.sum(k)),evalrank,gramrank,smith,
                smith['1']+2*smith['>=2'],shallow_rank)==(
            want['F'],want['evalrank'],want['gramrank'],want['smith'],
            want['index_lb'],want['shallowrank'])
        if p==7:
            assert wrong_metric_rank==303 and wrong_metric_rank!=gramrank
        rperm=np.arange(len(C))[::-1]
        assert rank_mod(C[rperm],p)==evalrank
        assert rank_mod(H[np.ix_(rperm,rperm)],p)==gramrank
        result[p]=(int(np.sum(k)),int(np.count_nonzero(k)),evalrank,gramrank)
        print('SOURCE',dict(D=D,p=p,inert=inert,Q=len(Q),R=R,S=S,J=J,
              entries=C.size,known_frobenius_sum=result[p][0],
              eval_rank_mod_p=evalrank,eval_nullity=400-evalrank,
              normalized_gram_rank_mod_p=gramrank,
              first_image_pairing_radical=evalrank-gramrank,
              truncated_smith=smith,
              p2_additional_eval_index_lower=smith['1']+2*smith['>=2'],
              dual_oracle_coordinate_checks=controls,
              wrong_metric_gram_rank=wrong_metric_rank,
              omitted_j3_eval_rank=shallow_rank),flush=True)
    w=split_frobenius_counterexample(11)
    print('HOSTILE_SPLIT_FROBENIUS',w,flush=True)
    assert result[7][0]>0 and result[11][0]==0
    print('PASS Phase277 source-matched first-two local Smith layers',flush=True)

if __name__=='__main__':
    run()
