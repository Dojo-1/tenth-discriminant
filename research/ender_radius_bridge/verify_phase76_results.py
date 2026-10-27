"""Check saved least-norm evidence without executing Lean or claiming basis completion."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE76_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE76_PROTOCOL.md', 'run_phase76.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 12
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
rs = d['builds']
assert [r['exit_code'] for r in rs] == [1, 1, 0]
assert [r['attempt'] for r in rs] == [1, 2, 3]
elapsed = Decimal(0)
for r in rs:
    assert not r['stop_reason'] and r['elapsed_seconds'] <= 600
    assert abs(Decimal(str(r['cumulative_before_seconds'])) - elapsed) < Decimal('1e-9')
    elapsed += Decimal(str(r['elapsed_seconds']))
    assert r['time_limit_seconds'] == 600 and r['memory_threshold_mb'] == 8192
    assert r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    log = raw[r['stdout']].decode('utf-8-sig')
    assert 'maximum number of heartbeats' not in log and '(deterministic) timeout' not in log
assert elapsed == Decimal(d['target_seconds']) == Decimal('206.0694790')
sources = [raw[r['source_snapshot']].decode('utf-8') for r in rs]
types = lambda s: {m.group(1): ' '.join(s[m.start():s.index(' := by', m.end())].split()) for m in re.finditer(r'(?m)^theorem\s+(\w+)', s)}
assert len(types(sources[-1])) == 9 and types(sources[0]) == types(sources[1]) == types(sources[2])
assert list(types(sources[-1])) == d['public_theorems']
assert not any(re.search(r'(?m)^def ', s) for s in sources)
assert len({s.split('\ntheorem unit_control', 1)[0] for s in sources}) == 1
assert len({s.split('\n#check', 1)[1] for s in sources}) == 1
assert raw[rs[-1]['source_snapshot']] == (f / 'Phase76LeastNorm.lean').read_bytes()
for r in rs[:2]:
    log = raw[r['stdout']].decode('utf-8-sig')
    assert 'error: type mismatch' in log and 'NONSTANDARD_AXIOMS TenthDiscriminant.LeastNorm.unit_control' in log and 'sorryAx' in log
log = raw[rs[-1]['stdout']].decode('utf-8-sig')
assert 'error:' not in log and 'sorryAx' not in log
assert 'AUDIT_OK TenthDiscriminant.LeastNorm: 12 logical declarations; 12 theorems; 0 runtime-only' in log
for n in ['norm_zsmul', 'primitive_of_minimal', 'bounded_class_least_primitive']:
    assert re.search(re.escape("'TenthDiscriminant.LeastNorm." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
for n in d['public_theorems']:
    assert '#check TenthDiscriminant.LeastNorm.' + n in sources[-1]
for p, h in d['preserved_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')], changed
assert (root / 'README.md').read_bytes() == blob(d['base'], 'README.md')
assert 'lean_internal_resource_limit' in (f / 'run_phase76.ps1').read_text(encoding='utf-8')
print('PASS: preregistration; FAIL/FAIL/PASS with12rawfiles;9unchanged types; only unit-control repairs;12/12/0standard-axiom audit; stopped75/prior evidence/production unchanged.')
print('Saved integrity only. All3invocations consumed; no rerun, production CI transfer, completed basis, leading-coefficient bound or new cutoff.')
