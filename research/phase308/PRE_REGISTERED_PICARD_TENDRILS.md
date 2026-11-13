# Phase308 — Picard Tendrils: ideal-class order four and disappearing determinants

**Date:** 2026-11-13. **Status:** AI-origin conjecture and hand-calculated evidence, not yet independently compiled/tested on GitHub. Stacked DRAFT on Phase307 PR #199 exact head ea15ff760c9507967dbe60b5f448879536d8bc54.

This file is written **before** the new computational witness and tests. This branch does not change the original 100-row source, its integer trace Gram, or the reported 322^4 bound.

## A. Original arithmetic Worldlet, actual ideal

In the maximal integer ring O=Z[omega] of K=Q(sqrt(-203)), omega^2=omega-51, set I=(3,omega), J=(3,omega-1). Roots 0 and 1 of x^2-x+51 modulo3 give distinct norm-3 prime ideals. Test I*J=(3). Let alpha=omega-6, Norm(alpha)=81.

**Predicted exact theorem [P-paper target]:**

    I^4 = (omega-6),   [I] has exact order 4 in Pic(Spec O).

Independent proof obligations:
1. I^4 has integral Z-generators 3^(4-k)*omega^k for k=0..4, with their omega-multiples closing O-action. Show all five generators divisible by alpha in O by evaluating g*conj(alpha)/81 in integer omega coordinates, exactly. Predicted quotients:
     k=0: -5-omega
     k=1: 17-2omega
     k=2: 34+5omega
     k=3: -85+13omega
     k=4: -221-24omega
2. Norm(I^4)=3^4=81=Norm(alpha); containment + equal finite index establishes ideal equality. Verify the Z-lattice index independently by gcd of all 2x2 minors of the O-ideal generator lattice.
3. No element of norm 3 or27, because 4Norm(a+b omega)=(2a+b)^2+203 b^2; for nonzero b this is >=203, while b=0 norm is a square. Norm9 elements are only +/-3 and (3)=IJ not I^2. Thus I^k not principal for k=1,2,3.
4. Independent classical reduced primitive positive binary quadratic forms of discriminant -203 yield exactly (1,1,51),(3,-1,17),(3,1,17),(7,7,9); do not confuse finite enumeration with a Lean proof of the reduction theorem.

## B. Actual Čech/Picard 1-cocycle on a legitimate arithmetic cover

Let U=D(omega), V=D(omega-1) in Spec O. Since omega-(omega-1)=1, {U,V} is a cover.

- On U, I_U=O_U: local generator g_U=1.
- On V, omega=-51/(omega-1) is a multiple of3: I_V=3 O_V, generator g_V=3.
- On U intersect V, 3 is a unit with inverse -17/(omega*(omega-1)). Thus transition t=g_V/g_U=3 is an honest O^*-valued Čech 1-cocycle.
- It is nontrivial in H^1(Spec O,G_m), because a coboundary would produce a global ideal generator, contradicting the norm-3 obstruction.
- Fourth tensor power has t^4=81. Trivialize with alpha=omega-6: local units u_U=alpha and u_V=alpha/81. Verify explicitly

    alpha^{-1}=(-221-24 omega)/omega^4   on U
    u_V = alpha/81 = (-245+24 omega)/(omega-1)^4   on V
    u_U / u_V =81 on overlap.

This is an actual arithmetic **line-bundle gluing obstruction**, distinct from the abstract Phase306 tetrahedral-nerve H2 class.

## C. Positive boundary and hostile semantic controls

For D=163, omega^2=omega-41, I_41=(41,omega)=(omega). On the analogous cover U=D(omega), V=D(omega-1), local generators 1 and 41 give transition t=41, but a true coboundary:

    u_U=omega,   u_V=omega/41=-1/(omega-1),    u_U/u_V=41.

Test Norm(omega)=41, exact quotient identity, nontriviality classifier must **reject** a false nonprincipal claim. Wrong split p or invalid cover/units must be rejected. A transition unit on U∩V must **not** be silently regarded as a global unit.

## D. New conditional mathematical prediction: determinant forgetfulness

For *separately defined* twisted O-module source M_N=I^{\oplus N}, its determinant line has class [I]^N. For N=4,100 the class is trivial while each individually named I component is nonprincipal. By the classical Steinitz classification of finite rank projectives over a Dedekind domain, M_4 and M_100 are abstractly free. **Do not identify M_100 with the repository's original 100 INTEGER polynomial-row lattice**, which is unchanged. An abstract module isomorphism does not preserve the original trace metric and is NOT an original source-gauge proof.

Operational failure discriminator: a scalar determinant/Steinitz-class-only gate reports "trivial" at N=4,100; the structured individual-Picard-label gate still reports all N independent original line labels as nontrivial. Measure this discrepancy, but don't call it improved mathematical intelligence without matched task evidence.

## E. Transport to other Worldlets without authority leakage

- Original integer trace-Gram: unchanged and never automatically multiplied by 3 or 81.
- Localized ring: t=3 invertible on U∩V is **not** invertible in global O. Reject fake GL_N(O) transport based on localization.
- Picard Worldlet: class order4, local-to-global obstruction.
- Tendril: U/V transition and 4-fold composition to trivialized line.
- Evidence Worldlet: [P-paper] conditional elementary ideal and Picard/Steinitz theorem; [M] exact finite certificate; [H] new same-Gram prime-mass bridge and empirical cognition advantage; [R] scalar determinant sufficiency for retaining individually labeled ideal classes.

## Kill conditions

Any failed norm, generator quotient, 2x2-minor ideal index, independent reduced-form count, local-unit reconstruction, or principal D163 boundary invalidates the Phase308 claim. The CI **must** run on exact draft head; no merge and no false "AI self-reviewed" status. No claims of original novelty in classical ideal theory, consciousness, physical quantum actions, or improvement over the existing 322^4 bound.
