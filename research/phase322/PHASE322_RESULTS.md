# Phase322 — exact ray characters and conductor distributions

**Status:** exact-head workflow passed all 8 adversarial tests. This is a finite, exact character construction for the conductor-125 ray class groups of D163, D187 and D203.

## Full dual groups

The invariant factors from Phase321-B are:
- D163: (C_{25}\times C_{300}), 7,500 characters;
- D187: (C_{50}\times C_{300}), 15,000 characters;
- D203: (C_{100}\times C_{300}), 30,000 characters.

The local signed-unit generators and ray generators were found and checked by exact order and a full coordinate bijection:

| D | Local order-25 generator | Local order-300 generator | Ray order-25h generator | Ray order-300 generator |
|---|---|---|---|---|
| 163 | (1,5) | (1,1) | (0,(1,5)) | (0,(1,1)) |
| 187 | (4,0) | (0,1) | (1,(28,37)) | (0,(0,1)) |
| 203 | (1,5) | (1,1) | (1,(44,58)) | (0,(1,1)) |

The section lifts used are the Phase321-B lifts: identity for D163, (1,(7,103)) for D187, and (1,(34,23)) for D203. The pair-power coordinate maps enumerate all 7,500, 15,000 and 30,000 group elements exactly once. Multiplication by either generator increments the corresponding coordinate at every element.

Every character is indexed by ((i,j)) and evaluated by the exact rational exponent
[
\chi_{i,j}(g_1^a g_2^b)
=\exp\left(2\pi i\left(\frac{ia}{25h}+\frac{jb}{300}\right)\right).
]
No floating complex approximations are used as proof data.

## Exact conductor distributions

| D | Conductor 1 | Conductor 5 | Conductor 25 | Conductor 125 | Total |
|---|---:|---:|---:|---:|---:|
| 163 | 1 | 11 | 288 | 7,200 | 7,500 |
| 187 | 2 | 22 | 576 | 14,400 | 15,000 |
| 203 | 4 | 44 | 1,152 | 28,800 | 30,000 |

The conductor filtration was reconstructed from the explicit annihilator kernels of the natural reduction maps:
- modulus 1: local kernel order 7,500;
- modulus 5: local kernel order 625;
- modulus 25: local kernel order 25;
- modulus 125: local kernel order 1.

The local reduction group orders are 1, 12, 300 and 7,500 for moduli 1, 5, 25 and 125. The corresponding full ray-group image orders are (h), (12h), (300h) and (7500h). The reduction maps were checked against the exact cocycle multiplication by both ray generators on every group element.

The conductor counts agree with the predicted (h,11h,288h,7200h), but the code recovers them by testing character annihilation on the actual kernel generators.

## Bounded prime-ideal character evaluations

Every character was evaluated on every prime ideal in the Phase321 catalog, for rational primes (p\le441). Values are stored as reduced rational exponents modulo one. The complete evaluation matrices are summarized by deterministic SHA-256 digests.

| D | Prime-ideal records | Character evaluations | Prime-ideal relation checks | Evaluation-matrix SHA-256 |
|---|---:|---:|---:|---|
| 163 | 118 | 885,000 | 630,000 | `b58d93d8622bbb652b73a0de55820d58286814447664b7db155e04fca27ae166` |
| 187 | 128 | 1,920,000 | 1,260,000 | `a3b094d355e4cdd0bff326fd89cac6d385ed6fa23bd574504793a83cc8b7ee34` |
| 203 | 125 | 3,750,000 | 2,520,000 | `d0af189face7e7b121f40a9a2e2e81974531cfbf554028d4e10074a6ca0fd81c` |

The prime-ideal catalogs retain:
- D163: 34 split rational primes, 1 ramified rational prime, no nonprincipal records;
- D187: 44 split, 2 ramified, 50 nonprincipal prime-ideal records;
- D203: 41 split, 2 ramified, 70 nonprincipal records.

For every character, the computation verifies:
- the two split conjugate prime ideals multiply to the principal ray class of ((p));
- each inert prime ideal ((p)) maps to that principal ray class;
- each ramified prime ideal squares to the principal ray class of ((p)).

The original Phase321 catalog digests are unchanged:
- D163: `6a606b7623aa89ca24e64f554367fc2396840747fbf022cac8e0d8dd4488929a`;
- D187: `dabb3659db2f715454a35947a5c1f393f2faf4f51ca894ae75e957970c55251a`;
- D203: `9df1c875e8eb3d2c7c3b1f13a5956f300cd01b1db713637acf41209a4d321f49`.

## Verification provenance

- Corrected exact-head workflow: run `43632573344`, job `132562216161`.
- 8/8 adversarial tests passed.
- The initial runs `43632498601` and `43632538827` failed only because the audit-scope step expected a `modulus` field missing from the first manifest. The field was added; the corrected exact-head run passed. This is retained as provenance.

## Evidence boundary

- **P:** exact finite duality, rational character exponents and conductor-annihilator criteria under the explicitly constructed ray groups and reduction maps.
- **M:** the three finite character groups, their conductor distributions and bounded prime-ideal evaluation matrices.
- **H:** any field-uniform conductor formula, prime-distribution theorem, exceptional-zero implication or discriminant improvement.
- **R:** treating the bounded evaluations as a global Euler product, computing L-values from them, or inferring a zero-free region.

No L-values are computed in Phase322. The bounded character table is not a global Euler product and does not establish a zero-free theorem.
