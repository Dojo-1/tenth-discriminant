"""Validate a preserved stopped failure; never infer a successful theorem."""
from pathlib import Path
import hashlib,json,subprocess,zipfile
f=Path(__file__).resolve().parent;root=f.parents[1]
d=json.loads((f/'PHASE69_RESULTS.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,p:subprocess.check_output(['git','show',ref+':'+p],cwd=root)
assert d['status']=='FAILED_INTERNAL_RESOURCE_STOP_NO_NORM_FORM_OR_ACTUAL_IDEAL_COUNT_THEOREM'
for n,h in d['sha256'].items():assert sha((f/n).read_bytes())==h,n
assert blob(d['registered_commit'],'research/ender_radius_bridge/PHASE69_PROTOCOL.md')==(f/'PHASE69_PROTOCOL.md').read_bytes()
subprocess.run(['git','merge-base','--is-ancestor',d['registered_commit'],'HEAD'],cwd=root,check=True)
zp=f/d['raw_archive']['path'];assert sha(zp.read_bytes())==d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None and len(z.namelist())==4
 raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['raw_sha256']
assert len(d['builds'])==1
r=d['builds'][0];assert r['attempt']==1 and r['exit_code']==1 and not r['stop_reason']
assert r['elapsed_seconds']<600 and r['memory_threshold_mb']==8192
assert r['observed_peak_working_set_bytes']<8192*1024**2
assert raw[r['source_snapshot']]==(f/'Phase69IdealNormForm.lean').read_bytes()
assert sha(raw[r['source_snapshot']])==r['source_sha256']
assert json.loads(raw[r['stdout'].replace('.stdout.log','.result.json')].decode('utf-8-sig'))==r
log=raw[r['stdout']].decode('utf-8-sig')
assert 'maximum number of heartbeats (200000)' in log and 'PROJECT_AXIOM' in log and 'error:' in log
assert 'AUDIT_OK TenthDiscriminant.IdealNormForm:' not in log
assert not list(f.glob('PHASE69_build_*.result.json'))[1:]
changed=subprocess.check_output(['git','diff','--name-only',d['base'],'--','lean','tools','.github','flow'],cwd=root,text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')],changed
for p in ['README.md','lean/TenthDiscriminant.lean','research/ender_radius_bridge/Phase68ResidueMultiplicity.lean','research/ender_radius_bridge/PHASE68_RESULTS.json','research/ender_radius_bridge/PHASE68_RAW.zip']:
 assert (root/p).read_bytes()==blob(d['base'],p),p
print('PASS: preserved preregistered single stopped failure, exact4rawfiles/source, internal heartbeat exhaustion and audit rejection; no rerun or production mutation.')
print('FAILURE PRESERVATION ONLY. No ideal norm-form/count theorem or mathematical counterexample established.')
