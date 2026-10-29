"""Package terminal registered checks; reads saved evidence only."""
from pathlib import Path
import hashlib,json,re,zipfile
r=Path(__file__).resolve().parents[1];p=r/'research/ender_radius_bridge'
sha=lambda b:hashlib.sha256(b).hexdigest()
raw={'PHASE128_CORRESPONDENCE.json':(p/'PHASE128_CORRESPONDENCE.json').read_bytes()};runs={};logs={}
for mode in ['build','root','input','audit']:
    files=list(p.glob(f'PHASE128_{mode}_*.result.json'));assert len(files)==1
    f=files[0];x=json.loads(f.read_bytes());assert x['exit_code']==0 and not x['stop_reason'];runs[mode]=x
    stem=f.name.removesuffix('.result.json')
    for q in p.glob(stem+'.*'):raw[q.name]=q.read_bytes()
    logs[mode]=raw[x['stdout']].decode('utf-8-sig')
assert len(raw)==33
audits={n:{'logical':int(a),'theorems':int(b),'runtime':int(c)} for n,a,b,c in re.findall(r'AUDIT_OK TenthDiscriminant\.([\w]+): (\d+) logical declarations; (\d+) theorems; (\d+) runtime-only auxiliaries excluded',logs['input'])}
whole=re.search(r'AUDIT_OK TenthDiscriminant: (\d+) logical declarations; (\d+) theorems; (\d+) runtime-only auxiliaries excluded',logs['audit']);assert whole
extract=lambda s:set(re.findall(r'DEPENDENCIES_CHECKED ([^;]+);',s))
with zipfile.ZipFile(p/'PHASE121_RAW.zip') as z:old=extract(z.read(next(n for n in z.namelist() if '_audit_' in n and n.endswith('.stdout.log'))).decode('utf-8-sig'))
new=extract(logs['audit']);assert not old-new
archive=p/'PHASE128_RAW.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for n,b in sorted(raw.items()):z.writestr(n,b)
d={'phase':128,'status':'EXACT_INTEGRATION_ALL_FOUR_FIRST_CHECKS_PASS','registered_commit':'3e95187dbcafc6c4a6fe77cb1964268d35a99479',
 'runs':runs,'namespace_audits':audits,'whole_audit_marker':whole[0],
 'whole_audit':dict(zip(['logical','theorems','runtime'],map(int,whole.groups()))),
 'added_declarations':sorted(new-old),'removed_declarations':sorted(old-new),'reachable_modules':205,
 'archive_sha256':sha(archive.read_bytes()),'raw_sha256':{n:sha(b) for n,b in raw.items()},
 'observer_incident':'Initial static preflight used character offsets as byte offsets; corrected before any Lean invocation. No proof changed and no trial restarted.',
 'publication':'Pending;local evidence does not imply pinned CI,merge or independent semantic review.'}
(p/'PHASE128_RESULTS.json').write_bytes((json.dumps(d,indent=2)+'\n').encode())
print('PACKAGED128:33raw;four terminal successful first checks;run saved verifier next')
