# Phase321-B — ray group invariant factors and split extensions

**Status:** exact arithmetic output obtained; corrected adversarial assertions are pending the next exact-head CI run. The first run is preserved as a failed expectation check, not silently relabelled green.

The Phase321 multiplication law was used to enumerate every element of each full ray class group. For each prime p dividing the group order, the implementation counted all elements killed by p^k. These counts recover the p-primary cyclic exponents and hence the invariant factors.

## Results

| D | Ray group order | Invariant factors | Exponent |
|---|---:|---|---:|
| 163 | 7,500 | C25 x C300 | 300 |
| 187 | 15,000 | C50 x C300 | 300 |
| 203 | 30,000 | C100 x C300 | 300 |

The exact p-primary torsion counts (N_{p,k}=|G[p^k]|) are:

| Field | p=2 | p=3 | p=5 |
|---|---|---|---|
| D163 | 1, 2, 4 | 1, 3 | 1, 25, 625, 625, 625 |
| D187 | 1, 4, 8, 8 | 1, 3 | 1, 25, 625, 625, 625 |
| D203 | 1, 4, 16, 16, 16 | 1, 3 | 1, 25, 625, 625, 625 |

These counts give 2-primary groups C4, C2 x C4 and C4 x C4 respectively; the 3-primary part is C3 in all cases and the 5-primary part is C25 x C25 in all cases.

## The ray exact sequence splits in all three fields

The ordinary class groups are cyclic: trivial for D163, C2 for D187 and C4 for D203. For each nontrivial field, every one of the 7,500 local kernel elements was tested as the local component of a lift of a fixed generator of the ordinary class group.

- D187: exactly 2 of the 7,500 lifts have square equal to the identity. The first is local residue (7,103).
- D203: exactly 4 of the 7,500 lifts have fourth power equal to the identity. The first is local residue (34,23).

Existence of an order-preserving lift of a generator of a cyclic quotient gives a section of the ray exact sequence. Thus the extensions split for D187 and D203; D163 splits tautologically.

The resulting invariant factors agree with the direct product of the Phase315 local kernel C25 x C300 and the ordinary class group:
- D163: C25 x C300;
- D187: C50 x C300;
- D203: C100 x C300.

This is a useful correction to the naive reading of the cocycle table: a chosen transversal can have nonidentity cocycle values even when a different choice of lifts gives a section. A nontrivial cocycle entry alone does not establish a nonsplit extension.

## Canonical-lift defect versus a genuine obstruction

The canonical lift with local component 1 is not itself the section lift:
- D187: canonical lift order 300; its square is local residue (2,124), of order 150 in the signed local kernel.
- D203: canonical lift order 300; its fourth power is local residue (6,124), of order 75 in the signed local kernel.

These are defects of the canonical choice of lift, not obstructions to splitting. The exhaustive section search finds alternative lifts of the required order.

## Interpretation boundary

For these three fields only, the measured pattern is
[
\mathrm{Cl}_{(125)}(K_D)\cong
\begin{cases}
C_{25}\times C_{300},&h=1,\\
C_{50}\times C_{300},&h=2,\\
C_{100}\times C_{300},&h=4.
\end{cases}
]
This is a finite result, not a general class-number formula.

The result supplies the actual invariant factors and an explicit section in each of the three cases. It does not yet construct a full character table or evaluate all characters on an unbounded prime-ideal family. No field-uniform valuation, zero-free region or discriminant bound follows from this computation.

The initial exact-head run (workflow 43631043257) exposed five incorrect test expectations: it computed the values above, while the tests still encoded a nonsplit extension and larger exponents. Those expectations are now corrected; the next exact-head run must pass before promotion.

Reproduction:
- `python3 -m py_compile research/phase321/*.py`
- `python3 research/phase321/ray_invariant_factors.py`
- `python3 -m unittest discover -s research/phase321 -p 'test_ray_invariant_factors.py' -v`

Workflow: `.github/workflows/phase321b-ray-invariant-factors.yml`.
