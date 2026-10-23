# Fixed Sylvester nonzero bridge - bounded continuation

Frozen main: 5bde735a86c93b938574128583b3396d07101093.
Upstream unmerged degree/contact PR #13: 96967b50d6479ff7e6eebc0847813ebfcfb5d4eb.
Scope: prove nonzero determinant of the SAME fixed coefficient matrix from
coprimality over a field; reflect from the fraction field of K[W]; derive the
characteristic-zero primitive-irreducible case when supported by pinned Mathlib.
No changed cutoff, classification, global jet uniqueness, or performance claim.
No main merge. Work on isolated draft branch. All current inputs are visible,
so this is a scope freeze before new execution, NOT blind preregistration.

Required gates: pinned Lean 4.19.0 / Mathlib c44e0c8; root imports; compiled
transitive axiom audit; inherited tests; matched true/false examples (exact
degree, characteristic zero, coprimality, polynomial nonzero vs specialization);
exact rational reference campaign including singular and degree-drop cases.
Preserve failures and repairs without changing mathematical target to fit CI.
No sorry, custom axioms, native_decide, assumed determinant nonzero or assumed
injectivity in the public nonzero theorem. Coefficient/matrix correspondence
must be proved, not assumed. Stop at the algebraic bridge and its actual
contact-budget instantiation; factor accounting and full jet uniqueness remain
separate. Promotion requires actual completed checks, not queued workflows.
The finite campaign is supporting evidence, not independent semantic review.
