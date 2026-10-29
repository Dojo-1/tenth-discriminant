"""Static exact integration checks; no Lean invocation or numerical trial."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess
p=Path(__file__).resolve().parent;r=p.parents[1]
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
sha=lambda b:hashlib.sha256(b).hexdigest()
c=json.loads((p/'PHASE121_CORRESPONDENCE.json').read_bytes())
assert git('branch','--show-current').decode().strip()=='codex/radial-cutoff-integration'
assert git('show',c['registered_commit']+':research/ender_radius_bridge/PHASE121_PROTOCOL.md')==(p/'PHASE121_PROTOCOL.md').read_bytes()
for name,x in c['modules'].items():
    source=git('show',c['accepted_commit']+':'+x['accepted_path'])
    assert sha(source)==x['accepted_sha256']
    a,b=x['body_range'];body=source[a:b]
    assert body.endswith(('end TenthDiscriminant.'+name+'\n').encode())
    expected=(''.join('import TenthDiscriminant.'+i+'\n' for i in x['imports'])+'\n').encode()+body
    assert sha(body)==x['body_sha256'] and sha(expected)==x['source_sha256']
    assert (r/x['path']).read_bytes()==expected,name
root=git('show',c['registered_commit']+':lean/TenthDiscriminant.lean')
newroot=root+''.join('import TenthDiscriminant.'+n+'\n' for n in c['modules']).encode()
assert sha(root)==c['root_before_sha256'] and sha(newroot)==c['root_after_sha256']
assert (r/'lean/TenthDiscriminant.lean').read_bytes()==newroot
harness=(p/'Phase121InputCheck.lean').read_bytes();assert sha(harness)==c['harness_sha256']
assert harness.count(b'#check ')==56 and harness.count(b'#print ')==6
assert harness.count(b'#audit_namespace ')==3
assert harness.count(b'#phase121_geom_inputs TenthDiscriminant.')==6
assert harness.count(b'#phase121_arith_inputs TenthDiscriminant.')==3
assert not re.search(rb'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',harness)
spec=importlib.util.spec_from_file_location('phase121_coverage',r/'lean/audit.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
assert len(module.project_coverage(r/'lean'))==202
frozen={}
for rec in git('ls-tree','-r','-z',c['registered_commit']).split(b'\0'):
    if not rec:continue
    meta,n=rec.split(b'\t',1);n=n.decode()
    if n.startswith('.agent/') or n in c['reader_exceptions'] or n=='lean/TenthDiscriminant.lean':continue
    frozen[n]=meta.split()[2].decode()
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for n,h in zip(names,hashes):assert h==frozen[n],n
for f in p.glob('PHASE121_*.root.lean'):
    assert f.with_name(f.name.replace('.root.lean','.result.json')).exists(),'Earlier integration call not reconciled'
for f in p.glob('PHASE121_*.result.json'):
    x=json.loads(f.read_bytes());assert x['exit_code']==0 and not x['stop_reason'],'Permanent integration stop'
baseline={'registered_commit':c['registered_commit'],'accepted_commit':c['accepted_commit'],
  'frozen_files':len(frozen),'reachable_modules':202,'reader_exceptions':c['reader_exceptions']}
f=p/'PHASE121_FROZEN_BASELINE.json'
if f.exists():assert json.loads(f.read_bytes())==baseline
else:f.write_bytes((json.dumps(baseline,indent=2)+'\n').encode())
print(f'PHASE121_PREFLIGHT_OK:3 modules/56types/6definitions exact;3 root imports;9fresh closures;{len(frozen)} old Git blobs frozen;202reachable modules')
