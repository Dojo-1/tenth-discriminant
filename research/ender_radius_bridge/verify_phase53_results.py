"""Seal or verify Phase53 evidence correspondence; does not run Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, sys, zipfile

here = Path(__file__).resolve().parent
root = here.parents[1]
sha = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda p: p.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
records = sorted(here.glob('PHASE53_*.result.json'))
rows = [json.loads(lf(p)) for p in records]
assert len(rows) == 5
builds = [r for r in rows if r['mode'] == 'build']
assert [r['exit_code'] for r in builds] == [1, 0]
assert all(r['exit_code'] == 0 for r in rows if r['mode'] != 'build')
assert all(not r['stop_reason'] for r in rows)
spent = sum(Decimal(str(r['elapsed_seconds'])) for r in builds)
assert spent < 1200
assert all(r['elapsed_seconds'] < r['time_limit_seconds'] for r in rows)
assert all(r['observed_peak_working_set_bytes'] <= 8192*1024**2 for r in rows)
source = root/'lean/TenthDiscriminant/SmallPrimeRecoveryGain.lean'
assert lf(here/'Phase53Attempt1.lean').replace(
    '  rw [Real.log_pow] at h5\n',
    '  rw [Real.log_pow] at h5\n  norm_num at h3 h5\n') == lf(source)
oldroot = subprocess.check_output(['git','show','9154317:lean/TenthDiscriminant.lean'], cwd=root).decode().replace('\r\n','\n')
assert lf(root/'lean/TenthDiscriminant.lean').replace('import TenthDiscriminant.SmallPrimeRecoveryGain\n','') == oldroot
changed = subprocess.check_output(['git','diff','--name-only','9154317','--','lean/TenthDiscriminant','lean/TenthDiscriminant.lean','tools','.github'], cwd=root, text=True).splitlines()
assert set(changed) <= {'lean/TenthDiscriminant.lean','lean/TenthDiscriminant/SmallPrimeRecoveryGain.lean'}
# Prior frozen evidence is historical; only its root is read at its own commit.
prior = json.loads(lf(here/'PHASE52_RESULTS.json'))
for n,h in prior['raw_sha256'].items(): assert sha((root/n).read_bytes()) == h, n
for n,h in prior['source_sha256_lf'].items():
    b = oldroot.encode() if n == 'lean/TenthDiscriminant.lean' else lf(root/n).encode()
    assert sha(b) == h, n
review = json.loads(lf(here/'PHASE51_RESULTS.json'))
assert sha((here/'PHASE51_REVIEW_REPORT.md').read_bytes()) == review['report_sha256']
for n,h in review['reviewed_source_sha256_lf'].items(): assert sha(lf(root/n).encode()) == h,n
assert sha(lf(here/'CONJUGATION_BRIDGE_GUIDE.md').encode()) == review['correction_sha256_lf']
sys.path.insert(0,str(root/'lean'))
import audit as coverage
mods = coverage.project_coverage(root/'lean')
assert len(mods) == 162
for m in mods:
    p = (root/'lean').joinpath(*m.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b',coverage.source_code(p))
audit = next(r for r in rows if r['mode'] == 'audit')
archive = here/'PHASE53_AXIOM_AUDIT_RAW.zip'
manifest = here/'PHASE53_RESULTS.json'
if '--seal' in sys.argv:
    assert not manifest.exists() and not archive.exists()
    raw = here/audit['stdout']; payload = raw.read_bytes()
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z: z.writestr(raw.name,payload)
    with zipfile.ZipFile(archive) as z: assert z.read(raw.name) == payload
    # Remove only the verified duplicate, after exact readback from the archive.
    assert raw.resolve().parent == here.resolve()
    raw.unlink()
    texts = [source,root/'lean/TenthDiscriminant.lean',here/'PHASE53_PROTOCOL.md',here/'Phase53Attempt1.lean',here/'Phase53InputCheck.lean',here/'run_phase53.ps1',here/'NORMALIZED_RECOVERY_GUIDE.md']
    files = records+list(here.glob('PHASE53_*.log'))+[archive]
    data = dict(status='LOCAL_PASS',scope='fixed 3/50 normalized recovery; no new cutoff',
        protocol_commit='a1428e61e42cfa2943c57c60bfe21a3b6d6f445f',cumulative_build_seconds=str(spent),
        interruption='first input/audit observation aborted; empty logs and absence of live lake/lean processes reconciled before retry. Two retry launcher failures (execution policy, missing PATH) occurred before Lean launch; no proof attempt consumed.',
        raw_sha256={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files},
        source_sha256_lf={p.relative_to(root).as_posix():sha(lf(p).encode()) for p in texts},
        audit_entry=audit['stdout'],audit_raw_sha256=sha(payload),audit_raw_bytes=len(payload),
        exact_head_ci='separate, not yet published',semantic_review='Phase51 predates Phase52 and Phase53')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data = json.loads(lf(manifest))
for n,h in data['raw_sha256'].items(): assert sha((root/n).read_bytes()) == h,n
for n,h in data['source_sha256_lf'].items(): assert sha(lf(root/n).encode()) == h,n
with zipfile.ZipFile(archive) as z: payload = z.read(data['audit_entry'])
assert sha(payload) == data['audit_raw_sha256'] and len(payload) == data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4687 logical declarations; 3944 theorems; 16968 runtime-only' in payload
assert lf(here/next(r for r in rows if r['mode']=='input')['stdout']).count('depends on axioms:') == 4
print('PASS: five terminal records, exact one-line repair, raw/source/archive hashes;')
print('Phase52 evidence and Phase51 reviewed sources/report/correction intact; 162 reachable modules/no escapes.')
print(next(x for x in payload.decode().splitlines() if 'AUDIT_OK TenthDiscriminant:' in x))
print('Evidence correspondence only; compiled checks and external review have separate scope.')
