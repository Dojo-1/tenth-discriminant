"""Untrusted proof scripts: one closed mask equality per declaration."""
from pathlib import Path
from generate_phase34_pilot import BASE, mask, prime

ROOT = Path(__file__).resolve().parents[2]


def main():
    ps = BASE + [p for p in range(29, 100000) if prime(p)][:200]
    text = ("import TenthDiscriminant.FusedWheelParameters\n\n"
            "/-! Generated literal-mask proofs. Each declaration is kernel checked;\n"
            "the generator is not trusted. No interval claim is made here. -/\n"
            "namespace TenthDiscriminant\nset_option autoImplicit false\n\n")
    for p in ps:
        text += f"theorem phase35_mask_{p} : negativeSquareMask {p}={mask(p)} := by decide +kernel\n"
    chunks = [ps[i:i+16] for i in range(0, len(ps), 16)]
    for i, chunk in enumerate(chunks):
        data = ",".join(f"({p},{mask(p)})" for p in chunk)
        names = ", ".join(f"phase35_mask_{p}" for p in chunk)
        text += (f"\ndef phase35MaskChunk{i} : List (Nat×Nat) := [{data}]\n"
                 f"theorem phase35MaskChunk{i}_checked :\n"
                 f"    (phase35MaskChunk{i}.all (fun e => negativeSquareMask e.1 == e.2))=true := by\n"
                 f"  simp only [phase35MaskChunk{i}, List.all_cons, List.all_nil, {names}] <;> rfl\n")
    split = "++".join(f"phase35MaskChunk{i}" for i in range(len(chunks)))
    checks = ", ".join(f"phase35MaskChunk{i}_checked" for i in range(len(chunks)))
    text += (f"\ntheorem phase35_entries_split : phase34Base++phase34Extra={split} := by rfl\n"
             "\ntheorem phase35_masks_checked :\n"
             "    ((phase34Base++phase34Extra).all (fun e => negativeSquareMask e.1 == e.2))=true := by\n"
             "  rw [phase35_entries_split]\n"
             f"  simp only [List.all_append, {checks}, Bool.and_self]\n\n"
             "end TenthDiscriminant\n")
    target = ROOT / "lean/TenthDiscriminant/FusedWheelMasks.lean"
    target.write_text(text, encoding="utf-8", newline="\n")
    print(f"Generated {len(ps)} per-mask proofs plus aggregate; acceptance still required.")


if __name__ == "__main__":
    main()
