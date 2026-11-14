# Phase321-B — invariant factors of the full ray class groups

Date: 14 November 2026. Preregistered before implementation or p-primary torsion counts. This line builds on the exact Phase321 group law; it does not assume the extension splits.

## Question

Determine the invariant-factor decomposition of the finite abelian groups
[
\mathrm{Cl}_{(125)}(K_D),qquad D\in\{163,187,203\},
]
from the explicit cocycle multiplication already constructed in Phase321.

The exact group orders are 7,500, 15,000 and 30,000. The local kernel has order 7,500, and the ordinary class groups have orders 1, 2 and 4. These orders alone do not determine the extension.

## Frozen method: p-primary torsion counts

For each prime (p) dividing the group order and each (1\le k\le v_p(|G|)), enumerate **every** element (g=(c,u)) of the exact pair model and count
[
N_{p,k}=\#\{g\in G:g^{p^k}=1\}.
]
Use the Phase321 multiplication law and exact modular arithmetic, not a guessed direct product.

For a finite abelian p-group with cyclic factors (C_{p^{e_i}}),
[
\log_p N_{p,k}=\sum_i\min(k,e_i).
]
Thus
[
r_{p,k}=\log_pN_{p,k}-\log_pN_{p,k-1}
]
is the number of cyclic p-primary factors whose exponent is at least k. Recover the multiplicity of exponent k as (r_{p,k}-r_{p,k+1}). Combine the p-primary lists, padding with zero exponents on the left, to obtain the invariant factors (n_1\mid n_2\mid\cdots\mid n_r).

## Independent checks

- Verify (N_{p,k}) is an exact power of p and the logarithm is integral.
- Reconstruct each p-primary order from the recovered exponents.
- Verify the product of all invariant factors equals the exact Phase321 ray-group order.
- Verify each invariant factor divides the next.
- Independently count the exponent of the full group from element powers and compare it with the largest invariant factor.
- Reproduce the D163 local-kernel invariant factors as a regression against the Phase315 local signed-unit group.
- Preserve the exact cocycle and ordinary class-group projection; do not replace the extension with (U\times\mathrm{Cl}(K_D)).

## Stop rules

Reject:
- any assumed splitting of the ray exact sequence;
- any invariant factors inferred only from group order or class-group order;
- any use of principal elements for nonprincipal ideals;
- any character table or global L-function claim based solely on the invariant factors.

## Evidence boundary

- **P:** the finite-abelian-group torsion-count identity and exact reconstruction of invariant factors from complete p-primary counts.
- **M:** the three computed invariant-factor decompositions after exact-head CI.
- **H:** any field-uniform arithmetic, analytic or discriminant-bound implication.
- **R:** treating the invariant factors as a proof that the extension splits, or confusing an abstract group decomposition with a canonical splitting of the exact sequence.

Phase321-B is the immediate prerequisite for a complete exact character group. It does not yet evaluate characters on all prime ideals or prove a zero-free theorem.


## Extension-splitting test

The ordinary class groups in these three cases are cyclic (trivial, C2, C4). For D187 and D203, exhaust every local lift (g=(c,u)) of a fixed generator (c) of the ordinary class group and test whether
[
g^{\operatorname{ord}(c)}=1.
]
For a cyclic quotient, existence of such a lift is equivalent to a group-theoretic section of the ray exact sequence. If one exists, record the explicit lift. If none exists, the extension is nonsplit. Do not infer splitting or nonsplitting from a nontrivial cocycle entry alone.

For D163 the quotient is trivial and the extension splits tautologically.


## Canonical lift obstruction witness

For the chosen reduced-form class generator, also record the order of the canonical lift with local component (u=1), and the exact local kernel element obtained by raising it to the ordinary class-group order. Compute that local element's order in the signed local kernel. This is an explicit cocycle witness, but the exhaustive all-lifts test above remains the criterion for nonsplitting.
