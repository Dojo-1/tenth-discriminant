"""Check saved common-family integration evidence without executing Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE80_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE80_PROTOCOL.md', 'run_phase80.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
for p, h in d['production_sha256'].items():
    assert sha((root / p).read_bytes()) == h, p
for p, h in d['prior_frozen_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 36
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
bs = d['builds']
assert [r['attempt'] for r in bs] == [1, 2] and [r['exit_code'] for r in bs] == [1, 0]
assert sum(Decimal(str(r['elapsed_seconds'])) for r in bs) == Decimal(d['target_seconds']) == Decimal('95.8588838')
assert bs[0]['cumulative_before_seconds'] == 0 and bs[1]['cumulative_before_seconds'] == bs[0]['elapsed_seconds']
assert set(d['checks']) == {'root', 'input', 'audit'}
for mode, r in d['checks'].items():
    assert r['mode'] == mode and r['attempt'] == 1 and r['exit_code'] == 0 and r['cumulative_before_seconds'] == 0
for r in bs + list(d['checks'].values()):
    mode = r['mode']
    assert not r['stop_reason'] and r['memory_threshold_mb'] == 8192
    assert r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert r['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    assert r['elapsed_seconds'] < r['time_limit_seconds']
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    prefix = r['stdout'].removesuffix('.stdout.log')
    for suffix, path in [('core', 'lean/TenthDiscriminant/ActualPrimeAxis.lean'), ('root', 'lean/TenthDiscriminant.lean'), ('input', 'research/ender_radius_bridge/Phase80InputCheck.lean')]:
        assert raw[prefix + '.' + suffix + '.lean'] == (root / path).read_bytes(), (mode, suffix)
    log = raw[r['stdout']].decode('utf-8-sig')
    assert 'maximum number of heartbeats' not in log
    if r['exit_code'] == 0:
        assert 'error:' not in log and 'sorryAx' not in log
        assert raw[r['source_snapshot']] == (root / 'lean/TenthDiscriminant/ControlledPrimeFamily.lean').read_bytes()
sources = [raw[r['source_snapshot']].decode('utf-8') for r in bs]
assert sources[0].count('simpa only [residueKernel_absNorm') == 4
assert sources[0].replace('simpa only [residueKernel_absNorm', 'simpa only [residueIdeal,residueKernel_absNorm') == sources[1]
assert re.findall(r'(?m)^theorem (\w+)', sources[1]) == d['public_theorems'] and len(d['public_theorems']) == 8
assert re.findall(r'(?m)^def (\w+)', sources[1]) == ['ClassCountData']
failed = raw[bs[0]['stdout']].decode('utf-8-sig')
assert failed.count('type mismatch, term') == 4 and 'NONSTANDARD_AXIOMS' in failed and 'sorryAx' in failed
build = raw[bs[-1]['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.ActualPrimeAxis: 10 logical declarations; 10 theorems; 0 runtime-only' in build
assert 'AUDIT_OK TenthDiscriminant.ControlledPrimeFamily: 19 logical declarations; 18 theorems; 0 runtime-only' in build
log = raw[d['checks']['input']['stdout']].decode('utf-8-sig')
for n, count in [('fixed_family_four_lifts', 29185), ('controlled_family', 54827)]:
    assert f'PHASE80_INPUTS_OK TenthDiscriminant.ControlledPrimeFamily.{n}: {count} reached' in log
    assert re.search(re.escape("'TenthDiscriminant.ControlledPrimeFamily." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
for n in ['ControlledPrimeFamily.ClassCountData', 'ResidueMultiplicity.FamilyGood', 'ResidueMultiplicity.PointAt', 'ResidueMultiplicity.Admissible']:
    assert 'def TenthDiscriminant.' + n in log
audit = raw[d['checks']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5031 logical declarations; 4261 theorems; 16993 runtime-only' in audit
structural = raw['PHASE80_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '181 project modules reachable' in structural and 'no source escapes' in structural and 'all 250 interval pairs' in structural
expected = (f / 'Phase79ActualPrimeAxis.lean').read_text(encoding='utf-8').replace('import TenthDiscriminant\n', 'import TenthDiscriminant.ControlledClassCount\n', 1)
assert (root / 'lean/TenthDiscriminant/ActualPrimeAxis.lean').read_text(encoding='utf-8') == expected
expected = blob(d['base'], 'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n', '\n') + 'import TenthDiscriminant.ActualPrimeAxis\nimport TenthDiscriminant.ControlledPrimeFamily\n'
assert (root / 'lean/TenthDiscriminant.lean').read_text(encoding='utf-8') == expected
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
assert block((f / 'Phase78InputCheck.lean').read_text(encoding='utf-8')) == block((f / 'Phase80InputCheck.lean').read_text(encoding='utf-8'))
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md')) == set(d['production_sha256']), changed
assert len((root / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: exact79transport; four normalization repairs only;2target+3one-shot checks/36rawfiles;181modules/250pairs;34input exclusions;5031/4261/16993audit; prior failures/evidence frozen.')
print('Saved integrity only. Same-family counts and multiplicity checked locally; class-slice sum/aggregate B/new range/external CI not inferred.')
