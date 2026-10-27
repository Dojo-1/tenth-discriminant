"""Verify the saved standalone closed-kernel proof without rerunning Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE83_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
prefix = 'research/ender_radius_bridge/'
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for name in ['PHASE83_PROTOCOL.md', 'run_phase83.ps1']:
    assert blob(data['registered_commit'], prefix + name) == (folder / name).read_bytes()
for name, expected in data['sha256'].items():
    assert sha((folder / name).read_bytes()) == expected, name
for path, expected in data['frozen_sha256'].items():
    assert sha((repo / path).read_bytes()) == expected == sha(blob(data['base'], path)), path
archive = folder / data['archive']['path']
assert sha(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 8
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
builds = data['builds']
assert [r['attempt'] for r in builds] == [1, 2]
assert [r['exit_code'] for r in builds] == [1, 0]
assert builds[0]['cumulative_before_seconds'] == 0
assert builds[1]['cumulative_before_seconds'] == builds[0]['elapsed_seconds']
assert sum(Decimal(str(r['elapsed_seconds'])) for r in builds) == Decimal(data['target_seconds']) == Decimal('98.8240654')
for r in builds:
    assert r['phase'] == 83 and r['mode'] == 'build' and not r['stop_reason']
    assert r['time_limit_seconds'] == 600 and 0 < r['elapsed_seconds'] < 600
    assert r['memory_threshold_mb'] == 8192 and 0 < r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert r['arguments'] == ['env', 'lean', '-j', '1', '../research/ender_radius_bridge/Phase83ClosedKernel.lean']
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    assert 'maximum number of heartbeats' not in raw[r['stdout']].decode('utf-8-sig')
sources = [raw[r['source_snapshot']].decode('utf-8') for r in builds]
repair = '  unfold countBound linearSlope\n  nlinarith\n'
assert sources[0].count(repair) == 1
assert sources[0].replace(repair, '  unfold countBound linearSlope\n  simp only [div_eq_mul_inv] at hs ⊢\n  nlinarith\n') == sources[1]
assert sources[1].encode('utf-8') == (folder / 'Phase83ClosedKernel.lean').read_bytes()
assert re.findall(r'(?m)^theorem (\w+)', sources[1]) == data['public_theorems']
assert len(data['public_theorems']) == 11
assert re.findall(r'(?m)^def (\w+)', sources[1]) == ['linearSlope', 'closedCost']
failed = raw[builds[0]['stdout']].decode('utf-8-sig')
assert 'linarith failed to find a contradiction' in failed
assert 'NONSTANDARD_AXIOMS' in failed and 'PHASE83_NONSTANDARD_AXIOM sorryAx' in failed
passed = raw[builds[1]['stdout']].decode('utf-8-sig')
assert 'error:' not in passed and 'sorryAx' not in passed
assert 'AUDIT_OK TenthDiscriminant.ClosedKernel: 28 logical declarations; 26 theorems; 0 runtime-only' in passed
assert 'PHASE83_INPUTS_OK TenthDiscriminant.ClosedKernel.closed_actual_gram_budget: 57618 reached' in passed
assert re.search(r"'TenthDiscriminant.ClosedKernel.closed_actual_gram_budget' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]", passed)
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
assert block(sources[1]) == block((folder / 'Phase82InputCheck.lean').read_text(encoding='utf-8'))
assert block(sources[1]).count('``TenthDiscriminant.') == 34
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=repo, text=True).splitlines()
assert all(p.endswith('.md') for p in changed), changed
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
subprocess.run(['python', str(folder / 'verify_phase82_results.py')], cwd=repo, check=True)
print('PASS: closed kernel and actual-Gram composition; 11 types/2 definitions unchanged; sole division-normalization repair; FAIL50.0273877/PASS48.7966777; 8 raw files; 28/26/0 audit; same34 exclusions/57618 reached.')
print('Standalone local result. Production82 unchanged; no new full-library or external CI, field transport, numerical cutoff or human review inferred.')
