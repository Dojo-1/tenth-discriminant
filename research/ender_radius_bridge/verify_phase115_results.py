"""Validate saved finite certificates; never import/execute the trial or Lean."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,itertools,json,math,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE115_RESULTS.json').read_bytes())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args,**kw):return subprocess.check_output(['git',*args],cwd=r,**kw)
assert d['status']=='FINITE_CHECKS_PASS_PAPER_CANDIDATE_ONLY'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE115_PROTOCOL.md')==(p/'PHASE115_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items():assert sha((r/name).read_bytes())==h,name
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==5
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
x=d['run'];prefix=x['data'].removesuffix('.data.jsonl')
assert json.loads(raw[prefix+'.result.json'])==x
assert x['attempt']==1 and x['exit_code']==0 and x['stop_reason']==''
assert x['time_limit_seconds']==120 and 0<x['elapsed_seconds']<120
assert x['memory_threshold_mb']==8192 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
assert raw[x['source_snapshot']]==(p/'phase115_radial_centering.py').read_bytes()
assert sha(raw[x['source_snapshot']])==x['source_sha256']
assert raw[x['stderr']]==b'' and len(list(p.glob('PHASE115_trial_*.result.json')))==1
rows=[json.loads(line) for line in raw[x['data']].splitlines()]
assert len(rows)==164 and rows[0]['kind']=='inputs' and rows[-1]['kind']=='summary'
assert rows[0]['base']==d['previous_evidence'] and rows[0]['source_sha256']==x['source_sha256']
assert rows[0]['rectangles']==[[0,3],[3,0],[1,1],[4,3],[3,4],[6,2]]
assert [v[0] for v in rows[0]['cohorts']]==[1,7,19] and rows[0]['a']==[-2,0,3] and rows[0]['J']==[0,1,4]
expected=[(D,R,S,a,J) for D,_ in rows[0]['cohorts'] for R,S in rows[0]['rectangles'] for a in (-2,0,3) for J in (0,1,4)]
cases=rows[1:-1]
assert [(v['D'],v['R'],v['S'],v['a'],v['J']) for v in cases]==expected
# Independent rational Gaussian elimination on the recorded matrices,
# distinct from the trial's fraction-free Bareiss implementation.
def det(A):
    B=[[F(v) for v in row] for row in A];n=len(B);answer=F(1)
    for k in range(n):
        i=next((i for i in range(k,n) if B[i][k]),None)
        if i is None:return F(0)
        if i!=k:B[i],B[k]=B[k],B[i];answer=-answer
        v=B[k][k];answer*=v
        for i in range(k+1,n):
            c=B[i][k]/v
            for j in range(k+1,n):B[i][j]-=c*B[k][j]
    return answer
positive=singular=0
for v in cases:
    n=v['R']*v['S'];T,G,H=v['T'],v['G'],v['H']
    assert all(len(A)==n and all(len(row)==n for row in A) for A in (T,G,H))
    assert all(T[i][i]==1 and all(T[i][j]==0 for j in range(i+1,n)) for i in range(n))
    for i in range(n):
        rr,ss=divmod(i,v['S']);m=min(rr,ss)
        expected_row=[0]*n
        for t in range(m+1):expected_row[(rr-t)*v['S']+ss-t]=math.comb(m,t)*(-v['a'])**t
        assert T[i]==expected_row
    TG=[[sum(T[i][k]*G[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    assert H==[[sum(TG[i][k]*T[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    assert det(T)==1 and det(G)==det(H)==v['det']>=0
    positive+=v['det']>0;singular+=v['det']==0
    assert all(p0==p1 for _,p0,p1 in v['ranks'])
    for prime,e,status in v['divisors']:
        assert pow((-v['D'])%prime,(prime-1)//2,prime)==prime-1
        assert v['det']%(prime**e)==0
        assert (status=='positive')==(v['det']>0)
s=rows[-1];assert s==d['summary'] and (positive,singular)==(99,63)
assert (s['jet_comparisons'],s['envelope_comparisons'],s['coefficient_cases'],s['eligible_checks'])==(7770,7770,4910,3516)
assert len(s['mutation_witnesses'])==9 and all(s['mutation_witnesses'].values())
for cert in s['log_bounds'].values():
    value=F(*cert['x']);q=(value-1)/(value+1);N=100
    lo=2*sum((q**(2*k+1)/(2*k+1) for k in range(N)),F(0))
    hi=lo+2*q**(2*N+1)/((2*N+1)*(1-q*q))
    assert (lo,hi)==(F(*cert['lower']),F(*cert['upper']))
    assert F(*cert['required_lower'])<=lo<hi
assert F(*s['gain_lower'])==F(2277,169000)>F(*s['fixed_gain'])==F(13,1000)
u=13*F(6931,10000)+F(109,100)+9*F(1609,1000)
assert u==F(*s['log_endpoint_lower']) and s['endpoint']==48000000000==2**13*3*5**9
slope=F(999997,1000000)-F(4,5)
assert slope==F(*s['affine_slope'])>0
assert slope*u-F(5739,1000)+F(813,1000)+F(13,1000)==F(*s['candidate_margin'])==F(31862561,10000000000)>0
frozen={}
for record in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not record:continue
    meta,name=record.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in d['reader_exceptions']:continue
    frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for name,h in zip(names,hashes):assert h==frozen[name],name
assert git('rev-parse','refs/heads/codex/control-priority-policy').decode().strip()==d['base_source']
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):assert len((r/name).read_text(encoding='utf-8').splitlines())==61
print(f'PASS saved evidence:162complete matrix certificates, independent determinants, rational log/margin certificates,5raw,{len(frozen)}frozen Git blobs.')
print('Finite/paper candidate48bONLY. Published checked cutoff50b; no trial or Lean replay.')
