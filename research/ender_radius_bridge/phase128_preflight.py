"""Check exact accepted proof correspondence before each registered integration call."""
from pathlib import Path
import hashlib,json,re,subprocess,importlib.util
p=Path(__file__).resolve().parent;r=p.parents[1]
git=lambda *x:subprocess.check_output(['git',*x],cwd=r)
sha=lambda b:hashlib.sha256(b).hexdigest()
c=json.loads((p/'PHASE128_CORRESPONDENCE.json').read_bytes())
assert git('show',c['registered_commit']+':research/ender_radius_bridge/PHASE128_PROTOCOL.md')==(p/'PHASE128_PROTOCOL.md').read_bytes()
for new,x in c['modules'].items():
    src=git('show',x['accepted_commit']+':'+x['accepted_path'])
    assert sha(src)==x['accepted_sha256'] and src==(r/x['accepted_path']).read_bytes()
    a,b=x['body_range'];body=src[a:b]
    assert sha(body)==x['body_sha256']
    expected=(''.join('import TenthDiscriminant.'+s+'\n' for s in x['imports'])+'\n').encode()+body.replace(x['old_namespace'].encode(),new.encode())
    assert sha(expected)==x['source_sha256'] and (r/x['path']).read_bytes()==expected,new
root=git('show',c['registered_commit']+':lean/TenthDiscriminant.lean')
assert sha(root)==c['root_before_sha256']
expected=root+''.join('import TenthDiscriminant.'+x+'\n' for x in c['modules']).encode()
assert sha(expected)==c['root_after_sha256'] and (r/'lean/TenthDiscriminant.lean').read_bytes()==expected
h=(p/'Phase128InputCheck.lean').read_bytes()
assert sha(h)==c['harness_sha256'] and h.count(b'#check ')==19 and h.count(b'#audit_namespace ')==3
assert sum(len(re.findall(rb'^#phase128_'+str(n).encode()+rb'_inputs ',h,re.M)) for n in [125,126,127])==8
assert not re.search(rb'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',h)
changed=git('diff',c['registered_commit'],'--name-only','--','lean','.github').decode().splitlines()
assert set(changed)<={'lean/TenthDiscriminant.lean','lean/FORMALIZATION.md'}|{x['path'] for x in c['modules'].values()},changed
assert 'lean/TenthDiscriminant.lean' in changed
spec=importlib.util.spec_from_file_location('coverage128',r/'lean/audit.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert len(m.project_coverage(r/'lean'))==205
for x in p.glob('PHASE128_*.result.json'):
    d=json.loads(x.read_bytes());assert d['exit_code']==0 and not d['stop_reason'],'Integration stopped;do not retry'
print('PHASE128_PREFLIGHT_OK:19types/2helpers exact;3root imports;8fresh closures;205modules;old Lean/workflows unchanged')
