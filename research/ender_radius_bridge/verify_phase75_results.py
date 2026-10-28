"""Preserve a stopped proof attempt; never invoke Lean or infer partial acceptance."""
from pathlib import Path
import hashlib, json, subprocess, zipfile

f = Path(__file__).resolve().parent
root = f.parents[1]
d = json.loads((f / 'PHASE75_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=root)
assert d['status'] == 'STOPPED_FAILURE_INTERNAL_HEARTBEAT_NO_RETRY'
assert d['accepted_main_roots'] == [] and not d['retry_allowed']
for n, h in d['sha256'].items():
    assert sha((f / n).read_bytes()) == h, n
for n in ['PHASE75_PROTOCOL.md', 'run_phase75.ps1']:
    assert blob(d['registered_commit'], 'research/ender_radius_bridge/' + n) == (f / n).read_bytes(), n
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=root, check=True)
zp = f / d['raw_archive']['path']
assert sha(zp.read_bytes()) == d['raw_archive']['sha256']
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None and len(z.namelist()) == 4
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == d['raw_sha256']
assert len(d['builds']) == 1
r = d['builds'][0]
assert r['attempt'] == 1 and r['exit_code'] == 1
assert r['time_limit_seconds'] == 600 and r['memory_threshold_mb'] == 8192
assert r['elapsed_seconds'] == 39.4407757 and r['cumulative_before_seconds'] == 0
assert r['stop_reason'] == '' and r['observed_peak_working_set_bytes'] < 8192 * 1024**2
assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
assert sha(raw[r['source_snapshot']]) == r['source_sha256']
assert raw[r['source_snapshot']] == (f / 'Phase75ControlledBasis.lean').read_bytes()
log = raw[r['stdout']].decode('utf-8-sig')
for s in ['error: unsolved goals', "unknown constant 'Int.natCast_natAbs.symm'", '(deterministic) timeout', 'maximum number of heartbeats (200000)', 'PROJECT_AXIOM TenthDiscriminant.ControlledBasis.unit_ideal_control']:
    assert s in log, s
assert 'AUDIT_OK TenthDiscriminant.ControlledBasis:' not in log
assert not d['outer_resource_threshold_reached'] and d['internal_heartbeat_stop']
for p, h in d['preserved_sha256'].items():
    assert sha((root / p).read_bytes()) == h == sha(blob(d['base'], p)), p
changed = subprocess.check_output(['git', 'diff', '--name-only', d['base'], '--', 'lean', 'tools', '.github', 'flow'], cwd=root, text=True).splitlines()
assert not [n for n in changed if not n.endswith('.md')], changed
assert (root / 'README.md').read_bytes() == blob(d['base'], 'README.md')
print('PASS: stopped failure preserved; single invocation/four raw files; internal 200000-heartbeat timeout and rejected namespace audit; no accepted main root; prior evidence/production unchanged.')
print('No rerun permitted in Phase75. Integrity only; no controlled-basis theorem, coefficient bound or new cutoff.')
