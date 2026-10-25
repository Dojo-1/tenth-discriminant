"""Preserve/verify one returned review and its documentation-only correction."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import subprocess
import sys

here=Path(__file__).resolve().parent
root=here.parents[1]
target='69010f4e5d2e0adc44c70932d20583e669b7b7c2'
report=here/'PHASE51_REVIEW_REPORT.md'
manifest=here/'PHASE51_RESULTS.json'
digest=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda b:b.decode('utf-8-sig').replace('\r\n','\n').encode()
names=['QuadraticGeneratorBridge','ImaginaryQuadraticRepresentation',
       'CentralSymmetry','ParityCompatibility']
sources={f'lean/TenthDiscriminant/{n}.lean':None for n in names}
for p in sources:
    baseline=subprocess.check_output(['git','show',target+':'+p],cwd=root)
    assert lf((root/p).read_bytes())==lf(baseline),p
    sources[p]=digest(lf(baseline))
assert subprocess.check_output(['git','diff','--name-only',target,'--',
    'lean/TenthDiscriminant','lean/TenthDiscriminant.lean','lean/lakefile.toml',
    'lean/lean-toolchain','tools','.github'],cwd=root).strip()==b''
guide='research/ender_radius_bridge/CONJUGATION_BRIDGE_GUIDE.md'
old=subprocess.check_output(['git','show',target+':'+guide],cwd=root).decode().replace('\r\n','\n')
expected=old.replace(
    'two is used at one specific field-theoretic step: identifying the fixed\nfield with Q.',
    'two has two field-theoretic roles: quadratic Galoisness lets complex\n'
    'conjugation act on K, and the two-element automorphism group makes its\n'
    'fixed field Q. The projector identities themselves need no degree-two\n'
    'hypothesis once a rational algebra involution is supplied.').replace(
    'Complex conjugation transports through an embedding into an automorphism\n'
    'sigma of K. It is nonidentity and squares to the identity. A quadratic',
    'Because the quadratic extension of Q is Galois, complex conjugation\n'
    'transports through an embedding into an automorphism sigma of K.\n'
    'It is nonidentity and squares to the identity. A quadratic').replace(
    'whole quadratic Galois group. Its fixed field is Q.\n',
    'whole quadratic Galois group. Its fixed field is Q.\n\n'
    'This rationality conclusion does not extend to every number field with an\n'
    'involution. In Q(i,sqrt(2)), conjugation negates u=i*(1+sqrt(2)), but\n'
    'u^2=-3-2*sqrt(2) is not rational. The projector identities still hold;\n'
    'the invariant part is larger. The large jet module never needed to have\n'
    'dimension two for this distinction to matter.\n')
assert lf((root/guide).read_bytes()).decode()==expected
if '--seal' in sys.argv:
    assert not manifest.exists()
    data=dict(scope='one fresh-context bounded AI source review; no inherited exhaustive audit',
        target=target,protocol_commit='7e6cd1ce5e7641746509ed0587180dd93e4cfbe5',
        user_authorization='Run one bounded reviewer',agent='/root/bridge_semantic_review',
        fork_turns='none',model_override=None,exact_model_identifier='not exposed by tool',
        dispatch_marker='2026-10-25T19:44:52Z',deadline='2026-10-25T20:14:52Z',
        last_inspection_reported='2026-10-25T19:47:16.4020468Z',
        return_confirmed_before='2026-10-25T19:50:00Z',reviewer_count=1,rerolls=0,
        report_kind='verbatim returned-review transcription, not raw tool archive',
        report_bytes=report.stat().st_size,report_sha256=digest(report.read_bytes()),
        reviewed_source_sha256_lf=sources,
        protocol_sha256_lf=digest(lf((here/'PHASE51_PROTOCOL.md').read_bytes())),
        brief_sha256_lf=digest(lf((here/'PHASE51_REVIEW_BRIEF.md').read_bytes())),
        findings=[dict(severity='SLOPPY',effect='documentation degree-two dependency, no proof repair',
            correction='quadratic Galoisness/conjugation and two-element-group/rationality distinguished',
            parent_inspected=True,corrected=True,re_reviewed=False)],
        conclusion='No contradiction established in five bounded checks; no FATAL/GAP finding established',
        limitations=['inherited analytic proof not reconstructed','no new build/audit by reviewer',
            'no human or model-family independence established','no publication-readiness verdict'],
        correction_sha256_lf=digest(expected.encode()))
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(manifest.read_text())
assert report.stat().st_size==data['report_bytes'] and digest(report.read_bytes())==data['report_sha256']
assert sources==data['reviewed_source_sha256_lf']
assert digest(expected.encode())==data['correction_sha256_lf']
assert digest(lf((here/'PHASE51_PROTOCOL.md').read_bytes()))==data['protocol_sha256_lf']
assert digest(lf((here/'PHASE51_REVIEW_BRIEF.md').read_bytes()))==data['brief_sha256_lf']
time=lambda s:datetime.fromisoformat(s.replace('Z','+00:00'))
assert time(data['dispatch_marker'])<time(data['last_inspection_reported'])<=time(data['return_confirmed_before'])<time(data['deadline'])
assert (time(data['deadline'])-time(data['dispatch_marker'])).total_seconds()==1800
assert data['reviewer_count']==1 and data['rerolls']==0
text=report.read_text(encoding='utf-8')
assert text.startswith('Phase51 first returned review — bounded, read-only\n')
assert 'Finding: SLOPPY' in text and 'No FATAL or GAP finding was established' in text
print('PASS: first returned review hash, four frozen source hashes, protocol/brief, time bounds;')
print('one documentation correction exactly accounted for; no mathematical/tool/pin/gate changes.')
print('Scope: provenance and correspondence, not another semantic review or proof execution.')
