# Phase317-D — preregister explicit Z/25 congruence before constructing it

2026-11-14 Europe/Madrid. This is AFTER the Phase317-C radical-tangent **measurement** on source and tests succeeded (focused run 43589928687, 19 tests): for each of the five trace-zero synthetic wild gauges, H=(G_k-G_actual)/5 mod5 restricts to ZERO on the 17-dimensional radical of the SAME original mod5 Gram. The constructive tangent solver verifies the F5 equation in a split basis, but the resulting original-coordinate Z/25 change of basis has NOT yet been implemented. This protocol is written BEFORE that additional code.

Frozen new target: construct EXPLICIT U_k=I+5 X_k in GL_40(Z/25) such that, for every k=0,1,2,3,4,

    G_k = U_k G_actual U_k^T mod25

for all 1600 cells of the original D163 primitive Gram (native integer order Q109,R40,S=J1). Recover X_k by transporting the previously verified split-basis tangent solution X' through a basis P which sends G0 to diag(A,0):
    X_k = P^{-T} X'_k P^T  over F5.

Check (1) H_k=X_k G0+G0 X_k^T over F5,
      (2) U_k (I-5X_k)=I mod25 (so U_k is an exact unit),
      (3) U_k G U_k^T=G_k mod25,
      (4) G_k-G= k*(G_1-G) mod25; equivalently X_k=k X_1 may be chosen as gauge family witness (no assumption all constructed arbitrary X_k agree unless normalized).

If all hold, the five mod25 Gram matrices are EXACTLY congruent over Z/25, not merely equal in rank or Smith strata. That is stronger than the already measured tangent result, but STILL not a proof their integral determinants or deeper 5-adic Smith exponents agree: U_k only lives mod25 and G_k are SYNTHETIC local-tag reconstructions, not actual global generator Grams.

Stop and preserve any failed matrix entry, inverse certificate or linearity check. No class-number-one characterization, new field or reported 322^4 change.
