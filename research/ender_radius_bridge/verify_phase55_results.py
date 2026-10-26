"""Seal/verify bounded-review provenance; does not decide mathematical validity."""
from pathlib import Path
from datetime import datetime
import hashlib, json, subprocess, sys

here=Path(__file__).resolve().parent; root=here.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
lf=lambda p:p.read_text(encoding='utf-8-sig').replace('\r\n','\n')
dispatch=json.loads(lf(here/'PHASE55_DISPATCH.json'))
receipt=json.loads(lf(here/'PHASE55_RECEIPT.json'))
parse=lambda s:datetime.fromisoformat(s.replace('Z','+00:00'))
elapsed=(parse(receipt['received_utc'])-parse(dispatch['dispatch_marker_utc'])).total_seconds()
assert 0<=elapsed<=1800 and parse(receipt['received_utc'])<=parse(dispatch['deadline_utc'])
assert dispatch['authorized_reviewers']==1
assert dispatch['target_commit']=='86abe21f1ca023f9f62f99d1f785cdb361d86010'
assert dispatch['target_tree']=='7383bdcc0fa035bc83628420785813240b0e535e'
commit_time=lambda ref:parse(subprocess.check_output(['git','show','-s','--format=%cI',ref],cwd=root,text=True).strip())
assert commit_time(dispatch['brief_commit'])<=commit_time(dispatch['protocol_commit'])<=parse(dispatch['dispatch_marker_utc'])
subprocess.run(['git','merge-base','--is-ancestor',dispatch['brief_commit'],dispatch['protocol_commit']],cwd=root,check=True)
assert subprocess.check_output(['git','rev-parse',dispatch['target_commit']+'^{tree}'],cwd=root,text=True).strip()==dispatch['target_tree']
for n,h in dispatch['source_sha256_lf'].items():
    b=subprocess.check_output(['git','show',dispatch['target_commit']+':'+n],cwd=root).decode().replace('\r\n','\n').encode()
    assert sha(b)==h==sha(lf(root/n).encode()),n
for name,ref in [('PHASE55_PROTOCOL.md',dispatch['protocol_commit']),('RECOVERED_CUTOFF_REVIEW_BRIEF.md',dispatch['brief_commit'])]:
    n='research/ender_radius_bridge/'+name
    b=subprocess.check_output(['git','show',ref+':'+n],cwd=root).decode().replace('\r\n','\n').encode()
    assert b==lf(root/n).encode(),n
changed=subprocess.check_output(['git','diff','--name-only',dispatch['target_commit'],'--','lean/TenthDiscriminant','lean/TenthDiscriminant.lean','tools','.github'],cwd=root,text=True).splitlines()
assert not changed,changed
report=here/'PHASE55_REVIEW_REPORT.md';payload=report.read_bytes()
assert sha(payload)==receipt['report_sha256'] and len(payload)==receipt['report_bytes']
manifest=here/'PHASE55_RESULTS.json'
files=[here/'PHASE55_DISPATCH.json',here/'PHASE55_RECEIPT.json',report]
if '--seal' in sys.argv:
    assert not manifest.exists()
    data=dict(scope='one six-obligation fresh-context AI source review; no whole-project certification',
        status='FIRST_REPORT_PRESERVED',target_commit=dispatch['target_commit'],target_tree=dispatch['target_tree'],
        protocol_commit=dispatch['protocol_commit'],brief_commit=dispatch['brief_commit'],
        conservative_elapsed_seconds=elapsed,report_origin='native first final report written once by authorized reviewer; not parent transcription',
        raw_sha256={p.relative_to(root).as_posix():sha(p.read_bytes()) for p in files},
        source_sha256_lf=dispatch['source_sha256_lf'],
        independence='fresh fork_turns=none; no model override; exact model-family and human independence not established',
        exact_head_ci='separate evidence; not inferred by this verifier')
    manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
data=json.loads(lf(manifest))
for n,h in data['raw_sha256'].items():assert sha((root/n).read_bytes())==h,n
assert data['conservative_elapsed_seconds']==elapsed
print('PASS: first native report and dispatch/receipt hashes; protocol and brief precede dispatch;')
print('frozen tree/seven source hashes and no proof/tool/gate edits; one reviewer, within30-minute bound.')
print('This verifies provenance, not the reviewer verdict or independent human/model-family review.')
