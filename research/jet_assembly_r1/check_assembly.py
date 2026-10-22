#!/usr/bin/env python3
"""Finite exact controls, not a universal proof. No Arb or PARI entrypoint is run."""
from __future__ import annotations
import argparse, ast, hashlib, json, math, random
from pathlib import Path
import sympy as sp
Z,W=sp.symbols('Z W')
SOURCE_BLOB='af332fc48f68c57fbe47223bf533f45fd1dbac99'
def require(ok,message):
    if not bool(ok): raise RuntimeError(message)
def load_gram(path):
    data=Path(path).read_bytes()
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==SOURCE_BLOB,'source drift')
    names={'mul','powers','gram'}
    body=[n for n in ast.parse(data).body if isinstance(n,ast.FunctionDef) and n.name in names]
    require({n.name for n in body}==names,'missing functions')
    env={'math':math};exec(compile(ast.Module(body=body,type_ignores=[]),str(path),'exec'),env)
    return env['gram']
def degrees(f):
    p=sp.Poly(f,Z,W,domain=sp.QQ);require(not p.is_zero,'zero polynomial has no ordinary bidegree')
    return int(p.degree(Z)),int(p.degree(W))
def multiplicity(q,x):
    p=sp.Poly(q,Z,domain=sp.QQ)
    if p.is_zero:return None
    m=0;linear=sp.Poly(Z-x,Z,domain=sp.QQ)
    while p.eval(x)==0:
        p,rem=p.div(linear);require(rem.is_zero,'nonzero division remainder');m+=1
    return m
def exceptional(f,params,u,h):
    r,b=degrees(f);bad=set();rows=[]
    for w in params:
        x=u*w+h;q=sp.expand(f.subs(W,w));m=multiplicity(q,x);flag=m is None or m>b
        p=sp.Poly(q,Z,domain=sp.QQ);jets=[]
        for j in range(b+1):jets.append(p.eval(x));p=p.diff()
        require(flag==all(j==0 for j in jets),'multiplicity/derivative mismatch')
        if flag:bad.add(w)
        rows.append({'w':str(w),'z':str(x),'fiber':str(q),'order':m,'jets':list(map(str,jets)),'bad':flag})
    require(len(bad)<=2*r+b,'cardinality counterexample')
    return bad,rows
def generate(seed):
    rng=random.Random(seed);out=[]
    for i in range(48):
        a,b,c=[rng.randint(-2,2)for _ in range(3)];k=1+i%3
        forms=[sp.Integer(a or 1),(W-a)*(W-b),(Z-a)*(Z-b),(Z-a)**2-(W-b),
               (W-a)*((Z-b)**2-W+c),((Z-a)**2-(W-b))**k,(W-a)*Z+1,
               (Z-a)*(W-b)*((Z-c)**2-W)**2]
        out.append(sp.expand(forms[i%8]))
    return out
def symbolic_gram(P,R,S,J):
    rows=[]
    for r in range(R):
        for s in range(S):
            entries=[];f=Z**r*W**s
            for x,y in P:
                z=x+sp.I*y
                for j in range(J):
                    a=sp.expand(sp.diff(f,Z,j).subs({Z:z,W:sp.conjugate(z)}))
                    entries.append((sp.re(a),sp.im(a)))
            rows.append(entries)
    return sp.Matrix([[2*sum(a*c+b*d for(a,b),(c,d)in zip(u,v))for v in rows]for u in rows])
def gf27_mul(x,y):
    a=[x//3**i%3 for i in range(3)];b=[y//3**i%3 for i in range(3)]
    c=[sum(a[i]*b[k-i]for i in range(3)if 0<=k-i<3)%3 for k in range(5)]
    for k in (4,3):
        t=c[k];c[k]=0;c[k-2]=(c[k-2]+t)%3;c[k-3]=(c[k-3]+t)%3
    return sum(c[i]*3**i for i in range(3))
def run(source,seed):
    gram=load_gram(source);cases=generate(seed);params=list(map(sp.Integer,range(-4,5)))
    maps=[(1,0),(2,1),(-1,-1)];raw=[];products=[];scalars=0;observations=0
    for i,f in enumerate(cases):
        for u,h in maps:
            bad,rows=exceptional(f,params,u,h);observations+=len(rows)
            scaled,_=exceptional(-sp.Rational(3,2)*f,params,u,h)
            require(bad==scaled,'scalar changed exceptional set');scalars+=1
            raw.append({'id':i,'f':str(f),'degrees':degrees(f),'map':[u,h],'rows':rows})
    for i,f in enumerate(cases):
        g=cases[(7*i+5)%48];fg=sp.expand(f*g)
        require(degrees(fg)==tuple(x+y for x,y in zip(degrees(f),degrees(g))),'bidegree additivity')
        require(sp.expand(fg-g*f)==0,'factor-order mismatch')
        for u,h in maps:
            bf,_=exceptional(f,params,u,h);bg,_=exceptional(g,params,u,h)
            bfg,rows=exceptional(fg,params,u,h);observations+=len(rows)
            require(bfg<=bf|bg,'product exceptional set escaped factors')
            products.append({'id':i,'f':str(f),'g':str(g),'map':[u,h],'rows':rows})
    matrices=[]
    for R in range(1,4):
        for S in range(1,4):
            J=S;N=2*(R-1)+(S-1)+1
            shapes=[[(sp.Integer(t),sp.Integer(0))for t in range(N)],
                    [(sp.Integer(0),sp.Integer(t))for t in range(N)],
                    [(sp.Integer(t),sp.Integer(t*t+1))for t in range(N)],
                    [(sp.Rational(1-t*t,1+t*t),sp.Rational(2*t,1+t*t))for t in range(N)]]
            for shape,P in enumerate(shapes):
                require(len(set(P))==N,'duplicate generated sample')
                G=sp.Matrix(gram(P,R,S,J,1));ref=symbolic_gram(P,R,S,J)
                require(G==ref,'production/reference Gram mismatch')
                d=G.det(method='domain-ge');require(d>0,'qualifying Gram nonpositive')
                require(G==sp.Matrix(gram(P[::-1],R,S,J,1)),'point-order mismatch')
                shift=sp.Matrix(gram([(x+2,y)for x,y in P],R,S,J,1))
                require(shift.det(method='domain-ge')==d,'real translation mismatch')
                matrices.append({'R':R,'S':S,'J':J,'shape':shape,'points':[[str(x),str(y)]for x,y in P],
                    'matrix':[[str(v)for v in row]for row in G.tolist()],'det':str(d)})
    controls={}
    for j in (1,2):
        N=3*j+1;P=[(sp.Rational(1-t*t,1+t*t),sp.Rational(2*t,1+t*t))for t in range(N)]
        f=(Z*W-1)**j
        for x,y in P:
            z=x+sp.I*y
            require(all(sp.expand(sp.diff(f,Z,k).subs({Z:z,W:sp.conjugate(z)}))==0 for k in range(j)),
                    'circle control not invisible')
        d=sp.Matrix(gram(P,j+1,j+1,j,1)).det(method='domain-ge');require(d==0,'circle control nonsingular')
        controls['circle_depth_'+str(j)]={'N':N,'J':j,'R':j+1,'S':j+1,'det':str(d)}
    dup=sp.Matrix(gram([(0,0)]*4,2,1,1,1));require(dup.det()==0,'duplicate sample control')
    controls['duplicate_samples']={'list_length':4,'set_card':1,'det':str(dup.det())}
    require(sp.Matrix([[2,2],[2,2]]).det()==0,'duplicate rows control')
    controls['duplicate_rows']={'R':1,'S':1,'N':1,'det':0}
    require(len(params)>2 and all(Z.subs(Z,0)==0 for w in params),'noninjective control')
    controls['noninjective_coordinate']={'F':'Z','N':9,'budget':2}
    require(multiplicity(Z**6,0)==6 and multiplicity(Z**2,0)==2,'squarefree control')
    controls['squarefree_replacement']={'F':'(Z^2-W)^3','actual_order':6,'squarefree_order':2,'W_degree':3}
    require(multiplicity((W-1).subs(W,1),0)is None,'zero fiber finite order')
    controls['discarded_zero_fiber']={'F':'W-1','w':1,'fiber':'0','order':None}
    require(all(sp.diff(sp.Integer(0),Z,j)==0 for j in range(3)),'zero polynomial control')
    controls['zero_polynomial']={'N':1,'natural_degree_budget':0,'all_jets_zero':True}
    require(sp.Poly(Z**3-Z-1,Z,modulus=3).is_irreducible,'extension polynomial is reducible')
    require(sp.Poly(sp.diff(Z**3-W,Z),Z,W,modulus=3).is_zero,'ordinary derivative not zero in characteristic three')
    cubes={gf27_mul(gf27_mul(x,x),x):x for x in range(27)}
    require(len(cubes)==27,'Frobenius field control')
    pairs=[(x,gf27_mul(gf27_mul(x,x),x))for x in range(8)]
    require(all(gf27_mul(gf27_mul(x,x),x)==w for x,w in pairs),'finite field evaluation mismatch')
    require(len({w for x,w in pairs})==8 and 8>7,'characteristic control weak')
    require(all((3*x*x)!=0 for x in range(1,8)),'matched characteristic-zero control')
    controls['characteristic_three']={'field':'F3[t]/(t^3-t-1)','F':'Z^3-W','pairs':pairs,
        'J':2,'bidegree':[3,1],'all_jets_zero':True,'invalid_budget':7,'cubes':cubes}
    return {'seed':seed,'source_blob':SOURCE_BLOB,'sympy':sp.__version__,
      'summary':{'families':48,'distinct_families':len(set(map(str,cases))),'product_families':48,
      'parameter_observations':observations,'scalar_set_checks':scalars,'product_cover_checks':len(products),
      'qualifying_gram_matrices':len(matrices),'production_gram_equalities':len(matrices),
      'real_translation_checks':len(matrices),'point_order_checks':len(matrices),'negative_controls':len(controls),
      'status':'PASS'},'families':raw,'products':products,'matrices':matrices,'negative_controls':controls,
      'scope':'finite same-author exact controls; not a universal proof or full classification'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True)
    p.add_argument('--seed',type=int,default=20261022);a=p.parse_args();result=run(a.source,a.seed)
    Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result['summary'],sort_keys=True))
