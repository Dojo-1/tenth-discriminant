# Phase322 — exact dual character groups and bounded prime-ideal evaluations

Date: 14 November 2026. Preregistered before character construction.

## Question

Given the exact conductor-125 ray class groups from Phase321/321-B, construct their full finite character groups
[
\widehat{\mathrm{Cl}_{(125)}(K_D)}
=\mathrm{Hom}(\mathrm{Cl}_{(125)}(K_D),\mathbb C^\times),
\qquad D\in\{163,187,203\},
]
and evaluate every character on the Phase321 bounded prime-ideal catalog (p\le441).

This is a finite exact character construction. It is not a global L-function computation, a zero-free theorem, or a statement about all primes.

## Frozen inputs

The Phase321/321-B results give:
- D163: ray group (C_{25}\times C_{300}), order 7,500;
- D187: ray group (C_{50}\times C_{300}), order 15,000;
- D203: ray group (C_{100}\times C_{300}), order 30,000.

The ordinary class groups have orders 1, 2 and 4. The ray exact sequences split in all three cases, with explicit sections. The local signed unit kernel modulo 125 has invariant factors (C_{25}\times C_{300}).

The character construction must reuse the exact Phase321 pair multiplication and Phase321-B section lifts. It must not replace a chosen nontrivial cocycle by an assumed identity cocycle.

## Frozen construction

1. **Local generators.** Find (u_{25},u_{300}\in(\mathcal O_D/(125))^\times/\{\pm1\}) of exact orders 25 and 300 whose generated subgroup has order 7,500. Verify exact orders and uniqueness of all (25\cdot300) products.
2. **Ray generators.** Let (s_D) be the identity section for D163 and the explicit order-2/order-4 section lift for D187/D203. Construct (g_{25h}=s_Du_{25}), where (h=1,2,4), and (g_{300}=u_{300}). Verify their orders and that their product-powers enumerate every ray group element exactly once.
3. **Exact coordinates.** Build a bijection
   [
   (a,b)\longleftrightarrow g_{25h}^{a}g_{300}^{b},
   quad 0\le a<25h,quad0\le b<300.
   ]
   Verify multiplication by each generator increments the corresponding coordinate for every group element.
4. **Dual group.** Index all characters by (0\le i<25h), (0\le j<300), with exact value
   [
   \chi_{i,j}(g_{25h}^{a}g_{300}^{b})
   =\exp\!\left(2\pi i\left(\frac{ia}{25h}+\frac{jb}{300}\right)\right).
   ]
   Store values as rational exponents modulo one; do not use floating complex approximations as proof data.
5. **Conductor filtration.** For (k=0,1,2,3), construct the kernel of the natural reduction map from modulus 125 to modulus (5^k). Here (k=0) means modulus 1. A character has conductor dividing (5^k) exactly when it is trivial on that kernel. Compute the exact conductor distribution for 1, 5, 25 and 125.
6. **Prime-ideal evaluations.** Map every Phase321 catalogued prime ideal through the exact coordinate bijection and evaluate all characters on it. Record a deterministic digest of the complete rational-exponent evaluation matrix, plus independently readable samples and the split/conjugate, inert-principal and ramified-square controls.

## Predicted conductor counts

The local signed unit quotients have orders 12, 300 and 7,500 modulo 5, 25 and 125. Combined with the ordinary class numbers (h=1,2,4), the preregistered expected counts are:
- conductor 1: (h);
- exact conductor 5: (11h);
- exact conductor 25: (288h);
- exact conductor 125: (7200h).

These counts must be recovered from the actual annihilator kernels, not inserted as outputs.

## Adversarial controls

- Reject local generator pairs whose powers fail to enumerate all 7,500 signed local units.
- Reject ray generators whose pair-powers are not a bijection onto the full ray group.
- Verify character values are exactly multiplicative on each ray generator and every bounded prime-ideal element.
- Verify conductor kernels are nested and have orders (7500,625,25,1) in the local component.
- Verify the character counts sum to the full ray group order.
- Verify every split conjugate pair multiplies to the principal ray class of ((p)), every inert ideal ((p)) maps to that principal class, and each ramified prime ideal squares to ((p)).
- Preserve the Phase321-B exact section lifts and the nontrivial canonical-cocycle defect; do not assume a canonical lift is the section.

## Stop rules

Reject:
- floating-point roots of unity as exact character data;
- a direct-product model without the Phase321-B section and generator checks;
- conductor counts inferred only from group order without explicit kernels;
- calling the bounded prime-ideal evaluation matrix a complete global Euler product;
- any L-function, zero-free or discriminant-bound conclusion based on this finite computation.

## Evidence boundary

- **P:** the finite abelian duality construction and conductor-annihilator criterion under the exact finite group and reduction maps.
- **M:** the three explicit character groups, conductor distributions and bounded prime-ideal evaluation matrices after exact-head CI.
- **H:** any field-uniform conductor, prime-distribution, exceptional-zero or discriminant theorem.
- **R:** inferring a general ray-class formula or zero-free region from three fields and finitely many prime ideals.

The immediate next mathematical object after Phase322 is not an L-value: it is an exact, source-matched description of the character values on a larger prime-ideal family, with the conductor and prime-range dependencies stated explicitly.
