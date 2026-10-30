from pathlib import Path
import hashlib,json,re
r=Path(__file__).resolve().parent
root=r.parents[1]
f=json.loads((r/'PHASE127_FROZEN.json').read_text(encoding='utf-8'))
s=(r/'Phase127RadialAction.lean').read_text(encoding='utf-8')
pattern=r'(^(?:private )?theorem .*?:= by\n).*?(?=^(?:private )?theorem |^end$)'
out,count=re.subn(pattern,lambda m:m.group(1)+'<PROOF>\n',s,flags=re.S|re.M)
assert count==9 and hashlib.sha256(out.encode()).hexdigest()==f['outside_proofs_sha256']
control=s[s.index('theorem nonmultiplicative_control'):s.index('\nend\n')]
assert hashlib.sha256(control.encode()).hexdigest()==f['control_sha256']
for name,digest in f['immutable_files'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
if not list(r.glob('PHASE127_build_*.result.json')):
    assert hashlib.sha256(s.encode()).hexdigest()==f['first_source_sha256']
assert len(re.findall(r'^(?:private )?theorem ',s,re.M))==9
print('PASS127static:actual matrices/9fixed types/control/70root policy;only positive proof bodies may vary')
