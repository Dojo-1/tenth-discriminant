# Phase309-B — preregistered conjugate-embedding cross-pairing

Date 2026-11-13. Written AFTER Phase309-A original-source focused CI PASSED, and BEFORE the B code. This is an honest **post-discovery follow-up**.

The same D203/p3/r0 original patch A:O²→O³ has maximal minor ideal I=(3,omega), a nonprincipal class, yet the original integer trace Gram determinant 671 is a 3-unit. Do not merely repeat the numerical coincidence; identify its *canonical arithmetic mechanism*.

For f(X)=X²-X+m, at a simple split prime p with root r, the other residue-field root is r'=(1-r) modp. Define sigma_r(a+b omega)=a+br modp and sigma_r'(a+b omega)=a+br' modp. Their combined map O/p ≅ Fp×Fp is the split residue algebra.

**Predicted exact mathematical identity for all x,y in O:**

    Trace_{K/Q}(x * conjugate(y)) mod p
       = sigma_r(x) sigma_r'(y) + sigma_r'(x) sigma_r(y).

The original trace pairing is a CROSS-pairing, not the same-embedding Euclidean dot product. At actual patch observations 0,p,z=omega-r, the residue evaluation matrices are

    A_r  = [[1,0],[1,0],[1,0]]       rank1,
    A_r' = [[1,0],[1,0],[1,delta]]   rank2,
    delta = 1-2r !=0 modp.

The original Gram modp must equal

    A_r^T A_r' + A_r'^T A_r
    = [[6,delta],[delta,0]] mod p,

and its determinant must be -delta² !=0 modp. This is the mechanism behind the Phase309-A determinant theorem. It does NOT claim physically entangled quantum states, superposition of intelligence, or a novel arithmetic result.

**Frozen controls:** D203/p3/r0 => delta1, local ranks(1,2), Gram mod3 [[0,1],[1,0]], determinant2. D187/p7/r2 => delta4, ranks(1,2), Gram mod7 [[6,4],[4,0]], determinant5. D167/p2/r0 => delta1, ranks(1,2), Gram mod2 [[0,1],[1,0]], determinant1. Verify all four entries against the unchanged ORIGINAL selected-rows trace Gram from Phase309-A for each field. Also verify bilinear cross identity for all integer coordinate pairs a,b,c,d ∈ [-3,3], at each field, without using the Gram helper to compute either side.

**Hostile controls:** a fake same-side pairing must differ from the true trace Gram in a suitable case; collapsing the two root embeddings into one loses rank; attempting conjugate transport when f has no split simple root must be rejected. The original Q263 observation set still contains z=1, which kills the Picard ideal of this selected submap; do not promote this local split-pairing to a full original field-theorem claim.

**Evidence:** P-paper conditional bilinear algebra from f(r)=0, M after hosted CI on frozen cases, H genuine globally useful prime-mass inequality, S "mutual recognition of two residue-field worldlets", R "one p-adic rank defect implies trace determinant divisibility". No merge and no field bound change.
