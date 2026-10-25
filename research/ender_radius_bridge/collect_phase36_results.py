"""Freeze observed Phase36 outcomes; a stopped seed is never a pass."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    pilot = read(HERE / "PHASE36_PILOT_RESULTS.json")
    seeds = []
    for item in pilot["seeds"]:
        if item["status"] == "terminal":
            item = {**item, "measurement": read(HERE / item["record"])}
        seeds.append(item)
    builds = []
    for path in sorted(HERE.glob("PHASE25_INTEGER_CHUNKS_*.result.json")):
        if path.name >= "PHASE25_INTEGER_CHUNKS_20261024235808.result.json":
            entry = read(path)
            if entry.get("build_target", "").startswith("TenthDiscriminant.QuotientFiber") or entry.get("build_target")=="TenthDiscriminant":
                builds.append({"record": path.name, **entry})
    result = {
        "phase": 36, "protocol_commit": "aad9ac8",
        "base_commit": "f0f6bae9c4191e9326ab0fd3e993d50c1eca1cd2",
        "original_interval": [1000000,700000000000], "upper_endpoint_exclusive": True,
        "quotient_positions_per_seed": 785, "all_extra_prime_labels_unchanged": True,
        "literal_inverse_pattern_entries": 200, "literal_validation_record": "PHASE25_INTEGER_CHUNKS_20261025000643.result.json",
        "pilot_outcome": "INCOMPLETE: ten seeds pass; seed179 time-stopped under remaining aggregate allowance",
        "passed_seeds": [x["seed"] for x in seeds if x.get("exit_code")==0],
        "stopped_seeds": [x["seed"] for x in seeds if x.get("exit_code")==99],
        "aggregate_limit_seconds": 720, "observed_elapsed_seconds": pilot["elapsed_seconds"],
        "stop_note": "Last seed retained nominal per-seed cap180 but only60 seconds remained in aggregate. Observed721.7588028s includes startup/polling/termination overshoot. No old budget was increased.",
        "seeds": seeds, "library_build_records": builds,
        "raw_metadata_note": "Legacy Phase25 file/scope metadata kept unchanged; build_target/stdout identify actual Phase36 targets.",
        "claim_boundary": "Phase36 alone does NOT supply a complete all-fiber certificate or new global classification. Existing bounded iff remains below892371480. A separately preregistered continuation must preserve this failure and may not relabel this pilot as complete."
    }
    (HERE / "PHASE36_RESULTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["pilot_outcome", "passed_seeds", "stopped_seeds", "observed_elapsed_seconds"]}))


if __name__ == "__main__":
    main()
