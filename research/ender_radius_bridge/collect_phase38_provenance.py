"""Validate a completed local inventory; names flag review, not method absence."""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

here = Path(__file__).resolve().parent
path = here / sys.argv[1]
run = json.loads(path.read_text(encoding='utf-8-sig'))
assert run['exit_code'] == 0 and not run['stop_reason'], 'No accepted completed run'
assert run['time_limit_seconds'] == 180 and run['memory_threshold_mb'] == 8192
records = []
archives = json.loads((here/'PHASE38_ARCHIVES.json').read_text(encoding='utf-8'))
if (here/run['stdout']).is_file():
    raw = (here/run['stdout']).read_bytes()
else:
    with zipfile.ZipFile(here/archives['raw_archive']) as z:
        raw = z.read(run['stdout'])
assert len(raw) == archives['raw_bytes']
assert hashlib.sha256(raw).hexdigest() == archives['raw_SHA256']
for line in raw.decode('utf-8-sig').splitlines():
    if line.startswith('PROVENANCE_JSON '):
        records.append(json.loads(line.removeprefix('PROVENANCE_JSON ')))
expected = [
    'ProvenanceProbe.clean', 'ProvenanceProbe.wrapped', 'ProvenanceProbe.typeOnly',
    'TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one',
    'TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound',
    'TenthDiscriminant.phase36_all_fibers',
    'TenthDiscriminant.known_nine_classNumber_one',
    'TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff',
]
assert [r['root'] for r in records] == expected, 'Missing, reordered or additional roots'
for r in records:
    names = [x['name'] for x in r['constants']]
    assert not r['missing'] and len(set(names)) == len(names) == r['visited_count']
    assert set(r['axioms']) <= {'propext', 'Classical.choice', 'Quot.sound'}
    assert not any(x['unsafe'] for x in r['constants'])
    assert r['root'] in names

def names(r):
    return {x['user_name'] for x in r['constants']}

fake = 'ProvenanceProbe.simulatedHeegnerInput'
assert fake not in names(records[0]), 'Environment-wide grep mistaken for reachability'
assert {fake, 'ProvenanceProbe.relay'} <= names(records[1]), 'Hidden relay was missed'
assert any(x['user_name'] == fake and x['kind'] == 'opaque' for x in records[1]['constants'])
assert 'ProvenanceProbe.taggedType' in names(records[2]), 'Type-only dependency was missed'
for r in records[3:]:
    assert not any(x['user_name'].startswith('ProvenanceProbe.') for x in r['constants'])

real = records[3:]
final_names = {x['name'] for x in real[-1]['constants']}
assert all({x['name'] for x in r['constants']} <= final_names for r in real[:-1]), 'Component closure missing from final closure'
selected = {}
flagged = {}
def discovery_flag(row):
    texts = [row['user_name'].lower(), row['module'].lower()]
    return any(k in text for text in texts for k in ['heegner', 'siegel']) or any(
        part.startswith(('lseries', 'lfunction')) for text in texts for part in text.split('.'))

assert discovery_flag({'user_name': 'Probe.LFunction.input', 'module': 'Probe'})
assert discovery_flag({'user_name': 'Probe.input', 'module': 'Probe.LSeries.Basic'})
assert not discovery_flag({'user_name': 'Real.exp', 'module': 'Mathlib.Analysis.SpecialFunctions.Exp'})

for r in real:
    selected[r['root']] = [x for x in r['constants'] if (
        x['module'].startswith('Mathlib.') and any(k in x['module'].lower() for k in
        ['classnumber', 'classgroup', 'minkowski']))]
    flagged[r['root']] = [x for x in r['constants'] if discovery_flag(x)]
result = {
    'phase': 38, 'protocol_commit': 'b514c46',
    'audited_proof_head': 'ebf14c2564102ef54139024ce9f9c46228307692',
    'auditor_source_SHA256': hashlib.sha256((here/'Phase38Provenance.lean').read_bytes()).hexdigest(),
    'run_record': path.name, 'run': run,
    'raw_archive_metadata': archives,
    'traversal_controls': 'PASS: unused exclusion, private/opaque relay and type-only dependency',
    'roots': [{k: r[k] for k in ['root', 'visited_count', 'axioms']} for r in real],
    'component_closures_are_subsets_of_final': True,
    'external_class_number_related_rows_for_source_review': selected,
    'discovery_flags_not_a_verdict': flagged,
    'discovery_filter_repair': 'V1 matched lfunction inside SpecialFunctions; V1 is preserved in PHASE38_DISCOVERY_V1.zip. V2 requires LSeries/LFunction namespace-token prefixes. No Lean run was repeated.',
    'semantic_review': 'See PROOF_INPUT_GUIDE.md for internal pinned-source inspection. This inventory alone is not method exclusion or independent human review.',
    'scope': 'Frozen internally performed compiled dependency-closure inventory, not independent human review or a permanent CI gate',
}
by_root = {r['root']: r for r in real}
def reaches(root, name):
    return any(x['name'] == name for x in by_root[root]['constants'])

cutoff = 'TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound'
positive = 'TenthDiscriminant.known_nine_classNumber_one'
certificate = 'TenthDiscriminant.phase36_all_fibers'
classification = 'TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff'
result['dependency_separation'] = {
    'cutoff_reaches_positive_cases': reaches(cutoff, positive),
    'cutoff_reaches_full_fiber_certificate': reaches(cutoff, certificate),
    'cutoff_reaches_final_classification': reaches(cutoff, classification),
    'positive_cases_reach_full_fiber_certificate': reaches(positive, certificate),
    'positive_cases_reach_million_sieve_module': any(x['module'] == 'TenthDiscriminant.MillionSieve'
        for x in by_root[positive]['constants']),
    'full_fiber_certificate_reaches_actual_class_number': reaches(certificate, 'NumberField.classNumber'),
    'final_classification_reaches_positive_cases': reaches(classification, positive),
    'final_classification_reaches_full_fiber_certificate': reaches(classification, certificate),
}
result['reached_number_theory_modules'] = {r['root']: sorted({x['module'] for x in r['constants']
    if x['module'].startswith('Mathlib.NumberTheory.')}) for r in real}
(here/'PHASE38_INVENTORY.json').write_text(json.dumps(result, indent=2)+'\n',
    encoding='utf-8', newline='\n')
print(json.dumps({'controls': 'PASS', 'roots': result['roots'],
    'review_rows': {k: len(v) for k, v in selected.items()},
    'discovery_flags': {k: len(v) for k, v in flagged.items()}}))
