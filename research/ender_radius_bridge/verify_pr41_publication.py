"""Read-only publication and historical integration evidence checks; never run Lean."""
from pathlib import Path
import hashlib,json,subprocess,zipfile
p=Path(__file__).resolve().parent;r=p.parents[1]
git=lambda *args:subprocess.check_output(['git',*args],cwd=r)
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((p/'PR41_MERGE_RECEIPT.json').read_bytes())
assert d['status']=='MERGED_AFTER_EXACT_HEAD_CI_SECURITY_SUCCESS'
assert d['conclusion']=='success' and d['attempt']==1
assert (d['source_correspondence_pairs'],d['synthetic_tests'],d['control_families'])==(250,8,8)
assert d['audit']=={'logical':5450,'theorems':4644,'runtime_auxiliaries':17026}
assert d['actual_tree_verified']
for rev in (d['source'],d['tested_merge'],d['actual_merge']):
    assert git('rev-parse',rev+'^{tree}').decode().strip()==d['tree']
assert git('show','-s','--format=%P',d['actual_merge']).decode().split()==d['actual_parents']
assert sha((p/'PR41_CI_EVIDENCE.zip').read_bytes())==d['archive_sha256']
with zipfile.ZipFile(p/'PR41_CI_EVIDENCE.zip') as z:
    assert z.testzip() is None and len(z.namelist())==8
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==d['sha256']
run=json.loads(raw['run']);job=json.loads(raw['job'])
assert run['head_sha']==d['source'] and run['conclusion']=='success'
assert run['id']==d['run'] and run['run_attempt']==1
assert job['id']==d['job'] and job['conclusion']=='success'
log=raw['job.log'].decode('utf-8-sig')
assert 'PASS: source digest and all 250 interval pairs match the Lean recurrence.' in log
assert 'AUDIT_OK TenthDiscriminant: 5450 logical declarations; 4644 theorems; 17026 runtime-only auxiliaries excluded' in log
assert 'Ran 8 tests in 2.155s' in log
assert log.count('CONTROL_FAMILY_OK ')==8
assert '2026-10-29T10:12:58.8909739Z' in log and '##[error]' not in log
for check in d['security_checks']:
    assert check['conclusion']=='success' and check['head']==d['source']
# Current reader updates intentionally change hashes in old reader snapshots.
# Check the frozen historical integration manifest against its published Git tree.
old=json.loads((p/'PHASE117_RESULTS.json').read_bytes())
for name,h in old['sha256'].items():assert sha(git('show',d['source']+':'+name))==h,name
for name in ('lean/TenthDiscriminant/RadialOperator.lean','lean/TenthDiscriminant.lean'):
    assert (r/name).read_bytes()==git('show',d['source']+':'+name)
print('PASS PR41 publication: exact source/tested/actual trees;8raw;250pairs;8tests;8families;security;historical117hashes;production source unchanged')
