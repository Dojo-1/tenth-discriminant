"""Phase371: deterministic task-bound GitHub source-guard probe.

Push attempt 1 is explicitly NOT issued evidence. Following a publicly
recorded issue event, a manual rerun (attempt >= 2) executes the original
source guard and prints an exact task and completion marker. This is
execution provenance, not independent mathematical or signing authority.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SOURCE="original-integer-pair-ordinary-Z-gram@phase367"
NONCE="phase371-source-anchor-external-issue-20261120-v1"
REF="refs/heads/research/phase371-causal-receipt-state-machine"
def task_fields(head):
    if not re.fullmatch(r"[0-9a-f]{40}",head):
        raise ValueError("full SHA required")
    return {"arm":"source_anchor_mutation","scope":"source_contract",
            "source":SOURCE,"repository_head":head,"issued_epoch":1,
            "research_clock":"fast","cost_units":1,"nonce":NONCE}
def task_id(head):
    x=json.dumps(task_fields(head),sort_keys=True,ensure_ascii=True,separators=(",",":"))
    return hashlib.sha256(x.encode("utf-8")).hexdigest()
def probe(env):
    head=env["GITHUB_SHA"]
    if env["GITHUB_REF"]!=REF:
        raise ValueError("incorrect Git ref")
    tid=task_id(head)
    attempt=int(env.get("GITHUB_RUN_ATTEMPT","0"))
    runid=env["GITHUB_RUN_ID"]
    if not runid.isdigit() or attempt<1:
        raise ValueError("invalid execution identity")
    if attempt==1:
        return "PHASE371_INITIAL_PUSH_NOT_ISSUED_NO_CREDIT"
    root=Path(__file__).resolve().parents[2]
    p=subprocess.run([sys.executable,str(root/"scripts"/"phase365_lean_anchor_guard.py")],
                     cwd=str(root),capture_output=True,text=True,check=True,timeout=90)
    if "PHASE365_TEXTUAL_LEAN_SOURCE_ANCHORS_OK" not in p.stdout:
        raise RuntimeError("missing original source success marker")
    if p.stdout.count("EXPECTED_REJECTION")!=5:
        raise RuntimeError("missing deliberately invalid source mutation controls")
    return (f"PHASE371_TASK_ID={tid}\nPHASE371_RUN_ID={runid}\n"
            f"PHASE371_RUN_ATTEMPT={attempt}\nVERIFIED_PHASE371_SOURCE_ANCHOR")
if __name__=="__main__":
    print(probe(dict(os.environ)),flush=True)
