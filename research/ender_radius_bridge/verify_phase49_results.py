"""Seal once, then verify preserved Phase49 evidence; never rerun Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import sys
import zipfile

here = Path(__file__).resolve().parent
root = here.parents[1]
manifest = here / 'PHASE49_RESULTS.json'
digest = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda p: p.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
records = sorted(here.glob('PHASE49_*.result.json'))
rows = [json.loads(p.read_text(encoding='utf-8-sig')) for p in records]
assert len(rows) == 6
builds = [r for r in rows if r['mode'] == 'build']
assert [r['exit_code'] for r in builds] == [1, 1, 0]
assert all(not r['stop_reason'] for r in rows)
assert all(r['exit_code'] == 0 for r in rows if r['mode'] != 'build')
spent = sum(Decimal(str(r['elapsed_seconds'])) for r in builds)
assert spent < 1200 and all(r['elapsed_seconds'] < 600 for r in builds)
assert all(r['observed_peak_working_set_bytes'] <= 8192*1024**2 for r in rows)
source = root / 'lean/TenthDiscriminant/CentralSymmetry.lean'
first = lf(here / 'Phase49Attempt1.lean')
second = lf(here / 'Phase49Attempt2.lean')
assert first.replace(
    'simp only [derivativeRow, if_pos hj, map_neg, neg_pow, pow_add]',
    'simp only [derivativeRow, if_pos hj, map_neg]\n'
    '    rw [neg_pow z (r-j), neg_pow (conj z) s, pow_add]').replace(
    'Int.cast_injective (R := Real)', 'Int.cast_injective (α := Real)') == second
assert second.replace('  simp\n\n/-- Opposite',
                      '  simp <;> ring\n\n/-- Opposite') == lf(source)
base = subprocess.check_output(['git', 'show', 'deab8c2:lean/TenthDiscriminant.lean'], cwd=root).decode()
assert lf(root / 'lean/TenthDiscriminant.lean').replace(
    'import TenthDiscriminant.CentralSymmetry\n', '') == base.replace('\r\n', '\n')
changed = subprocess.check_output(['git', 'diff', '--name-only', 'deab8c2', '--',
    'lean', 'tools', '.github'], cwd=root, text=True).splitlines()
assert set(changed) <= {'lean/TenthDiscriminant.lean',
                        'lean/TenthDiscriminant/CentralSymmetry.lean',
                        'lean/FORMALIZATION.md'}
audit = next(r for r in rows if r['mode'] == 'audit')
archive = here / 'PHASE49_AXIOM_AUDIT_RAW.zip'
if '--seal' in sys.argv:
    assert not manifest.exists() and not archive.exists()
    raw = here / audit['stdout']
    payload = raw.read_bytes()
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(raw.name, payload)
    with zipfile.ZipFile(archive) as z:
        assert z.read(raw.name) == payload
    assert raw.resolve().parent == here.resolve()
    raw.unlink()  # Only the verified duplicate; archive retains exact raw bytes.
    files = records + list(here.glob('PHASE49_*.log')) + [archive]
    textfiles = [source, root/'lean/TenthDiscriminant.lean',
        here/'PHASE49_PROTOCOL.md', here/'Phase49Attempt1.lean',
        here/'Phase49Attempt2.lean', here/'Phase49InputCheck.lean',
        here/'run_phase49.ps1', here/'CENTRAL_SYMMETRY_GUIDE.md']
    data = dict(scope='central-negation parity orthogonality, no cutoff improvement',
        status='LOCAL_PASS', protocol_commit='6cada73', cumulative_build_seconds=str(spent),
        raw_sha256={str(p.relative_to(root)):digest(p.read_bytes()) for p in files},
        source_sha256_lf={str(p.relative_to(root)):digest(lf(p).encode()) for p in textfiles},
        audit_entry=audit['stdout'], audit_raw_sha256=digest(payload),
        audit_raw_bytes=len(payload), exact_head_ci='separate; not yet published')
    manifest.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8', newline='\n')
data = json.loads(manifest.read_text())
for name, expected in data['raw_sha256'].items():
    assert digest((root/name.replace('\\', '/')).read_bytes()) == expected, name
for name, expected in data['source_sha256_lf'].items():
    assert digest(lf(root/name.replace('\\', '/')).encode()) == expected, name
with zipfile.ZipFile(archive) as z:
    payload = z.read(data['audit_entry'])
assert digest(payload) == data['audit_raw_sha256']
assert len(payload) == data['audit_raw_bytes']
assert b'AUDIT_OK TenthDiscriminant: 4637 logical declarations; 3900 theorems; 16958 runtime-only' in payload
inp = lf(here / next(r for r in rows if r['mode']=='input')['stdout'])
assert inp.count('depends on axioms:') == 4
assert all(x in inp for x in ['propext', 'Classical.choice', 'Quot.sound'])
sys.path.insert(0, str(root/'lean'))
import audit as coverage
mods = coverage.project_coverage(root/'lean')
assert len(mods) == 159
for module in mods:
    p = (root/'lean').joinpath(*module.split('.')).with_suffix('.lean')
    assert not re.search(r'\b(sorry|admit|axiom|native_decide|unsafe)\b', coverage.source_code(p))
print('PASS: six terminal records; two failed sources/exact repairs; all source/raw hashes;')
print('159 reachable modules/no source escapes; compiled audit 4637/3900/16958.')
print('Scope: preserved evidence correspondence, not a fresh proof run or independent review.')
