# Phase339 — ordinary-jet divisibility of powers of the mixed factor

**Evidence status:** elementary paper proof; **not yet a Lean theorem**.
The exact-integer controls accompanying this note are finite checks, not
a replacement for the universal proof. This lemma is *not* included in
the Phase338 arithmetic lower or its putative 313^4 field theorem.

## Objects (nothing about the source changes)

Let D be a positive integer and L = Z[t] / (t^2 + D), with
z = x + y t, w = x - y t for x,y in Z. Let

```math
H(Z,W)=Z^2-W^2,qquad
P(Z,W)=H(Z,W)^b Q(Z,W),
quad b\in\mathbb N, Q\in\mathbb Z[Z,W].
```

Use the *original ordinary derivative* in Z, with W held constant,
evaluated at (Z,W)=(z,w). No Hasse-derivative substitution and no
maximal-order samples are permitted.

### Proposition (universal paper-level)

For all b,j >= 0, x,y,D and Q as above,

```math
\boxed{
\left.\partial_Z^j P(Z,W)\right|_{(z,w)}
\in j!\,2^{\max(2b-j,0)}L.
}
```

Equivalently, for each coefficient of the source pair in the
integral basis (1,t), the ordinary jet is divisible by
j! times 2 to the indicated power.

### Proof

First compute exactly

```math
A=z^2-w^2=4xy\,t\in4L.
```

In L[u], with u an independent formal variable,

```math
H(z+u,w)=A+2zu+u^2.
```

Every term in the coefficient of u^k of the b-th power
(A+2zu+u^2)^b comes from nonnegative a,c,d with
a+c+d=b and c+2d=k. Its coefficient contains the product

```math
A^a (2z)^c\in2^{2a+c}L
  =2^{2b-k}L.
```

Thus the k-th ordinary derivative of H^b at z belongs to
k! * 2^(2b-k) L for 0<=k<=2b, and is zero for k>2b.
This is an exact coefficient argument, not an asymptotic estimate.

For Q, ordinary integer-polynomial differentiation gives

```math
\partial_Z^m Q(z,w)\in m!L.
```

Apply Leibniz's rule:

```math
\partial_Z^j(H^bQ)
  =\sum_{k=0}^j{j\choose k}
     (\partial_Z^kH^b)(\partial_Z^{j-k}Q).
```

Every nonzero term has 0<=k<=min(j,2b) and is divisible by

```math
{j\choose k}k!(j-k)!\,2^{2b-k}
  =j!\,2^{2b-k}.
```

The minimum guaranteed exponent is 2b-min(j,2b)
= max(2b-j,0). Since L is closed under addition, the same divisor
holds for the sum. QED.

## Sharp controls and exclusions

- For b=1, Q=1, j=0, x=y=1, H(z,w)=4t. The factor 4 is sharp
  in the integral source coordinates.
- For b=1, Q=1, j=1, z=w=1, the first jet is 2, not 4.
  This kills a false uniform 4-divisibility claim for all j.
- For b=1, Q=1, j=2, the jet is 2=2!, so no factor 2
  beyond the ordinary-derivative factorial is forced.
- For b=2, Q=1, j=2, z=w=1, the jet is 8, matching
  2! * 2^(4-2) exactly.

The proposition concerns **the same original source lattice** L.
At a maximal-order generator omega, H(omega,bar omega)=2omega-1,
so the source congruence does NOT transfer to arbitrary maximal-order
observations. See Phase334–335 for the conductor-two obstruction.

## What is (not) implied

- **Mathematical:** the coefficient-level graded original-jet
  divisibility follows by the displayed finite multinomial identity.
- **Formal (open):** a Lean theorem for every b,j,Q, preserving this
  precise exponent and its ordinary derivative convention.
- **Determinant (open):** if rows are transformed by powers of H,
  their simultaneous 2-adic invariant factors must be proved in one
  unimodular basis of the *original* Gram. This lemma alone supplies
  NO new joint determinant exponent.
- **Numerical field bound (unaffected):** Phase338 uses the existing
  combined binary/odd lower and no additional mixed-binary gain.

**Kill condition for any new factor:** produce an explicit original
ordinary-jet matrix whose joint row transformation does not achieve the
claimed new invariant factors; never count independent filtrations
additively without a simultaneous integral basis witness.
