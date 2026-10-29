"""Sealed phase113 finite feasibility only; no new Lean/cutoff claim."""
import ast, base64, hashlib, json, math, subprocess, sys, time
from collections import defaultdict
from decimal import Decimal, localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = '7913eba8ac3ec0bcf765036ba5cebd8f0197463f'
SOURCE_HASHES = {}
def load_functions(name, names):
    raw = (ROOT/name).read_bytes()
    assert raw == subprocess.check_output(['git','show',BASE+':'+name],cwd=ROOT)
    SOURCE_HASHES[name] = hashlib.sha256(raw).hexdigest()
    tree = ast.parse(raw)
    functions = [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in functions} == set(names)
    env = {'math':math}
    exec(compile(ast.Module(body=functions,type_ignores=[]),name,'exec'),env)
    return env
ALG = load_functions('tools/verify_exact.py', ['mul','powers','gram'])
OLD = load_functions('tools/radial_bounds.py', ['radial_moments','diagonal','cross','annulus_points','radial_partition'])
WEIGHT = load_functions('tools/green_h1.py', ['G_sum','g','F_exact'])

def encoded(n):
    return {'sign':(n>0)-(n<0),'bits':abs(n).bit_length(),
            'b64':base64.b64encode(abs(n).to_bytes((abs(n).bit_length()+7)//8,'big')).decode()}

def determinant(matrix):
    n = len(matrix)
    if not n: return 1
    a = [list(row) for row in matrix]
    assert all(len(row)==n for row in a)
    sign, previous = 1,1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None: return 0
        if pivot != k:
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*v-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
            a[i][k]=0
        previous=v
    return sign*a[-1][-1]

def groups(R,S):
    out=defaultdict(list)
    for r in range(R):
        for s in range(S):out[r-s].append((r,s))
    return [out[k] for k in sorted(out)]

def validate(partition,R,S):
    flat=[row for block in partition for row in block]
    if sorted(flat)!=[(r,s) for r in range(R) for s in range(S)]:
        raise ValueError('partition overlap or missing row')
    if any(not block or len({r-s for r,s in block})!=1 for block in partition):
        raise ValueError('mixed angular weights')

def entry(m,r,s,t,u,J):
    if r+u!=t+s:raise ValueError('nonmatching integer weights')
    return 2*sum(math.perm(r,j)*math.perm(t,j)*m[r+u-j]
                 for j in range(min(r,t,J-1)+1))

def block_products(D,P,R,S,J,small=False):
    m=OLD['radial_moments'](D,P,R+S-2)
    partition=groups(R,S);validate(partition,R,S)
    diagonals={(r,s):OLD['diagonal'](m,r,s,J) for r in range(R) for s in range(S)}
    H=math.prod(diagonals.values())
    pairs,singles=OLD['radial_partition'](R,S,J)
    B2=math.prod(diagonals[row] for row in singles)
    for (r,s),other in pairs:
        B2*=diagonals[r,s]*diagonals[other]-OLD['cross'](m,r,s,J)**2
    BK=1;blocks=[]
    for block in partition:
        matrix=[[entry(m,r,s,t,u,J) for t,u in block] for r,s in block]
        value=determinant(matrix)
        BK*=value
        blocks.append({'weight':block[0][0]-block[0][1],'rows':block,'det':encoded(value)})
    return m,H,B2,BK,blocks

def controls():
    assert determinant([])==1 and determinant([[3]])==3
    assert determinant([[0,1],[1,0]])==-1
    assert determinant([[1,1],[1,1]])==0
    assert determinant([[1,2,3],[0,4,5],[1,0,6]])==22
    cases=[]
    cohorts=[(7,[(0,0),(2,1),(-1,2),(3,-1)]),(19,[(x,y) for x in range(3) for y in range(2)])]
    for D,P in cohorts:
        for J in (1,2,6):cases.append((D,P,4,3,J))
    cases.append((1,[(1,0),(-1,0)],3,3,1))
    evidence=[]
    for D,P,R,S,J in cases:
        G=ALG['gram'](P,R,S,J,D)
        m,H,B2,BK,blocks=block_products(D,P,R,S,J)
        for block in groups(R,S):
            for r,s in block:
                for t,u in block:assert entry(m,r,s,t,u,J)==G[r*S+s][t*S+u]
        actual=determinant(G)
        assert 0<=actual<=BK<=B2<=H
        evidence.append({'D':D,'points':P,'R':R,'S':S,'J':J,'gram':G,
                         'det':actual,'block':encoded(BK),'paired':encoded(B2),'diagonal':encoded(H)})
    P=cohorts[0][1];m=OLD['radial_moments'](7,P,8)
    correct=entry(m,0,0,1,1,1)
    assert correct!=correct//2 and correct!=2*m[2]
    assert entry(m,1,1,1,1,2)>entry(m,1,1,1,1,1)
    for rows in ((0,2,0,1),(0,1,1,0)):
        try:entry(m,*rows,1)
        except ValueError:pass
        else:raise AssertionError('invalid angular label accepted')
    broken=groups(4,3);broken[0].append(broken[0][0])
    try:validate(broken,4,3)
    except ValueError:pass
    else:raise AssertionError('overlap accepted')
    missing=groups(4,3);missing[0].pop()
    try:validate(missing,4,3)
    except ValueError:pass
    else:raise AssertionError('missing row accepted')
    assert ALG['gram'](P,4,3,1,7)[0][3]!=0
    assert groups(4,3)[0][0]==(0,2)
    for p in (3,5,7):
        for R in (1,4,9):
            for S in (1,2,4):
                assert sum(min(r//p,s) for r in range(R) for s in range(S))==WEIGHT['F_exact'](p,R,S)
    return {'kind':'controls','full_grams':evidence,'mutations':'factor2/exponent/extra jet/angular label/negative weight/overlap/missing row/false orthogonality rejected','weight_comparisons':27}

def primes(R):
    return [p for p in range(3,R+1,2) if all(p%d for d in range(2,math.isqrt(p)+1))]

def log_integer(n):
    assert n>0
    shift=max(0,n.bit_length()-1024)
    return Decimal(n>>shift).ln()+Decimal(shift)*Decimal(2).ln()

def diagnostics(H,B2,BK,lower,scale,precision):
    with localcontext() as ctx:
        ctx.prec=precision
        h,b,k,l=map(log_integer,(H,B2,BK,lower))
        return {'digits':precision,'full_gain':str((h-k)/scale),
                'pair_gain':str((h-b)/scale),'extra_gain':str((b-k)/scale),
                'gap_above_actual_inert':str((k-l)/scale)}

def campaign(output):
    with output.open('x',encoding='utf-8',newline='\n') as f:
        def save(row):f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush()
        save({'kind':'inputs','base':BASE,'source_sha256':SOURCE_HASHES,
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'encoding':'signed base64 big-endian magnitude; zero has empty magnitude',
              'scope':'finite exact arithmetic plus approximate log diagnostics; no Lean/all-range/cutoff theorem'})
        save(controls());print('CONTROLS_PASS seven full matrices and registered adversarial cases',flush=True)
        focal=[];statuses=[]
        for D in (19,43,163):
            P=OLD['annulus_points'](D);lines={y:sum(y==v for _,v in P) for _,y in P}
            L,M=max(lines.values()),len(lines);J=L+M
            for R in (40,80,160,320):
                started=time.perf_counter();S=R//25
                guard=J>=L+M and len(P)*J>2*R*S+J*(R+S)
                row={'kind':'case','D':D,'R':R,'S':S,'J':J,'L':L,'M':M,'points':P,
                     'rank_guard':guard,'strict_inertness_guard':4*R<D+1}
                if not guard:
                    row['status']='NO CERTIFICATE: sufficient rank guard failed'
                else:
                    m,H,B2,BK,blocks=block_products(D,P,R,S,J)
                    inert=[p for p in primes(R) if pow((-D)%p,(p-1)//2,p)==p-1]
                    lower=math.prod(p**(2*WEIGHT['F_exact'](p,R,S)) for p in inert)
                    assert 0<BK<=B2<=H and lower<=BK
                    row.update({'status':'FINITE GUARDED MOMENT PRODUCT','moments':[encoded(n) for n in m],
                                'blocks':blocks,'products':{n:encoded(v) for n,v in [('H',H),('B2',B2),('BK',BK),('lower',lower)]},
                                'actual_inert_primes':inert,'diagnostics':[diagnostics(H,B2,BK,lower,R*R*S,q) for q in (80,160)]})
                if R==160:
                    if not guard:focal.append('FAIL')
                    else:
                        values=[Decimal(v['full_gain']) for v in row['diagnostics']]
                        focal.append('UNRESOLVED' if any(abs(v-Decimal('.02'))<=Decimal('1e-60') for v in values)
                                     else 'PASS' if all(v>=Decimal('.02') for v in values) else 'FAIL')
                row['elapsed_seconds']=time.perf_counter()-started
                save(row);statuses.append(row['status'])
                print(json.dumps({k:row[k] for k in ('D','R','S','J','rank_guard','status','elapsed_seconds')}),flush=True)
                if guard:print('GAIN',row['diagnostics'][0]['full_gain'],'EXTRA',row['diagnostics'][0]['extra_gain'],flush=True)
        gate='UNRESOLVED' if 'UNRESOLVED' in focal else 'PASS' if focal==['PASS']*3 else 'FAIL'
        save({'kind':'summary','cases':len(statuses),'guarded':sum(s=='FINITE GUARDED MOMENT PRODUCT' for s in statuses),
              'focal_R160':focal,'feasibility_gate':gate,'interpretation':'a passing finite gate only justifies a future uniform-estimate attempt; no new cutoff'})
        print('FEASIBILITY_GATE',gate,'FOCAL',focal,flush=True)

if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1]=='--output'
    campaign(Path(sys.argv[2]))
