"""Verify saved basis-completion evidence, without a Lean rerun or CI transfer."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE77_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE77_PROTOCOL.md', 'run_phase77.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 8
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
rs = d['builds']
assert [r['exit_code'] for r in rs] == [1, 0]
assert [r['attempt'] for r in rs] == [1, 2]
elapsed = Decimal(0)
for r in rs:
    assert not r['stop_reason'] and r['elapsed_seconds'] <= 600
    assert abs(Decimal(str(r['cumulative_before_seconds'])) - elapsed) < Decimal('1e-9')
    elapsed += Decimal(str(r['elapsed_seconds']))
    assert r['time_limit_seconds'] == 600 and r['memory_threshold_mb'] == 8192
    assert r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    assert 'maximum number of heartbeats' not in raw[r['stdout']].decode('utf-8-sig')
assert elapsed == Decimal(d['target_seconds']) == Decimal('65.4360465')
sources = [raw[r['source_snapshot']].decode('utf-8') for r in rs]
types = lambda s: {m.group(1): ' '.join(s[m.start():s.index(' := by', m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)', s)}
assert len(types(sources[-1])) == 6 and types(sources[0]) == types(sources[1])
assert list(types(sources[-1])) == d['public_theorems']
assert not any(re.search(r'(?m)^def ', s) for s in sources)
assert sources[0].split('\ntheorem actual_form_of_primitive_bound', 1)[1] == sources[1].split('\ntheorem actual_form_of_primitive_bound', 1)[1]
assert raw[rs[-1]['source_snapshot']] == (f / 'Phase77BasisCompletion.lean').read_bytes()
failed = raw[rs[0]['stdout']].decode('utf-8-sig')
assert 'error: type mismatch' in failed and "'change' tactic failed" in failed
assert 'NONSTANDARD_AXIOMS' in failed and 'sorryAx' in failed
log = raw[rs[-1]['stdout']].decode('utf-8-sig')
assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.BasisCompletion: 6 logical declarations; 6 theorems; 0 runtime-only' in log
for n in ['primitive_completion', 'actual_form_of_primitive_bound']:
    assert re.search(re.escape("'TenthDiscriminant.BasisCompletion." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
assert 'def TenthDiscriminant.IdealCoordinates.FormData' in log
for n in d['public_theorems']:
    assert '#check TenthDiscriminant.BasisCompletion.' + n in sources[-1]
for p, h in d['preserved_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')], changed
assert (root / 'README.md').read_bytes() == blob(d['base'], 'README.md')
print('PASS: preregistration; FAIL/PASS and8rawfiles;6unchanged types; norm/coefficient proof and controls unchanged;6/6/0standard-axiom audit; stopped75/accepted76/production unchanged.')
print('Saved integrity only: no Lean rerun, class-family composition, production CI transfer or new cutoff.')
