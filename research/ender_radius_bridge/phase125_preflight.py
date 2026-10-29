from pathlib import Path
import hashlib,json,re,sys
r=Path(__file__).resolve().parent
root=r.parents[1]
f=json.loads((r/'PHASE125_FROZEN.json').read_text(encoding='utf-8'))
source=(r/'Phase125Endpoint.lean').read_text(encoding='utf-8')
pattern=r'(theorem endpoint_log_lower.*?:= by\n).*?(?=\ntheorem endpoint_separation)'
normalized,count=re.subn(pattern,lambda m:m.group(1)+'<ADAPTER>\n',source,flags=re.S)
assert count==1
assert hashlib.sha256(normalized.encode()).hexdigest()==f['outside_adapter_sha256']
assert hashlib.sha256((r/'Phase122Endpoint.lean').read_bytes()).hexdigest()==f['old_source_sha256']
for name,digest in f['immutable_files'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
prior=list(r.glob('PHASE125_build_*.result.json'))
if not prior:
    assert hashlib.sha256(source.encode()).hexdigest()==f['first_source_sha256']
assert len(re.findall(r'^theorem ',source,re.M))==10
assert len(re.findall(r'``TenthDiscriminant\.',source))==77
print('PASS125static:frozen statements/imports/controls/77roots;only adapter body may vary;Phase122unchanged')
