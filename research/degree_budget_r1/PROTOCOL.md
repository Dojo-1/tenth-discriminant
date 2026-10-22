# Degree/contact-budget review: frozen verification plan

Base: 791ebf4815d8eb4be5da3b01527ca7f0877b6d0e. Review PR 12 at 34f41c9d9b52802b9afb9de13add74a5bfbb8eba rather than duplicating its stronger affine proof. PR 9 proof repairs must preserve all nine statements. PR 13 contains only the new degree/contact chain and explicit controls.

Target: for the ACTUAL fixed F,F_Z Sylvester matrix E(W), prove natDegree(E) <= (2a-1)b from coefficient degree <= b, then sum local orders at distinct W-values under E != 0 and nonzero specializations. Prove at most 2a-1 points with multiplicity greater than b>0. Do not discharge E != 0 by assumption laundering. No global classification or improved discriminant threshold.

Finite independent-path controls: seed 222026; 60 general polynomial matrices n=0..4 with column-specific degrees 0..3; 48 bivariate polynomial cases a=1..4, b=0..2 with exact and overpadded dimensions; 24 planted multiple-root families and 5 adversarial known cases. Retain zero determinant separately, degree drops and zero specializations. Use exact integer/rational arithmetic, no fitted tolerance. Compare rational production determinants with symbolic determinants/resultants where the dimensions agree. Rerun under Python -O.

Lean gates: pinned 4.19.0 and Mathlib c44e0c8, root import, source correspondence, compiled dependency audit, all inherited controls, plus matched true/false degree-budget controls. Any erroneous acceptance blocks promotion. CI failures remain in history. Source-to-statement review remains same-author.

Stop: after degree/contact connection, return to the named nonzero-determinant obligation rather than add a new representation.
