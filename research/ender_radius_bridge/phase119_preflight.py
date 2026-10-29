"""Freeze the complete new target and accepted dependency before bounded Lean."""
from pathlib import Path
import hashlib,json,re,subprocess
p=Path(__file__).resolve().parent;r=p.parents[1];primary=r.parent/'tenth-discriminant'
git=lambda *args,**kw:subprocess.check_output(['git',*args],cwd=r,**kw)
protocol='781aec84006fde74517da17e31b3474ab33dd831'
assert git('show',protocol+':research/ender_radius_bridge/PHASE119_PROTOCOL.md')==(p/'PHASE119_PROTOCOL.md').read_bytes()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=primary).decode().strip()=='ab5558ff7b482a6bec185b37115b6faf57a82c28'
accepted=(p/'Phase118RadialJetMajorant.lean').read_bytes().decode()
dependency=accepted[:accepted.index('#audit_namespace TenthDiscriminant.RadialJetMajorant')]
s=(p/'Phase119RadialDetBound.lean').read_bytes().decode()
assert s.startswith(dependency),'Accepted118 body changed'
assert not re.search(r'\b(sorry|admit|axiom)\b|set_option (maxHeartbeats|maxRecDepth)',s)
body=s[s.index('namespace TenthDiscriminant.RadialDetBound'):]
surface={'types':{m[1]:m[0] for m in re.findall(r'(?m)^(theorem (\w+)[\s\S]*?) := by',body)},'definitions':{m[1]:m[0] for m in re.findall(r'(?m)^(def (\w+)[\s\S]*?)(?=\n\n)',body)}}
assert len(surface['types'])==22 and len(surface['definitions'])==4
for name in surface['types']:assert '#check TenthDiscriminant.RadialDetBound.'+name+'\n' in s
for name in surface['definitions']:assert '#print TenthDiscriminant.RadialDetBound.'+name+'\n' in s
f=p/'PHASE119_FROZEN_SURFACE.json'
if f.exists():assert json.loads(f.read_bytes())==surface,'Public target or data definition changed'
else:f.write_bytes((json.dumps(surface,ensure_ascii=False,indent=2)+'\n').encode())
readers=['README.md','STATUS.md','lean/FORMALIZATION.md','TAO_OBJECTIVES_CURRENT.md','TAO_REPLY_BRIEF.md','research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md']
frozen={}
for rec in git('ls-tree','-r','-z',protocol).split(b'\0'):
    if not rec:continue
    meta,name=rec.split(b'\t',1);name=name.decode()
    if name.startswith('.agent/') or name in readers:continue
    frozen[name]=meta.split()[2].decode()
names=sorted(frozen);hashes=git('hash-object','--stdin-paths',input=('\n'.join(names)+'\n').encode()).decode().splitlines()
assert len(names)==len(hashes)
for name,h in zip(names,hashes):assert h==frozen[name],name
for name in ('lean/TenthDiscriminant/RadialOperator.lean','lean/TenthDiscriminant.lean'):
    assert (primary/name).read_bytes()==(r/name).read_bytes()
baseline={'registered_commit':protocol,'reader_exceptions':readers,'frozen_files':len(frozen),
  'accepted_dependency_sha256':hashlib.sha256(dependency.encode()).hexdigest(),
  'accepted_dependency_commit':'39e8eaf2d9ccf008671ecc93abcc7477c98194a3'}
f=p/'PHASE119_FROZEN_BASELINE.json'
if f.exists():assert json.loads(f.read_bytes())==baseline
else:f.write_bytes((json.dumps(baseline,indent=2)+'\n').encode())
prior=list(p.glob('PHASE119_build_*.result.json'))
for file in prior:assert not json.loads(file.read_bytes())['stop_reason'],'Permanent resource stop'
assert not any(json.loads(f.read_bytes())['exit_code']==0 for f in prior),'Full target already passed; no replay'
for file in p.glob('PHASE119_build_*.source.lean'):
    assert file.with_name(file.name.replace('.source.lean','.result.json')).exists(),'Unreconciled prior invocation'
assert len(prior)<3 and sum(json.loads(f.read_bytes())['elapsed_seconds'] for f in prior)<1200
print(f'PHASE119_PREFLIGHT_OK:22 public targets/4 complete data definitions frozen;accepted118 dependency exact;{len(frozen)} prior Git blobs unchanged;primary ab555;prior invocations {len(prior)}')
