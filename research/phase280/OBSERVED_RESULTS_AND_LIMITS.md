# Phase280 — observed full-row D403 p² Smith results and limitations

**Recorded 11 November 2026 AFTER pre-registration** at commit 60de605 (before writing or running the numerical code). The user originated the geometric/mathematical research direction; the present model authored the executable and audit note. These figures are exact finite arithmetic [M] supported by [GitHub Actions 43086210971](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43086210971), not independent human mathematical validation.

## Frozen source, algorithm, and exact results

Same ORIGINAL trace Gram as Phases207–208: D403, rho40, R100,S=J4, Q219 full ellipse, n=400 original rows, m=1752 integer coordinate columns, all four **ordinary** ∂Z derivatives with W fixed during differentiation, and B=diag(2,806,...), not a Euclidean or Hasse replacement.

At inert p3,p5 the original integer unimodular Frobenius row source is normalized ONCE, with previously counted F3=570/F5=550. At split p11, no inert Frobenius factor is legal (F11=0). Every normalized row coefficient was first verified divisible by p^k before dividing. Precision K=2 was frozen; every ">=2" factor below is CENSORED and may have greater valuation.

| prime p | chi(-403,p) | old F (once) | FULL 400-row Smith 0/1/>=2 | C0 rank modp | C0 B C0^T rank modp | FULL additional evaluation index >= | original det G valuation >= |
|---:|---|---:|---|---:|---:|---:|---:|
| 3 | inert | 570 | 90 / 36 / 274 | 90 | 54 | 584 | 2(570+584)=2308 |
| 5 | inert | 550 | 240 / 15 / 145 | 240 | 240 | 305 | 2(550+305)=1710 |
| 11 | SPLIT | 0 | 132 / 66 / 202 | 132 | 132 | 470 | 2(0+470)=940 |

These are full-row, source-typed improvements over the already known Phase208 **SELECTED k>=2-row** lower bounds: p3 improved finite valuation lower 1640→2308 (gain 668); p5 improved 1310→1710 (gain 400). This changes no analytic cutoff and requires no class-number-one assumption to calculate the literal Gram (indeed D403 is a negative case for h=1).

All source verification controls passed: same exact original integer-jet oracle on deterministic row/point samples, independently implemented high-order dual-number oracle, both signed channels and all j=0..3, two distinct full-rank implementations, p² toy diag(1,p,p²), row shear and column reversal invariance, original signed-metric G rank, and exactly reproducible high-Frobenius subset histograms:
- p3 subset rows 188: 0/1/>=2 = 54/18/116; selected lower index 250;
- p5 subset rows 180: 0/1/>=2 = 120/15/45; selected lower index 105.

Dropping highest ordinary jet j=3, an INVALID altered source, changes ranks: p3 90→81, p5 240→180, p11 132→99. For split p11, original B imaginary weight 806 ≡3 (mod11), while the fake Euclidean weight 2 is different. No fake metric was used for the Gram rank.

## What follows mathematically — classical conditional result

For an integral n×m evaluation matrix C0 with full row rank over Q and Smith exponents a_i, all maximal minors are divisible by p^{sum a_i}. The diagonal original metric B is integral, so Cauchy–Binet gives v_p(det(C0 B C0^T))>=2 sum a_i. The original old source row transformation is unimodular, followed by explicit diagonal p^k divisions of row polynomials. Therefore if the literal original E is full rank, v_p(det G)>=2(F_p+sum a_i). With only K2, sum a_i>=r1+2r_ge2. The original source's interpolation positivity condition was checked in prior phases: |Q|=219>2(R-1)+(S-1)=201. This link is from the archive, not new independent semantic review.

Importantly, **the above lower bound includes no primitive restricted-pairing valuation whatsoever**. At inert p3 the normalized modp image radical has dimension r-g=90−54=36, but this may be wholly or partly an UNSATURATED artifact; do NOT add 36. At p5 and split p11 the corresponding radical is zero, but this does NOT prove their fully saturated primitive restricted pairings are p-adic units.

The split prime p11 already exhibits 470 capped evaluation-index units and a lower Gram valuation 940 WITHOUT an inert Frobenius factor. This is an essential negative control: large evaluation lattice indices by themselves do not uniquely identify an inert-prime mechanism. Moreover p11<403/4 is split, so this D403 field is NOT a class-number-one counterexample; no h=1 implication may be inferred from it.

## What remains unresolved

1. The exact p3/p5/p11 full row Smith index beyond level 2 is UNKNOWN. All three have >0 factors at cap.
2. No primitive Cprim of rank 400 was reconstructed, so no residual primitive pairing valuation and no full determinant valuation can be reported for D403.
3. The exact D283 primitive p3=29 and primitive p5=0 results from merged Phase278/279 remain valuable but come from a DIFFERENT source and cannot be glued into D403 valuations.
4. The universal target — uniform, source-compatible additional prime mass of order R²S log D on admissible class-number-one hypotheses — remains unproved. Some earlier bounds might already incorporate parts of the full index. To call anything "uncounted" requires explicit source-to-proof accounting.
5. This is a finite, correlated AI-authored experiment. No independent mathematician reviewed the interpolation-to-field bridge, as stated in issue #50; PR157 remains unmerged.

## Specific next falsification (requires new registration)

A partial third-depth K=3 pass on the FULL D403 source could sharpen the C0 evaluation index without yet reaching primitive H. It should only be attempted with a new frozen budget, deterministic resource ceiling, all four ordinary jets, and the same inert/split negative controls. Do not chase the depth until it becomes favorable. An alternative is a proof of why the observed deep defects arise from modular observation-class collisions, which could be falsified against split p11.

**Outcome:** Phase280 strengthens finite evaluation-index lower bounds at D403, but contributes no measured primitive residual at that source and makes no claim about Siegel zeroes or a new tenth discriminant.
