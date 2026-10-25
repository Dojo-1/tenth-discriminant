"""Generate untrusted affine patterns and per-entry kernel proof scripts.

No sieve is executed here. All 785 quotient positions are encoded in each
leaf; every literal pattern/inverse needs the separately generated proof.
"""
from pathlib import Path
from generate_phase34_pilot import prime
from generate_phase35_pilot import SEEDS

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
M = 892371480
PS = [p for p in range(29, 100000) if prime(p)][:200]


def pattern(p, a):
    bad = 0
    for t in range(p):
        bad |= 1 << ((-a*t*t) % p)
    allowed = ((1 << p)-1) ^ bad
    return sum(1 << j for j in range(785+p) if (allowed >> (j % p)) & 1)


def save(name, source):
    (ROOT / "lean/TenthDiscriminant" / f"{name}.lean").write_text(source, encoding="utf-8", newline="\n")


def main():
    text = ("import TenthDiscriminant.QuotientFiberCore\n\n"
            "/-! Generated untrusted literals; no mathematical exclusion until checked. -/\n"
            "namespace TenthDiscriminant\n\n")
    for p in PS:
        a = pow(M, -1, p)
        text += f"def phase36Entry{p} : QuotientPattern := ⟨{p},{a},{pattern(p,a)}⟩\n"
    names = ",".join(f"phase36Entry{p}" for p in PS)
    text += f"\ndef phase36Entries : List QuotientPattern := [{names}]\n"
    chunks = [PS[i:i+16] for i in range(0, len(PS), 16)]
    for i, chunk in enumerate(chunks):
        names = ",".join(f"phase36Entry{p}" for p in chunk)
        text += f"def phase36Chunk{i} : List QuotientPattern := [{names}]\n"
    text += "\nend TenthDiscriminant\n"
    save("QuotientFiberData", text)
    previous = "QuotientFiberData"
    for i, chunk in enumerate(chunks):
        module = f"QuotientFiberCheck{i:02d}"
        text = f"import TenthDiscriminant.{previous}\n\nnamespace TenthDiscriminant\n"
        for p in chunk:
            text += (f"theorem phase36Entry{p}_checked : quotientPatternCheck {M} phase36Entry{p}=true := by decide +kernel\n")
        checks = ",".join(f"phase36Entry{p}_checked" for p in chunk)
        text += (f"\ntheorem phase36Chunk{i}_checked : quotientPatternsCheck {M} phase36Chunk{i}=true := by\n"
                 f"  simp only [quotientPatternsCheck, phase36Chunk{i}, List.all_cons, List.all_nil, {checks}, Bool.and_self]\n"
                 "end TenthDiscriminant\n")
        save(module, text)
        previous = module
    split = "++".join(f"phase36Chunk{i}" for i in range(len(chunks)))
    checks = ",".join(f"phase36Chunk{i}_checked" for i in range(len(chunks)))
    text = (f"import TenthDiscriminant.{previous}\n\nnamespace TenthDiscriminant\n"
            f"theorem phase36_entries_split : phase36Entries={split} := by rfl\n"
            f"theorem phase36_patterns_checked : quotientPatternsCheck {M} phase36Entries=true := by\n"
            "  rw [phase36_entries_split]\n"
            f"  simp only [quotientPatternsCheck, List.all_append, {checks}, Bool.and_self]\n"
            "end TenthDiscriminant\n")
    # Keep the aggregate checker opaque to simplification: its append law
    # is supplied by the generic bridge, not by recomputing literal patterns.
    text = text.replace(f"import TenthDiscriminant.{previous}\n", f"import TenthDiscriminant.{previous}\nimport TenthDiscriminant.QuotientFiberBridge\n")
    text = text.replace("quotientPatternsCheck, List.all_append,", "quotientPatternsCheck_append,")
    save("QuotientFiberChecked", text)
    save("QuotientFiberParameters", "import TenthDiscriminant.QuotientFiberData\n"
         "import TenthDiscriminant.FusedWheelParameters\n\nnamespace TenthDiscriminant\n"
         "def phase36Leaf (r : Nat) : Bool := quotientFilter r (quotientInitial r) phase36Entries == 0\n"
         "def phase36Seed (seed : Nat) : Bool := maskWheelVisit phase35Prefix 184 seed phase36Leaf\n"
         "end TenthDiscriminant\n")
    for i, seed in enumerate(SEEDS):
        (HERE / f"Phase36Seed{i}Check.lean").write_text(
            "import TenthDiscriminant.QuotientFiberParameters\n\n"
            "/-! Candidate ALL785 cost test; not a field theorem without validated data/semantics. -/\n"
            "namespace TenthDiscriminant\n"
            f"example : phase36Seed {seed}=true := by decide +kernel\n"
            "end TenthDiscriminant\n", encoding="utf-8", newline="\n")
    print(f"Generated {len(PS)} patterns, {len(chunks)} validation groups, {len(SEEDS)} ALL785 seed inputs; no cost test executed.")


if __name__ == "__main__":
    main()
