"""Verify saved prototype evidence, not execute Lean or validate higher class numbers."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import subprocess
import zipfile

folder = Path(__file__).resolve().parent
root = folder.parents[1]
data = json.loads((folder / "PHASE59_RESULTS.json").read_text(encoding="utf-8"))
archive = folder / data["raw_archive"]["path"]
assert hashlib.sha256(archive.read_bytes()).hexdigest() == data["raw_archive"]["sha256"]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist()) == 12
    payload = {name: z.read(name) for name in z.namelist()}
for name, expected in data["sha256"].items():
    content = payload[name] if name in payload else (folder / name).read_bytes()
    assert hashlib.sha256(content).hexdigest() == expected, name
protocol = subprocess.check_output(["git", "show", data["registered_commit"] + ":research/ender_radius_bridge/PHASE59_PROTOCOL.md"], cwd=root)
assert hashlib.sha256(protocol).hexdigest() == data["sha256"]["PHASE59_PROTOCOL.md"]
records = data["builds"]
assert len(records) == 3 and [x["exit_code"] for x in records] == [1, 1, 0]
assert [x["attempt"] for x in records] == [1, 2, 3]
spent = sum(Decimal(str(x["elapsed_seconds"])) for x in records)
assert spent == Decimal(data["cumulative_target_seconds"]) and spent < 1200

def headers(text):
    result = {}
    for m in re.finditer(r"(?m)^theorem\s+(\w+)\b", text):
        end = text.find(" := by", m.start())
        next_decl = text.find("\ntheorem ", m.end())
        if end < 0 or (next_decl >= 0 and next_decl < end):
            end = text.find(" :=", m.start())
        assert end >= 0
        result[m.group(1)] = " ".join(text[m.start():end].split())
    return result

original = payload[records[0]["source_snapshot"]].decode("utf-8")
fixed_types = headers(original)
assert len(fixed_types) == 11
for record in records:
    assert not record["stop_reason"] and record["elapsed_seconds"] <= 600
    assert record["memory_threshold_mb"] == 8192
    assert record["observed_peak_working_set_bytes"] < 8192 * 1024**2
    source = payload[record["source_snapshot"]]
    assert hashlib.sha256(source).hexdigest() == record["source_sha256"]
    text = source.decode("utf-8")
    assert headers(text) == fixed_types
    assert text.split("theorem indicator_prefix", 1)[0] == original.split("theorem indicator_prefix", 1)[0]
    assert text.split("#audit_namespace", 1)[1] == original.split("#audit_namespace", 1)[1]
    saved_result = json.loads(payload[record["stdout"].replace(".stdout.log", ".result.json")].decode("utf-8-sig"))
    assert saved_result == record
last = records[-1]
assert (folder / "Phase59Prototype.lean").read_bytes() == payload[last["source_snapshot"]]
log = payload[last["stdout"]].decode("utf-8-sig")
assert "error:" not in log and "sorryAx" not in log
assert "AUDIT_OK TenthDiscriminant.ExcludedPrimePrototype: 36 logical declarations; 32 theorems; 5 runtime-only" in log
assert log.count("PROTOTYPE_INPUTS_OK") == 3
for name, count in data["closures"].items():
    assert f"ExcludedPrimePrototype.{name}: {count} reached" in log
changes = subprocess.check_output(["git", "diff", "--name-only", data["base"], "--", "lean", "tools", ".github"], cwd=root, text=True)
assert not [name for name in changes.splitlines() if not name.endswith(".md")], changes
print("PASS: fixed protocol; all three attempts and two failures; raw archive; unchanged definitions and 11 theorem type prefixes; final source/audit/closures; production tree unchanged.")
print("Saved-evidence integrity only. No new Lean execution, production-root integration, higher-class-number cutoff or independent review inferred.")
