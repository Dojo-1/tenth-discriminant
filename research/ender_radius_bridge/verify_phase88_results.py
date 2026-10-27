"""Verify saved actual-field transport evidence without executing Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE88_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
prefix = 'research/ender_radius_bridge/'
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for name in ['PHASE88_PROTOCOL.md', 'run_phase88.ps1']:
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
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 37
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
builds = data['builds']
assert [r['attempt'] for r in builds] == [1, 2, 3] and [r['exit_code'] for r in builds] == [1, 1, 0]
spent = Decimal(0)
for result in builds:
    assert Decimal(str(result['cumulative_before_seconds'])) == spent
    spent += Decimal(str(result['elapsed_seconds']))
assert spent == Decimal('178.7601425') == Decimal(data['target_seconds']) and spent < 1200
assert set(data['checks']) == {'root', 'input', 'audit'}
for mode, result in data['checks'].items():
    assert result['mode'] == mode and result['attempt'] == 1 and result['exit_code'] == 0
    assert result['cumulative_before_seconds'] == 0
for result in builds + list(data['checks'].values()):
    mode = result['mode']
    assert result['phase'] == 88 and not result['stop_reason']
    assert result['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    assert 0 < result['elapsed_seconds'] < result['time_limit_seconds']
    assert result['memory_threshold_mb'] == 8192 and 0 < result['observed_peak_working_set_bytes'] < 8192 * 1024**2
    stem = result['stdout'].removesuffix('.stdout.log')
    assert json.loads(raw[stem + '.result.json'].decode('utf-8-sig')) == result
    assert sha(raw[result['source_snapshot']]) == result['source_sha256']
    for suffix, path in [('root', 'lean/TenthDiscriminant.lean'), ('input', prefix + 'Phase88InputCheck.lean')]:
        assert raw[stem + '.' + suffix + '.lean'] == (repo / path).read_bytes()
    log = raw[result['stdout']].decode('utf-8-sig')
    assert 'maximum number of heartbeats' not in log
    if result['exit_code'] == 0:
        assert 'error:' not in log and 'sorryAx' not in log and 'NONSTANDARD_AXIOMS' not in log
        assert raw[result['source_snapshot']] == (repo / 'lean/TenthDiscriminant/OddFieldTwoClass.lean').read_bytes()
sources = [raw[r['source_snapshot']].decode('utf-8') for r in builds]

def headers(source):
    return {m.group(1): source[m.start():source.index(':=', m.start())]
            for m in re.finditer(r'(?m)^theorem (\w+)', source)}

assert headers(sources[0]) == headers(sources[1]) == headers(sources[2])
assert list(headers(sources[2])) == data['public_theorems'] and len(data['public_theorems']) == 11
defs = lambda s: s.split('theorem idealMap_symm', 1)[0].split('def idealMap', 1)[1]
assert defs(sources[0]) == defs(sources[1]) == defs(sources[2])
assert re.findall(r'(?m)^def (\w+)', sources[2]) == ['idealMap', 'classMap', 'classEquiv']
main = lambda s: s.split('theorem field_classNumber_eq', 1)[1]
assert main(sources[0]) == main(sources[1]) == main(sources[2])
old = '  rw [classMap_mk0]\n  congr 1\n  apply Subtype.ext\n  exact Ideal.map_id\nend Domains'
replacement = '  rw [classMap_mk0]\n  have hid : idealMap (RingEquiv.refl R) I=I := by\n    apply Subtype.ext\n    change (I : Ideal R).map (RingHom.id R)=(I : Ideal R)\n    exact Ideal.map_id\n  exact congrArg (fun J : (Ideal R)⁰ => ClassGroup.mk0 J) hid\nend Domains'
assert sources[0].count(old) == 1 and sources[0].replace(old, replacement) == sources[1]
assert sources[1].replace('    exact Ideal.map_id\n  exact congrArg', '    exact (I : Ideal R).map_id\n  exact congrArg') == sources[2]
for result in builds[:2]:
    log = raw[result['stdout']].decode('utf-8-sig')
    assert 'typeclass instance problem is stuck' in log and 'Semiring ?m.' in log
    assert 'NONSTANDARD_AXIOMS TenthDiscriminant.OddFieldTwoClass.identity_class_control' in log
build = raw[builds[-1]['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant.OddFieldTwoClass: 20 logical declarations; 17 theorems; 3 runtime-only' in build
input_log = raw[data['checks']['input']['stdout']].decode('utf-8-sig')
for name, count in data['input_closures'].items():
    assert f'PHASE88_INPUTS_OK TenthDiscriminant.OddFieldTwoClass.{name}: {count} reached' in input_log
    assert re.search(re.escape("'TenthDiscriminant.OddFieldTwoClass." + name + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', input_log)
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
names = lambda s: re.findall(r'``([A-Za-z0-9_.]+)', block(s))
inputs = (folder / 'Phase88InputCheck.lean').read_text(encoding='utf-8')
assert names(inputs) == names((folder / 'Phase87InputCheck.lean').read_text(encoding='utf-8')) + ['TenthDiscriminant.classNumber_one_of_field_equiv']
assert len(names(inputs)) == 35
audit = raw[data['checks']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5165 logical declarations; 4384 theorems; 16999 runtime-only' in audit
structural = raw['PHASE88_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '187 project modules reachable' in structural and 'no source escapes' in structural and 'all 250 interval pairs' in structural
root = blob(data['base'], 'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n', '\n')
assert root + 'import TenthDiscriminant.OddFieldTwoClass\n' == (repo / 'lean/TenthDiscriminant.lean').read_text(encoding='utf-8')
production_changes = [p for p in changed if p.startswith(('lean/', 'tools/', '.github/', 'flow/')) and not p.endswith('.md')]
assert set(production_changes) == {'lean/TenthDiscriminant.lean', 'lean/TenthDiscriminant/OddFieldTwoClass.lean'}
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: generic class-number invariance and actual arbitrary odd-discriminant field bound;11types/3defs/main proofs unchanged;identity-control-only repairs;FAIL35.8059275/FAIL100.5685172/PASS42.3856978;37rawfiles;187modules/250endpoint identities;35input exclusions;5165/4384/16999 whole audit;prior evidence frozen.')
print('All3 target slots consumed; no target replay. Even discriminants, external exact-head CI, human review and classification remain separate.')
