# Phase321 — ideal-aware ray class groups modulo 125

> Local units are the kernel. Ideal classes are the quotient. The cocycle is the bridge.
>
> Do not replace an ideal by an element merely because the local ring is familiar.

Phase321 constructs the full ray class groups modulo (125) for
\[
K_D=\mathbb Q(\sqrt{-D}),\qquad D\in\{163,187,203\}.
\]
It uses exact reduced-form ideal representatives, rank-two integer lattices, exact HNF multiplication and the cocycle
\[
I_cI_d=(\alpha_{c,d})I_{c+d}.
\]
The full group is represented by pairs (c,u), with multiplication
\[
(c,u)(d,v)=(c+d,uv\alpha_{c,d}\bmod\{\pm1\}).
\]
The extension is constructed, not assumed to split.

## Exact local and global orders

The inert prime is 5 in all three fields. Exhaustion of O_D/(125) gives 15,000 units and 7,500 signed local ray residues. The ordinary class numbers are counted from exact reduced primitive forms.

| Field | Ordinary class group | h | |Cl_(125)| |
|---|---|---:|---:|
| D163 | trivial | 1 | 7,500 |
| D187 | C2 | 2 | 15,000 |
| D203 | C4 | 4 | 30,000 |

The ray-group orders agree with the exact sequence
\[
\mathcal O_D^\times\to(\mathcal O_D/(125))^\times
\to\mathrm{Cl}_{(125)}(K_D)\to\mathrm{Cl}(K_D)\to1.
\]
The class group structures are measured from the exact multiplication tables: D187's nontrivial class has order 2; D203's two nonidentity generators of order 4 and one element of order 2 give C4.

## Exact cocycle data

Every ideal-class pair was multiplied as a lattice and compared with every reduced class representative. The scaling element was found by an exhaustive norm-bounded rational-coordinate search; its denominator is bounded by the first HNF coordinate of the target ideal. The resulting ideal equality is checked by exact HNF, not floating coordinates.

The chosen normalized cocycle residues modulo 125 include:
- D187: alpha(1,1) = (2,-1).
- D203: the full 4x4 cocycle table is emitted by the executable and checked against all 64 associativity triples.

Exact cocycle associativity counts are 1, 8 and 64 for D163, D187 and D203. Commutativity modulo global units is checked for every class pair. The full ray-group inverse checks cover all 7,500, 15,000 and 30,000 group elements respectively.

The local kernel has exactly 7,500 elements in each field. D163 reduces to the Phase315 local signed-unit group. Nonprincipal ideals in D187 and D203 are represented explicitly; no principal-generator substitution is made.

## Bounded prime-ideal catalog

The executable enumerates every rational prime p <= 441, excluding p=5 because the ray modulus is supported there. It retains both split prime ideals, checks their product is (p), checks ramified prime squares, and maps every prime ideal into the constructed ray group.

| Field | Prime-ideal records | Split rational primes | Ramified rational primes | Nonprincipal records |
|---|---:|---:|---:|---:|
| D163 | 118 | 34 | 1 | 0 |
| D187 | 128 | 44 | 2 | 50 |
| D203 | 125 | 41 | 2 | 70 |

These are bounded catalogs, not an assertion that the finite list exhausts all prime ideals or all characters. A SHA-256 digest of each deterministically ordered catalog is printed by the executable.

## Reproduction

Run these commands from the repository root:

- python3 -m py_compile research/phase321/*.py
- python3 -u research/phase321/ideal_aware_ray_class.py
- python3 -m unittest discover -s research/phase321 -p 'test_*.py' -v

The implementation uses only the Python standard library. The local container run passed all eight adversarial tests and all three ray-group constructions. The exact-head GitHub workflow is the next gate.

## Evidence boundary

- **P:** exact quadratic multiplication, trace/norm, ideal lattice and ray exact-sequence identities under the stated hypotheses.
- **M:** the finite ideal products, cocycle tables, ray group inverses and bounded prime-ideal catalog after exact-head CI.
- **H:** any field-uniform class-number/valuation theorem, uniform conductor statement, or new tenth-discriminant bound.
- **R:** using principal elements to stand in for nonprincipal ideals; assuming a direct-product extension; treating a bounded prime catalog as global character completeness.

Phase321 supplies the missing global ideal-theoretic object for Phase320's h=1,2,4 comparison. It does not yet construct the full character table or connect ray characters to a uniform discriminant argument.
