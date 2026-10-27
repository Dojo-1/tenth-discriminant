"""Saved-evidence and transport integrity; does not run Lean or certify class numbers."""
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile
folder=Path(__file__).resolve().parent
root=folder.parents[1]
data=json.loads((folder/"PHASE64_RESULTS.json").read_text(encoding="utf-8"))
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda ref,path:subprocess.check_output(["git","show",ref+":"+path],cwd=root)
for path,digest in data["sha256"].items():
    assert sha((root/path).read_bytes())==digest,path
assert sha(blob(data["registered_commit"],"research/ender_radius_bridge/PHASE64_PROTOCOL.md"))==data["sha256"]["research/ender_radius_bridge/PHASE64_PROTOCOL.md"]
subprocess.run(["git","merge-base","--is-ancestor",data["registered_commit"],"HEAD"],cwd=root,check=True)
archive=folder/data["raw_archive"]["path"]
assert sha(archive.read_bytes())==data["raw_archive"]["sha256"]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist())==21
    raw={n:z.read(n) for n in z.namelist()}
assert {n:sha(b) for n,b in raw.items()}==data["raw_sha256"]
records=data["records"]
assert len(records)==4 and sorted(r["mode"] for r in records)==["audit","build","input","root"]
build=next(r for r in records if r["mode"]=="build")
assert build["attempt"]==1 and str(build["elapsed_seconds"])==data["target_seconds"]
for r in records:
    assert r["attempt"]==1 and r["exit_code"]==0 and not r["stop_reason"]
    assert r["elapsed_seconds"]<=r["time_limit_seconds"]
    assert r["memory_threshold_mb"]==8192
    assert r["observed_peak_working_set_bytes"]<8192*1024**2
    assert sha(raw[r["source_snapshot"]])==r["source_sha256"]
    assert raw[r["source_snapshot"]]==(root/"lean/TenthDiscriminant/QuadraticAreaCount.lean").read_bytes()
    saved=r["stdout"].replace(".stdout.log",".result.json")
    assert json.loads(raw[saved].decode("utf-8-sig"))==r
    log=raw[r["stdout"]].decode("utf-8-sig")
    assert "error:" not in log and "sorryAx" not in log
    core=r["source_snapshot"].replace(".source.lean",".core.lean")
    assert raw[core]==(root/"lean/TenthDiscriminant/QuadraticRowCount.lean").read_bytes()
assert "AUDIT_OK TenthDiscriminant.QuadraticRows: 48 logical declarations; 43 theorems; 4 runtime-only" in raw[build["stdout"]].decode("utf-8-sig")
audit=raw[next(r for r in records if r["mode"]=="audit")["stdout"]].decode("utf-8-sig")
assert "AUDIT_OK TenthDiscriminant: 4869 logical declarations; 4114 theorems; 16982 runtime-only" in audit
inputs=raw[next(r for r in records if r["mode"]=="input")["stdout"]].decode("utf-8-sig")
assert inputs.count("PHASE64_INPUTS_OK")==2
for name,count in data["closures"].items():
    assert f"QuadraticRows.{name}: {count} reached" in inputs
assert "'TenthDiscriminant.QuadraticRows.off_axis_area_bound' depends on axioms: [propext, Classical.choice, Quot.sound]" in inputs
structural=raw["PHASE64_SOURCE_CHECKS.log"].decode("utf-8")
assert "170 project modules" in structural and "all 250 interval pairs" in structural
# Transport is mechanically identical except for the registered namespace/import/header changes.
old=(folder/"Phase63NonzeroRows.lean").read_text(encoding="utf-8")
expected=old.replace("import TenthDiscriminant\n","import Mathlib\nimport TenthDiscriminant.AxiomAudit\n").replace("TenthDiscriminant.NonzeroRows","TenthDiscriminant.QuadraticRows")
expected=expected.replace("open scoped BigOperators","/-! Frozen Phase63 row-count proof transported to production.\nThe closed area evaluation is in QuadraticAreaCount. -/\n\nopen scoped BigOperators",1)
assert expected==(root/"lean/TenthDiscriminant/QuadraticRowCount.lean").read_text(encoding="utf-8")
base_root=blob(data["base"],"lean/TenthDiscriminant.lean").decode("utf-8").replace("\r\n","\n")
assert (root/"lean/TenthDiscriminant.lean").read_text(encoding="utf-8")==base_root+"import TenthDiscriminant.QuadraticRowCount\nimport TenthDiscriminant.QuadraticAreaCount\n"
changes=subprocess.check_output(["git","diff","--name-only",data["base"],"--","lean","tools",".github","flow"],cwd=root,text=True).splitlines()
assert set(n for n in changes if not n.endswith(".md"))<={"lean/TenthDiscriminant.lean","lean/TenthDiscriminant/QuadraticRowCount.lean","lean/TenthDiscriminant/QuadraticAreaCount.lean"},changes
for path in data["prior_frozen_paths"]:
    assert (root/path).read_bytes()==blob(data["base"],path),path
assert len((root/"README.md").read_text(encoding="utf-8").splitlines())==61
print("PASS: preregistration; first target/root/input/audit; exact frozen row transport; closed area source/raw bytes; listed input exclusions;170module coverage;250pairs; prior artifacts unchanged.")
print("Integrity only. No new Lean run, external CI pass, arithmetic B, class-number cutoff or independent review inferred.")
