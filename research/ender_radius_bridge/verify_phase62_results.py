"""Saved-evidence integrity; does not execute Lean or prove the split count."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
root = folder.parents[1]
data = json.loads((folder/"PHASE62_RESULTS.json").read_text(encoding="utf-8"))
sha = lambda b: hashlib.sha256(b).hexdigest()
for name, digest in data["sha256"].items():
    assert sha((folder/name).read_bytes()) == digest,name
protocol = subprocess.check_output(["git","show",data["registered_commit"]+":research/ender_radius_bridge/PHASE62_PROTOCOL.md"],cwd=root)
assert sha(protocol) == data["sha256"]["PHASE62_PROTOCOL.md"]
subprocess.run(["git","merge-base","--is-ancestor",data["registered_commit"],"HEAD"],cwd=root,check=True)
archive = folder/data["raw_archive"]["path"]
assert sha(archive.read_bytes()) == data["raw_archive"]["sha256"]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == 8
    raw = {n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()} == data["raw_sha256"]
records = data["builds"]
assert [r["exit_code"] for r in records] == [1,0]
assert [r["attempt"] for r in records] == [1,2]
assert sum(Decimal(str(r["elapsed_seconds"])) for r in records) == Decimal(data["target_seconds"]) < 600

def types(source):
    return {m.group(1):" ".join(source[m.start():source.index(" := by",m.start())].split())
            for m in re.finditer(r"(?m)^theorem\s+(\w+)",source)}

initial = raw[records[0]["source_snapshot"]].decode("utf-8")
final = raw[records[-1]["source_snapshot"]].decode("utf-8")
assert len(types(initial)) == 8 and types(initial) == types(final)
assert initial.replace("have hxone : x.natAbs=1 := by nlinarith", "have hxone : x.natAbs=1 := by simpa [Nat.pow_eq_one] using hu") == final
for record in records:
    assert not record["stop_reason"] and record["elapsed_seconds"] <= 300
    assert record["memory_threshold_mb"] == 8192
    assert record["observed_peak_working_set_bytes"] < 8192*1024**2
    assert sha(raw[record["source_snapshot"]]) == record["source_sha256"]
    saved = record["stdout"].replace(".stdout.log",".result.json")
    assert json.loads(raw[saved].decode("utf-8-sig")) == record
assert raw[records[-1]["source_snapshot"]] == (folder/"Phase62PrimeAxis.lean").read_bytes()
failed = raw[records[0]["stdout"]].decode("utf-8-sig")
assert "linarith failed" in failed and "NONSTANDARD_AXIOMS" in failed and "sorryAx" in failed
passed = raw[records[-1]["stdout"]].decode("utf-8-sig")
assert "error:" not in passed and "sorryAx" not in passed
assert "AUDIT_OK TenthDiscriminant.PrimeAxisRepair: 18 logical declarations; 16 theorems; 2 runtime-only" in passed
assert "'TenthDiscriminant.PrimeAxisRepair.two_class_accounting' depends on axioms: [propext, Classical.choice, Quot.sound]" in passed
changed = subprocess.check_output(["git","diff","--name-only",data["base"],"--","lean","tools",".github","flow"],cwd=root,text=True)
assert not [n for n in changed.splitlines() if not n.endswith(".md")],changed
for path in ["lean/TenthDiscriminant.lean","lean/TenthDiscriminant/ExcludedPrimeAssembly.lean","lean/TenthDiscriminant/PrimeWeightKernel.lean"]:
    assert (root/path).read_bytes() == subprocess.check_output(["git","show",data["base"]+":"+path],cwd=root)
print("PASS: registered target; both raw builds and exact repair; unchanged eight theorem types; axis/conditional accounting audit; production proofs unchanged.")
print("Integrity only. No new nonzero-row bound, arithmetic B, cutoff, production-CI coverage or independent review inferred.")
