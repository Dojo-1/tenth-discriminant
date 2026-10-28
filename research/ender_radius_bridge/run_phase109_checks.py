"""Bounded synthetic scheduler test receipt; does not execute Lean."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys,time
p=Path(__file__).resolve().parent;r=p.parents[1]
previous=[json.loads(n.read_text(encoding='utf-8')) for n in p.glob('PHASE109_checks_*.result.json')]
if len(previous)>=3 or any(n['stop_reason'] or n['exit_code']==0 for n in previous):
    raise SystemExit('Phase109 test slots exhausted, resource stop, or already accepted')
stamp=datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')
stem='PHASE109_checks_'+stamp
sources={}
for n in ['control_schedule.py','control_schedule_tests.py','negative_controls.py']:
    snapshot=stem+'.'+n;b=(r/'lean'/n).read_bytes();(p/snapshot).write_bytes(b)
    sources[snapshot]=hashlib.sha256(b).hexdigest()
command=[sys.executable,'control_schedule_tests.py'];start=time.monotonic();reason=''
try:
    process=subprocess.run(command,cwd=r/'lean',capture_output=True,timeout=120)
    code=process.returncode;stdout=process.stdout;stderr=process.stderr
except subprocess.TimeoutExpired as error:
    code=124;reason='outer_time_limit';stdout=error.stdout or b'';stderr=error.stderr or b''
(p/(stem+'.stdout.log')).write_bytes(stdout);(p/(stem+'.stderr.log')).write_bytes(stderr)
d={'phase':109,'scope':'SYNTHETIC scheduler tests, no Lean','attempt':len(previous)+1,'exit_code':code,
'elapsed_seconds':time.monotonic()-start,'time_limit_seconds':120,'stop_reason':reason,
'observed_peak_memory':'UNOBSERVED','command':command,'cwd':'lean','source_sha256':sources,
'stdout':stem+'.stdout.log','stderr':stem+'.stderr.log'}
(p/(stem+'.result.json')).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8',newline='\n')
print(stderr.decode('utf-8',errors='replace')[-3000:]);print(json.dumps(d,indent=2));raise SystemExit(code)
