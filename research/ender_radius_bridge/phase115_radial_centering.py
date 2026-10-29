"""ONE sealed exact check of the monic radial basis; not a Lean/cutoff proof."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, math, subprocess
BASE='47563334e5374f15d490ece98a7ed1184a6822cd'
COHORTS=((1,[(0,0),(1,0),(-1,0),(0,1)]),(7,[(0,0),(2,1),(-1,2),(3,-1)]),(19,[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]))
RECTS=((0,3),(3,0),(1,1),(4,3),(3,4),(6,2))
def digest(x): return hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest()
def pairmul(u,v,D): return (u[0]*v[0]-D*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def pairpow(u,n,D):
    out=(1,0)
    for _ in range(n): out=pairmul(out,u,D)
    return out
def pscale(c,u):return (c*u[0],c*u[1])
def padd(u,v):return (u[0]+v[0],u[1]+v[1])
def fall(r,j):return math.perm(r,j) if 0<=j<=r else 0
def monomialjet(r,s,j,z,D):
    if j>r:return (0,0)
    return pscale(fall(r,j),pairmul(pairpow(z,r-j,D),pairpow((z[0],-z[1]),s,D),D))
def polymul(a,b):
    out={}
    for (r,s),c in a.items():
        for (t,u),d in b.items():out[r+t,s+u]=out.get((r+t,s+u),0)+c*d
    return {k:v for k,v in out.items() if v}
def polybasis(r,s,a):
    m=min(r,s);out={(r-m,s-m):1}
    for _ in range(m):out=polymul(out,{(1,1):1,(0,0):-a})
    return out
def polyjet(poly,j,z,D):
    out=poly.copy()
    for _ in range(j):out={(r-1,s):r*c for (r,s),c in out.items() if r}
    value=(0,0)
    for (r,s),c in out.items():value=padd(value,pscale(c,pairmul(pairpow(z,r,D),pairpow((z[0],-z[1]),s,D),D)))
    return value
def transform(R,S,a):
    n=R*S;T=[[0]*n for _ in range(n)]
    for r in range(R):
        for s in range(S):
            m=min(r,s)
            for t in range(m+1):T[r*S+s][(r-t)*S+s-t]=math.comb(m,t)*(-a)**t
    return T
def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def transpose(A):return [list(x) for x in zip(*A)]
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def determinant(A):
    if not A:return 1
    B=[row[:] for row in A];sign=1;old=1;n=len(B)
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if B[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:B[k],B[pivot]=B[pivot],B[k];sign=-sign
        q=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=B[i][j]*q-B[i][k]*B[k][j]
                assert v%old==0
                B[i][j]=v//old
            B[i][k]=0
        old=q
    return sign*B[-1][-1]
def rankmod(A,p):
    B=[[v%p for v in row] for row in A];n=len(B);k=0
    for j in range(n):
        i=next((i for i in range(k,n) if B[i][j]),None)
        if i is None:continue
        B[k],B[i]=B[i],B[k];u=pow(B[k][j],-1,p)
        B[k]=[(v*u)%p for v in B[k]]
        for i in range(k+1,n):
            c=B[i][j];B[i]=[(x-c*y)%p for x,y in zip(B[i],B[k])]
        k+=1
    return k
def gram(rows,D):
    return [[2*sum(x[0]*y[0]+D*x[1]*y[1] for x,y in zip(u,v)) for v in rows] for u in rows]
def coefficient(r,s,j,h):
    if j>r:return F(0)
    if r<s:return F(fall(r,j))*h**(r-j)
    return sum((F(math.comb(j,l)*fall(s,l)*fall(r-s,j-l))*h**(s-l)
                for l in range(min(s,j)+1) if j-l<=r-s),F(0))
def log_bounds(x):
    q=(x-1)/(x+1);N=100
    lower=2*sum((q**(2*k+1)/(2*k+1) for k in range(N)),F(0))
    return lower,lower+2*q**(2*N+1)/((2*N+1)*(1-q*q))
def frac(x):return [x.numerator,x.denominator]
def run(output):
    root=Path(__file__).resolve().parents[2]
    assert subprocess.check_output(['git','show','-s','--format=%H',BASE],cwd=root,text=True).strip()==BASE
    out=open(output,'x',encoding='utf-8',newline='\n')
    def emit(x):out.write(json.dumps(x,sort_keys=True)+'\n');out.flush()
    emit({'kind':'inputs','base':BASE,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rectangles':RECTS,'cohorts':COHORTS,'a':[-2,0,3],'J':[0,1,4]})
    cases=jets=envelopes=positive=singular=0
    for D,P in COHORTS:
        N=max(x*x+D*y*y for x,y in P);rho=max(5,math.isqrt(N)+(math.isqrt(N)**2<N));a0=rho*rho//2
        h=F(rho*rho-a0,rho*rho);assert h<=F(13,25)
        for R,S in RECTS:
            labels=[(r,s) for r in range(R) for s in range(S)];n=R*S
            for a in (-2,0,3):
                T=transform(R,S,a)
                assert all(T[i][i]==1 and all(T[i][j]==0 for j in range(i+1,n)) for i in range(n))
                assert determinant(T)==1 and mm(T,transform(R,S,-a))==identity(n)
                assert mm(T,transform(R,S,-1))==transform(R,S,a-1)
                for J in (0,1,4):
                    original=[[monomialjet(r,s,j,z,D) for z in P for j in range(J)] for r,s in labels]
                    direct=[[polyjet(polybasis(r,s,a),j,z,D) for z in P for j in range(J)] for r,s in labels]
                    for i in range(n):
                        for c in range(len(P)*J):
                            u=(0,0)
                            for k in range(n):u=padd(u,pscale(T[i][k],original[k][c]))
                            assert u==direct[i][c];jets+=1
                    G=gram(original,D);H=gram(direct,D)
                    assert H==mm(mm(T,G),transpose(T))
                    det=determinant(G);assert determinant(H)==det and det>=0
                    positive+=det>0;singular+=det==0
                    ranks=[];divisors=[]
                    for p in (3,5):
                        rg,rh=rankmod(G,p),rankmod(H,p);assert rg==rh
                        ranks.append([p,rg,rh])
                        if pow((-D)%p,(p-1)//2,p)==p-1:
                            exponent=2*sum(min(r//p,s) for r,s in labels)
                            assert det%(p**exponent)==0
                            divisors.append([p,exponent,'positive' if det else 'zero determinant: no positive lower bound'])
                    for r,s in labels:
                        for z in P:
                            for j in range(J):
                                u=polyjet(polybasis(r,s,a0),j,z,D);sq=u[0]**2+D*u[1]**2
                                if j>r:assert sq==0
                                else:assert sq<=rho**(2*(r+s-j))*coefficient(r,s,j,h)**2
                                envelopes+=1
                    emit({'kind':'case','D':D,'R':R,'S':S,'a':a,'J':J,'rho':rho,'center':a0,'det':det,'ranks':ranks,'divisors':divisors,'T':T,'G':G,'H':H})
                    cases+=1
    count=eligible=0;h=F(13,25)
    for r in range(1,49):
        for s in range(min(r,8)+1):
            for j in range(min(r,12)+1):
                B=coefficient(r,s,j,h)
                expansion=h**s*sum((F(math.comb(s,k)*fall(j,k),fall(r,k))*(1/h-1)**k for k in range(s+1)),F(0))
                assert B/F(fall(r,j))==expansion
                assert B<=fall(r,j)*(h+(1-h)*F(j,r))**s
                count+=1
                for S in range(1,9):
                    if r>=5*S and j<S and s<S:
                        assert B<=fall(r,j)*F(5,8)**s;eligible+=1
    # Explicit witnesses to stronger, false claims; these are rejected, not repaired.
    witnesses={}
    witnesses['factor_two']=gram([[(1,0)]],1)[0][0]==2!=1
    witnesses['ordinary_not_divided']=monomialjet(2,0,2,(1,0),1)==(2,0)
    witnesses['sign_of_center']=transform(2,2,3)!=transform(2,2,-3)
    witnesses['extra_leibniz_term']=polyjet(polybasis(1,1,3),1,(1,0),1)==(1,0) and fall(0,1)==0
    old=monomialjet(1,1,0,(0,0),1);new=polyjet(polybasis(1,1,12),0,(0,0),1)
    witnesses['actual_row_norm_can_increase']=old==(0,0) and new==(-12,0)
    witnesses['S1_gain_zero']=(25-5)*1*(1-1)==0
    witnesses['rounding_not_exact_half']=F(25-25//2,25)==F(13,25)>F(1,2)
    witnesses['singular_not_positive']=determinant([[0]])==0 and not determinant([[0]])>0
    witnesses['no_naive_h_power']=coefficient(1,1,1,h)==1>h*fall(1,1)
    assert all(witnesses.values())
    logs={}
    for name,x,lower in [('2',F(2),F(6931,10000)),('3',F(3),F(109,100)),('5',F(5),F(1609,1000)),('8/5',F(8,5),F(46,100))]:
        lo,hi=log_bounds(x);assert lower<=lo<hi
        logs[name]={'x':frac(x),'lower':frac(lo),'upper':frac(hi),'required_lower':frac(lower)}
    guaranteed=F(20)*F(99,100)/676*F(46,100)
    assert guaranteed>F(13,1000)
    logD=13*F(6931,10000)+F(109,100)+9*F(1609,1000)
    assert 2**13*3*5**9==48000000000
    slope=F(999997,1000000)-F(4,5);assert slope>0
    margin=slope*logD-F(5739,1000)+F(813,1000)+F(13,1000)
    assert margin>0 and cases==162
    emit({'kind':'summary','status':'FINITE_CHECKS_PASS_PAPER_CANDIDATE_ONLY','cases':cases,'positive_determinants':positive,'singular_determinants':singular,'jet_comparisons':jets,'envelope_comparisons':envelopes,'coefficient_cases':count,'eligible_checks':eligible,'mutation_witnesses':witnesses,'log_bounds':logs,'gain_lower':frac(guaranteed),'fixed_gain':frac(F(13,1000)),'endpoint':48000000000,'log_endpoint_lower':frac(logD),'affine_slope':frac(slope),'candidate_margin':frac(margin),'scope':'NOT a Lean theorem, all-D machine certificate, new cutoff or independent review'})
    print(json.dumps({'status':'FINITE_CHECKS_PASS_PAPER_CANDIDATE_ONLY','cases':cases,'coefficient_cases':count,'eligible_checks':eligible,'candidate_margin':frac(margin),'positive_determinants':positive,'singular_determinants':singular}));out.close()
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);run(parser.parse_args().output)
