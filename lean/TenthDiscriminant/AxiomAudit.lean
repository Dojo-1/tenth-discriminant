import Lean

/-! Verification infrastructure: enumerate compiled declarations, including private
ones, rather than treating a regex of theorem source text as authoritative. -/
open Lean Elab Command

elab "#audit_namespace " ns:ident : command => do
  let prefix := ns.getId
  let env ← getEnv
  let mut count := 0
  for (name, info) in env.constants.toList do
    if prefix.isPrefixOf (Lean.privateToUserName name) then
      match info with
      | .axiomInfo _ => throwError "PROJECT_AXIOM {name}"
      | .thmInfo _ =>
        let dependencies ← Lean.collectAxioms name
        for dep in dependencies do
          unless dep == ``propext || dep == ``Classical.choice || dep == ``Quot.sound do
            throwError "NONSTANDARD_AXIOMS {name}: {dependencies}"
        logInfo m!"AXIOMS {name}: {dependencies}"
        count := count + 1
      | _ => pure ()
  if count == 0 then
    throwError "EMPTY_PROOF_AUDIT {prefix}"
  logInfo m!"AUDIT_OK {prefix}: {count} theorem declarations (including generated auxiliaries)"
