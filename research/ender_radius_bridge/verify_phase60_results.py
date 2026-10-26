"""Verify saved boundary-test integrity; do not rerun the one-invocation probe."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
root = folder.parents[1]
data = json.loads((folder / "PHASE60_RESULTS.json").read_text(encoding="utf-8"))
archive = folder / data["raw_archive"]["path"]
assert hashlib.sha256(archive.read_bytes()).hexdigest() == data["raw_archive"]["sha256"]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == 4
    raw = {n:z.read(n) for n in z.namelist()}
for name, expected in data["sha256"].items():
    content = raw[name] if name in raw else (folder/name).read_bytes()
    assert hashlib.sha256(content).hexdigest() == expected, name
protocol = subprocess.check_output(["git", "show", data["registered_commit"] + ":research/ender_radius_bridge/PHASE60_PROTOCOL.md"], cwd=root)
assert hashlib.sha256(protocol).hexdigest() == data["sha256"]["PHASE60_PROTOCOL.md"]
for name, expected in data["source_context_sha256"].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == expected, name
record = data["run"]
assert record["attempt"] == 1 and record["exit_code"] == 0 and not record["stop_reason"]
assert record["elapsed_seconds"] < record["time_limit_seconds"] == 60
assert record["memory_threshold_mb"] == 256
assert hashlib.sha256(raw[record["source_snapshot"]]).hexdigest() == record["source_sha256"]
assert (folder/"Phase60BoundaryCheck.py").read_bytes() == raw[record["source_snapshot"]]
output = json.loads(raw[record["stdout"]].decode("utf-8-sig"))
assert output == data["output"] and output["status"] == "PER_FORM_ESTIMATE_VIOLATED"
assert all(output["guards"].values()) and output["D"] == 12011
assert output["case"]["prime_representations"] == [[-1,0,3],[1,0,3]]
assert output["principal_control"]["prime_representations"] == []
assert Fraction(output["rigorous_upper_exclusive"]) == Fraction(34,25) < output["actual_prime_representation_count"] == 2
assert output["aggregate_split_bound"] == "NOT_TESTED" and output["class_number"] == "NOT_COMPUTED"
changes = subprocess.check_output(["git", "diff", "--name-only", data["base"], "--", "lean", "tools", ".github", "flow"], cwd=root, text=True)
assert not [x for x in changes.splitlines() if not x.endswith(".md")], changes
print("PASS: fixed-case source/protocol/context hashes; one bounded raw record; archived output and narrow per-form result preserved.")
print("Integrity only; no probe rerun, class-number computation, aggregate refutation or new cutoff inferred.")
