"""Verify saved Phase82 evidence; never invokes Lean or numerical campaigns."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE82_RESULTS.json').read_text(encoding='utf-8'))
digest = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
for ref in [data['registered_commit'], data['runner_correction_commit']]:
    subprocess.run(['git', 'merge-base', '--is-ancestor', ref, 'HEAD'], cwd=repo, check=True)
for path, expected in data['sha256'].items():
    assert digest((repo / path).read_bytes()) == expected, path
prefix = 'research/ender_radius_bridge/'
original = blob(data['registered_commit'], prefix + 'run_phase82.ps1')
assert original == (folder / 'PHASE82_RUNNER_ORIGINAL.ps1').read_bytes()
assert original.count(b'default {182}') == 1
assert original.replace(b'default {182}', b'default {180}') == (folder / 'run_phase82.ps1').read_bytes()
for path in ['run_phase82.ps1', 'PHASE82_RUNNER_ORIGINAL.ps1', 'PHASE82_RUNNER_ADDENDUM.md']:
    assert blob(data['runner_correction_commit'], prefix + path) == (folder / path).read_bytes()
assert blob(data['registered_commit'], prefix + 'PHASE82_PROTOCOL.md') == (folder / 'PHASE82_PROTOCOL.md').read_bytes()
for path, expected in data['frozen_sha256'].items():
    assert digest((repo / path).read_bytes()) == expected, path
# One Git comparison verifies baseline identity for all frozen tracked paths.
baseline_changes = set(subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow', 'research/ender_radius_bridge'], cwd=repo, text=True).splitlines())
assert not baseline_changes.intersection(data['frozen_sha256']), baseline_changes.intersection(data['frozen_sha256'])
archive = folder / data['archive']['path']
assert digest(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 31
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: digest(b) for n, b in raw.items()} == data['raw_sha256']
assert set(data['runs']) == {'build', 'root', 'input', 'audit'}
snapshots = {'source': 'lean/TenthDiscriminant/SplitPrimeBudget.lean',
             'core': 'lean/TenthDiscriminant/ClassAggregation.lean',
             'root': 'lean/TenthDiscriminant.lean',
             'input': prefix + 'Phase82InputCheck.lean'}
for mode, result in data['runs'].items():
    assert result['phase'] == 82 and result['mode'] == mode
    assert result['attempt'] == 1 and result['exit_code'] == 0
    assert result['cumulative_before_seconds'] == 0 and not result['stop_reason']
    assert result['memory_threshold_mb'] == 8192
    assert 0 < result['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert result['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 182, 'audit': 180}[mode]
    assert 0 < result['elapsed_seconds'] < {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    stem = result['stdout'].removesuffix('.stdout.log')
    assert json.loads(raw[stem + '.result.json'].decode('utf-8-sig')) == result
    assert digest(raw[result['source_snapshot']]) == result['source_sha256']
    for suffix, path in snapshots.items():
        assert raw[stem + '.' + suffix + '.lean'] == (repo / path).read_bytes(), (mode, suffix)
    log = raw[result['stdout']].decode('utf-8-sig')
    assert not any(s in log for s in ['error:', 'sorryAx', 'maximum number of heartbeats', 'NONSTANDARD_AXIOMS'])
source = (repo / snapshots['source']).read_text(encoding='utf-8')
assert re.findall(r'(?m)^theorem (\w+)', source) == data['public_theorems']
assert len(data['public_theorems']) == 7
assert re.findall(r'(?m)^def (\w+)', source) == ['goodPrimes', 'splitRemainder', 'countBound']
transport = (folder / 'Phase81ClassAggregation.lean').read_text(encoding='utf-8')
assert transport.count('import TenthDiscriminant\n') == 1
assert transport.replace('import TenthDiscriminant\n', 'import TenthDiscriminant.ControlledPrimeFamily\n', 1) == (repo / snapshots['core']).read_text(encoding='utf-8')
expected_root = blob(data['base'], snapshots['root']).decode('utf-8').replace('\r\n', '\n')
expected_root += 'import TenthDiscriminant.ClassAggregation\nimport TenthDiscriminant.SplitPrimeBudget\n'
assert expected_root == (repo / snapshots['root']).read_text(encoding='utf-8')
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
inputs = (folder / 'Phase82InputCheck.lean').read_text(encoding='utf-8')
assert block(inputs) == block((folder / 'Phase80InputCheck.lean').read_text(encoding='utf-8'))
assert block(inputs).count('``TenthDiscriminant.') == 34
input_log = raw[data['runs']['input']['stdout']].decode('utf-8-sig')
for name, count in [('ClassAggregation.uniform_two_class_bound', 54831), ('SplitPrimeBudget.actual_gram_budget', 57545)]:
    assert f'PHASE82_INPUTS_OK TenthDiscriminant.{name}: {count} reached' in input_log
    assert re.search(re.escape("'TenthDiscriminant." + name + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', input_log)
build = raw[data['runs']['build']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.ClassAggregation: 8 logical declarations; 8 theorems; 0 runtime-only' in build
assert 'AUDIT_OK TenthDiscriminant.SplitPrimeBudget: 19 logical declarations; 16 theorems; 0 runtime-only' in build
audit = raw[data['runs']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5058 logical declarations; 4285 theorems; 16993 runtime-only' in audit
structural = raw['PHASE82_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '183 project modules reachable' in structural and 'no source escapes' in structural
assert 'all 250 interval pairs' in structural and 'Arb inequalities are not certified' in structural
for name in ['PHASE82_RUNNER_ORIGINAL.ps1', 'PHASE82_RUNNER_ADDENDUM.md']:
    assert raw[name] == (folder / name).read_bytes()
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=repo, text=True).splitlines()
assert set(p for p in changed if not p.endswith('.md')) == set(snapshots.values()) - {prefix + 'Phase82InputCheck.lean'}, changed
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: four first-pass saved runs/31 raw files; exact81 transport; 34 exclusions; 183 modules/250 endpoint identities; audit5058/4285/16993; frozen sources unchanged.')
print('INPUT CAP DISCREPANCY PRESERVED: nominal182s, actual43.1749583s <= registered180s; audit corrected to180s before execution. No rerun.')
print('Local finite weighted original-Gram budget only. No closed kernel estimate, new cutoff, external exact-head CI or human review inferred.')
