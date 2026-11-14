# Phase307-I — post-H follow-up preregistration: actual Picard/class-group field bridge

2026-11-13. This test was formulated AFTER the abstract sphere-vs-functions H2 result and prior source controls; it is a new follow-up, NOT part of original prior-to-all-code preregistration.

**Mathematical bridge [P-paper]:** For the Dedekind domain O_K of an imaginary quadratic number field, the isomorphism class of an invertible ideal lies in Pic(Spec O_K)=H^1(Spec O_K,G_m)=Cl(O_K). The class-number-one condition is precisely triviality of this Picard group. The implemented tool must NOT claim to compute a Čech cocycle or prove a class-group presentation.

For D>0 squarefree, D=3 mod4, let omega²=omega-m with m=(D+1)/4 and norm N(a+b omega)=a²+ab+m b². For a rational prime p and root r in Fp of f(X)=X²-X+m, the ring map psi_r:O_K->Fp given omega->r is well-defined and surjective; its kernel is the maximal ideal I=(p,omega-r) with norm p. If I=(alpha) principal, then |N(alpha)|=p, impossible if p<m and p is not a square, because any b !=0 has norm >=m while b=0 gives a square.

**Frozen tests BEFORE code:** D203,p3, polynomial roots0,1, p3<m51, no principal norm3 -> nontrivial Pic. D187,p7, roots2,6, p7<m47 -> nontrivial. D167,p2 roots0,1, p2<m42 -> nontrivial. D163,p3 is inert (no F3 root), so must NOT construct a degree-one p3 prime ideal by this recipe. **Boundary control D163,p41:** roots0,1, p=m=41; norm(omega)=41, so the test must accept a principal ideal generator and NOT issue a false nonprincipal certificate.

Check actual ring homomorphism multiplicativity across a fixed bounded set of integer coordinate pairs without assuming the norm obstruction from finite search alone. Test that p divides D? ramification is distinct; do not assert every root pair is split without squarefree/good-prime hypotheses.

[P-paper] standard norm/ideal/Pic reasoning; [M after CI] bounded roots and ring hom tests. [H] a new uniform arithmetic-to-original-Gram weight link and a new discriminant bound. [R] abstract tetrahedral H2 as if it were the ideal class group. No new main changes or merges.