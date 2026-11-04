# Round201 extension, preregistered before T5: non-surjective finite-level kernel transport

Date: 2026-11-04, after original Round201 T0–T4 and before the new finite-level transition test. **This is a separate, post-registered prediction; do not backdate it into the Round201 preregistration.**

## Mathematical tension

The earlier kernel *size* profile h_{p,m} = log_p |ker(G mod p^m)| reconstructs the p-primary Smith depth, but the groups K_{p,m} are not naturally nested as subsets of one fixed group. Reduction K_{p,m+1}->K_{p,m} is well-defined but can fail to be onto. In particular, many nonzero finite-level kernel elements may fail to lift to a compatible infinite p-adic solution.

This is a decisive typed-transport caution: **cardinalities alone do not specify the transition morphisms**. For the original positive definite integer Grams, the inverse-limit kernel is expected to be zero although individual K_{p,m} can be very large.

## Predicted tests (registered before execution)

- **T5a:** Scalar G=[3] at p=3. For each 1<=m<=4, K_{3,m} is exactly the multiples of 3^(m-1) in Z/3^m, and |K|=3. The reduction K_{3,m+1}->K_{3,m} has image {0} for every m>=1, in particular is *not surjective* even though both domain and codomain have size 3.
- **T5b:** Scalar G=[0] gives K_{3,m}=Z/3^m with the usual surjective reductions, showing singularity changes the inverse-limit behavior. This is an intentional non-SPD countercontrol.
- **T5c:** For diagonal G=diag(1,3,27) (from original T1), compute finite kernel levels m=1,2,3,4 and actual image sizes for transitions m+1->m by exact enumeration (the p^4 three-coordinate domain is 81^3 and expensive; use algebraic generator formula instead with explicit checks). Distinguish group size from image size and record failure to lift to the full tower.
- **T5d:** For any nonsingular G over Z, prove on paper (not automatically Lean) that inverse limit K_{p,m}(G) is ker(G:Z_p^n->Z_p^n)={0}: by adjugate identity det(G)*x=0 in the integral domain Z_p; det(G) is nonzero, so x=0. This is classical algebra and not a new theorem of number fields.

## Evidence and falsification

The scalar exact computations are M, the general adjugate argument is P (standard algebra, not a compiled Lean proof). Fail if reduction maps are conflated with inclusion, or if a nontrivial compatible inverse-limit kernel is claimed for nonsingular G. The only possible new research consequence requires **more structure than kernel size**: explicit cross-level maps, associated graded pieces, and an independent source-exact geometric constraint. A result with no new discriminant advantage is not to be advertised as such.

No changes to PR #126, its ordinary jets, or the existing Round201 preregistration. This extension should appear as a separate git commit before its test script.
