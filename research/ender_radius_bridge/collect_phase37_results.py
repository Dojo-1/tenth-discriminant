"""Collect existing records only; never execute or relabel a proof attempt."""
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
repo = here.parents[1]
completion = here / 'PHASE37_CHECK_20261025002509049.result.json'
record = json.loads(completion.read_text(encoding='utf-8-sig'))
assert record['exit_code'] == 0 and not record['stop_reason']
assert record['time_limit_seconds'] == 180
assert record['memory_threshold_mb'] == 8192
assert record['proof_file'] == '../research/ender_radius_bridge/Phase36Seed10Check.lean'
inputs = [
    'research/ender_radius_bridge/Phase36Seed10Check.lean',
    'lean/TenthDiscriminant/QuotientFiberCore.lean',
    'lean/TenthDiscriminant/QuotientFiberData.lean',
    'lean/TenthDiscriminant/QuotientFiberParameters.lean',
]
builds = []
for p in sorted(here.glob('PHASE25_INTEGER_CHUNKS_*.result.json')):
    if p.name < 'PHASE25_INTEGER_CHUNKS_20261025002646.result.json':
        continue
    builds.append({'record': p.name, **json.loads(p.read_text(encoding='utf-8-sig'))})
result = {
    'phase': 37,
    'protocol_commit': '22d0ac4',
    'frozen_incomplete_phase36_commit': 'c1bafe7',
    'phase36_outcome_unchanged': 'ten pass; seed179 aggregate-time-stopped; INCOMPLETE',
    'new_completion_record': completion.name,
    'new_completion': record,
    'unchanged_input_SHA256': {p: hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in inputs},
    'original_interval': [1000000, 700000000000],
    'upper_endpoint_exclusive': True,
    'quotient_positions': 785,
    'all_200_extra_primes_unchanged': True,
    'local_build_records_including_failures': builds,
    'archived_raw_audit_stdout': json.loads((here/'PHASE37_AUDIT_ARCHIVE.json').read_text(encoding='utf-8')),
    'repair': 'First root build retained: list-normalization elaboration error in signed-discriminant corollary; fixed with List.not_mem_nil/or_false, unchanged statements and limits.',
    'raw_metadata_note': 'Legacy Phase25 filenames/scope metadata preserved. build_target, proof_file and stdout identify actual Phase37 checks.',
    'publication': 'Exact tested head/tree and terminal pinned CI status belong to the final PR verification record; no full local parent/apparatus or negative-control-suite pass inferred.',
    'scope': 'Canonical actual positive-squarefree imaginary quadratic field family; no arbitrary-field representation theorem, optimized constant, independent human review, merge or Tao post.',
}
(here/'PHASE37_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({'completion': record['exit_code'], 'local_records': len(builds)}))
