"""Saved production-transport evidence; does not run Lean or certify a new cutoff."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent
root=f.parents[1]
d=json.loads((f/'PHASE67_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,path:subprocess.check_output(['git','show',ref+':'+path],cwd=root)
for p,h in d['sha256'].items():assert sha((root/p).read_bytes())==h,p
assert sha(blob(d['registered_commit'],'research/ender_radius_bridge/PHASE67_PROTOCOL.md'))==d['sha256']['research/ender_radius_bridge/PHASE67_PROTOCOL.md']
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],d['source_commit']],cwd=root,check=True)
subprocess.run(['git','merge-base','--is-ancestor',d['source_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path']
assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==21
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
rs=d['records'];assert len(rs)==4 and sorted(r['mode'] for r in rs)==['audit','build','input','root']
for r in rs:
 assert r['exit_code']==0 and r['attempt']==1 and not r['stop_reason']
 assert r['elapsed_seconds']<=r['time_limit_seconds']
 assert r['memory_threshold_mb']==8192 and r['observed_peak_working_set_bytes']<8192*1024**2
 assert sha(raw[r['source_snapshot']])==r['source_sha256']
 assert raw[r['source_snapshot']]==(root/'lean/TenthDiscriminant/PrimeDivisorLoss.lean').read_bytes()
 assert raw[r['source_snapshot'].replace('.source.lean','.core.lean')]==(root/'lean/TenthDiscriminant/ClassFiber.lean').read_bytes()
 assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
 log=raw[r['stdout']].decode('utf-8-sig');assert 'error:' not in log and 'sorryAx' not in log
build=next(r for r in rs if r['mode']=='build')
assert str(build['elapsed_seconds'])==d['target_seconds']
log=raw[build['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.PrimeDivisorLoss: 13 logical declarations; 13 theorems; 0 runtime-only' in log
assert 'AUDIT_OK TenthDiscriminant.ClassFiber: 15 logical declarations; 12 theorems; 3 runtime-only' in log
log=raw[next(r for r in rs if r['mode']=='audit')['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 4897 logical declarations; 4139 theorems; 16985 runtime-only' in log
log=raw[next(r for r in rs if r['mode']=='input')['stdout']].decode('utf-8-sig')
assert log.count('PHASE67_INPUTS_OK')==3
for n,c in d['closures'].items():assert f'{n}: {c} reached' in log
for n in ['PrimeDivisorLoss.excluded_budget_without_divisors','ClassFiber.residue_class_lifting']:
 assert re.search(re.escape("'TenthDiscriminant."+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log),n
assert 'def TenthDiscriminant.ClassFiber.NormLift.' in log
structural=raw['PHASE67_SOURCE_CHECKS.log'].decode('utf-8')
assert '172 project modules reachable' in structural and 'all 250 interval pairs' in structural
for old,new,imports in [('Phase65PrimeDivisorLoss.lean','PrimeDivisorLoss.lean','import TenthDiscriminant.PrimeWeightKernel\nimport TenthDiscriminant.AxiomAudit'),('Phase66ClassFiber.lean','ClassFiber.lean','import TenthDiscriminant.PrincipalIdealBridge\nimport TenthDiscriminant.AxiomAudit')]:
 assert (f/old).read_text(encoding='utf-8').replace('import TenthDiscriminant',imports,1)==(root/'lean/TenthDiscriminant'/new).read_text(encoding='utf-8')
expected=blob(d['base'],'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n','\n')+'import TenthDiscriminant.PrimeDivisorLoss\nimport TenthDiscriminant.ClassFiber\n'
assert (root/'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')==expected
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md'))=={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/PrimeDivisorLoss.lean','lean/TenthDiscriminant/ClassFiber.lean'},changed
for p in d['prior_frozen_paths']:assert (root/p).read_bytes()==blob(d['base'],p),p
assert len((root/'README.md').read_text(encoding='utf-8').splitlines())==61
print('PASS: preregistration;4first-attempt terminal checks;21rawfiles; exact65/66 import-only transport;3 dependency closures;172modules/250pairs;4897/4139/16985 audit; prior artifacts frozen.')
print('Integrity only. No Lean rerun, new-head CI pass, controlled form basis, representation multiplicity, arithmetic B or cutoff inferred.')
