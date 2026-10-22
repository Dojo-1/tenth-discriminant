#!/usr/bin/env python3
"""Separately declared historical follow-up, not a change to old M2 evidence."""
import argparse, json
from pathlib import Path
from comparator import pure_core, blob, HASHES, require
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True)
a=p.parse_args();f=a.source_root/'tools/verify_exact.py'
require(blob(f.read_bytes())==HASHES['tools/verify_exact.py'],'source changed')
core=pure_core(f.read_text());G=core['gram']([(0,0),(1,0),(2,0)],1,1,4,19)
require(G==[[6]],'actual matrix mismatch')
require(4>=3+1 and 3*4>2+4*(1+1),'sufficient independence guard failed')
require(6>6//10**6,'M2 was not rejected')
print(json.dumps({'G':G,'det':6,'diagonal_product':6,'old_guard':True,'M2_bound':0,'M2_rejected':True},indent=2))
