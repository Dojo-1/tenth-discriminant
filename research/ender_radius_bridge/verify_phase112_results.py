"""Verify saved priority-policy evidence; never launches Lean or tests."""
from pathlib import Path
import ast, hashlib, json, subprocess, zipfile

p = Path(__file__).resolve().parent
r = p.parents[1]
d = json.loads((p/'PHASE112_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
def git(*args, **kw):
    return subprocess.check_output(['git', *args], cwd=r, **kw)
def blob(ref, name):
    return git('show', ref+':'+name)
subprocess.run(['git', 'merge-base', '--is-ancestor', d['registered_commit'], 'HEAD'], cwd=r, check=True)
assert blob(d['registered_commit'], 'research/ender_radius_bridge/PHASE112_PROTOCOL.md') == (p/'PHASE112_PROTOCOL.md').read_bytes()
for name, digest in d['sha256'].items():
    assert sha((r/name).read_bytes()) == digest, name
old = blob(d['base'], 'lean/control_schedule.py').decode('utf-8').replace('\r\n', '\n')
new = (r/'lean/control_schedule.py').read_text(encoding='utf-8')
before = """    with ThreadPoolExecutor(max_workers=2) as pool:
        results = pool.map(lambda family: _run(root, family), families)
        for (name, _), (code, stdout, stderr) in zip(families, results):
"""
after = """    priority = sorted(families, key=lambda family: -family[1])
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = {name: pool.submit(_run, root, (name, timeout))
                   for name, timeout in priority}
        for name, _ in families:
            code, stdout, stderr = results[name].result()
"""
assert old.count(before) == 1 and old.replace(before, after) == new
old_tests = ast.parse(blob(d['base'], 'lean/control_schedule_tests.py').decode('utf-8'))
new_tests = ast.parse((r/'lean/control_schedule_tests.py').read_text(encoding='utf-8'))
old_class = next(n for n in old_tests.body if isinstance(n, ast.ClassDef))
new_class = next(n for n in new_tests.body if isinstance(n, ast.ClassDef))
old_names = [n.name for n in old_class.body if isinstance(n, ast.FunctionDef)]
assert len(old_names) == 6 and len(new_class.body) == 8
assert {n.name for n in new_class.body} - set(old_names) == {
    'test_priority_dispatch_preserves_declared_diagnostics',
    'test_queue_model_exposes_tail_and_proxy_limitation'}
new_class.body = [n for n in new_class.body if n.name in old_names]
assert ast.dump(new_tests) == ast.dump(old_tests)
driver = (r/'lean/negative_controls.py').read_bytes()
assert driver == blob(d['base'], 'lean/negative_controls.py')
calls = [n for n in ast.walk(ast.parse(driver)) if isinstance(n, ast.Call)
         and isinstance(n.func, ast.Name) and n.func.id == 'run_families']
assert len(calls) == 1 and ast.unparse(calls[0].args[0]) == 'root'
assert ast.literal_eval(calls[0].args[1]) == [
    ('exact_gram_controls.py',120), ('jet_uniqueness_controls.py',120),
    ('jet_negative_controls.py',120), ('multiplicity_negative_controls.py',120),
    ('degree_negative_controls.py',240), ('nonzero_negative_controls.py',360),
    ('affine_negative_controls.py',240), ('assembly_negative_controls.py',360)]
allowed = set(d['allowed_base_changes'])
frozen = {}
for record in git('ls-tree', '-r', '-z', d['frozen_base']).split(b'\0'):
    if not record:
        continue
    meta, name = record.split(b'\t',1)
    name = name.decode('utf-8')
    if name.startswith('.agent/') or name in allowed:
        continue
    assert meta.split()[1] == b'blob' and '\n' not in name and not name.startswith('"')
    frozen[name] = meta.split()[2].decode()
assert len(frozen) == d['frozen_files']
names = sorted(frozen)
hashes = git('hash-object', '--stdin-paths', input=('\n'.join(names)+'\n').encode('utf-8')).decode().splitlines()
assert len(hashes) == len(names)
for name, digest in zip(names, hashes):
    assert digest == frozen[name], name
archive = p/d['archive']['path']
assert sha(archive.read_bytes()) == d['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 5
    raw = {name:z.read(name) for name in z.namelist()}
assert {n:sha(b) for n,b in raw.items()} == d['raw_sha256']
x = d['runs'][0]
assert len(d['runs']) == 1 and x['phase'] == 112 and x['attempt'] == 1
assert x['exit_code'] == 0 and not x['stop_reason']
assert x['time_limit_seconds'] == 120 and 0 < x['elapsed_seconds'] < 120
assert x['memory_threshold_mb'] == 8192
peak = x['observed_peak_working_set_bytes']
assert peak is None and x['memory_observation'] == 'UNOBSERVED' or 0 < peak < 8192*1024**2
assert x['command'][1:] == ['control_schedule_tests.py'] and x['cwd'] == 'lean'
stem = x['stdout'].removesuffix('.stdout.log')
assert json.loads(raw[stem+'.result.json']) == x
normalization = json.loads((p/'PHASE112_FORMAT_NORMALIZATION.json').read_text(encoding='utf-8'))
for name, snapshot in [('lean/control_schedule.py', x['controller_snapshot']), ('lean/control_schedule_tests.py', x['tests_snapshot'])]:
    current = (r/name).read_bytes()
    assert b'\r' not in current and raw[snapshot].replace(b'\r\n', b'\n') == current
    assert ast.dump(ast.parse(raw[snapshot])) == ast.dump(ast.parse(current))
    entry = normalization['files'][name]
    assert entry['raw_snapshot'] == snapshot and entry['raw_sha256'] == sha(raw[snapshot])
    assert entry['repository_lf_sha256'] == sha(current)
log = raw[x['stderr']].decode('utf-8')
assert 'Ran 8 tests in 3.002s' in log and 'OK' in log and 'FAILED' not in log
assert log.count(' ... ok') == 8
receipt = json.loads((p/'PR39_CI_LIMIT_RECEIPT.json').read_text(encoding='utf-8'))
assert receipt['conclusion'] == 'cancelled' and receipt['families_completed'] == 8
assert sha((p/'PR39_CI_LIMIT_EVIDENCE.zip').read_bytes()) == receipt['archive_sha256']
with zipfile.ZipFile(p/'PR39_CI_LIMIT_EVIDENCE.zip') as z:
    old_raw = {n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in old_raw.items()} == receipt['sha256']
assert json.loads(old_raw['job'])['conclusion'] == 'cancelled'
assert 'maximum execution time of 25m0s' in old_raw['annotations'].decode()
assert old_raw['job.log'].count(b'CONTROL_FAMILY_OK ') == 8
for name in ('README.md','TAO_OBJECTIVES_CURRENT.md'):
    assert len((r/name).read_text(encoding='utf-8').splitlines()) == 61
print(f'PASS: static priority only; max2; same8calls/timeouts/driver and6inheritedtests; all8synthetic tests FIRST PASS;5raw;{len(frozen)}base Git blobs frozen; PR39cancel preserved.')
print('No Lean/real-family replay, measured wall-clock speedup, new cutoff or overall CI success is inferred. New final-source CI remains separate.')
