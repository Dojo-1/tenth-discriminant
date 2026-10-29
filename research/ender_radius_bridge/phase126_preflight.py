from pathlib import Path
import hashlib,json,re
r=Path(__file__).resolve().parent
root=r.parents[1]
f=json.loads((r/'PHASE126_FROZEN.json').read_text(encoding='utf-8'))
s=(r/'Phase126Classification.lean').read_text(encoding='utf-8')
pattern=r'(^theorem .*?:= by\n).*?(?=^theorem |^end$)'
out,count=re.subn(pattern,lambda m:m.group(1)+'<PROOF>\n',s,flags=re.S|re.M)
assert count==2 and hashlib.sha256(out.encode()).hexdigest()==f['outside_proofs_sha256']
for name,digest in f['immutable_files'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
if not list(r.glob('PHASE126_build_*.result.json')):
    assert hashlib.sha256(s.encode()).hexdigest()==f['first_source_sha256']
assert len(re.findall(r'^theorem ',s,re.M))==2
print('PASS126static:2frozen actual-field targets/imports/options/audits;only proof bodies may vary')
