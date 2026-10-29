"""Verify exact integration and preserved first-run evidence, never run Lean."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
d=json.loads((p/'PHASE117_RESULTS.json').read_bytes())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args,**kw):return subprocess.check_output(['git',*args],cwd=r,**kw)
assert d['status']=='EXACT_RADIAL_OPERATOR_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS'
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=r,check=True)
assert git('show',d['registered_commit']+':research/ender_radius_bridge/PHASE117_PROTOCOL.md')==(p/'PHASE117_PROTOCOL.md').read_bytes()
for name,h in d['sha256'].items():assert sha((r/name).read_bytes())==h,name
accepted=git('show',d['accepted_source_commit']+':research/ender_radius_bridge/Phase116RadialOperator.lean')
marker=b'#audit_namespace TenthDiscriminant.RadialOperator';i=accepted.index(marker)
source=accepted[:i].replace(b'import TenthDiscriminant\n',b'import TenthDiscriminant.PassiveTransport\n',1)
assert (r/'lean/TenthDiscriminant/RadialOperator.lean').read_bytes()==source
harness=b'import TenthDiscriminant\n\n'+accepted[i:].replace(b'phase116',b'phase117').replace(b'PHASE116',b'PHASE117')
assert (p/'Phase117InputCheck.lean').read_bytes()==harness
root=git('show',d['registered_commit']+':lean/TenthDiscriminant.lean')+b'import TenthDiscriminant.RadialOperator\n'
assert (r/'lean/TenthDiscriminant.lean').read_bytes()==root
assert root.count(b'import TenthDiscriminant.RadialOperator\n')==1
assert sha((p/d['archive']['path']).read_bytes())==d['archive']['sha256']
with zipfile.ZipFile(p/d['archive']['path']) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))==25
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert raw['PHASE117_CORRESPONDENCE.json']==(p/'PHASE117_CORRESPONDENCE.json').read_bytes()
logs={};caps={'build':600,'root':1200,'input':180,'audit':180}
expected={'build':['build','TenthDiscriminant.RadialOperator'],'root':'build','input':['env','lean','-j','1','../research/ender_radius_bridge/Phase117InputCheck.lean'],'audit':['env','lean','-j','1','Audit.lean']}
assert set(d['runs'])==set(caps)
for mode,x in d['runs'].items():
    assert len(list(p.glob(f'PHASE117_{mode}_*.result.json')))==1
    assert x['phase']==117 and x['mode']==mode and x['attempt']==1 and x['exit_code']==0 and x['stop_reason']==''
    assert x['time_limit_seconds']==caps[mode] and x['memory_threshold_mb']==8192
    assert 0<x['elapsed_seconds']<caps[mode] and 0<x['observed_peak_working_set_bytes']<8192*1024**2
    assert x['arguments']==expected[mode]
    prefix=x['source_snapshot'].removesuffix('.source.lean')
    assert json.loads(raw[prefix+'.result.json'])==x
    assert raw[prefix+'.source.lean']==source and raw[prefix+'.root.lean']==root and raw[prefix+'.input.lean']==harness
    assert sha(source)==x['source_sha256'] and raw[x['stderr']]==b''
    log=raw[x['stdout']].decode('utf-8-sig');logs[mode]=log
    assert ': error:' not in log and 'maximum number of heartbeats' not in log
    if mode in ('build','root'):assert 'Build completed successfully.' in log
assert 'AUDIT_OK TenthDiscriminant.RadialOperator: 57 logical declarations; 51 theorems; 11 runtime-only auxiliaries excluded' in logs['input']
assert logs['input'].count('PHASE117_INPUTS_OK ')==3
for name,count in d['fresh_closures'].items():assert f'PHASE117_INPUTS_OK TenthDiscriminant.RadialOperator.{name}: {count} reached;70forbidden roots excluded;axioms' in logs['input']
assert d['whole_audit_marker'] in logs['audit']
extract=lambda s:set(re.findall(r'DEPENDENCIES_CHECKED ([^;]+);',s))
with zipfile.ZipFile(p/'PHASE111_RAW.zip') as z:
    n=next(n for n in z.namelist() if '_audit_' in n and n.endswith('stdout.log'))
    old=extract(z.read(n).decode('utf-8-sig'))
new=extract(logs['audit']);added=sorted(new-old);removed=sorted(old-new)
corr=json.loads(raw['PHASE117_CORRESPONDENCE.json'])
assert len(old)==5393 and len(new)==5450 and len(added)==57 and not removed
assert added==corr['inventory']['added'] and removed==corr['inventory']['removed']
assert all(name.startswith('TenthDiscriminant.RadialOperator.') or '.TenthDiscriminant.RadialOperator.' in name for name in added)
assert corr['accepted_namespace_body_exact'] and corr['public_theorems']==27 and corr['definitions']==6
assert corr['source_sha256']==sha(source) and corr['accepted_source_sha256']==sha(accepted)
assert corr['root_after_sha256']==sha(root) and corr['harness_sha256']==sha(harness)
spec=importlib.util.spec_from_file_location('phase117_frozen_coverage',r/'lean/audit.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
assert len(module.project_coverage(r/'lean'))==corr['reachable_project_modules']==d['reachable_modules']==199
frozen={}
for record in git('ls-tree','-r','-z',d['registered_commit']).split(b'\0'):
    if not record:continue
    meta,name=record.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in d['reader_exceptions'] or name=='lean/TenthDiscriminant.lean':continue
    frozen[name]=meta.split()[2].decode()
assert len(frozen)==d['frozen_files']
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for name,h in zip(names,hashes):assert h==frozen[name],name
assert git('rev-parse','refs/heads/codex/control-priority-policy').decode().strip()==d['pinned_previous_source']
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):assert len((r/name).read_text(encoding='utf-8').splitlines())==61
print(f'PASS exact integration:27types/proofs/6definitions unchanged;4first successes;5450logical/4644theorems/17026runtime;57namespace additions/0removals;199modules;25raw;{len(frozen)}frozen Git blobs.')
print('CI is final-head/versioned separately. No Lean replay or cutoff improvement.')
