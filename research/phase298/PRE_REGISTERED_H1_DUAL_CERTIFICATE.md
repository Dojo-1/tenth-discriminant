# Phase298-C — preregister independent original D163 h1 dual witness after exhaustive scan

**2026-11-13. AFTER the Phase298-B 38-step exact-original-source scan PASSED [CI #43379240150](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43379240150), BEFORE Phase298-C code and result.** The selection n13 is RETROSPECTIVE and explicitly named, not a hidden preregistered prediction. No Work or merge, no actual-field cutoff claim.

The full D163 source is the repository's ORIGINAL Q109/R40/S=J1 monomial Gram with B=diag(2,326). The quadratic FIELD has h1 by classical Minkowski and inertness of 2,3,5,7; the source itself is the original integer order sampler, not the full maximal-order two-coset lattice. The previous run checked all1600 exact Gram entries against an independent original mixed-moment oracle; 31 of38 contiguous first stages projected integrally, 7 did not, and eight later steps had order5 cross-image defects. All 31 permissible integral-first composition formulas passed; no *new* residual Schur obstruction appeared in this J1 class-one scan.

**New independent question:** Can one exhibit a *short, source-correct*, directly checkable obstruction to the overstrong proposal "class number one makes every original trace Gram row extension project integrally"? Take the **FIRST nonintegral original row attachment in the exhaustive fixed-order scan**, n13→14, where the 13 old original monomials are Z^0,...,Z^12 and the new original row is Z^13. The previous result measured an order5 cross-image class with the complete old Smith profile uncensored at K16. The target is an exact finite functional rather than another histogram.

Let `A=G_D163[:13,:13]`, `c=G_D163[:13,13]` from full ORIGINAL source. Use an independently replayed tracked `U A V=diag` original modular Smith reduction over Z/5^16 (Phase297-D integer module solver) solely as a witness search device. Find a deterministic Smith row i of p-adic grade e<K with `ell = U[i] mod5^e` such that
```
 ell A = 0 mod5^e  (ALL 13 columns);
 ell c !=0 mod5^e.
```
This CERTIFIES `c∉ A Z5^13`, so the original Z^13 row does not admit an integral orthogonal projection to the old 13 rows, although the FIELD has class number one. Publish the full 13-element ell in the CI log, with its exact modulus, all old Gram zero checks, new nonzero residue and JSON SHA256. Recompute A and c independently from the original source_probe mixed moments and manually rebuilt original j0 evaluation Gram, no synthetic observations. The witness need not have valuation e-1; record exactly what occurs, and do not change n=13 if the witness fails. Original rank 13 and small p^K controls are suitable for explicit human inspection.

Additional positive control: at the immediately preceding original attachment n12→13, the Phase298-B exhaustive scan reported integral first-stage projection (index0). Reconstruct that original A12,c12, solve `A12 x=c12 mod5^16` and directly check every one of the 12 congruences. Both old Smith systems must have max exponent<K. Retain Phase298-A hostile positive-definite toys, and ensure the original field D163/J1 status cannot be misreported as a full higher-jet or maximal-order theorem.

**Stop if:** source hash changes, D163 class-one inertness check fails, independently reconstructed G entries disagree, n13 old Smith is censored, dual witness does not exist, or n12 positive projection fails. No cherry-picking another n. No adding cross-image index to original determinant valuation.

**Evidence:** [P-paper] dual annihilator linear-algebra obstruction and conditional h1-classical Minkowski proof; [M after focused CI] explicit 13-vector original sampler witness and 12-row positive original control; [R] universal integrality of every original-source row attachment from h=1; [H] any uniform high-J field inequality or improved tenth-discriminant cutoff.
