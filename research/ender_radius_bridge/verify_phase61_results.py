"""Check frozen evidence and transport integrity; does not execute Lean."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
root = folder.parents[1]
data = json.loads((folder / "PHASE61_RESULTS.json").read_text(encoding="utf-8"))
sha = lambda b: hashlib.sha256(b).hexdigest()
blob = lambda ref, path: subprocess.check_output(["git", "show", ref+":"+path], cwd=root)
assert sha(blob(data["registered_commit"], "research/ender_radius_bridge/PHASE61_PROTOCOL.md")) == data["sha256"]["research/ender_radius_bridge/PHASE61_PROTOCOL.md"]
subprocess.run(["git", "merge-base", "--is-ancestor", data["registered_commit"], "HEAD"], cwd=root, check=True)
for path, digest in data["sha256"].items():
    assert sha((root/path).read_bytes()) == digest, path
with zipfile.ZipFile(folder/data["raw_archive"]["path"]) as archive:
    assert archive.testzip() is None
    raw = {n: archive.read(n) for n in archive.namelist()}
assert sha((folder/data["raw_archive"]["path"]).read_bytes()) == data["raw_archive"]["sha256"]
assert {n: sha(b) for n,b in raw.items()} == data["raw_sha256"]
records = data["records"]
builds = [r for r in records if r["mode"] == "build"]
assert [r["exit_code"] for r in builds] == [1,0,0]
assert len(builds) <= 3
spent = sum(Decimal(str(r["elapsed_seconds"])) for r in builds)
assert spent == Decimal(data["target_seconds"]) < 1200

def types(source):
    return {m.group(1): " ".join(source[m.start():source.index(" := by",m.start())].split())
            for m in re.finditer(r"(?m)^theorem\s+(\w+)", source)}

initial = raw[builds[0]["source_snapshot"]].decode("utf-8")
assert len(types(initial)) == 9
for record in records:
    assert not record["stop_reason"] and record["elapsed_seconds"] <= record["time_limit_seconds"]
    assert record["memory_threshold_mb"] == 8192
    assert record["observed_peak_working_set_bytes"] < 8192*1024**2
    source = raw[record["source_snapshot"]]
    assert sha(source) == record["source_sha256"]
    assert types(source.decode("utf-8")) == types(initial)
    saved = record["stdout"].replace(".stdout.log", ".result.json")
    assert json.loads(raw[saved].decode("utf-8-sig")) == record
    if record["mode"] != "build": assert record["exit_code"] == 0
final = builds[-1]
assert raw[final["source_snapshot"]] == (root/"lean/TenthDiscriminant/PrimeWeightKernel.lean").read_bytes()
assert "AUDIT_OK TenthDiscriminant.ExcludedPrime: 49 logical declarations; 43 theorems; 7 runtime-only" in raw[final["stdout"]].decode("utf-8-sig")
assert "NONSTANDARD_AXIOMS" in raw[builds[0]["stdout"]].decode("utf-8-sig")
for record in records:
    if record["exit_code"] == 0:
        assert "error:" not in raw[record["stdout"]].decode("utf-8-sig")
inputs = raw[next(r for r in records if r["mode"] == "input")["stdout"]].decode("utf-8-sig")
assert inputs.count("PHASE61_INPUTS_OK") == 4
assert "excluded_prime_budget_log_div: 48263 reached" in inputs
assert "sorryAx" not in inputs
whole = raw[next(r for r in records if r["mode"] == "audit")["stdout"]].decode("utf-8-sig")
assert "AUDIT_OK TenthDiscriminant: 4821 logical declarations; 4071 theorems; 16978 runtime-only" in whole
negative = raw["PHASE61_negative_controls.log"].decode("utf-8-sig")
assert "TimeoutExpired" in negative and "timed out after 120 seconds" in negative
assert "multiplicity_negative_controls.py" in negative
assert "PASS: mathematical controls, proof-audit probes, Gram, jet, multiplicity, degree, nonzero, affine and assembly controls." not in negative
assert data["controls"]["negative_controls"] == "INCOMPLETE_TIMEOUT_120_SECONDS_NO_LOCAL_RERUN"
assert "PASS:" in raw["PHASE61_apparatus_controls.log"].decode("utf-8-sig")
assert "168 project modules" in raw["PHASE61_source_checks.log"].decode("utf-8")
assert "all 250 interval pairs" in raw["PHASE61_source_checks.log"].decode("utf-8")

# The Phase59 core has only an import/header/namespace transport, no proof edits.
original = (folder/"Phase59Prototype.lean").read_text(encoding="utf-8")
expected = original[:original.index("#audit_namespace")].replace("import TenthDiscriminant\n", "import TenthDiscriminant.PrimeMassAssembly\nimport TenthDiscriminant.AxiomAudit\n").replace("ExcludedPrimePrototype", "ExcludedPrime")
expected = expected.replace("open scoped BigOperators", "/-! The finite count-to-loss assembly, transported verbatim from frozen Phase59.\nNo class-number-one input is used: only the good primes are nonsquare. -/\n\nopen scoped BigOperators", 1)
assert expected.rstrip()+"\n" == (root/"lean/TenthDiscriminant/ExcludedPrimeAssembly.lean").read_text(encoding="utf-8")
for name in raw:
    if name.endswith(".core.lean"):
        assert raw[name].decode("utf-8").rstrip() == expected.rstrip()
base_root = blob(data["base"], "lean/TenthDiscriminant.lean").decode("utf-8").replace("\r\n","\n")
assert (root/"lean/TenthDiscriminant.lean").read_text(encoding="utf-8") == base_root + "import TenthDiscriminant.ExcludedPrimeAssembly\nimport TenthDiscriminant.PrimeWeightKernel\n"
changes = subprocess.check_output(["git","diff","--name-only",data["base"],"--","lean","tools",".github"], cwd=root,text=True).splitlines()
assert set(n for n in changes if not n.endswith(".md")) <= {"lean/TenthDiscriminant.lean","lean/TenthDiscriminant/ExcludedPrimeAssembly.lean","lean/TenthDiscriminant/PrimeWeightKernel.lean"},changes
# Frozen prior artifacts are checked against committed bytes, without relabeling
# their historical current-tree verifiers as applicable to this expanded root.
for path in data["prior_frozen_paths"]:
    assert (root/path).read_bytes() == blob(data["base"],path),path
print("PASS: registered target; failed and successful attempts; unchanged nine theorem types; exact core transport; root/audit/closures; apparatus pass and negative-suite timeout preserved; frozen prior evidence.")
print("Saved-evidence integrity only. No new arithmetic count bound, cutoff, semantic review or Lean execution inferred.")
