#!/usr/bin/env python3
"""Exact same-author comparator; symbolic oracle and frozen production source.
Usage: python comparator.py --source-root PATH --output PATH
Requires SymPy 1.14.0. Only pure functions are loaded from verify_exact.py;
this does NOT execute its Arb/PARI entrypoint or certify global claims.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, math, pathlib, random, subprocess, sys
import sympy as sp
Z,W,T=sp.symbols('Z W T')
SHA='791ebf4815d8eb4be5da3b01527ca7f0877b6d0e'
HASHES={'tools/verify_exact.py':'af332fc48f68c57fbe47223bf533f45fd1dbac99',
        'lean/multiplicity_exact_controls.py':'0c4ccb8f2dab99a5317f80345eae7920390fcbc0'}
def require(test,message):
    if not test: raise AssertionError(message)
def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def pure_core(source):
    nodes=[n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name in {'mul','powers','gram','vp'}]
    require(len(nodes)==4,'missing production function')
    env={'math':math}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),'frozen-production-functions','exec'),env)
    return env
def coeffs(expr,var,count):
    p=sp.Poly(expr,var)
    return [p.nth(i) for i in range(count)]
def fixed_reference(F,G,a,b):
    # Direct symbolic coefficient map (A,B) -> AF+BG.
    polys=[sp.Poly(Z**j*F,Z) for j in range(b)]+[sp.Poly(Z**j*G,Z) for j in range(a)]
    return sp.Matrix(a+b,a+b,lambda i,j:polys[j].nth(i))
def jet_reference(P,R,S,J,D):
    # Formal differentiation first, then specialization in Q[T]/(T^2+D).
    aa=[];bb=[]
    for r in range(R):
        for s in range(S):
            ar=[];br=[]
            for x,y in P:
                for j in range(J):
                    d=sp.diff(Z**r*W**s,Z,j)
                    q=sp.Poly(sp.expand(d.subs({Z:x+y*T,W:x-y*T},simultaneous=True)),T)
                    rem=q.rem(sp.Poly(T*T+D,T))
                    ar.append(rem.nth(0));br.append(rem.nth(1))
            aa.append(ar);bb.append(br)
    n=R*S;c=len(P)*J
    A=sp.Matrix(n,c,lambda i,j:aa[i][j]);B=sp.Matrix(n,c,lambda i,j:bb[i][j])
    return 2*(A*A.T+D*B*B.T)
def gram_round(core,src):
    mutants={
      'trace_factor_two':src.replace('2 * (a[0] * b[0] + D * a[1] * b[1])','(a[0] * b[0] + D * a[1] * b[1])'),
      'missing_conjugation':src.replace('a[0] * b[0] + D * a[1] * b[1]','a[0] * b[0] - D * a[1] * b[1]'),
      'drop_imaginary_coordinate':src.replace('a[0] * b[0] + D * a[1] * b[1]','a[0] * b[0]'),
      'missing_D_weight':src.replace('D * a[1] * b[1]','a[1] * b[1]'),
      'divided_derivatives':src.replace('math.perm(r, j)','math.comb(r, j)'),
      'drop_last_jet':src.replace('range(J)','range(max(J-1,0))'),
      'truncate_at_j_equals_r':src.replace('if j > r:','if j >= r:')}
    for name,s in mutants.items(): require(s!=src,f'inert mutation {name}')
    funcs={k:pure_core(s)['gram'] for k,s in mutants.items()}
    counts={k:0 for k in funcs};witnesses={}
    inputs=[([],2,2,3,7), ([(0,0)],0,2,3,7), ([(0,0)],2,0,3,7),
            ([(0,0)],2,2,0,7), ([(0,1)],2,1,1,1), ([(0,0)],2,1,1,1)]
    for seed in [20261022,1792679188]:
        rng=random.Random(seed)
        for k in range(48):
            R=1+k%4;S=1+(k//4)%3;J=[0,1,R,R+2][(k//12)%4]
            P=rng.sample([(x,y) for x in range(-2,3) for y in range(-2,3)],1+k%6)
            inputs.append((P,R,S,J,[1,3,7,19][k%4]))
    records=[]
    for number,(P,R,S,J,D) in enumerate(inputs):
        expected=jet_reference(P,R,S,J,D)
        raw=core['gram'](P,R,S,J,D);observed=sp.Matrix(raw)
        require(observed==expected,f'GRAM_MISMATCH {number}')
        require(core['gram'](P[::-1],R,S,J,D)==raw,f'point ordering {number}')
        determinant=expected.det(method='domain-ge')
        trans=sp.Matrix(core['gram']([(x+2,y) for x,y in P],R,S,J,D))
        require(trans.det(method='domain-ge')==determinant,f'real translation {number}')
        require(determinant>=0,'negative Gram determinant')
        product=math.prod(expected[i,i] for i in range(R*S))
        require(determinant<=product,'Hadamard violation')
        for name,fn in funcs.items():
            if sp.Matrix(fn(P,R,S,J,D))!=expected:
                counts[name]+=1;witnesses.setdefault(name,number)
        records.append({'id':number,'P':P,'R':R,'S':S,'J':J,'D':D,'det':str(determinant),
                        'diagonal_product':str(product),'matrix':[[str(x) for x in row] for row in expected.tolist()]})
    require(all(counts.values()),'a Gram mutation was not detected')
    return {'cases':records,'mutant_detection_counts':counts,'first_mutant_witness':witnesses,
            'point_reordering_checks':len(records),'real_translation_checks':len(records)}
def sylvester_round(prod):
    rng=random.Random(1792679188);records=[];sharp=0;drops=0;zeros=0
    for k in range(48):
        a=2+k%4;drop=bool(k%2 and a>=3)
        m=rng.randint(2,a-1 if drop else a)
        w0=sp.Rational(rng.randint(-3,3),rng.choice([1,2]))
        z0=sp.Rational(rng.randint(-3,3),rng.choice([1,2]))
        q=a-m-int(drop)
        f0=(Z-z0)**m*(Z**q-z0**q+1)
        g=sum(rng.randint(-2,2)*Z**i for i in range(a))+rng.choice([-2,-1,1,2])*Z**a
        F=sp.expand(f0+(W-w0)*g);G=sp.diff(F,Z);n=2*a-1
        M=fixed_reference(F,G,a,a-1)
        symbolic_det=sp.expand(M.det(method='domain-ge'))
        require(sp.expand(symbolic_det-sp.resultant(F,G,Z))==0,f'resultant sign {k}')
        values=[]
        for w in range(2*a):
            mat=prod.fixed_sylvester(coeffs(F.subs(W,w),Z,a+1),a)
            require(sp.Matrix(mat)==M.subs(W,w),f'matrix orientation {k},{w}')
            values.append(prod.det(mat))
        rebuilt=sum(sp.Rational(c)*W**i for i,c in enumerate(prod.interpolate(values)))
        require(sp.expand(rebuilt-symbolic_det)==0,f'polynomial comparator {k}')
        for w in [sp.Rational(-13,2),2*a+5]:
            require(prod.det(prod.fixed_sylvester(coeffs(F.subs(W,w),Z,a+1),a))==symbolic_det.subs(W,w),f'held-out {k}')
        shifted=sp.Poly(sp.expand(symbolic_det.subs(W,W+w0)),W)
        order=min((ex[0] for ex,c in shifted.terms() if c),default=None)
        require(order is None or order>=m-1,f'local multiplicity {k}')
        require(sp.rem(sp.Poly(F.subs(W,w0),Z),sp.Poly((Z-z0)**m,Z)).is_zero,'plant invalid')
        Tay=sp.Matrix(n,n,lambda i,j:sp.Poly((Z+z0)**j,Z).nth(i))
        require(Tay.det()==1,'Taylor determinant')
        TM=Tay*M.subs(W,w0)
        require(all(v==0 for v in TM[:m-1,:]),f'Taylor rows {k}')
        for col in range(n):
            poly=sum(M[i,col].subs(W,w0)*Z**i for i in range(n))
            require([TM[i,col] for i in range(n)]==coeffs(sp.expand(poly.subs(Z,Z+z0)),Z,n),f'Taylor action {k},{col}')
        sharp+=order==m-1;zeros+=order is None;drops+=drop
        records.append({'id':k,'a':a,'m':m,'w0':str(w0),'z0':str(z0),'F':str(F),
                        'det':str(symbolic_det),'order':order,'degree_drop':drop})
    return {'cases':records,'positive_exponent_cases':48,'degree_drop_cases':drops,'zero_determinants':zeros,'sharp_order_cases':sharp}
def boundaries(core,prod):
    F=Z**2-W;proper=fixed_reference(F,sp.diff(F,Z),2,1).det();padded=fixed_reference(F,sp.diff(F,Z),3,2).det()
    require(sp.expand(proper+4*W)==0 and padded==0,'padding counterexample')
    Fdrop=W*Z**2+Z+1;fixed=sp.expand(fixed_reference(Fdrop,sp.diff(Fdrop,Z),2,1).det())
    rebuilt=sp.resultant(Fdrop.subs(W,0),sp.diff(Fdrop,Z).subs(W,0),Z)
    require(fixed.subs(W,0)==0 and rebuilt==1,'degree drop')
    f=Z+W;g=Z+1;odd=fixed_reference(f,g,1,1).det();standard=sp.resultant(f,g,Z)
    require(sp.expand(odd+standard)==0 and sp.expand(odd-standard)!=0,'odd-block sign')
    require(sp.Poly(Z**3,Z,modulus=3).diff().is_zero,'characteristic control')
    P=[(0,0)]*7;R,S,J,D=3,2,8,7
    guard=J>=len(P)+1 and len(P)*J>2*R*S+J*(R+S)
    duplicate_det=sp.Matrix(core['gram'](P,R,S,J,D)).det()
    require(guard and duplicate_det==0,'duplicate guard')
    origin=sp.Matrix(core['gram']([(0,0)],2,1,1,1)).det()
    shifted=sp.Matrix(core['gram']([(0,1)],2,1,1,1)).det()
    require(origin==0 and shifted==4,'complex translation')
    return {'overpadding':{'F':'Z^2-W','a_exact':2,'exact_det':str(proper),'a_padded':3,'padded_det':str(padded)},
      'degree_drop':{'F':str(Fdrop),'fixed_det':str(fixed),'fixed_at_0':0,'rebuilt_at_0':str(rebuilt)},
      'block_sign':{'F':str(f),'G':str(g),'fixed_det':str(odd),'standard_resultant':str(standard)},
      'finite_characteristic':{'p':3,'F':'Z^3-W','F_Z_mod_p':'0','consequence':'zero determinant, not finite root budget'},
      'duplicate_points':{'P':P,'R':R,'S':S,'J':J,'D':D,'old_guard':guard,'det':str(duplicate_det),'domain':'outside set-valued contract; accepted by Python list interface'},
      'complex_translation':{'P':'{0} -> {i}','R':2,'S':1,'J':1,'before':str(origin),'after':str(shifted)},
      'sharp_exponent':{'F':'Z^2-W','m':2,'det':str(proper),'order':1},
      'repeated_factor':{'F':'Z^2','det':str(fixed_reference(Z**2,2*Z,2,1).det())}}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=pathlib.Path,required=True);ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    for rel,expected in HASHES.items(): require(blob((args.source_root/rel).read_bytes())==expected,f'source hash {rel}')
    text=(args.source_root/'tools/verify_exact.py').read_text();core=pure_core(text)
    spec=importlib.util.spec_from_file_location('pinned_multiplicity',args.source_root/'lean/multiplicity_exact_controls.py')
    prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
    for name,call in [('inherited_multiplicity',prod.run),('gram',lambda:gram_round(core,text)),('sylvester',lambda:sylvester_round(prod)),('boundaries',lambda:boundaries(core,prod))]:
        print('START',name,flush=True);result=call();(args.output/(name+'.json')).write_text(json.dumps(result,indent=2,sort_keys=True));print('PASS',name,flush=True)
    vp=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name=='vp')
    try:
        p=subprocess.run([sys.executable,'-c',ast.unparse(vp)+'\nprint(vp(0,3))\n'],capture_output=True,text=True,timeout=1)
        vpres={'status':'returned','returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    except subprocess.TimeoutExpired:
        vpres={'status':'timeout','seconds':1,'domain':'zero input; no finite valuation; unguarded while loop'}
    (args.output/'valuation_zero.json').write_text(json.dumps(vpres,indent=2))
    summary={'target':SHA,'status':'PASS_WITH_BOUNDARY_FINDINGS','sympy':sp.__version__,'python':sys.version,
      'source_hashes':HASHES,'gram_cases':102,'sylvester_cases':48,'valuation_zero':vpres,
      'independence':'same author; different symbolic algorithms; not blind review or independent authorship',
      'scope':'exact finite calculations and statement audit; not full formal equivalence or classification'}
    (args.output/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True));print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
