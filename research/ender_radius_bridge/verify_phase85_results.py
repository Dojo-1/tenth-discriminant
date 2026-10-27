"""Verify saved feasibility records using hashes and exact rational arithmetic.

Does not rerun the experiment or evaluate logarithms/square roots.
"""
from pathlib import Path
from fractions import Fraction as F
import ast
import hashlib
import json
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
repo = folder.parents[1]
data = json.loads((folder / 'PHASE85_RESULTS.json').read_text(encoding='utf-8'))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, p: subprocess.check_output(['git', 'show', ref + ':' + p], cwd=repo)
for name in ['PHASE85_PROTOCOL.md', 'run_phase85.ps1']:
    assert blob(data['registered_commit'], 'research/ender_radius_bridge/' + name) == (folder / name).read_bytes()
subprocess.run(['git', 'merge-base', '--is-ancestor', data['registered_commit'], 'HEAD'], cwd=repo, check=True)
for path, expected in data['sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
for path, expected in data['frozen_sha256'].items():
    assert sha((repo / path).read_bytes()) == expected, path
changed = subprocess.check_output(['git', 'diff', '--name-only', data['base'], '--', 'lean', 'tools', '.github', 'flow', 'research/ender_radius_bridge'], cwd=repo, text=True).splitlines()
assert not set(changed).intersection(data['frozen_sha256'])
assert all(p.endswith('.md') for p in changed if p.startswith(('lean/', 'tools/', '.github/', 'flow/')))
archive = folder / data['archive']['path']
assert sha(archive.read_bytes()) == data['archive']['sha256']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 4
    raw = {n: z.read(n) for n in z.namelist()}
assert {n: sha(b) for n, b in raw.items()} == data['raw_sha256']
r = data['run']
assert r['phase'] == 85 and r['mode'] == 'run' and r['attempt'] == 1 and r['exit_code'] == 0
assert not r['stop_reason'] and r['time_limit_seconds'] == 120 and 0 < r['elapsed_seconds'] < 120
assert r['cumulative_before_seconds'] == 0 and r['memory_threshold_mb'] == 8192
# This fast run ended before a process-memory sample: zero means unobserved.
assert r['observed_peak_working_set_bytes'] == 0 and data['memory_observation'] == 'UNOBSERVED_NOT_ZERO_USAGE'
assert r['arguments'] == ['research/ender_radius_bridge/Phase85Feasibility.py']
assert json.loads(raw[r['stdout'].replace('.stdout.log', '.result.json')].decode('utf-8-sig')) == r
source = raw[r['source_snapshot']]
assert sha(source) == r['source_sha256']
assert source == (folder / 'Phase85Feasibility.py').read_bytes()
assert not any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(ast.parse(source)))
result = json.loads(raw[r['stdout']].decode('utf-8-sig'))
assert result['phase'] == 85 and result['source_sha256'] == r['source_sha256']
grid = list(range(36, 66, 2)) + [80, 96, 128]
assert result['grid_N'] == grid and len(grid) == 18
assert set(result['precisions']) == {'100', '200'}
assert F('0.999997') - F('0.8') - F(1, 25) == F('0.159997')
assert F('5.739') - F('0.813') == F('4.926')

def bounds(record):
    lo, hi = F(record['lo']), F(record['hi'])
    assert lo <= hi
    return lo, hi

records = {}
for precision, experiment in result['precisions'].items():
    assert len(experiment['controls']) == 8 and all(v is True for v in experiment['controls'].values())
    samples = experiment['samples']
    assert [s['N'] for s in samples] == grid
    assert experiment['first_positive_N'] == 50
    assert [s['classification'] for s in samples] == ['negative'] * 7 + ['positive'] * 11
    for row in samples:
        n, d = row['N'], int(row['D'])
        assert d >= 50000000000 and d == 2**n and int(row['R']) == d // 4 and int(row['S']) == (d // 4) // 25
        u, v = bounds(row['logD'])
        a, b = bounds(row['sqrtD'])
        c, e = bounds(row['fourthRootD'])
        assert 0 < a <= b and a*a <= d <= b*b
        assert 0 < c <= e and c**4 <= d <= e**4
        assert 0 < u <= v
        base_lo, base_hi = bounds(row['without_constant'])
        exact_lo = (4 / b + 1 / e) * (2 + u * (1 + u))
        exact_hi = (4 / a + 1 / c) * (2 + v * (1 + v))
        assert base_lo <= exact_lo <= exact_hi <= base_hi
        h_lo, h_hi = bounds(row['H'])
        assert h_lo <= base_lo + F(1, 3) and base_hi + F(1, 3) <= h_hi
        m_lo, m_hi = bounds(row['margin'])
        assert m_lo <= F('0.159997') * u - F('4.926') - h_hi
        assert F('0.159997') * v - F('4.926') - h_lo <= m_hi
        assert row['classification'] == ('positive' if m_lo > 0 else ('negative' if m_hi < 0 else 'unresolved'))
        if n == 48:
            assert m_hi < -F(21, 100)
        if n == 50:
            assert m_lo > F(7, 100)
        records[precision, n] = row
for n in grid:
    assert result['precision_nesting'][str(n)] is True
    for key in ['logD', 'sqrtD', 'fourthRootD', 'without_constant', 'H', 'margin']:
        a, b = bounds(records['100', n][key])
        c, d = bounds(records['200', n][key])
        assert a <= c <= d <= b
assert len((repo / 'README.md').read_text(encoding='utf-8').splitlines()) == 61
print('PASS: one sealed run/18points at100+200digits;16controls;7negative+11positive perprecision; firstpositive2^50margin>0.07;2^48margin<-0.21;exact rational enclosure arithmetic/nesting;four raw files;prior proof/evidence frozen.')
print('Memory unobserved, not zero usage. No logarithm/sqrt rerun, all-D monotonicity, new Lean cutoff, field classification, external CI or independent implementation review inferred.')
