"""Paired frozen evaluation of fixed, crisp, fuzzy, empirical-mixture routing.
Uses actual fixed_sylvester/det from the hash-pinned repository control module.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, importlib.util, json, random, sys, time
import sympy as sp
from granules import Z,W,Target,Witness,EmpiricalLocalModel,order_candidates,empirical_zplus,verify_nonzero_witness

SOURCE_BLOB='0c4ccb8f2dab99a5317f80345eae7920390fcbc0'
FAMILIES=('generic','degree_drop','high_contact','vertical','repeated','constant')
POLICIES=('fixed','crisp','fuzzy','blend')

def load_source(path):
    data=path.read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual != SOURCE_BLOB:
        raise ValueError('source drift; start a new round rather than silently adapting')
    spec=importlib.util.spec_from_file_location('pinned_multiplicity',path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def generate(seed, per_family):
    rng=random.Random(seed)
    for family in FAMILIES:
        for index in range(per_family):
            a=rng.choice([2,3,4]); z=Q(rng.randint(-4,4),rng.choice([1,2])); w=rng.randint(-3,3)
            x=Z-sp.Rational(z); e=sp.Rational(rng.choice([-2,-1,1,2]),rng.choice([1,2,10,100]))
            if family=='generic':
                f=sum((rng.randint(-3,3)+rng.randint(-3,3)*W)*Z**i for i in range(a))+(1+e*W)*Z**a
            elif family=='degree_drop':
                f=(W-w)*x**a+x**(a-1)-(W-w)
            elif family=='high_contact': f=x**a-e*(W-w)
            elif family=='vertical': f=(W-w)*(x**a-1)
            elif family=='repeated': f=(x*x-(W-w))**2; a=4
            else: f=x**a-1
            f=sp.expand(f); Target.of(f,a)
            points=list(map(Q,range(-3,4))); rng.shuffle(points)
            yield {'id':f'{seed}/{family}/{index}','family':family,'a':a,'f':f,'points':points}

def evaluate(case, source):
    f,a=case['f'],case['a']
    result=[]
    for t in case['points']:
        p=sp.Poly(f.subs(W,sp.Rational(t)),Z)
        coeff=[Q(p.nth(i)) for i in range(a+1)]
        d=source.det(source.fixed_sylvester(coeff,a))
        result.append({'point':t,'coeff':coeff,'det':d})
    # Different algorithm, same exact fixed polynomial and sample.
    E=sp.Poly(sp.resultant(f,sp.diff(f,Z),Z),W,domain=sp.QQ)
    for row in result:
        if row['det'] != Q(E.eval(sp.Rational(row['point']))):
            raise AssertionError('production/resultant mismatch')
    return result, E

def run(source_path):
    source=load_source(source_path)
    start=time.monotonic(); observations=[]; training=[]
    for case in generate(2026102201,4):
        rows,E=evaluate(case,source)
        observations.extend((r['coeff'],r['det']!=0) for r in rows)
        training.append({'id':case['id'],'polynomial':str(case['f']), 'rows':rows})
    model=EmpiricalLocalModel.fit(observations,'seed2026102201/24polynomials/168probes')
    test=[]; scalar_checks=0
    for case in generate(2026102202,16):
        rows,E=evaluate(case,source); coefficients=[r['coeff'] for r in rows]
        outcomes={}
        for policy in POLICIES:
            order=order_candidates(policy,coefficients,model)
            # Representation test: nonzero rational scalar factor leaves routing unchanged.
            scaled=[[Q(-7,3)*v for v in cs] for cs in coefficients]
            if order_candidates(policy,scaled,model)!=order:
                raise AssertionError('scalar-rescaling routing drift')
            scalar_checks+=1
            selected=next(((k+1,rows[i]) for k,i in enumerate(order) if rows[i]['det']!=0),None)
            if selected:
                count,r=selected
                witness=Witness(Target.of(case['f'],case['a']),r['point'],r['det'],case['id'])
                if not verify_nonzero_witness(case['f'],witness): raise AssertionError('false certificate')
                outcomes[policy]={'cost':count,'probes':count,'witness':str(r['point']),'det':str(r['det'])}
            else:
                outcomes[policy]={'cost':8,'probes':7,'witness':None,
                                  'status':'inconclusive; no nonzero witness within budget'}
        test.append({'id':case['id'],'family':case['family'],'polynomial':str(case['f']),
                     'a':case['a'],'resultant':str(E.as_expr()),'identically_zero':E.is_zero,
                     'candidate_rows':rows,'outcomes':outcomes})
    summary={}
    for policy in POLICIES:
        costs=[c['outcomes'][policy]['cost'] for c in test]
        summary[policy]={'mean_penalized_probes':str(Q(sum(costs),len(costs))),
                         'total_actual_probes':sum(c['outcomes'][policy]['probes'] for c in test),
                         'failures':sum(c['outcomes'][policy]['witness'] is None for c in test),
                         'zplus':empirical_zplus(costs,7),
                         'per_family':{fam:str(Q(sum(c['outcomes'][policy]['cost'] for c in test if c['family']==fam),16)) for fam in FAMILIES}}
    gain={}
    for base in ['fixed','crisp','fuzzy']:
        diffs=[c['outcomes']['blend']['cost']-c['outcomes'][base]['cost'] for c in test]
        gain[base]={'mean_blend_minus_baseline':str(Q(sum(diffs),len(diffs))),
                    'wins':sum(d<0 for d in diffs),'ties':sum(d==0 for d in diffs),'losses':sum(d>0 for d in diffs)}
    passed=all(Q(gain[b]['mean_blend_minus_baseline'])<0 for b in ['crisp','fuzzy'])
    return {'status':'PASS exact comparisons and certificates',
            'source_commit':'791ebf4815d8eb4be5da3b01527ca7f0877b6d0e','source_blob':SOURCE_BLOB,
            'environment':{'python':sys.version.split()[0],'sympy':sp.__version__},
            'train_tasks':24,'test_tasks':96,'train_probes':168,'test_oracle_probes':672,
            'test_oracle_note':'all 672 outputs computed once for paired replay; not a wall-clock speed benchmark',
            'model':{'mass':model.mass,'success':model.success,'source':model.source},
            'summary':summary,'paired':gain,'performance_gate_passed':passed,
            'scalar_rescaling_checks':scalar_checks,'training':training,'test':test,
            'independence':'same author, different exact algorithms; no independent semantic review',
            'wall_seconds_descriptive':round(time.monotonic()-start,3)}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True,type=Path); ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args(); result=run(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('training','test')},indent=2,default=str))
