"""R2 sequential replay. Generator labels never enter Runner.run."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import random
from time import perf_counter
import platform
import sympy as sp
from transport import Poly,Frame,Runner,POLICIES,load_production,Z,W

SEEDS=(1701,2701)

def multiply(p,q):
    return Poly.make((r+i,s+j,c*d) for r,s,c in p.terms for i,j,d in q.terms)

def corpus(seed):
    rng=random.Random(seed); bases=[]
    for i in range(8):
        a,b=2+i%3,1+i%2
        terms=[(a,b,1),(a,0,rng.randint(1,4)),(0,b,rng.randint(-4,4)),
               (1,0,rng.randint(1,5)),(0,0,10*i+rng.randint(1,9))]
        bases.append(Poly.make(terms))
    for k in (1,2):
        p=Poly.make([(k,1,1),(1,0,1),(0,0,k+2)])
        bases.append(multiply(p,p))
    bases += [Poly.make([(3,0,1),(1,0,2),(0,2,1),(0,0,5)]),
              Poly.make([(4,0,1),(2,0,3),(0,1,1),(0,0,7)])]
    tasks=[]
    for orbit,base in enumerate(bases):
        for j in range(6):
            frame=Frame(Q(rng.choice((-3,-1,1,2,3)),rng.choice((1,2))),
                        Q(1),Q(j-2,2),Q(1),Q((j*3+orbit)%11-5,2))
            tasks.append((orbit,j,frame.apply(base)))
    return bases,tasks

def ordering(tasks,mode,seed):
    out=list(tasks)
    if mode=='shuffled': random.Random(seed+991).shuffle(out)
    elif mode=='round_robin': out.sort(key=lambda x:(x[1],x[0]))
    return [x[2] for x in out]

def expected(poly):
    f=poly.expr(); val=sp.Poly(sp.resultant(f,sp.diff(f,Z),Z),W,domain=sp.QQ)
    return val

def run(source,output):
    production=load_production(source); oracle={}; raw=[]; streams=[]; generation=[]
    corpus_started=perf_counter()
    for seed in SEEDS:
        bases,tasks=corpus(seed)
        generation.append({'seed':seed,'bases':[p.payload() for p in bases],
                           'tasks':[p.payload() for _,_,p in tasks],
                           'distinct_raw':len({p.key() for _,_,p in tasks})})
        for _,_,p in tasks:
            if p.digest() not in oracle: oracle[p.digest()]=expected(p)
    oracle_setup=perf_counter()-corpus_started
    audit_time=0.0
    for si,seed in enumerate(SEEDS):
        _,tasks=corpus(seed)
        for mi,mode in enumerate(('blocked','shuffled','round_robin')):
            polys=ordering(tasks,mode,seed)
            shift=(3*si+mi)%len(POLICIES)
            order=POLICIES[shift:]+POLICIES[:shift]
            for policy in order:
                runner=Runner(policy,production)
                for index,p in enumerate(polys):
                    answer=runner.run(p); t0=perf_counter()
                    for point,value in answer['samples']:
                        t,d=Q(point),Q(value)
                        actual=oracle[p.digest()].eval(sp.Rational(t.numerator,t.denominator))
                        if actual != sp.Rational(d.numerator,d.denominator):
                            raise RuntimeError(f'FALSE CERTIFICATE {seed} {mode} {policy} {index}')
                    audit_time+=perf_counter()-t0
                    raw.append({'seed':seed,'mode':mode,'policy':policy,'index':index,**answer})
                streams.append({'seed':seed,'mode':mode,'policy':policy,
                                **runner.counts,'seconds':runner.times})
    totals={}
    for policy in POLICIES:
        rows=[x for x in streams if x['policy']==policy]
        total={k:sum(x[k] for x in rows) for k in ('production_calls','admission_calls','hits','misses','nonzero','unresolved','hard_resets')}
        total['max_entries']=max(x['max_entries'] for x in rows)
        total['max_bytes']=max(x['max_bytes'] for x in rows)
        total['seconds']={k:sum(x['seconds'][k] for x in rows) for k in rows[0]['seconds']}
        totals[policy]=total
    baseline=totals['canonical_lru']['production_calls']
    promotion={}
    for p in ('euclidean','hyperbolic','euclidean_slow','hyperbolic_slow'):
        no_worse=all(r['production_calls']<=next(x['production_calls'] for x in streams if x['policy']=='canonical_lru' and x['seed']==r['seed'] and x['mode']==r['mode']) for r in streams if r['policy']==p)
        promotion[p]=no_worse and totals[p]['production_calls']<=0.9*baseline
    result={'frozen_main':'791ebf4815d8eb4be5da3b01527ca7f0877b6d0e',
            'protocol_sha256':hashlib.sha256(Path(__file__).with_name('PROTOCOL.md').read_bytes()).hexdigest(),
            'python':platform.python_version(),'sympy':sp.__version__,'seeds':list(SEEDS),
            'tasks_per_policy':432,'cache_capacity':4,'false_acceptances':0,
            'oracle_setup_seconds':oracle_setup,'postcheck_seconds':audit_time,
            'totals':totals,'per_stream':streams,'promotion_call_count':promotion,
            'interpretation':'same-author synthetic reuse corpus, not unseen-family generalization; no Lean proof or general geometric speedup'}
    path=Path(output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2))
    path.with_name(path.stem+'_trace.json').write_text(json.dumps(raw,indent=2))
    path.with_name(path.stem+'_corpus.json').write_text(json.dumps(generation,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--output',required=True)
    args=ap.parse_args();run(args.source,args.output)
