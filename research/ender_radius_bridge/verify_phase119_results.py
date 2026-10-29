"""Read-only verification of the full same-integer upper bound; never run Lean."""
from pathlib import Path
import difflib,hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
d=json.loads((p/'PHASE119_RESULTS.json').read_bytes())
assert d['status']=='FULL_SAME_INTEGER_PRODUCTION_RADIUS_UPPER_BOUND_PASS_STANDALONE'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE119_PROTOCOL.md')==(p/'PHASE119_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items():assert sha((r/name).read_bytes())==h,name
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==8
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==len(list(p.glob('PHASE119_build_*.result.json')))==2
assert sum(x['elapsed_seconds'] for x in d['runs'])==d['cumulative_elapsed_seconds']<1200
accepted=git('show',d['accepted_dependency_commit']+':research/ender_radius_bridge/Phase118RadialJetMajorant.lean').decode()
dependency=accepted[:accepted.index('#audit_namespace TenthDiscriminant.RadialJetMajorant')]
assert sha(dependency.encode())==d['accepted_dependency_sha256']
sources=[];logs=[]
for i,x in enumerate(d['runs'],1):
    assert x['attempt']==i and x['phase']==119 and x['mode']=='build'
    assert x['exit_code']==(1 if i==1 else 0) and x['stop_reason']==''
    assert x['time_limit_seconds']==600 and x['memory_threshold_mb']==8192
    assert x['protocol_commit']==d['registered_commit'][:7]
    assert 0<x['elapsed_seconds']<600 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
    assert x['arguments']==['env','lean','-j','1','../../tenth-radial-blocks/research/ender_radius_bridge/Phase119RadialDetBound.lean']
    assert x['cwd'].replace('\\','/').endswith('/work/tenth-discriminant/lean')
    source=raw[x['source_snapshot']];sources.append(source.decode());assert source.startswith(dependency.encode())
    assert sha(source)==x['source_sha256']
    prefix=x['source_snapshot'].removesuffix('.source.lean')
    assert json.loads(raw[prefix+'.result.json'])==x and raw[x['stderr']]==b''
    for suffix in ('.source.lean','.stdout.log','.stderr.log','.result.json'):
        assert (p/(prefix+suffix)).read_bytes()==raw[prefix+suffix]
    log=raw[x['stdout']].decode('utf-8-sig');logs.append(log)
    assert not re.search(r'maximum number of heartbeats|maximum recursion depth|deterministic.*timeout',log)
    if i==1:
        assert 'error:' in log and 'NONSTANDARD_AXIOMS' in log
        assert 'PHASE119_NONSTANDARD_AXIOM sorryAx' in log and d['audit_marker'] not in log
    else:
        assert 'error:' not in log and "declaration uses 'sorry'" not in log and 'NONSTANDARD' not in log
        assert log.count(d['audit_marker'])==1 and log.count('warning:')==5
        assert log.count('PHASE119_INPUTS_OK ')==3
        for name,count in d['fresh_closures'].items():
            m=re.search(rf'PHASE119_INPUTS_OK TenthDiscriminant.RadialDetBound\.{name}: {count} reached;70forbidden roots excluded;axioms \[([^]]+)\]',log)
            assert m and set(re.findall(r'[\w.]+',m[1]))=={'propext','Quot.sound','Classical.choice'}

def surface(s):
    s=s[s.index('namespace TenthDiscriminant.RadialDetBound'):]
    return {'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',s)},
      'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',s)}}
frozen_surface=json.loads((p/'PHASE119_FROZEN_SURFACE.json').read_bytes())
assert surface(sources[0])==surface(sources[1])==frozen_surface
assert list(frozen_surface['types'])==d['public_theorems'] and len(d['public_theorems'])==22
assert list(frozen_surface['definitions'])==d['definitions'] and len(d['definitions'])==4
assert (p/'Phase119RadialDetBound.lean').read_bytes()==sources[-1].encode()
for s in sources:
    assert not re.search(r'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',s)
    for name in d['public_theorems']:assert '#check TenthDiscriminant.RadialDetBound.'+name+'\n' in s
    for name in d['definitions']:assert '#print TenthDiscriminant.RadialDetBound.'+name+'\n' in s
for name in d['public_theorems']:assert 'TenthDiscriminant.RadialDetBound.'+name in logs[-1]
repair=json.loads((p/'PHASE119_REPAIR1.json').read_bytes())
assert repair['before_sha256']==sha(sources[0].encode()) and repair['after_sha256']==sha(sources[1].encode())
assert repair['prior_attempt']==d['runs'][0]
assert repair['diff']==''.join(difflib.unified_diff(sources[0].splitlines(True),sources[1].splitlines(True),fromfile='attempt1',tofile='attempt2'))
old=(p/'Phase116RadialOperator.lean').read_bytes().decode()
extract=lambda s:s[s.index('  let forbidden : Array Name := #['):s.index('  for name in forbidden do')]
assert extract(sources[-1])==extract(old)
frozen={}
for rec in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not rec:continue
    meta,name=rec.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in d['reader_exceptions']:continue
    frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']==1784
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for name,h in zip(names,hashes):assert h==frozen[name],name
assert (d['published_cutoff'],d['candidate_cutoff'],d['geometry_domain_lower'])==(50000000000,48000000000,41006250000)
assert d['normalized_upper']=='4/5*logD-823/1000'
print('PASS saved119: FAIL then FULLPASS;22types/4definitions and accepted118 dependency exact;55logical/51theorems;3fresh closures/70exclusions;8raw;1784frozen Git blobs. Actual production-radius original integer determinant upper bound;not a48b cutoff.')
