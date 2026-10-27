"""Saved production-transport evidence; does not run Lean or certify a new cutoff."""
from pathlib import Path
import hashlib,json,re,subprocess,zipfile
f=Path(__file__).resolve().parent
root=f.parents[1]
d=json.loads((f/'PHASE72_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,path:subprocess.check_output(['git','show',ref+':'+path],cwd=root)
for p,h in d['sha256'].items():assert sha((root/p).read_bytes())==h,p
assert sha(blob(d['registered_commit'],'research/ender_radius_bridge/PHASE72_PROTOCOL.md'))==d['sha256']['research/ender_radius_bridge/PHASE72_PROTOCOL.md']
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
 assert raw[r['source_snapshot']]==(root/'lean/TenthDiscriminant/IdealCoordinates.lean').read_bytes()
 assert raw[r['source_snapshot'].replace('.source.lean','.core.lean')]==(root/'lean/TenthDiscriminant/IdealBasisArithmetic.lean').read_bytes()
 assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
 log=raw[r['stdout']].decode('utf-8-sig');assert 'error:' not in log and 'sorryAx' not in log
build=next(r for r in rs if r['mode']=='build')
assert str(build['elapsed_seconds'])==d['target_seconds']
log=raw[build['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.IdealBasisArithmetic: 23 logical declarations; 20 theorems; 5 runtime-only' in log
assert 'AUDIT_OK TenthDiscriminant.IdealCoordinates: 23 logical declarations; 21 theorems; 3 runtime-only' in log
log=raw[next(r for r in rs if r['mode']=='audit')['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 4963 logical declarations; 4196 theorems; 16993 runtime-only' in log
log=raw[next(r for r in rs if r['mode']=='input')['stdout']].decode('utf-8-sig')
assert log.count('PHASE72_INPUTS_OK')==2
for n,c in d['closures'].items():assert f'{n}: {c} reached' in log
for n in ['IdealBasisArithmetic.normalized_form_of_basis','IdealCoordinates.actual_ideal_form_and_count']:
 assert re.search(re.escape("'TenthDiscriminant."+n+"' depends on axioms:")+r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]',log),n
assert 'def TenthDiscriminant.IdealCoordinates.FormData' in log
structural=raw['PHASE72_SOURCE_CHECKS.log'].decode('utf-8')
assert '175 project modules reachable' in structural and 'all 250 interval pairs' in structural
expected_source=(f/'Phase71BasisArithmetic.lean').read_text(encoding='utf-8').replace('import TenthDiscriminant','import TenthDiscriminant.ClassFiber\nimport TenthDiscriminant.ClassNumberInertBridge\nimport TenthDiscriminant.AxiomAudit',1)
assert expected_source==(root/'lean/TenthDiscriminant/IdealBasisArithmetic.lean').read_text(encoding='utf-8')
expected=blob(d['base'],'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n','\n')+'import TenthDiscriminant.IdealBasisArithmetic\nimport TenthDiscriminant.IdealCoordinates\n'
assert (root/'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')==expected
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md'))=={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/IdealCoordinates.lean','lean/TenthDiscriminant/IdealBasisArithmetic.lean'},changed
for p in d['prior_frozen_paths']:assert (root/p).read_bytes()==blob(d['base'],p),p
assert len((root/'README.md').read_text(encoding='utf-8').splitlines())==61
old_failure=json.loads((f/'PHASE69_RESULTS.json').read_text(encoding='utf-8'))
assert old_failure['status']=='FAILED_INTERNAL_RESOURCE_STOP_NO_NORM_FORM_OR_ACTUAL_IDEAL_COUNT_THEOREM'
assert len(old_failure['builds'])==1 and old_failure['builds'][0]['exit_code']==1
for path in ['lean/TenthDiscriminant/IdealBasisArithmetic.lean','lean/TenthDiscriminant/IdealCoordinates.lean']:
 assert 'maxHeartbeats' not in (root/path).read_text(encoding='utf-8')
print('PASS: new preregistered composition;4first-attempt checks/21rawfiles; exact71transport;2closures;175modules/250pairs;4963/4196/16993 audit; stopped69/prior artifacts frozen.')
print('Integrity only. No Lean rerun, new-head CI pass, uniform leading bound, class-wide B or new cutoff inferred.')
