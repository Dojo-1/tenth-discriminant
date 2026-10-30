"""One registered exact minor check; never imports or runs the old jet oracle."""
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path
import ast,hashlib,json,sys,zipfile

HERE=Path(__file__).resolve().parent
POINTS=((0,0),(1,0),(0,1),(1,1),(-1,1))
PARAMETERS=((1,3),(19,3),(2,5),(1,7))
ARCHIVE_SHA='e9a0b39a5924075e17b8da58a76f10123e758b6b0a379b5188eda0cc87e42ed6'

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def power2(a,n):
    out=[[1,0],[0,1]]
    while n:
        if n%2:out=multiply(out,a)
        a=multiply(a,a);n//=2
    return out

def observations(D,R,S):
    # Left multiplication on the selected order's basis (1,t), t^2=-D.
    # The protocol fixes J=1: only the ordinary zero-order observation.
    out=[]
    for r in range(R):
        for s in range(S):
            row=[]
            for x,y in POINTS:
                q=[[x,-D*y],[y,x]];bar=[[x,D*y],[-y,x]]
                value=multiply(power2(q,r),power2(bar,s))
                row.extend((value[0][0],value[1][0]))
            out.append(row)
    return out

def determinant(a):
    a=[[Fraction(x) for x in row] for row in a];n=len(a);value=Fraction(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];value=-value
        v=a[k][k];value*=v
        for i in range(k+1,n):
            c=a[i][k]/v
            for j in range(k,n):a[i][j]-=c*a[k][j]
    assert value.denominator==1
    return value.numerator

def gram(e,b):
    return [[sum(x*w*y for x,w,y in zip(a,b,c)) for c in e] for a in e]

def minors(e):
    return {I:determinant([[row[j] for j in I] for row in e])
            for I in combinations(range(len(e[0])),len(e))}

def rank_mod(a,p):
    a=[[x%p for x in row] for row in a];rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p);a[rank]=[(x*inv)%p for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                c=a[i][j];a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank

def main():
    manifest=json.loads((HERE/'PHASE123_RESULTS.json').read_bytes())
    archive=HERE/manifest['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==ARCHIVE_SHA
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name,digest in manifest['raw_sha256'].items():
            assert hashlib.sha256(z.read(name)).hexdigest()==digest
        source=ast.parse(z.read(manifest['native_result']['source_snapshot']))
        points=next(ast.literal_eval(n.value) for n in source.body if isinstance(n,ast.Assign)
                    and any(isinstance(t,ast.Name) and t.id=='POINTS' for t in n.targets))
        assert tuple(map(tuple,points))==POINTS
        data=json.loads(z.read(manifest['native_result']['data']))
    wanted={(D,p,R,S,1) for D,p in PARAMETERS for R,S in [(1,1),(4,2)]}
    selected=[c for c in data['cases'] if (c['D'],c['p'],c['R'],c['S'],c['J']) in wanted]
    assert len(selected)==8 and {(c['D'],c['p'],c['R'],c['S'],c['J']) for c in selected}==wanted
    records=[];square_mutations=0;exponent_mutations=0
    for c in selected:
        D,p,R,S=(c[k] for k in ('D','p','R','S'));e=observations(D,R,S)
        b=[v for _ in POINTS for v in (2,2*D)]
        assert gram(e,b)==c['G']
        ue=multiply(c['U'],e);delta=[p**k for k in c['weights']]
        assert determinant(c['U'])==1 and sum(c['weights'])==c['F']
        assert all(x%d==0 for row,d in zip(ue,delta) for x in row)
        quotient=[[x//d for x in row] for row,d in zip(ue,delta)]
        assert gram(quotient,b)==c['K']
        original=minors(e);changed=minors(ue);reduced=minors(quotient)
        factor=p**c['F'];entries=[]
        for I,v in original.items():
            assert changed[I]==v==factor*reduced[I]
            entries.append({'columns':list(I),'minor':v,'transformed_minor':changed[I],
                            'quotient_minor':reduced[I],'metric_weight':prod(b[j] for j in I)})
        cb=sum(x['metric_weight']*x['minor']**2 for x in entries)
        cb_quotient=sum(x['metric_weight']*x['quotient_minor']**2 for x in entries)
        assert cb==c['detG']==determinant(c['G'])
        assert cb_quotient==c['detK']==determinant(c['K'])
        assert cb==factor**2*cb_quotient
        without_square=sum(x['metric_weight']*x['minor'] for x in entries)
        square_mutations+=without_square!=cb
        if c['F']>0 and cb_quotient:
            exponent_mutations+=cb!=factor*cb_quotient
        records.append({'D':D,'p':p,'R':R,'S':S,'J':1,'E':e,'Ehat':quotient,
            'B_diagonal':b,'F':c['F'],'minor_factor':factor,'minors':entries,
            'detG':cb,'detK':cb_quotient,'without_square':without_square})
    assert sum(len(c['minors']) for c in records)==220
    assert square_mutations>0 and exponent_mutations>0
    # General counterexamples, not replacements for the original jet Gram.
    identity=[[1,0],[0,1]];shear=[[1,1],[0,1]]
    g0=gram(identity,[1,1]);g1=gram(shear,[1,1])
    assert determinant(g0)==determinant(g1)==1
    assert prod(g0[i][i] for i in range(2))==1
    assert prod(g1[i][i] for i in range(2))==2
    p=3;g2=gram([[p,0],[0,1]],[1,1])
    assert determinant(g2)>0 and rank_mod(g2,p)==1
    controls={'omitted_square_cases_caught':square_mutations,
              'halved_exponent_nonzero_cases_caught':exponent_mutations,
              'shear_determinant':1,'diagonal_products':[1,2],
              'rank_reduction':{'real_rank':2,'mod3_rank':1}}
    all_minors=[x for c in records for x in c['minors']]
    payload={'scope':'Eight fixed saved Gram cases;new zero-order observations and exact exterior minors;not a new jet campaign or universal proof',
        'cases':records,'minor_count':len(all_minors),
        'nonzero_minors':sum(x['minor']!=0 for x in all_minors),
        'zero_determinants':sum(c['detG']==0 for c in records),'controls':controls}
    Path(sys.argv[1]).write_bytes((json.dumps(payload,indent=2)+'\n').encode())
    print('PASS131:8fixedcases/220maximalminors;weightedCauchyBinet/originalandquotientGram/minorfactors;4negativecontrolfamilies;no new cutoff or universal-proof claim')

if __name__=='__main__':main()
