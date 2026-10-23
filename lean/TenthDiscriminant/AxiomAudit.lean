import Lean

/-!
# Compiled dependency audit

Check every logical project constant, including private definitions and opaque
values, not just declarations introduced by `theorem`. An unused definition is
still part of the apparatus. Source/import coverage is checked by audit.py.

The three allowed axioms are the existing classical Lean foundation. This gate
checks dependency hygiene, not the external interpretation of a statement.
Compiler-generated unsafe runtime implementations are reported separately via
Lean safety metadata; they are not kernel proof objects. Source-level unsafe
declarations remain forbidden by audit.py.
-/
open Lean Elab Command

elab "#audit_namespace " ns:ident : command => do
  let scopeName := ns.getId
  let env ← getEnv
  let mut count := 0
  let mut theoremCount := 0
  let mut runtimeCount := 0
  for (name, info) in env.constants.toList do
    if scopeName.isPrefixOf (Lean.privateToUserName name) then
      if info.isUnsafe then
        runtimeCount := runtimeCount + 1
        logInfo m!"RUNTIME_ONLY {name}"
        continue
      match info with
      | .axiomInfo _ => throwError "PROJECT_AXIOM {name}"
      | _ =>
        let dependencies ← Lean.collectAxioms name
        for dep in dependencies do
          unless dep == ``propext || dep == ``Classical.choice || dep == ``Quot.sound do
            throwError "NONSTANDARD_AXIOMS {name}: {dependencies}"
        logInfo m!"AXIOMS {name}: {dependencies}"
        count := count + 1
        match info with
        | .thmInfo _ => theoremCount := theoremCount + 1
        | _ => pure ()
  if count == 0 then
    throwError "EMPTY_PROOF_AUDIT {scopeName}"
  logInfo m!"AUDIT_OK {scopeName}: {count} logical declarations; {theoremCount} theorems; {runtimeCount} runtime-only auxiliaries excluded"
