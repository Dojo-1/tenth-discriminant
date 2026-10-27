# Phase64: closed off-axis area bound and production integration

Register before new source/execution. Basee92d05b7f0f7dbade8a5a89f834550d1ebb78ccc; frozen Phase63 source/results/raw remain unchanged. Separate local branch while PR31 CI40407136985/job121867685012 runs; no cancel/restart/replacement push/status transfer. PR30 merge approval still pending; no merge/reviewer authorized. No Phase61 or62 proof/control campaign rerun.

## Fixed target and integration

Transport frozen Phase63 to production QuadraticRowCount.lean, changing only imports (Mathlib+AxiomAudit instead of Root), namespace NonzeroRows->QuadraticRows and a reader header. Preserve all definitions, actual finite-count statements/guards/proof bodies/controls under that transport. Add QuadraticAreaCount.lean and two Root imports.

For real a,D,t with a>0,D>0,t>=0, prove the EXACT identity
  2*integral_0^sqrt(4at/D) sqrt(4at-D*s^2)/a ds =2*pi*t/sqrtD,
including t=0, and height=2*sqrt(at/D). Compose the actual Phase63 count, not a supplied count assumption, to prove for every finite integer-pair U:
  a>0,4ac-b^2>0,t>=0, Q(U)<=t, y!=0
    => cardU<=2*pi*t/sqrt(4ac-b^2)+4*sqrt(at/(4ac-b^2)).

Use Mathlib integral_sqrt_one_sub_sq and homogeneous integral scaling. Prefer the scaling identity that also holds at zero height; no hidden division by Y. Use evenness/actual reflection and adjacent-interval additivity to connect full and half integrals. No custom pi, numerical oracle, Arb or new axiom. No coefficient/radius/matrix replacement, supplied area premise or abstract-count fallback.

Fixed controls: zero threshold gives zero budget and retains the origin falsifier when y!=0 is dropped; unit-circle two off-axis points satisfy2<=pi+2; actual sheared form(a,b,c,t)=(1,2,2,1), with integer points(-1,1),(1,-1), gives the same bound and tests shifted row centers. All transported controls and fixed full target must compile together with standard-three-axiom namespace audit. Inspect the final public type and axiom print.

## Budget and verification

At most3 complete builds of the new production modules,600seconds/8192MB each,1200seconds cumulative; at most2 proof repairs with unchanged target/types/guards. Stop after any target resource stop. Snapshot both source files and raw stdout/stderr/result for every attempt. Preserve failure/incomplete evidence; no easier endpoint/parameter sweep/hidden rerun.

After target acceptance: production root once (1200seconds/8192MB), compiled full audit once (180seconds/8192MB), fixed statement/control print once(180seconds), structural import/source-escape coverage and unchanged source correspondence; then unchanged pinned CI. Do not repeat the timed-out local Phase61 negative campaign. The existing complete production controls will be exercised by independent pinned Linux CI, and its scope must be recorded explicitly. Original proof sources/tools/certificates/pins/CI gates and61-line README stay unchanged except these two modules/Rootimports. Old current-root verifiers become historical; preserve their source/evidence bytes at frozen refs, do not weaken their original manifests.

No closed arithmetic count B, class/form dictionary, four-representation proof, ramified budget, h<=2 numerical cutoff, classification, novelty, independent review or Mathlib acceptance follows. Explain one human proof of the actual geometric bound. Publish only after PR31's terminal exact-head CI record, combining this with Phase63 into one coherent follow-up rather than opening another half-result PR. The broader goal remains open.
