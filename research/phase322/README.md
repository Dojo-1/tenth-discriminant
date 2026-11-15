# Phase322 — exact ray characters and conductor filtration

> A ray group is not yet a character table. The dual is the next finite object.

Phase322 takes the exact ideal-aware ray class groups from Phase321 and the invariant-factor/section results from Phase321-B. It constructs every character of the conductor-125 ray class group for D163, D187 and D203, assigns its exact conductor in the chain 1, 5, 25, 125, and evaluates it on the bounded Phase321 prime-ideal catalog.

## Frozen group structure

| D | Ray class group | Order |
|---|---|---:|
| 163 | C25 x C300 | 7,500 |
| 187 | C50 x C300 | 15,000 |
| 203 | C100 x C300 | 30,000 |

The ordinary class-group quotient has order 1, 2 and 4 respectively. The exact sequences split; the code reuses the explicit Phase321-B section lifts rather than assuming a canonical transversal has trivial cocycle.

## Character coordinates

For (h=1,2,4), the invariant factors are (C_{25h}\times C_{300}). Once exact generators (g_1,g_2) and a bijective coordinate map are verified, every character is indexed by
[
0\le i<25h,\qquad 0\le j<300
]
and has exact value
[
\chi_{i,j}(g_1^a g_2^b)
=\exp\left(2\pi i\left(\frac{ia}{25h}+\frac{jb}{300}\right)\right).
]
The implementation stores the rational exponent modulo one. No floating complex approximation is used as proof data.

## Conductor filtration

The natural reductions from modulus 125 to 25, 5 and 1 have local kernel orders 25, 625 and 7,500 respectively. A character factors through a smaller modulus exactly when it annihilates the corresponding reduction kernel.

The preregistered conductor counts are:

| D | conductor 1 | conductor 5 | conductor 25 | conductor 125 |
|---|---:|---:|---:|---:|
| 163 | 1 | 11 | 288 | 7,200 |
| 187 | 2 | 22 | 576 | 14,400 |
| 203 | 4 | 44 | 1,152 | 28,800 |

These counts must be recovered from explicit kernels and character annihilators, not inserted as outputs.

## Bounded prime-ideal evaluations

Every character is evaluated exactly on every prime ideal in the Phase321 catalog through (p\le441). The complete rational-exponent evaluation matrix is summarized by a deterministic SHA-256 digest, with sample values retained for human inspection.

The prime-ideal relations are rechecked for every character:
- split conjugate ideals multiply to the principal ideal ((p));
- inert prime ideals are the principal ideal ((p));
- ramified prime ideals square to ((p)).

## Reproduction

From the repository root:

- `python3 -m py_compile research/phase321/*.py research/phase322/*.py`
- `python3 research/phase322/exact_ray_characters.py`
- `python3 -m unittest discover -s research/phase322 -p 'test_*.py' -v`

## Evidence boundary

- **P:** exact finite abelian duality and conductor-annihilator criteria under the explicitly constructed group and reduction maps.
- **M:** finite character groups, conductor distributions and bounded prime-ideal evaluations after exact-head CI.
- **H:** any uniform conductor formula, prime-distribution theorem, exceptional-zero implication or discriminant improvement.
- **R:** calling the finite evaluation matrix a global Euler product or inferring a zero-free region from these three fields and a bounded prime list.

No L-values are computed in this phase. The next step, if these finite constructions pass, is to extend the prime-ideal evaluation range with explicit bounds and then study which analytic statements are actually supported by that range.
