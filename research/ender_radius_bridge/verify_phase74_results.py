"""Verify saved Phase74 evidence; does not invoke Lean or certify a new range."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE74_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
assert blob(d['registered_commit'], 'research/ender_radius_bridge/PHASE74_PROTOCOL.md') == (f / 'PHASE74_PROTOCOL.md').read_bytes()
assert blob(d['registered_commit'], 'research/ender_radius_bridge/run_phase74.ps1') == (f / 'run_phase74.ps1').read_bytes()
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
assert elapsed == Decimal(d['target_seconds']) < 1200
sources = [raw[r['source_snapshot']].decode('utf-8') for r in rs]
types = lambda s: {m.group(1): ' '.join(s[m.start():s.index(' := by', m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)', s)}
assert len(types(sources[-1])) == 8 and types(sources[0]) == types(sources[1])
assert list(types(sources[-1])) == d['public_theorems']
assert sources[0].replace('have hg := pow_card_eq_one g', 'have hg : g ^ Fintype.card G = 1 := pow_card_eq_one') == sources[1]
assert raw[rs[-1]['source_snapshot']] == (f / 'Phase74ClassSquare.lean').read_bytes()
failed = raw[rs[0]['stdout']].decode('utf-8-sig')
assert 'error: function expected' in failed and 'NONSTANDARD_AXIOMS' in failed and 'sorryAx' in failed
log = raw[rs[-1]['stdout']].decode('utf-8-sig')
assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.ClassSquare: 9 logical declarations; 9 theorems; 0 runtime-only' in log
for n in ['self_inverse_of_card_le_two', 'bounded_class_vector']:
    assert re.search(re.escape("'TenthDiscriminant.ClassSquare." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
for n in ['NormLift', 'normBound']:
    assert 'def TenthDiscriminant.ClassFiber.' + n in log
for n in d['public_theorems']:
    assert '#check TenthDiscriminant.ClassSquare.' + n in sources[-1]
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')], changed
assert (root / 'README.md').read_bytes() == blob(d['base'], 'README.md')
for p, h in d['preserved_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
print('PASS: preregistration; FAIL/PASS and eight raw files; unchanged eight types; one implicit-argument repair; 9/9/0 standard-axiom audit; prior evidence/production unchanged.')
print('Saved evidence integrity only: no Lean rerun, production CI coverage, controlled basis or new cutoff inferred.')
