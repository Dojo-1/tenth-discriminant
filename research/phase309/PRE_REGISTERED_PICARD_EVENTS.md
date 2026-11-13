# Phase309-C — post-B preregistered Picard event filtration

Date: 2026-11-13. Written AFTER Phase309 A/B checks were observed passing, BEFORE Phase309-C code. This is a test of nontrivial observation-cover dynamics on the **same original (1,Z) source**.

For a quadratic integer ring O and ordered *actual* original observations (0,z1,...,z_k), form the restricted O-linearized original-row map A_k(a,b)=(a,a+z1*b,...,a+zk*b). For k>=1, its maximal 2x2 minor ideal is

    J_k = (z1,...,zk),

because the minors are all zi-zj, and z0=0 is included.

The integral saturation of the K-span is always

    Sat(im A_k) ≅ O ⊕ J_k^(-1),

as a **projective O-module**, where b∈J_k^(-1) is exactly the requirement that all zi*b belong to O. This formula depends on a chosen anchor observation z0=0, which the original source actually has.

**Prerecorded Phase309-C chain for D203/p3/r0:**

    observations S2=(0,3)        J2=(3)        Norm(J2)=9     Picard class=0,
    observations S3=(0,3,omega)  J3=(3,omega)  Norm(J3)=3     class order4,
    observations S4=(0,3,omega,1) J4=O        Norm(J4)=1     class=0.

The ideals strictly increase J2⊂J3⊂J4, their inverse fractional coefficient modules strictly DECREASE:

    (1/3)O ⊃ I^(-1) ⊃ O.

Exhibit explicit strict witnesses:
    b=1/3 ∈ (1/3)O but NOT I^(-1), because omega/3∉O;
    b=conjugate(omega)/3 ∈ I^(-1) but NOT O.

This predicts a **class birth/death event** under monotone addition of actual observations, despite the coefficient fractional ideals shrinking monotonically. A class-group residue is not an ordered scalar persistence barcode, and this is NOT a claim of topological persistent homology.

**Controls:** every selected observation must be inside the native D203 maximal-order radius and match its exact original j0 row labels; the final full actual observation set contains 1. An arbitrary new point outside the source is rejected. For the principal D163/p41 control, original source absence of point41 must be respected. No 100-row full-source Picard result or improved same-original-Gram inequality follows.

**Typed remainders:** missing observations during restriction; changed finite source cover; Picard class cannot be read from scalar ideal norm or from original trace Gram p-adic mass.

Stop if any ideal index, inclusion witness, source-fidelity, or class-order assertion fails. No merger, no user-affecting action, no claim of cognitive benchmark improvement.
