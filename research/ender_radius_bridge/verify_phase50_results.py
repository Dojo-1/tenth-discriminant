"""Seal once or verify preserved operator-compatibility evidence; no Lean run."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import zipfile

here = Path(__file__).resolve().parent
root = here.parents[1]
manifest = here/'PHASE50_RESULTS.json'
digest = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda p: p.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
path = lambda name: root/name.replace('\\', '/')
records = sorted(here.glob('PHASE50_*.result.json'))
rows = [json.loads(p.read_text(encoding='utf-8-sig')) for p in records]
assert len(rows)==4 and {r['mode'] for r in rows}=={'build','root','input','audit'}
assert all(r['exit_code']==0 and not r['stop_reason'] for r in rows)
assert all(r['elapsed_seconds']<r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes']<=8192*1024**2 for r in rows)
assert next(r for r in rows if r['mode']=='build')['attempt']==1
oldroot = subprocess.check_output(['git','show','f0fe28a:lean/TenthDiscriminant.lean'],cwd=root).decode().replace('\r\n','\n')
assert lf(root/'lean/TenthDiscriminant.lean').replace(
    'import TenthDiscriminant.ParityCompatibility\n','')==oldroot
changed = subprocess.check_output(['git','diff','--name-only','f0fe28a','--',
    'lean/TenthDiscriminant','lean/TenthDiscriminant.lean','tools','.github'],
    cwd=root,text=True).splitlines()
assert set(changed)<={'lean/TenthDiscriminant.lean',
    'lean/TenthDiscriminant/ParityCompatibility.lean'}
previous=json.loads((here/'PHASE49_RESULTS.json').read_text())
for name,h in previous['raw_sha256'].items():
    assert digest(path(name).read_bytes())==h,name
for name,h in previous['source_sha256_lf'].items():
    payload=oldroot.encode() if name.replace('\\','/')=='lean/TenthDiscriminant.lean' else lf(path(name)).encode()
    assert digest(payload)==h,name
audit=next(r for r in rows if r['mode']=='audit')
archive=here/'PHASE50_AXIOM_AUDIT_RAW.zip'
if '--seal' in sys.argv:
    assert not manifest.exists() and not archive.exists()
    raw=here/audit['stdout']; payload=raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z:
        assert z.read(raw.name)==payload
    assert raw.resolve().parent==here.resolve()
    raw.unlink()  # Exact duplicate only, after archive readback.
    files=records+list(here.glob('PHASE50_*.log'))+[archive]
    texts=[root/'lean/TenthDiscriminant/ParityCompatibility.lean',
        root/'lean/TenthDiscriminant.lean',here/'PHASE50_PROTOCOL.md',
        here/'Phase50InputCheck.lean',here/'run_phase50.ps1',
        here/'PARITY_COMPATIBILITY_GUIDE.md']
    data=dict(scope='same parity-sign operator commutes with actual odd-p basis and symmetric-sample Gram; no quantitative gain',
        status='LOCAL_PASS',protocol_commit='f2dd1f7d89d29581f0d41ed7fe12b526bd2dca22',
        raw_sha256={p.relative_to(root).as_posix():digest(p.read_bytes()) for p in files},
        source_sha256_lf={p.relative_to(root).as_posix():digest(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=digest(payload),audit_raw_bytes=len(payload),
        exact_head_ci='separate; not yet published')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(manifest.read_text())
for name,h in data['raw_sha256'].items():
    assert digest(path(name).read_bytes())==h,name
for name,h in data['source_sha256_lf'].items():
    assert digest(lf(path(name)).encode())==h,name
with zipfile.ZipFile(archive) as z:
    payload=z.read(data['audit_entry'])
assert digest(payload)==data['audit_raw_sha256'] and len(payload)==data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4650 logical declarations; 3910 theorems; 16968 runtime-only' in payload
inp=lf(here/next(r for r in rows if r['mode']=='input')['stdout'])
assert inp.count('depends on axioms:')==4
sys.path.insert(0,str(root/'lean'))
import audit as coverage
mods=coverage.project_coverage(root/'lean')
assert len(mods)==160
for m in mods:
    p=(root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
print('PASS: four terminal successful records, all source/raw hashes, prior Phase49 evidence preserved;')
print('160 reachable modules/no source escapes; compiled audit4650/3910/16968.')
print('Scope: evidence correspondence, not a fresh proof run or independent review.')
