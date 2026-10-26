"""Validate saved proof evidence; does not execute Lean or evaluate the area integral."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile
folder=Path(__file__).resolve().parent
root=folder.parents[1]
data=json.loads((folder/"PHASE63_RESULTS.json").read_text(encoding="utf-8"))
sha=lambda b:hashlib.sha256(b).hexdigest()
for name,digest in data["sha256"].items():
    assert sha((folder/name).read_bytes())==digest,name
protocol=subprocess.check_output(["git","show",data["registered_commit"]+":research/ender_radius_bridge/PHASE63_PROTOCOL.md"],cwd=root)
assert sha(protocol)==data["sha256"]["PHASE63_PROTOCOL.md"]
subprocess.run(["git","merge-base","--is-ancestor",data["registered_commit"],"HEAD"],cwd=root,check=True)
archive=folder/data["raw_archive"]["path"]
assert sha(archive.read_bytes())==data["raw_archive"]["sha256"]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist())==8
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==data["raw_sha256"]
records=data["builds"]
assert [r["exit_code"] for r in records]==[1,0]
assert [r["attempt"] for r in records]==[1,2]
assert sum(Decimal(str(r["elapsed_seconds"])) for r in records)==Decimal(data["target_seconds"])<1200

def types(s):
    return {m.group(1):" ".join(s[m.start():s.index(":=",m.end())].split())
            for m in re.finditer(r"(?m)^theorem\s+(\w+)",s)}

def definitions(s):
    return {m.group(1):m.group(0) for m in re.finditer(r"(?ms)^def (\w+)\b.*?(?=^theorem |^def |\Z)",s)}

first=raw[records[0]["source_snapshot"]].decode("utf-8")
last=raw[records[-1]["source_snapshot"]].decode("utf-8")
assert len(types(first))==14 and types(first)==types(last)
assert len(definitions(first))==5 and definitions(first)==definitions(last)
assert first.split("#audit_namespace",1)[1]==last.split("#audit_namespace",1)[1]
for r in records:
    assert not r["stop_reason"] and r["elapsed_seconds"]<=600
    assert r["memory_threshold_mb"]==8192
    assert r["observed_peak_working_set_bytes"]<8192*1024**2
    assert sha(raw[r["source_snapshot"]])==r["source_sha256"]
    assert json.loads(raw[r["stdout"].replace(".stdout.log",".result.json")].decode("utf-8-sig"))==r
assert raw[records[-1]["source_snapshot"]]==(folder/"Phase63NonzeroRows.lean").read_bytes()
failed=raw[records[0]["stdout"]].decode("utf-8-sig")
assert "error:" in failed and "NONSTANDARD_AXIOMS" in failed and "sorryAx" in failed
passed=raw[records[-1]["stdout"]].decode("utf-8-sig")
assert "error:" not in passed and "sorryAx" not in passed
assert "AUDIT_OK TenthDiscriminant.NonzeroRows: 34 logical declarations; 29 theorems; 4 runtime-only" in passed
assert "'TenthDiscriminant.NonzeroRows.off_axis_count' depends on axioms: [propext, Classical.choice, Quot.sound]" in passed
changes=subprocess.check_output(["git","diff","--name-only",data["base"],"--","lean","tools",".github","flow"],cwd=root,text=True)
assert not [n for n in changes.splitlines() if not n.endswith(".md")],changes
for path in ["lean/TenthDiscriminant.lean","lean/TenthDiscriminant/ExcludedPrimeAssembly.lean","lean/TenthDiscriminant/PrimeWeightKernel.lean","research/ender_radius_bridge/Phase62PrimeAxis.lean","research/ender_radius_bridge/PHASE62_RESULTS.json","research/ender_radius_bridge/PHASE62_RAW.zip"]:
    assert (root/path).read_bytes()==subprocess.check_output(["git","show",data["base"]+":"+path],cwd=root),path
print("PASS: registered actual off-axis target; both raw attempts; unchanged14 theorem types/5 definitions; final audit and guards; production and prior axis proof unchanged.")
print("Integrity only. No Lean rerun, closed area evaluation, arithmetic B, cutoff, production-CI coverage or independent review inferred.")
