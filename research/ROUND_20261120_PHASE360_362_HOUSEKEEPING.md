# E100 — 20 November 2026 source-locked research and housekeeping update

**Read this before historical research summaries.** Snapshot based on fresh GitHub PR heads and CI; check live status for later changes. No outside human number-theoretic referee report has been received. The only publicly integrated actual-field Lean theorem on main remains the strict **322⁴** bound (PR #126); **302⁴ and below are research**, regardless of successful kernel checks.

## Formal / analytic / field fiber

| Gate | PR | Exact evidence | What is NOT established |
| --- | --- | --- | --- |
| Original integer Qthin geometry and Gram positivity from 14⁴ | #261 | P relative to checked Lean definitions | Does not give field bound |
| Original 302 normalized lower (binary + odd) | #263 | P relative to checked class-number-one, squarefree, positive-Gram hypotheses | Independent p-adic row proof not provided |
| Original 302 normalized upper | #265 | P relative to checked same-Gram Hadamard definition | No external semantic reconstruction |
| Actual field 302 candidate | #267 | P relative to encoded NumberField.discr theorem | Not a refereed new result |
| **Unified original 302 root** | **#268** | **Full-root/source/allowed-axiom/negative-controls passed, merged into Phase350 research parent as be605cb3** | **Not public main**; issue #50 human review open |
| Original 301 radius and conditional scalar separation | **#270** | **P relative to exact-head checked 847/1000 radius and 1377/10000 saving, merged as 952deb8b** | **Not yet an original 301 Gram bound or field theorem** |
| Complete original 301 Gram analytic upper | **#272** | H pending exact-head full-root Lean / source audit | No 301 arithmetic lower or field theorem yet |

The original objects are fixed: R=floor(D/4), S=floor(R/25), thinRadius=ceil(11 D^(3/4)/25), padded rho=ceil(13 D^(3/4)/25); the **complete** integer ellipse Qthin, original ordinary-Z jets with W fixed, original integer trace weights (2,2D), original integer rectangular trace Gram G, and comparisonScale R²S. Padded radius may upper-bound sample count, never replace G. The old R>=76 D^(3/4) fails at 302 and the old fixed-upper 301 scalar gap is negative. These are preserved negative controls, not defects to erase.

## Conductor / inverse-clock / counterexample fiber

- E31 #235 original-Gram unit counterexample **merged into research**: ambient conductor observer kernel does not force a 5-adic factor of the sampled original Gram.
- E32 #237 **merged into research**: source has a nonzero square-zero residue while the Gaussian target is reduced.
- E37 #250 **merged into research**: valid unimodular original-jet factorization versus a universally impossible one.
- E38 #251 **merged into research**: finite kernel nontrivial at every tested/general level but coherent integer-representative thread zero.
- E30/E31 #234 **merged into E29 research parent** as 67ec01cd. Historical parallel E30 ZMod source #233 conflicts with the new parent; source-clean replacement #271, exact E30AdicPersistence file and note, is undergoing fresh exact-head CI. Do not conflate finite ZMod kernel counts with formal p-adic inverse-limit theorems.
- E46 #264 original-source observer consolidation is merged; a new CRT observer is not an extra arithmetic factor of the original Gram.
- Older E24–E29, E33–E42 branches are retained for matched negative controls, source-fidelity review and nonconflicting integration; **do not bulk merge** them into main.

## Corrections and housekeeping

- Historical Phase346–349 #223 closed as superseded: build succeeded but its earlier root audit failed on 54 unaudited project modules. Phase350 #232 later audited those modules; retain both receipts.
- Historical E42 #254 closed as superseded by the source-clean checked E46 #264.
- Main README/RESEARCH_NOW/STATUS should state **302⁴ unified research verified** and **301⁴ conditional radius/scalar P** while **301⁴ analytic upper H**.
- PR #232 is a long-lived Phase350 research-stack root; its head evolves as child merges occur and requires **a new exact-head CI** after each integration. Do not assume an earlier successful root run covers later children.
- The dated open-PR triage ledger is a historical snapshot, not a dynamic count or merger queue.

## Next falsifiable gates

1. Phase362 #272: uniformly prove a 301 original-Gram analytic upper using unchanged padded-count majorant and stronger Phase361 radius saving. If Lean fails, preserve exact failing lemma and repair it; no 302 premise may be silently retained.
2. Only if #272 passes, independently rederive binary-plus-odd **301** lower on the literal SAME positive Gram and source, with no new prime powers.
3. Only after both inequalities and a fresh combined-root proof, attempt a research actual-field 301 chart. Do not promote to main or claim mathematical priority without external review.
4. Independently reconstruct the original p-adic row operations and odd/even maximal-order field charts in [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). A concrete counterexample or missing-hypothesis report is more informative than another self-authored green CI badge.

**Evidence labels:** P = theorem relative to imported Lean definitions and standard axioms; M = bounded numerical oracle; H = open source/fiber bridge; R = corrected invalid inference. Never infer a bound on the actual discriminant from an auxiliary Gram without the explicit typed field-transport theorem.
