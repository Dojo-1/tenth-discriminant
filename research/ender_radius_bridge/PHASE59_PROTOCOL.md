# Phase59: one conditional excluded-prime bridge prototype

Registered before writing or executing the prototype. Base:7b80ff310080ed6b8dd2ce4a7cadeaada1229b8a. This is a separate research branch; the final documentation PR29/head7b stays fixed in CI. No additional reviewer is authorized.

## Fixed mathematical target

Keep the actual integer/real ellipse trace-Gram, ordinary derivatives and factor-two normalization. Let P be a finite set of odd primes at most L, L>=3; let G be a subset of P, with -D nonsquare modulo each p in G; let E=P\G. Put w(p)=2*valuationWeight(R,S,p)*log(p), using real casts. Retain exactly the existing positive-radius geometry hypotheses for D,D2,rho,R,S, with no class-number, squarefree, mod4, old-cutoff or finite-answer input.

Use a real kernel f:Nat->Real, antitone on [3,L], with f(L)>=0. Let N(n)=#{p in E:p<=n}, interpreted as real. Assume N(n)<=B(n) for every n in [3,L], C>=0, and w(p)<=C*f(p) for p in E. Define

    K = f(L)*B(L) + sum(n in Ico 3 L, (f(n)-f(n+1))*B(n)).

The fixed end-to-end conditional conclusion is

    sum(p in P,w(p))
      <= log(product(actual ellipse Gram diagonal)) + C*K.

All count/kernel/weight assumptions remain explicit. This is a prototype of the bridge, not a proof that class number<=2 supplies B or f, and not a new numerical exclusion. Do not replace the matrix or weakening target with a purely unrelated finite-sum result. The actual-Gram good-prime bound, exact indicator/partial-count Abel identity, positive-kernel bound and final assembly must all compile together for acceptance.

Reuse pinned Mathlib Finset.sum_Ico_by_parts, not a duplicate general summation theorem. Existing local nonsquare valuation and generic coprime-product/geometry/cast lemmas are allowed. The proof must not call class-number-one prime-mass wrappers or any old cutoff/classification conclusion. Imports alone are not dependencies; inspect the compiled prototype closure.

## Fixed controls and scope

Include a nonempty finite rational-kernel identity E={3,5},L=5,f(n)=1/n giving8/15; an empty excluded set; and rejection of the abstract count-bound transfer after dropping coefficient signs (increasing kernel example at3,4), plus a negative endpoint-kernel example. These test the finite operator, not necessity of every hypothesis in the number-field theorem. Show the split local input D=19,p=5 fails the nonsquare predicate; do not claim a determinant counterexample from that predicate check alone.

Prototype source stays outside production modules, under research/ender_radius_bridge/Phase59Prototype.lean, with explicit standard-axiom namespace audit and compiled dependency exclusions. Production .lean files/root, numerical tools/certificates/pins and CI gates remain unchanged. No whole-project/higher-class-number result is inferred from a standalone checked prototype.

## Budget and evidence

At most3 complete prototype builds,600seconds/8192MB per process,1200seconds cumulative target budget. Stop after any resource stop, preserve INCOMPLETE. At most2 local proof repairs, with the same target and guards. Snapshot every attempted prototype and raw stdout/stderr/result before repair. No alternate theorem, easier endpoint, parameter sweep or hidden rerun. Fixed input/exclusion checks must be part of acceptance; namespace audit permits only propext,Classical.choice,Quot.sound. No sorry/native_decide/custom axiom escape.

The candidate paper algebra and existing Mathlib API were inspected before registration; this is not a blinded discovery experiment. On success report only the conditional checked bridge and its remaining arithmetic inputs. On failure preserve the missing lemma/error/cap honestly. No full-classification, novelty, optimality, human review or historical-year claim.

Do not cancel/restart/push over the existing final documentation CI. Preserve its exact terminal record before any later publication. Any successful prototype belongs in a separate reviewable delivery, not another expansion of the README.
