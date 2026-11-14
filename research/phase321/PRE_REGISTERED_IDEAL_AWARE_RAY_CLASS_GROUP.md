# Phase321 — ideal-aware ray class groups beyond class number one

Date: 14 November 2026. Preregistered before implementation. This line follows Phase320's cross-field local-unit and source-support experiments. It addresses the global gap that prevents D163's principal split-prime construction from being transported to D187 and D203.

## Question

For the same inert prime (5) and modulus (mathfrak m=(5)^3=(125)), construct the **full ray class group** for
[
K_D=mathbb Q(sqrt{-D}),qquad Din{163,187,203},
]
using all ideal classes, not only principal ideals. The exact class numbers from Phase320 are (h(-163)=1), (h(-187)=2), (h(-203)=4).

This phase constructs the group and its exact multiplication law. It does not yet construct all complex characters, prove a field-uniform theorem, or infer a new discriminant bound.

## Frozen local data and group order

For each field, (5) is inert and
[
mathcal O_D/(125)cong mathcal O_D/5^3.
]
The local unit group has 15,000 elements; quotienting by the global unit group (mathcal O_D^	imes={pm1}) gives 7,500 local ray residues.

Use the ray exact sequence
[
mathcal O_D^	imeslongrightarrow
(mathcal O_D/(125))^	imeslongrightarrow
operatorname{Cl}_{(125)}(K_D)longrightarrow
operatorname{Cl}(K_D)longrightarrow1.
]
The required finite group orders are therefore:
- D163, (h=1): 7,500;
- D187, (h=2): 15,000;
- D203, (h=4): 30,000.

These are order predictions from the exact sequence and the verified local unit counts, not assumptions about the group structure. Do **not** assume the extension splits as a direct product.

## Ideal-class representatives

Enumerate the exact reduced primitive positive-definite forms ([a,b,c]) of discriminant (-D). For each class use
[
I_{[a,b,c]}=
left(a,rac{-b+sqrt{-D}}2ight)
=left(a,omega-rac{b+1}{2}ight),
quad omega=rac{1+sqrt{-D}}2.
]
Represent each ideal as an exact rank-two (mathbb Z)-lattice in the basis (1,omega). Verify every representative is coprime to ((125)); this follows in the current small class tables but must be checked by the executable.

## Exact ideal multiplication and the extension cocycle

For every pair of class representatives (I_c,I_d):
1. Multiply their (mathbb Z)-lattices using the quadratic-order multiplication table.
2. Compute a canonical Hermite-normal-form basis of (I_cI_d).
3. Identify the unique reduced class (e=c+d) and solve exactly for (alpha_{c,d}in K_D^	imes) such that
   [
   I_cI_d=(alpha_{c,d})I_e.
   ]
4. Verify the lattice equality in both directions with rational coordinates, not a floating basis comparison.
5. Verify (alpha_{c,d}) is a 5-adic unit and reduce it in ((mathcal O_D/(125))^	imes/{pm1}).

The cocycle must satisfy, modulo the global units,
[
alpha_{c,d}alpha_{c+d,e}
=alpha_{d,e}alpha_{c,d+e},
qquad
alpha_{c,d}equivalpha_{d,c}.
]
Normalize (alpha_{0,c}=alpha_{c,0}=1).

## Construct the ray group

Represent a ray class by a pair
[
(c,u),quad cinoperatorname{Cl}(K_D),quad
uin(mathcal O_D/(125))^	imes/{pm1}.
]
Use the cocycle multiplication
[
(c,u)cdot(d,v)=
(c+d,uvalpha_{c,d}).
]
Verify:
- identity and inverse for every class;
- associativity for every triple of ideal-class representatives, using the exact cocycle identity;
- commutativity modulo ({pm1});
- the projection onto the ordinary class group;
- the kernel is exactly the 7,500 local ray residues;
- total group order is (7,500h(K_D));
- D163 reduces to the Phase315 local signed-unit group.

Do not report cyclic factors or a direct-product decomposition until the group law has been constructed and independently checked.

## Global prime-ideal catalog — bounded companion

As a separate finite companion, enumerate prime ideals above rational primes (ellle441), recording split, inert and ramified cases and their ordinary ideal class. For split (ell), retain both conjugate prime ideals even when neither is principal. Map each ideal into the constructed ray group by exact lattice equivalence. This catalog is not an assertion that the finite list exhausts all prime ideals or all characters.

## Stop rules

Reject:
- any use of element division as a substitute for nonprincipal ideal arithmetic;
- any class representative not coprime to 125;
- any cocycle equality checked only numerically or before quotienting by units;
- any assumed splitting of the ray exact sequence;
- any omission of a conjugate prime ideal;
- any transfer of D163's principal-generator character list to D187/D203.

If exact ideal scaling cannot be recovered, stop at the ordinary class group and report the obstruction. Do not guess a cocycle.

## Evidence boundary

- **P:** the ray exact sequence, ideal-lattice multiplication and cocycle law under the stated hypotheses.
- **M:** the three finite ray groups and bounded prime-ideal catalog after exact-head CI and independent lattice replay.
- **H:** any uniform field-class-number-to-valuation implication, uniform conductor theorem, or new tenth-discriminant cutoff.
- **R:** treating the class-number-(>1) ray group as only its principal ideal subgroup, or assuming the extension is a direct product.

Phase321 is the missing global arithmetic bridge. It is a prerequisite for any honest comparison of D163's principal split-prime family with D187/D203.
