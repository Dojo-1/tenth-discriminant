"""Verify saved odd-field normalization evidence without rerunning Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE84_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
prefix = 'research/ender_radius_bridge/'
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for name in ['PHASE84_PROTOCOL.md', 'run_phase84.ps1']:
    assert blob(data['registered_commit'], prefix + name) == (folder / name).read_bytes()
for path, expected in data['sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
for path, expected in data['frozen_sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow', 'research/ender_radius_bridge'], cwd=repo, text=True).splitlines()
assert not set(changed).intersection(data['frozen_sha256'])
archive = folder / data['archive']['path']
assert sha(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 36
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
builds = data['builds']
assert [r['attempt'] for r in builds] == [1, 2] and [r['exit_code'] for r in builds] == [1, 0]
assert builds[0]['cumulative_before_seconds'] == 0
assert builds[1]['cumulative_before_seconds'] == builds[0]['elapsed_seconds']
assert sum(Decimal(str(r['elapsed_seconds'])) for r in builds) == Decimal('135.575929') == Decimal(data['target_seconds'])
assert set(data['checks']) == {'root', 'input', 'audit'}
for mode, result in data['checks'].items():
    assert result['mode'] == mode and result['attempt'] == 1 and result['exit_code'] == 0
    assert result['cumulative_before_seconds'] == 0
for result in builds + list(data['checks'].values()):
    mode = result['mode']
    assert result['phase'] == 84 and not result['stop_reason']
    assert result['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    assert 0 < result['elapsed_seconds'] < result['time_limit_seconds']
    assert result['memory_threshold_mb'] == 8192 and 0 < result['observed_peak_working_set_bytes'] < 8192 * 1024**2
    stem = result['stdout'].removesuffix('.stdout.log')
    assert json.loads(raw[stem + '.result.json'].decode('utf-8-sig')) == result
    assert sha(raw[result['source_snapshot']]) == result['source_sha256']
    for suffix, path in [('core', 'lean/TenthDiscriminant/ClosedKernel.lean'), ('root', 'lean/TenthDiscriminant.lean'), ('input', prefix + 'Phase84InputCheck.lean')]:
        assert raw[stem + '.' + suffix + '.lean'] == (repo / path).read_bytes(), (mode, suffix)
    log = raw[result['stdout']].decode('utf-8-sig')
    assert 'maximum number of heartbeats' not in log
    if result['exit_code'] == 0:
        assert 'error:' not in log and 'sorryAx' not in log and 'NONSTANDARD_AXIOMS' not in log
        assert raw[result['source_snapshot']] == (repo / 'lean/TenthDiscriminant/OddMinkowski.lean').read_bytes()
first, final = [raw[r['source_snapshot']].decode('utf-8') for r in builds]
repaired = first.replace('open NumberField ExcludedPrime ClosedKernel', 'open NumberField ExcludedPrime ClosedKernel Polynomial')
repaired = repaired.replace('    simpa [z,quadraticFieldPoly] using AdjoinRoot.eval₂_root (quadraticFieldPoly c)', '    have he := AdjoinRoot.eval₂_root (quadraticFieldPoly c)\n    change (X^2-X+C (c : Rat)).eval₂ (AdjoinRoot.of (quadraticFieldPoly c)) z=0 at he\n    simpa only [eval₂_add,eval₂_sub,eval₂_pow,eval₂_X,eval₂_C] using he')
repaired = repaired.replace('theorem three_control :', 'local instance threeFieldFact : Fact (0<4*(1 : Int)-1) := ⟨by norm_num⟩\n\ntheorem three_control :')
repaired = repaired.replace('actual_minkowski 3 (by decide)', 'actual_minkowski 3 ((by norm_num : Nat.Prime 3).squarefree)')
repaired = repaired.replace('actual_minkowski 7 (by decide)', 'actual_minkowski 7 ((by norm_num : Nat.Prime 7).squarefree)')
repaired = repaired.replace('theorem nonsquarefree_control : ¬ Squarefree (9 : Nat) := by decide', 'theorem nonsquarefree_control : ¬ Squarefree (9 : Nat) := by\n  intro h\n  exact Nat.squarefree_iff_prime_squarefree.mp h 3 (by norm_num) (by norm_num)')
assert repaired == final
assert re.findall(r'(?m)^theorem (\w+)', final) == data['public_theorems'] and len(data['public_theorems']) == 10
assert re.findall(r'(?m)^def (\w+)', final) == ['chartCost']
old = (folder / 'Phase83ClosedKernel.lean').read_text(encoding='utf-8')
transport = old.split('\nopen Lean Elab Command', 1)[0].replace('import TenthDiscriminant\n', 'import TenthDiscriminant.SplitPrimeBudget\n', 1)
assert transport == (repo / 'lean/TenthDiscriminant/ClosedKernel.lean').read_text(encoding='utf-8')
root = blob(data['base'], 'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n', '\n')
assert root + 'import TenthDiscriminant.ClosedKernel\nimport TenthDiscriminant.OddMinkowski\n' == (repo / 'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
inputs = (folder / 'Phase84InputCheck.lean').read_text(encoding='utf-8')
assert block(inputs) == block(old) and block(inputs).count('``TenthDiscriminant.') == 34
input_log = raw[data['checks']['input']['stdout']].decode('utf-8-sig')
for name, count in data['input_closures'].items():
    assert f'PHASE84_INPUTS_OK TenthDiscriminant.OddMinkowski.{name}: {count} reached' in input_log
    assert re.search(re.escape("'TenthDiscriminant.OddMinkowski." + name + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', input_log)
build = raw[builds[1]['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.ClosedKernel: 28 logical declarations; 26 theorems; 0 runtime-only' in build
assert 'AUDIT_OK TenthDiscriminant.OddMinkowski: 17 logical declarations; 16 theorems; 0 runtime-only' in build
audit = raw[data['checks']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5103 logical declarations; 4327 theorems; 16993 runtime-only' in audit
structural = raw['PHASE84_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '185 project modules reachable' in structural and 'no source escapes' in structural and 'all 250 interval pairs' in structural
production_changes = [p for p in changed if p.startswith(('lean/', 'tools/', '.github/', 'flow/')) and not p.endswith('.md')]
assert set(production_changes) == set(data['production_sha256']), production_changes
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: exact83 mathematical/report transport; intended10 new types/1 definition; explicit polynomial/control-only repairs;2target+3one-shot checks/36 raw files;185modules/250endpoint identities;fresh34exclusions;5103/4327/16993 audit;prior evidence frozen.')
print('First D3 control did not elaborate; final control is checked. Local odd-chart normalization only: no new cutoff, arbitrary-field/even transport, external exact-head CI or human review inferred.')
