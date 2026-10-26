"""Collect completed fixed-target proof/verification records; never run a proof."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

here = Path(__file__).resolve().parent
repo = here.parents[1]
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

attempts = [{'record': p.name, **read(p)} for p in sorted(here.glob('PHASE39_BUILD_*.result.json'))]
assert len(attempts) == 1 and attempts[0]['exit_code'] == 0 and not attempts[0]['stop_reason']
assert attempts[0]['time_limit_seconds'] == 600
assert attempts[0]['cumulative_allowance_seconds'] == 900
assert attempts[0]['memory_threshold_mb'] == 8192
assert attempts[0]['build_target'] == 'TenthDiscriminant.OptimizedAnalyticCutoff'
checks = [{'record': p.name, **read(p)} for p in sorted(here.glob('PHASE39_VERIFY_*.result.json'))]
assert len(checks) == 2 and all(x['exit_code'] == 0 and not x['stop_reason'] for x in checks)
sig = next(x for x in checks if x['proof_file'].endswith('Phase39InputCheck.lean'))
audit = next(x for x in checks if x['proof_file'] == 'Audit.lean')
sigtext = (here/sig['stdout']).read_text(encoding='utf-8-sig')
roots = re.findall(r'ANALYTIC_INPUTS_OK (\S+): (\d+) reached;', sigtext)
assert roots == [
    ('TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b', '55439'),
    ('TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b', '55572'),
    ('TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b', '55775')]
arc = read(here/'PHASE39_ARCHIVES.json')
with zipfile.ZipFile(here/arc['archive']) as z:
    raw = z.read(arc['entry'])
assert len(raw) == arc['raw_bytes'] and hashlib.sha256(raw).hexdigest() == arc['SHA256']
assert 'AUDIT_OK TenthDiscriminant: 4534 logical declarations; 3803 theorems; 16951 runtime-only auxiliaries excluded' in raw.decode('utf-8-sig')
rootbuild = read(here/'PHASE25_INTEGER_CHUNKS_20261025014958.result.json')
assert rootbuild['build_target'] == 'TenthDiscriminant' and rootbuild['exit_code'] == 0
files = ['lean/TenthDiscriminant.lean', 'lean/TenthDiscriminant/UniformRadiusFamily.lean',
    'lean/TenthDiscriminant/UniformUpperEnvelope.lean',
    'lean/TenthDiscriminant/OptimizedAnalyticCutoff.lean',
    'research/ender_radius_bridge/Phase39InputCheck.lean',
    'research/ender_radius_bridge/run_phase39_build.ps1']
result = {
    'phase': 39, 'protocol_commit': '35a6b4b392c294da259dbb84b155bb1ac2a8976c',
    'publication_baseline': '580c0b95fdb788857e29f61a7bdc2d13b559fd3d',
    'baseline_CI': '40151064234 SUCCESS; final record issuecomment-6392200072 before any newer publication',
    'fixed_direct_analytic_cutoff': 200000000000, 'previous_analytic_cutoff': 700000000000,
    'classification_endgame_unchanged': True,
    'attempts_including_failures': attempts, 'post_acceptance_checks': checks,
    'whole_root_build': rootbuild, 'root_import_count': 153,
    'input_exclusion_closures': {name: int(n) for name,n in roots},
    'compiled_audit': {'logical': 4534, 'theorems': 3803, 'runtime_only': 16951,
        'allowed_axioms': ['propext', 'Classical.choice', 'Quot.sound']},
    'audit_archive': arc,
    'source_SHA256': {f: hashlib.sha256((repo/f).read_bytes()).hexdigest() for f in files},
    'claim_boundary': 'Direct new analytic bound in the canonical actual positive-squarefree family, not classification recycling. No optimality, novelty or independent human review claim.',
    'publication_CI': 'Pending exact-head pinned CI; final PR verification record supersedes pending checkpoints.',
    'frozen_phase38_snapshot': 'Remains at ebf14c2; not automatically transferred to this changed mathematical source.',
}
(here/'PHASE39_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({'cutoff': result['fixed_direct_analytic_cutoff'], 'first_attempt': 'PASS',
    'root': 'PASS', 'input_checks': roots, 'compiled_audit': result['compiled_audit']}))
