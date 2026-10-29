"""Verify preserved partial certificates only. Never imports or reruns the trial."""
from pathlib import Path
from decimal import Decimal
import base64,hashlib,json,math,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE113_RESULTS.json').read_bytes())
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,**kw):return subprocess.check_output(['git',*args],cwd=r,**kw)
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE113_PROTOCOL.md')==(p/'PHASE113_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items():assert sha((r/name).read_bytes())==h,name
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==5
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
x=d['run'];stem=x['data'].removesuffix('.data.jsonl')
assert json.loads(raw[stem+'.result.json'])==x
assert x['phase']==113 and x['attempt']==1 and x['exit_code']==99 and x['stop_reason']=='time_limit'
assert x['time_limit_seconds']==180 and x['elapsed_seconds']>=180 and x['memory_threshold_mb']==8192
assert x['observed_peak_working_set_bytes'] is None or 0<x['observed_peak_working_set_bytes']<8192*1024**2
assert raw[x['source_snapshot']]==(p/'phase113_radial_blocks.py').read_bytes()
assert sha(raw[x['source_snapshot']])==x['source_sha256']
rows=[json.loads(line) for line in raw[x['data']].splitlines()]
assert rows[0]['kind']=='inputs' and rows[0]['base']==d['base']
assert rows[0]['script_sha256']==x['source_sha256']
for name,h in rows[0]['source_sha256'].items():assert sha((r/name).read_bytes())==h
assert rows[1]['kind']=='controls' and len(rows[1]['full_grams'])==7 and rows[1]['weight_comparisons']==27
assert not any(v['kind']=='summary' for v in rows)
cases=[v for v in rows if v['kind']=='case']
grid=[(D,R,R//25) for D in (19,43,163) for R in (40,80,160,320)]
assert [(v['D'],v['R'],v['S']) for v in cases]==grid[:11]
assert len(cases)==11 and grid[11]==(163,320,12)
def decode(v):
 b=base64.b64decode(v['b64'],validate=True);n=int.from_bytes(b,'big')
 assert n.bit_length()==v['bits'] and (not b or b[0]!=0)
 assert v['sign'] in (-1,0,1) and (v['sign']==0)==(n==0)
 return v['sign']*n
focal=[];guarded=0
for v in cases:
 P=[tuple(q) for q in v['points']];D,R,S,J=v['D'],v['R'],v['S'],v['J']
 assert len(P)==len(set(P)) and all(18*D<=a*a+D*b*b<=36*D for a,b in P)
 lines={b:sum(b==y for _,y in P) for _,b in P};L,M=max(lines.values()),len(lines)
 assert (L,M,J)==(v['L'],v['M'],L+M)
 guard=J>=L+M and len(P)*J>2*R*S+J*(R+S)
 assert guard==v['rank_guard'] and v['strict_inertness_guard']==(4*R<D+1)
 if not guard:
  assert v['status']=='NO CERTIFICATE: sufficient rank guard failed' and 'products' not in v
  continue
 guarded+=1
 products={k:decode(n) for k,n in v['products'].items()}
 assert 0<products['lower']<=products['BK']<=products['B2']<=products['H']
 assert math.prod(decode(b['det']) for b in v['blocks'])==products['BK']
 flat=[tuple(q) for b in v['blocks'] for q in b['rows']]
 assert sorted(flat)==[(a,b) for a in range(R) for b in range(S)]
 assert all(all(a-b==block['weight'] for a,b in block['rows']) for block in v['blocks'])
 assert len(v['moments'])==R+S-1 and decode(v['moments'][0])==len(P)
 assert [q['digits'] for q in v['diagnostics']]==[80,160]
 for name in ('full_gain','pair_gain','extra_gain','gap_above_actual_inert'):
  a,b=[Decimal(q[name]) for q in v['diagnostics']]
  assert abs(a-b)<Decimal('1e-70')
 if R==40:assert all(Decimal(q['full_gain'])==0 for q in v['diagnostics'])
 if R==160:
  assert all(Decimal(q['full_gain'])>Decimal('.02')+Decimal('1e-60') for q in v['diagnostics'])
  focal.append((D,v['diagnostics'][0]['full_gain']))
assert guarded==9 and len(focal)==3 and focal==[tuple(q) for q in d['partial_focal_gains']]
assert d['status']=='RESOURCE_STOP_INCOMPLETE_NO_GATE_ACCEPTANCE'
frozen={}
for record in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
 if not record:continue
 meta,name=record.split(b'\t',1);name=name.decode()
 if name.startswith('.agent/') or name in d['reader_exceptions']:continue
 frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']
names=sorted(frozen)
hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(hashes)==len(names)
for name,h in zip(names,hashes):assert h==frozen[name],name
assert git('rev-parse','refs/heads/codex/control-priority-policy').decode().strip()==d['base']
receipt=json.loads((p/'PR40_MERGE_RECEIPT.json').read_bytes())
assert receipt['source']==d['base'] and receipt['conclusion']=='success'
assert git('show','-s','--format=%T',receipt['actual_merge']).decode().strip()==receipt['tree']
assert sha((p/'PR40_CI_EVIDENCE.zip').read_bytes())==receipt['archive_sha256']
with zipfile.ZipFile(p/'PR40_CI_EVIDENCE.zip') as z:
 assert {n:sha(z.read(n)) for n in z.namelist()}==receipt['sha256']
 assert json.loads(z.read('job'))['conclusion']=='success'
 assert z.read('job.log').count(b'CONTROL_FAMILY_OK ')==8
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):
 assert len((r/name).read_text(encoding='utf-8').splitlines())==61
print(f'PASS: preserved180sRESOURCE_STOP;11/12case prefix,9guarded/2no-certificate;7smallGramcontrols;3focal observations ONLY;5raw;{len(frozen)}base Git blobs frozen; PR40success/tree receipt separate.')
print('NO complete feasibility verdict, trial rerun, missing-case reconstruction, new Lean theorem or cutoff gain.')
