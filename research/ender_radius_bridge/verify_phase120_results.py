"""Read-only check of the complete first-call actual-field cutoff evidence."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
d=json.loads((p/'PHASE120_RESULTS.json').read_bytes())
assert d['status']=='FULL_ACTUAL_FIELD_48B_CUTOFF_FIRST_CALL_PASS_STANDALONE'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE120_PROTOCOL.md')==(p/'PHASE120_PROTOCOL.md').read_bytes()
for n,h in d['sha256'].items():assert sha((r/n).read_bytes())==h,n
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==4
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==len(list(p.glob('PHASE120_build_*.result.json')))==1
assert not list(p.glob('PHASE120_REPAIR*.json'))
x=d['runs'][0]
assert x['attempt']==1 and x['phase']==120 and x['mode']=='build' and x['exit_code']==0 and x['stop_reason']==''
assert x['time_limit_seconds']==600 and x['memory_threshold_mb']==8192 and x['cumulative_before_seconds']==0
assert x['protocol_commit']==d['registered_commit'][:7]
assert 0<x['elapsed_seconds']==d['cumulative_elapsed_seconds']<600
assert 0<x['observed_peak_working_set_bytes']<8192*1024**2
assert x['arguments']==['env','lean','-j','1','../../tenth-radial-blocks/research/ender_radius_bridge/Phase120RadialCutoff.lean']
assert x['cwd'].replace('\\','/').endswith('/work/tenth-discriminant/lean')
source=raw[x['source_snapshot']];s=source.decode();assert sha(source)==x['source_sha256']
prefix=x['source_snapshot'].removesuffix('.source.lean')
assert json.loads(raw[prefix+'.result.json'])==x and raw[x['stderr']]==b''
for suffix in ('.source.lean','.stdout.log','.stderr.log','.result.json'):
    assert (p/(prefix+suffix)).read_bytes()==raw[prefix+suffix]
assert (p/'Phase120RadialCutoff.lean').read_bytes()==source
accepted=git('show',d['accepted_dependency_commit']+':research/ender_radius_bridge/Phase119RadialDetBound.lean').decode()
dependency=accepted[:accepted.index('#audit_namespace TenthDiscriminant.RadialDetBound')]
assert s.startswith(dependency) and sha(dependency.encode())==d['accepted_dependency_sha256']
body=s[s.index('namespace TenthDiscriminant.RadialCutoff'):]
surface={'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',body)},
  'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',body)}}
assert surface==json.loads((p/'PHASE120_FROZEN_SURFACE.json').read_bytes())
assert list(surface['types'])==d['public_theorems'] and len(d['public_theorems'])==15
assert surface['definitions']=={} and d['definitions']==[]
assert not re.search(r'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',s)
for n in d['public_theorems']:assert '#check TenthDiscriminant.RadialCutoff.'+n+'\n' in s
log=raw[x['stdout']].decode('utf-8-sig')
assert 'error:' not in log and "declaration uses 'sorry'" not in log and 'NONSTANDARD' not in log
assert not re.search(r'maximum number of heartbeats|maximum recursion depth|deterministic.*timeout',log)
assert log.count(d['audit_marker'])==1 and log.count('warning:')==5
assert log.count('PHASE120_INPUTS_OK ')==3
for n,c in d['fresh_closures'].items():
    m=re.search(rf'PHASE120_INPUTS_OK TenthDiscriminant.RadialCutoff\.{n}: {c} reached;73forbidden roots excluded;axioms \[([^]]+)\]',log)
    assert m and set(re.findall(r'[\w.]+',m[1]))=={'propext','Quot.sound','Classical.choice'}
assert d['final_declaration'] in log and '58736 reached;73forbidden roots excluded' in log
extract=lambda text:set(re.findall(r'``(TenthDiscriminant\.[\w.]+)',text[text.index('  let forbidden : Array Name := #['):text.index('  for name in forbidden do')]))
policy=json.loads((p/'PHASE120_DEPENDENCY_POLICY.json').read_bytes());assert policy==d['dependency_policy']
assert len(policy['allowed_from_earlier_operator_exclusions'])==4 and len(policy['additional_exclusions'])==7
assert extract(s)==(extract(accepted)-set(policy['allowed_from_earlier_operator_exclusions']))|set(policy['additional_exclusions'])
assert len(extract(s))==policy['forbidden_roots']==d['forbidden_roots']==73
frozen={}
for rec in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not rec:continue
    meta,n=rec.split(b'\t',1);n=n.decode()
    if n.startswith('.agent/') or n in d['reader_exceptions']:continue
    frozen[n]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']==1796
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for n,h in zip(names,hashes):assert h==frozen[n],n
assert (d['published_integrated_cutoff'],d['checked_standalone_actual_field_cutoff'])==(50000000000,48000000000)
print('PASS saved120:FIRST_CALL_FULLPASS;15types/0data;exact118+119 dependencies;28logical/28theorems;3fresh closures/73registered exclusions;4raw;1796frozen Git blobs. Actual arbitrary-field48b theorem standalone;integration/CI pending.')
