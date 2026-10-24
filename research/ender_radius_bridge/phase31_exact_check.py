"""Independent exact control for the frozen Phase31 interval, not a proof."""
import json

WHEEL = [3, 5, 7, 11]
EXTRA = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
         71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
LOW, HIGH = 92, 1000000


def negative_squares(p):
    return {(-r * r) % p for r in range(p)}


def main():
    modulus, residues = 8, [3]
    for p in WHEEL:
        forbidden = negative_squares(p)
        residues = [r + modulus * k for k in range(p) for r in residues
                    if (r + modulus * k) % p not in forbidden]
        modulus *= p
    candidates = [r + modulus * k for k in range(HIGH // modulus + 1)
                  for r in residues if LOW <= r + modulus * k < HIGH]
    forbidden = {p: negative_squares(p) for p in EXTRA}
    survivors = [d for d in candidates
                 if all(d < 4 * p or d % p not in forbidden[p] for p in EXTRA)]
    print(json.dumps({"scope": "independent exact control, not Lean proof",
                      "lo": LOW, "hi_exclusive": HIGH, "wheel": WHEEL,
                      "extra": EXTRA, "modulus": modulus,
                      "residue_count": len(residues),
                      "candidate_count": len(candidates), "survivors": survivors}, indent=2))


if __name__ == "__main__":
    main()
