# Phase321-B — ray group invariant factors and nonsplit extensions

**Status:** local exact enumeration passed; exact-head GitHub CI pending.

The Phase321 multiplication law is now used to enumerate every element of each full ray class group. For each prime p dividing the group order, the implementation counts all elements killed by p^k. These counts recover the p-primary cyclic exponents and therefore the invariant factors.

## Results

| D | Ray group order | Invariant factors | Exponent |
|---|---:|---|---:|
| 163 | 7,500 | C25 x C300 | 300 |
| 187 | 15,000 | C25 x C600 | 600 |
| 203 | 30,000 | C25 x C1200 | 1,200 |

The exact p-primary torsion counts are:

| Field | p=2: N(2), N(4), ... | p=3 | p=5 |
|---|---|---|---|
| D163 | 1, 2, 4 | 1, 3 | 1, 25, 625, 625, 625 |
| D187 | 1, 2, 4, 8 | 1, 3 | 1, 25, 625, 625, 625 |
| D203 | 1, 2, 4, 8, 16 | 1, 3 | 1, 25, 625, 625, 625 |

Here the entries for p are (N_{p,k}=|G[p^k]|), with the final entry corresponding to the largest p-power dividing the group order.

## The extension does not split for D187 or D203

The ordinary class groups are cyclic: C2 for D187 and C4 for D203. For each nontrivial field, every one of the 7,500 local kernel elements was tested as the local component of a lift of a generator of the ordinary class group.

- D187: no lift of the nontrivial class has square equal to the identity.
- D203: no lift of a generator of C4 has fourth power equal to the identity.

Thus the ray exact sequence is nonsplit in both cases. D163 has trivial quotient and splits tautologically.

This is also visible in the invariant factors. If the extension were the direct product of the Phase315 local kernel C25 x C300 with the ordinary class group, the predicted invariant factors would be:
- D187: C50 x C300;
- D203: C100 x C300.

The actual groups are C25 x C600 and C25 x C1200. The extension is therefore not merely a nontrivial cocycle presentation of an abstract direct product; the abstract group structures differ as well.

## Interpretation boundary

For these three fields only, the measured pattern is
[
\mathrm{Cl}_{(125)}(K_D)\cong C_{25}\times C_{300h(K_D)}
]
for (h=1,2,4). This is a finite result, not a general class-number formula.

The nonsplitting matters for the next step: character construction must use the actual ray-group invariant factors, not a product of the local character group with the ordinary class group. No field-uniform valuation, zero-free region or discriminant bound follows from this computation.
