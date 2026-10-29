"""Verify saved Lean evidence and unchanged targets; NEVER invokes Lean."""
from pathlib import Path
import difflib,hashlib,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE116_RESULTS.json').read_bytes())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args,**kw):return subprocess.check_output(['git',*args],cwd=r,**kw)
assert d['status']=='FULL_OPERATOR_TARGET_PASS_STANDALONE'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE116_PROTOCOL.md')==(p/'PHASE116_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items():assert sha((r/name).read_bytes())==h,name
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==8
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['runs'])==2 and len(list(p.glob('PHASE116_build_*.result.json')))==2
assert sum(x['elapsed_seconds'] for x in d['runs'])==d['cumulative_elapsed_seconds']<1200
sources=[];logs=[]
for i,x in enumerate(d['runs'],1):
    assert x['attempt']==i and x['phase']==116 and x['mode']=='build'
    assert x['exit_code']==(1 if i==1 else 0) and x['stop_reason']==''
    assert x['time_limit_seconds']==600 and x['memory_threshold_mb']==8192
    assert 0<x['elapsed_seconds']<600 and 0<x['observed_peak_working_set_bytes']<8192*1024**2
    assert x['protocol_commit']==d['registered_commit'][:7]
    assert x['cwd'].replace('\\','/').endswith('/work/tenth-discriminant/lean')
    assert x['arguments']==['env','lean','-j','1','../../tenth-radial-blocks/research/ender_radius_bridge/Phase116RadialOperator.lean']
    source=raw[x['source_snapshot']];sources.append(source.decode())
    assert sha(source)==x['source_sha256']
    prefix=x['source_snapshot'].removesuffix('.source.lean')
    assert json.loads(raw[prefix+'.result.json'])==x and raw[x['stderr']]==b''
    log=raw[x['stdout']].decode('utf-8-sig');logs.append(log)
    assert 'maximum number of heartbeats' not in log and 'maximum recursion depth' not in log
    if i==1:
        assert 'error:' in log and 'NONSTANDARD_AXIOMS TenthDiscriminant.RadialOperator.integer_bridge' in log
        assert 'AUDIT_OK TenthDiscriminant.RadialOperator:' not in log
    else:
        assert 'error:' not in log and "declaration uses 'sorry'" not in log
        assert log.count('AUDIT_OK TenthDiscriminant.RadialOperator:')==1
        assert 'AUDIT_OK TenthDiscriminant.RadialOperator: 57 logical declarations; 51 theorems; 11 runtime-only auxiliaries excluded' in log
        for root,count in d['fresh_closures'].items():
            assert f'PHASE116_INPUTS_OK TenthDiscriminant.RadialOperator.{root}: {count} reached;70forbidden roots excluded;axioms' in log
        assert log.count('PHASE116_INPUTS_OK ')==3
assert (p/'Phase116RadialOperator.lean').read_bytes()==sources[1].encode()
def surface(s):return {'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',s)},'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',s)}}
frozen_surface=json.loads((p/'PHASE116_FROZEN_SURFACE.json').read_bytes())
assert surface(sources[0])==surface(sources[1])==frozen_surface
assert list(frozen_surface['types'])==d['public_theorems'] and len(d['public_theorems'])==27
assert list(frozen_surface['definitions'])==d['definitions'] and len(d['definitions'])==6
for name in d['public_theorems']:
    assert f'#check TenthDiscriminant.RadialOperator.{name}\n' in sources[1]
    assert f'TenthDiscriminant.RadialOperator.{name}' in logs[1]
for name in d['definitions']:assert f'#print TenthDiscriminant.RadialOperator.{name}\n' in sources[1]
assert not re.search(r'(?m)^\s*(axiom|unsafe|set_option maxHeartbeats|set_option maxRecDepth)\b',sources[1])
assert not re.search(r'\bsorry\b|\badmit\b|\bnative_decide\b',sources[1])
repair=json.loads((p/'PHASE116_REPAIR1.json').read_bytes())
assert repair['unified_diff']==list(difflib.unified_diff(sources[0].splitlines(),sources[1].splitlines(),fromfile='attempt1',tofile='attempt2'))
old=(p/'Phase110PassiveTransport.lean').read_text(encoding='utf-8')
block=lambda s:re.search(r'let forbidden[^\n]*[\s\S]*?for name in forbidden',s).group()
assert block(sources[1])==block(old) and block(old).count('``')==70
frozen={}
for record in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not record:continue
    meta,name=record.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in d['reader_exceptions']:continue
    frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(hashes)==len(names)
for name,h in zip(names,hashes):assert h==frozen[name],name
assert git('rev-parse','refs/heads/codex/control-priority-policy').decode().strip()==d['base_source']
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):assert len((r/name).read_text(encoding='utf-8').splitlines())==61
print(f'PASS saved universal operator evidence:FAIL then FULLPASS;27types/6definitions byte-exact;57logical/51theorems;3fresh closures;8raw;{len(frozen)}frozen Git blobs.')
print('Standalone algebraic bridge ONLY. No Lean replay, quantitative gain, cutoff upgrade, integration or CI.')
