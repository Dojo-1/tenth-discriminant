"""Seal/verify exact-staircase evidence; no Lean execution or semantic review."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,zipfile

here=Path(__file__).resolve().parent;root=here.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda p:p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
blob=lambda ref,n:subprocess.check_output(['git','show',ref+':'+n],cwd=root)
records=sorted(here.glob('PHASE57_*.result.json'));rows=[json.loads(lf(p)) for p in records]
assert len(rows)==4 and {r['mode'] for r in rows}=={'build','root','input','audit'}
assert all(r['attempt']==1 and r['exit_code']==0 and not r['stop_reason'] for r in rows)
assert all(r['elapsed_seconds']<r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes']<=8192*1024**2 for r in rows)
source=root/'lean/TenthDiscriminant/StaircaseExact.lean'
oldroot=blob('21a1b88','lean/TenthDiscriminant.lean').decode().replace('\r\n','\n')
assert lf(root/'lean/TenthDiscriminant.lean').replace('import TenthDiscriminant.StaircaseExact\n','')==oldroot
changed=subprocess.check_output(['git','diff','--name-only','21a1b88','--','lean/TenthDiscriminant','lean/TenthDiscriminant.lean','lean/lean-toolchain','lean/lakefile.lean','tools','.github'],cwd=root,text=True).splitlines()
assert set(changed)<={'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/StaircaseExact.lean'},changed
priorpath=here/'PHASE56_RESULTS.json';assert priorpath.read_bytes()==blob('21a1b88',priorpath.relative_to(root).as_posix())
prior=json.loads(lf(priorpath))
for n,h in prior['raw_sha256'].items():
    assert sha((root/n).read_bytes())==h==sha(blob('21a1b88',n)),n
for n,h in prior['source_sha256_lf'].items():
    payload=oldroot.encode() if n=='lean/TenthDiscriminant.lean' else lf(root/n).encode()
    assert sha(payload)==h,n
review=here/'PHASE55_REVIEW_REPORT.md'
assert sha(review.read_bytes())==sha(blob('80107ff',review.relative_to(root).as_posix()))=='b8d659d555d8f2be460771ad03037f9cfbe8c7ed724004f4ed75b7ff1260c0da'
sys.path.insert(0,str(root/'lean'));import audit as coverage
mods=coverage.project_coverage(root/'lean');assert len(mods)==166
for m in mods:
    p=(root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
audit=next(r for r in rows if r['mode']=='audit')
archive=here/'PHASE57_AXIOM_AUDIT_RAW.zip';manifest=here/'PHASE57_RESULTS.json'
if '--seal' in sys.argv:
    assert not archive.exists() and not manifest.exists()
    raw=here/audit['stdout'];payload=raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z:assert z.read(raw.name)==payload
    assert raw.resolve().parent==here.resolve()
    raw.unlink() # Verified duplicate only; original bytes remain in archive.
    texts=[source,root/'lean/TenthDiscriminant.lean',here/'PHASE57_PROTOCOL.md',here/'Phase57InputCheck.lean',here/'run_phase57.ps1',here/'STAIRCASE_EXACT_GUIDE.md']
    files=records+list(here.glob('PHASE57_*.log'))+[archive]
    data=dict(status='LOCAL_PASS',scope='exact original weight under positive-p/last-threshold guards; no cutoff change',
        protocol_commit='a0765da675694d37f03bb8c789f9a7f797d1c189',target_attempts=1,
        raw_sha256={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files},
        source_sha256_lf={p.relative_to(root).as_posix():sha(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=sha(payload),audit_raw_bytes=len(payload),
        exact_head_ci='separate; not yet published',semantic_review='earlier reviews predate this lemma')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(lf(manifest))
for n,h in data['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
for n,h in data['source_sha256_lf'].items():assert sha(lf(root/n).encode())==h,n
with zipfile.ZipFile(archive) as z:payload=z.read(data['audit_entry'])
assert sha(payload)==data['audit_raw_sha256'] and len(payload)==data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4772 logical declarations; 4028 theorems; 16971 runtime-only' in payload
inp=lf(here/next(r for r in rows if r['mode']=='input')['stdout'])
assert inp.count('depends on axioms:')==3
print('PASS: four first-attempt terminal records; exact one-module/root diff; raw/source/archive hashes;')
print('166 reachable modules/no escapes; audit4772/4028/16971; prior56 evidence and native review Git bytes intact.')
print('Integrity only; no new cutoff, valuation, independent review or exact-head CI inferred.')
