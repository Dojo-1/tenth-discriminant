"""Check saved all-range two-class proof evidence, without executing Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE86_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
prefix = 'research/ender_radius_bridge/'
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for name in ['PHASE86_PROTOCOL.md', 'run_phase86.ps1']:
    assert blob(data['registered_commit'], prefix + name) == (folder / name).read_bytes()
for name, expected in data['sha256'].items():
    assert sha((folder / name).read_bytes()) == expected, name
for path, expected in data['frozen_sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow', 'research/ender_radius_bridge'], cwd=repo, text=True).splitlines()
assert not set(changed).intersection(data['frozen_sha256'])
assert all(p.endswith('.md') for p in changed if p.startswith(('lean/', 'tools/', '.github/', 'flow/')))
archive = folder / data['archive']['path']
assert sha(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 12
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
builds = data['builds']
assert [r['attempt'] for r in builds] == [1, 2, 3] and [r['exit_code'] for r in builds] == [1, 1, 0]
spent = Decimal(0)
for result in builds:
    assert result['phase'] == 86 and result['mode'] == 'build' and not result['stop_reason']
    assert Decimal(str(result['cumulative_before_seconds'])) == spent
    spent += Decimal(str(result['elapsed_seconds']))
    assert result['time_limit_seconds'] == 600 and 0 < result['elapsed_seconds'] < 600
    assert result['memory_threshold_mb'] == 8192 and 0 < result['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert result['arguments'] == ['env', 'lean', '-j', '1', '../research/ender_radius_bridge/Phase86UniformTwoClass.lean']
    assert sha(raw[result['source_snapshot']]) == result['source_sha256']
    assert json.loads(raw[result['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == result
    assert 'maximum number of heartbeats' not in raw[result['stdout']].decode('utf-8-sig')
assert spent == Decimal(data['target_seconds']) == Decimal('174.6439402') and spent < 1200
sources = [raw[r['source_snapshot']].decode('utf-8') for r in builds]
assert sources[-1].encode('utf-8') == (folder / 'Phase86UniformTwoClass.lean').read_bytes()

def headers(source):
    answer = {}
    for match in re.finditer(r'(?m)^theorem (\w+)', source):
        end = source.index(':=', match.start())
        answer[match.group(1)] = source[match.start():end]
    return answer

assert headers(sources[0]) == headers(sources[1]) == headers(sources[2])
assert list(headers(sources[2])) == data['public_theorems'] and len(data['public_theorems']) == 21
assert re.findall(r'(?m)^def (.+)$', sources[0]) == re.findall(r'(?m)^def (.+)$', sources[1]) == re.findall(r'(?m)^def (.+)$', sources[2])
assert re.findall(r'(?m)^def (\w+)', sources[2]) == ['q', 'Hlog']
main = lambda s: s.split('theorem odd_classNumber_gt_two', 1)[1].split('theorem endpoint_control', 1)[0]
assert main(sources[0]) == main(sources[1]) == main(sources[2])
expected = sources[0].replace('    simpa using Real.log_le_sub_one_of_pos (by norm_num : (0 : Real)<3)', '    have hh := Real.log_le_sub_one_of_pos (by norm_num : (0 : Real)<3)\n    linarith')
expected = expected.replace('  have he : u=50*Real.log 2 := by dsimp [u]; rw [Nat.cast_pow,Real.log_pow]; norm_num', '  have he : u=50*Real.log 2 := by\n    have hz : Real.log ((2^50 : Nat) : Real)=50*Real.log 2 := by\n      rw [Nat.cast_pow,Real.log_pow]\n      norm_num\n    exact hz')
expected = expected.replace('    rw [Real.exp_neg,Real.exp_log (by positivity)]\n    rfl', '    rw [Real.exp_neg,Real.exp_log (by positivity)]\n    simp only [one_div]')
expected = expected.replace('    dsimp [u]\n    rw [Real.exp_neg,quarter_exp (2^50) (by norm_num)]', '    have hexp : Real.exp (u/4)=fourthRoot (2^50) := quarter_exp (2^50) (by norm_num)\n    rw [Real.exp_neg,hexp]')
expected = expected.replace('  have hl := Real.log_le_log (by norm_num : (0 : Real)<((2^50 : Nat) : Real))\n    (by exact_mod_cast hD)', '  have hl : Real.log ((2^50 : Nat) : Real)≤Real.log (D : Real) :=\n    Real.log_le_log (by norm_num) (by exact_mod_cast hD)')
expected = expected.replace('  exact (mul_le_mul_of_nonneg_left hC ha).trans (mul_le_mul_of_nonneg_right hr (by norm_num))', '  calc\n    lossScale R S*C ≤ lossScale R S*(3/5) := mul_le_mul_of_nonneg_left hC ha\n    _ ≤ comparisonScale R S*(3/5) :=\n      mul_le_mul_of_nonneg_right hr (by norm_num : (0 : Real)≤3/5)\n    _ = (3/5)*comparisonScale R S := by ring')
assert expected == sources[1]
expected = sources[1].replace('  exact ⟨(envelope_antitone _ _ (by linarith [he.1]) hl).trans endpoint_envelope,he.1.trans hl⟩', '  have ha : (9 : Real)≤Real.log ((2^50 : Nat) : Real) :=\n    (show (9 : Real)≤693/20 by norm_num).trans he.1\n  have hb := envelope_antitone (Real.log ((2^50 : Nat) : Real)) (Real.log (D : Real)) ha hl\n  exact ⟨hb.trans endpoint_envelope,he.1.trans hl⟩')
assert expected == sources[2]
for result in builds[:2]:
    log = raw[result['stdout']].decode('utf-8-sig')
    assert 'error:' in log and 'NONSTANDARD_AXIOMS' in log and 'PHASE86_NONSTANDARD_AXIOM sorryAx' in log
passed = raw[builds[-1]['stdout']].decode('utf-8-sig')
assert 'error:' not in passed and 'sorryAx' not in passed
assert 'AUDIT_OK TenthDiscriminant.UniformTwoClass: 42 logical declarations; 40 theorems; 3 runtime-only' in passed
assert 'PHASE86_INPUTS_OK TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two: 59721 reached' in passed
assert re.search(r"'TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two' depends on axioms:\s*\[propext,\s*Classical.choice,\s*Quot.sound\]", passed)
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
assert block(sources[-1]) == block((folder / 'Phase84InputCheck.lean').read_text(encoding='utf-8'))
assert block(sources[-1]).count('``TenthDiscriminant.') == 34
assert 'Phase85' not in sources[-1] and 'Feasibility' not in sources[-1]
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: full actual odd-chart class-number>2 theorem for all D>=2^50;21types/2defs/main proof/controls unchanged;only recorded normalization repairs;FAIL79.5313154/FAIL46.5392337/PASS48.5733911;12rawfiles;42/40/3audit;59721closure/same34exclusions;production unchanged.')
print('All3 target slots consumed; no target rerun. Standalone local theorem, not new root/external CI, even-chart/arbitrary-field extension, classification or human review.')
