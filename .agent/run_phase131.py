"""One-shot registered comparator supervisor; no old trial/Lean invocation."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time
r=Path(__file__).resolve().parents[1];p=r/'research/ender_radius_bridge'
sha=lambda b:hashlib.sha256(b).hexdigest()
f=json.loads((p/'PHASE131_FROZEN.json').read_bytes())
assert not list(p.glob('PHASE131_trial_*')),'A trial already exists;reconcile it,never restart'
source=p/'phase131_exterior_comparator.py'
assert sha(source.read_bytes())==f['source_sha256']
assert sha((p/'PHASE131_PROTOCOL.md').read_bytes())==f['protocol_sha256']
assert subprocess.check_output(['git','diff','03cb58c','--name-only','--','lean','.github'],cwd=r)==b''
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
prefix=p/('PHASE131_trial_'+stamp)
snapshot=prefix.with_suffix('.source.py');shutil.copyfile(source,snapshot)
data=prefix.with_suffix('.data.json');stdout=prefix.with_suffix('.stdout.log');stderr=prefix.with_suffix('.stderr.log')
start=time.monotonic();stop=''
with stdout.open('wb') as out,stderr.open('wb') as err:
    process=subprocess.Popen([sys.executable,str(source),str(data)],cwd=r,stdout=out,stderr=err)
    live={'phase':131,'pid':process.pid,'prefix':str(prefix),'status':'running','max_seconds':60}
    (r/'.agent/PHASE131_LIVE.json').write_bytes((json.dumps(live,indent=2)+'\n').encode())
    try:code=process.wait(timeout=60)
    except subprocess.TimeoutExpired:
        process.kill();process.wait();code=99;stop='time_limit'
elapsed=time.monotonic()-start
result={'phase':131,'attempt':1,'exit_code':code,'stop_reason':stop,'elapsed_seconds':elapsed,'max_seconds':60,
    'source_frozen_commit':f['source_frozen_commit'],'protocol_commit':f['protocol_commit'],
    'source_snapshot':snapshot.name,'source_sha256':sha(snapshot.read_bytes()),'data':data.name,
    'stdout':stdout.name,'stderr':stderr.name,'memory_measurement':'not measured;no memory cap or peak claim',
    'scope':'New220minor comparator on8fixed sealedGramcases;not old80case or Lean replay'}
prefix.with_suffix('.result.json').write_bytes((json.dumps(result,indent=2)+'\n').encode())
live['status']='terminal';(r/'.agent/PHASE131_LIVE.json').write_bytes((json.dumps(live,indent=2)+'\n').encode())
print(stdout.read_text(encoding='utf-8'));print(stderr.read_text(encoding='utf-8'));print(json.dumps(result,indent=2))
sys.exit(code)
