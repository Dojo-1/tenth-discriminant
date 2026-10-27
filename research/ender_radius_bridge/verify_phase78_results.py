"""Verify saved integration evidence; no Lean execution or external CI claim."""
from pathlib import Path
import hashlib, json, re, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE78_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE78_PROTOCOL.md', 'run_phase78.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
for p, h in d['production_sha256'].items():
    assert sha((root / p).read_bytes()) == h, p
for p, h in d['prior_frozen_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 37
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
assert set(d['checks']) == {'build', 'root', 'input', 'audit'}
for mode, r in d['checks'].items():
    assert r['mode'] == mode and r['attempt'] == 1 and r['exit_code'] == 0 and not r['stop_reason']
    assert r['cumulative_before_seconds'] == 0 and r['memory_threshold_mb'] == 8192
    assert r['observed_peak_working_set_bytes'] < 8192 * 1024**2
    assert r['time_limit_seconds'] == {'build': 600, 'root': 1200, 'input': 180, 'audit': 180}[mode]
    assert r['elapsed_seconds'] < r['time_limit_seconds']
    assert sha(raw[r['source_snapshot']]) == r['source_sha256']
    assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
    prefix = r['stdout'].removesuffix('.stdout.log')
    for suffix, path in [('source', 'lean/TenthDiscriminant/ControlledClassCount.lean'), ('principal', 'lean/TenthDiscriminant/PrincipalBasis.lean'), ('least', 'lean/TenthDiscriminant/LeastNorm.lean'), ('basis', 'lean/TenthDiscriminant/BasisCompletion.lean'), ('root', 'lean/TenthDiscriminant.lean'), ('input', 'research/ender_radius_bridge/Phase78InputCheck.lean')]:
        assert raw[prefix + '.' + suffix + '.lean'] == (root / path).read_bytes(), (mode, suffix)
    log = raw[r['stdout']].decode('utf-8-sig')
    assert 'error:' not in log and 'sorryAx' not in log and 'maximum number of heartbeats' not in log
build = raw[d['checks']['build']['stdout']].decode('utf-8-sig')
for ns, counts in [('PrincipalBasis', (15, 13, 0)), ('LeastNorm', (12, 12, 0)), ('BasisCompletion', (6, 6, 0)), ('ControlledClassCount', (6, 6, 0))]:
    assert f'AUDIT_OK TenthDiscriminant.{ns}: {counts[0]} logical declarations; {counts[1]} theorems; {counts[2]} runtime-only' in build
log = raw[d['checks']['input']['stdout']].decode('utf-8-sig')
for n, count in [('controlled_class_basis', 54328), ('controlled_class_form_and_count', 54613)]:
    assert f'PHASE78_INPUTS_OK TenthDiscriminant.ControlledClassCount.{n}: {count} reached' in log
    assert re.search(re.escape("'TenthDiscriminant.ControlledClassCount." + n + "' depends on axioms:") + r'\s*\[propext,\s*Classical.choice,\s*Quot.sound\]', log), n
assert 'def TenthDiscriminant.IdealCoordinates.FormData' in log and 'def TenthDiscriminant.ClassFiber.normBound' in log
audit = raw[d['checks']['audit']['stdout']].decode('utf-8-sig')
assert 'AUDIT_OK TenthDiscriminant: 5002 logical declarations; 4233 theorems; 16993 runtime-only' in audit
structural = raw['PHASE78_SOURCE_CHECKS.log'].decode('utf-8-sig')
assert '179 project modules reachable' in structural and 'no source escapes' in structural and 'all 250 interval pairs' in structural
for name, source in [('PrincipalBasis', 'Phase73PrincipalBasis.lean'), ('LeastNorm', 'Phase76LeastNorm.lean'), ('BasisCompletion', 'Phase77BasisCompletion.lean')]:
    expected = (f / source).read_text(encoding='utf-8').replace('import TenthDiscriminant\n', 'import TenthDiscriminant.IdealCoordinates\nimport TenthDiscriminant.AxiomAudit\n', 1)
    assert (root / 'lean/TenthDiscriminant' / (name + '.lean')).read_text(encoding='utf-8') == expected, name
expected = blob(d['base'], 'lean/TenthDiscriminant.lean').decode('utf-8').replace('\r\n', '\n') + ''.join('import TenthDiscriminant.' + n + '\n' for n in ['PrincipalBasis', 'LeastNorm', 'BasisCompletion', 'ControlledClassCount'])
assert (root / 'lean/TenthDiscriminant.lean').read_text(encoding='utf-8') == expected
old = (f / 'Phase72InputCheck.lean').read_text(encoding='utf-8')
new = (f / 'Phase78InputCheck.lean').read_text(encoding='utf-8')
block = lambda s: s.split('let forbidden : Array Name := #[', 1)[1].split('for name in forbidden do', 1)[0]
assert block(old) == block(new) and len(re.findall(r'``TenthDiscriminant\.', block(new))) == 34
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert set(n for n in changed if not n.endswith('.md')) == set(d['production_sha256']), changed
assert len((root / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: preregistered exact73/76/77transport; four first-attempt checks/37rawfiles;179modules/250pairs;34input exclusions;5002/4233/16993audit; stopped69/75 and prior evidence frozen.')
print('Saved integrity only. Local integrated class count, not external CI success, aggregate B, even-field transport or a new cutoff.')
