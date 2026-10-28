"""Verify exact integration and saved pinned checks; never executes Lean."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE87_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
prefix = 'research/ender_radius_bridge/'
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for name in ['PHASE87_PROTOCOL.md', 'run_phase87.ps1']:
    assert blob(data['registered_commit'], prefix + name) == (folder / name).read_bytes()
for path, expected in data['sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
for path, expected in data['frozen_sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow', 'research/ender_radius_bridge', 'review', 'ledger', 'TAO_OBJECTIVE_AUDIT.md', 'TAO_OBJECTIVES_HISTORY.md', 'PRIOR_ART.md'], cwd=repo, text=True).splitlines()
assert not set(changed).intersection(data['frozen_sha256'])
archive = folder / data['archive']['path']
assert sha(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 25
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
assert set(data['runs']) == {'build', 'root', 'input', 'audit'}
for mode, result in data['runs'].items():
    assert result['phase'] == 87 and result['mode'] == mode and result['attempt'] == 1
    assert result['exit_code'] == 0 and result['cumulative_before_seconds'] == 0 and not result['stop_reason']
    assert result['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    assert 0 < result['elapsed_seconds'] < result['time_limit_seconds']
    assert result['memory_threshold_mb'] == 8192 and 0 < result['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert sha(raw[result['source_snapshot']]) == result['source_sha256']
    stem = result['stdout'].removesuffix('.stdout.log')
    assert json.loads(raw[stem + '.result.json'].decode('utf-8-sig')) == result
    for suffix, path in [('source', 'lean/TenthDiscriminant/UniformTwoClass.lean'), ('root', 'lean/TenthDiscriminant.lean'), ('input', prefix + 'Phase87InputCheck.lean')]:
        assert raw[stem + '.' + suffix + '.lean'] == (repo / path).read_bytes()
    log = raw[result['stdout']].decode('utf-8-sig')
    assert not any(s in log for s in ['error:', 'sorryAx', 'NONSTANDARD_AXIOMS', 'maximum number of heartbeats'])
old = (folder / 'Phase86UniformTwoClass.lean').read_text(encoding='utf-8')
expected = old.split('\nopen Lean Elab Command', 1)[0].replace('import TenthDiscriminant\n', 'import TenthDiscriminant.OddMinkowski\nimport TenthDiscriminant.FiftyBillionCutoff\n', 1)
source = (repo / 'lean/TenthDiscriminant/UniformTwoClass.lean').read_text(encoding='utf-8')
assert source == expected
assert re.findall(r'(?m)^theorem (\w+)', source) == data['public_theorems'] and len(data['public_theorems']) == 21
root = blob(data['base'], 'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n', '\n')
assert root + 'import TenthDiscriminant.UniformTwoClass\n' == (repo / 'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
inputs = (folder / 'Phase87InputCheck.lean').read_text(encoding='utf-8')
assert block(inputs) == block(old) and block(inputs).count('``TenthDiscriminant.') == 34
build = raw[data['runs']['build']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.UniformTwoClass: 42 logical declarations; 40 theorems; 3 runtime-only' in build
input_log = raw[data['runs']['input']['stdout']].decode('utf-8-sig')
assert f"PHASE87_INPUTS_OK TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two: {data['input_closure']} reached" in input_log
assert re.search(r"'TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]", input_log)
audit = raw[data['runs']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5145 logical declarations; 4367 theorems; 16996 runtime-only' in audit
structural = raw['PHASE87_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '186 project modules reachable' in structural and 'no source escapes' in structural and 'all 250 interval pairs' in structural
production_changes = [p for p in changed if p.startswith(('lean/', 'tools/', '.github/', 'flow/')) and not p.endswith('.md')]
assert set(production_changes) == {'lean/TenthDiscriminant.lean', 'lean/TenthDiscriminant/UniformTwoClass.lean'}
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: exact86 mathematics/control/report transport;one new module/rootimport;four first-invocation checks/25rawfiles;186modules/250endpoint identities;fresh34exclusions;5145/4367/16996 whole audit;prior failures/evidence frozen.')
print('Integrated locally, no standalone86 replay. External exact-head CI, independent human review, even-chart/arbitrary-field extension and classification are not inferred.')
