"""Collect actual terminal records; never manufacture a missing result."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    pilot = read(HERE / "PHASE35_PILOT_RESULTS.json")
    records = []
    for path in sorted(HERE.glob("PHASE25_INTEGER_CHUNKS_*.result.json")):
        if path.name >= "PHASE25_INTEGER_CHUNKS_20261024225940.result.json":
            record = read(path)
            target = record.get("build_target", "")
            if target.startswith("TenthDiscriminant.Fused") or target == "TenthDiscriminant":
                records.append({"record": path.name, **record})
    successful = []
    stopped = []
    for block in pilot["blocks"]:
        if block["status"] == "terminal":
            record = read(HERE / block["record"])
            (successful if block["exit_code"] == 0 else stopped).append({**block, "measurement": record})
    complete = [q for q in [0, 1, 392, 784] if len([
        b for b in successful if b["quotient"] == q]) == 11]
    result = {
        "phase": 35, "base_commit": "29a155e5843e1764ebcccc48c8bbb78ff5718cbf",
        "protocol_commit": "d56f17d", "planned_quotients": [0, 1, 392, 784],
        "planned_blocks": 44, "complete_pilot_quotients": complete,
        "passed_block_count": len(successful), "stopped_block_count": len(stopped),
        "skipped_block_count": sum(b["status"] == "skipped" for b in pilot["blocks"]),
        "aggregate_limit_seconds": 720, "aggregate_elapsed_seconds": pilot["elapsed_seconds"],
        "aggregate_overhead_note": "Observed wall time includes process startup, polling and termination; limit was not increased.",
        "passed_blocks_peak_bytes": max(b["measurement"]["observed_peak_working_set_bytes"] for b in successful),
        "successful_blocks": successful, "stopped_blocks": stopped,
        "full_pilot_record": "PHASE35_PILOT_RESULTS.json", "library_build_records": records,
        "build_metadata_note": "Legacy Phase25 filenames/scope metadata retained raw; build_target and stdout identify actual targets.",
        "local_verification_checkpoint": "See PHASE35_VERIFICATION.txt: explicitly condensed terminal transcription, not raw log; root build, source correspondence, import closure, compiled audit and exact signatures passed. Full local parent/apparatus/eight-script suite rerun is not claimed; exact-head pinned CI required.",
        "exact_head_CI": "pending; final PR verification record must identify tested head/tree and terminal status",
        "claim_boundary": "Only complete translates can feed actual-field exclusion. No full 785-quotient coverage, optimized cutoff, independent human review, merge or Tao post. Original global goal remains active."
    }
    (HERE / "PHASE35_RESULTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["complete_pilot_quotients", "passed_block_count",
        "stopped_block_count", "skipped_block_count", "aggregate_elapsed_seconds", "passed_blocks_peak_bytes"]}))


if __name__ == "__main__":
    main()
