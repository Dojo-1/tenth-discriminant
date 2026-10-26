import TenthDiscriminant

/-! Frozen proof-input inventory. This research command is not a theorem
or a new permanent CI gate. Reuse the pinned compiler's own dependency walk. -/
open Lean Elab Command

private def provenanceKind (info : ConstantInfo) : String :=
  match info with
  | .axiomInfo _ => "axiom"
  | .defnInfo _ => "definition"
  | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quotient"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"
  | .inductInfo _ => "inductive"

elab "#proof_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PROVENANCE_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let mut rows : Array Json := #[]
  let mut missing : Array String := #[]
  for name in state.visited do
    let source := match env.getModuleIdxFor? name with
      | some idx => env.header.moduleNames[idx]!.toString
      | none => "<current-research-driver>"
    match env.checked.get.find? name with
    | none => missing := missing.push name.toString
    | some info =>
      rows := rows.push (Json.mkObj [
        ("name", toJson name.toString),
        ("user_name", toJson (Lean.privateToUserName name).toString),
        ("module", toJson source),
        ("kind", toJson (provenanceKind info)),
        ("unsafe", toJson info.isUnsafe)])
  let report := Json.mkObj [
    ("root", toJson target.toString),
    ("visited_count", toJson rows.size),
    ("axioms", toJson (state.axioms.map (·.toString))),
    ("missing", toJson missing),
    ("constants", Json.arr rows)]
  liftIO (IO.println ("PROVENANCE_JSON " ++ report.compress))
  unless missing.isEmpty do
    throwError "PROVENANCE_UNRESOLVED {missing}"

namespace ProvenanceProbe
-- A simulated forbidden input, not a real classification theorem.
opaque simulatedHeegnerInput : True := True.intro
private def relay : True := simulatedHeegnerInput
theorem wrapped : True := relay
theorem clean : True := True.intro
def taggedType : Prop := True
theorem typeOnly : taggedType := True.intro
end ProvenanceProbe

#proof_inputs ProvenanceProbe.clean
#proof_inputs ProvenanceProbe.wrapped
#proof_inputs ProvenanceProbe.typeOnly
#proof_inputs TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one
#proof_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound
#proof_inputs TenthDiscriminant.phase36_all_fibers
#proof_inputs TenthDiscriminant.known_nine_classNumber_one
#proof_inputs TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff
