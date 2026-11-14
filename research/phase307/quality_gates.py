#!/usr/bin/env python3
"""Phase307-F: sixteen typed, executable *research quality gates*.

These roles are not mental faculties, consciousness, metacognition, general
intelligence or evidence of performance improvement. They test invariants,
refusals and typed remainders on fixed bounded cases.
"""
from dataclasses import dataclass
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research"/"phase306"))
import arithmetic_fabric as ar
from higher_categorical import tetrahedral_sphere_nerve, nontrivial_H2_certificate
from actual_sheaf_cohomology import demonstrate_coefficient_sensitive_H2
from precision_towers import PrecisionWorldlet, GovernanceClock, TransportRemainder


@dataclass(frozen=True)
class Probe:
    role: str
    evidence: str
    observable: str
    hostile_control: str
    passed: bool


def refusal(operation, exception):
    try:
        operation()
    except exception:
        return True
    return False


def probes():
    manifest=json.loads((ROOT/"research"/"phase306"/"worldlet_manifest.json").read_text())
    expected=set(manifest["qualities"])
    assert len(expected)==16
    points=ar.actual_d203_points()
    e=ar.exact_original_jet_rows(points,degrees=(0,1,2),jets=2,d=203)
    g=ar.trace_gram(e)
    u=ar.matrix(((1,2,0),(0,1,-1),(0,0,1)))
    v=ar.matrix(((1,0,0),(1,1,0),(0,0,1)))
    q=ar.Claim("finite-gram","AI-source","M","source_measurement","pinned")
    witness=ar.Attestation("AI-source","formal_kernel","self-made")
    gate={}
    def add(role,observable,control,passed):
        assert role in expected and role not in gate
        gate[role]=Probe(role,"M-finite-gate-only",observable,control,bool(passed))

    add("Q0_grounding","actual D203 six-point norm and Gram",
        "arbitrary source points would fail norm",all(ar.omega_norm(z,203)<=576 for z in points) and ar.det(g)>0)
    moved,correct,d0,d1=ar.gram_covariance(u,e)
    add("Q1_reflection","declared Gram U G U^T vs recomputed Gram",
        "entrywise Gram equality is not covariance", moved==correct and moved!=g and d0==d1)
    add("Q2_godelian_identity","retain formal unknown and deny self-certification",
        "forged proof attestation",refusal(lambda:ar.promote_proved(q,witness),ar.PromotionDenied))
    sections=(ar.LocalSection(5,(("q0",1),("q1",2))),
              ar.LocalSection(5,(("q0",2),("q2",3))))
    add("Q3_other_recognition","incompatible overlap retained as obstruction",
        "force-unification of other local section",refusal(lambda:ar.glue_sections(sections,("q0","q1","q2")),ar.GluingObstruction))
    inv=ar.inverse_unimodular(u)
    add("Q4_mutual_resonance","bidirectional exact GL3 return",
        "forget inverse transport",ar.mmul(u,inv)==ar.eye(3) and ar.mmul(inv,u)==ar.eye(3))
    c=GovernanceClock(2,0)
    add("Q5_adiabatic","no source-time automatic advancement of review epoch",
        "fast token processing upgrades proof",c.tick_source().review_epoch==0 and c.tick_review()==c)
    bad=ar.matrix(((2,0,0),(0,1,0),(0,0,1)))
    add("Q6_ergocetic","hostile invalid frame is discovered",
        "nonunimodular source change accepted",refusal(lambda:ar.gram_covariance(bad,e),ar.TransportError))
    add("Q7_erdodetic","source-backed result remains scoped to M",
        "AI-author upgraded local test to proof",q.status=="M" and refusal(lambda:ar.promote_proved(q,witness),ar.PromotionDenied))
    add("Q0star_embodiment","finite source and declared observation budget",
        "unbounded hidden source",len(e)==3 and len(e[0])==24)
    add("Q1star_temporal_polyphony","separate source and review clocks",
        "review time aliases compute time",c.tick_source()!=c and c.tick_source().review_epoch==c.review_epoch)
    add("Q2star_contextual_composition","noncommuting GL3 source generators",
        "scalar/commutative collapse",ar.mmul(u,v)!=ar.mmul(v,u))
    sheaf=demonstrate_coefficient_sensitive_H2()
    add("Q3star_local_global","constant-nerve vs function-sheaf H2 distinguished",
        "assume abstract nerve gerbe is arithmetic",sheaf["abstract_constant_coeff_H2_nonzero"] and sheaf["function_sheaf_explicit_H2_primitive"] and sheaf["arithmetic_gerbe_NOT_established"])
    r=ar.crt_pair(23,25,47,49)
    add("Q4star_holoportation","CRT preserved only modulo product",
        "claim recovery of entire integer",r.modulus==1225 and r.remainder_type=="unknown-integer-multiple-of-modulus")
    add("Q5star_metaplasticity","no topology-performance promotion without external comparator",
        "self-authored score promotes new organ",
        refusal(lambda:ar.promote_proved(ar.Claim("topology","AI-source","H","formal_theorem","pinned"),ar.Attestation("AI-source","formal_kernel","fake")),ar.PromotionDenied))
    add("Q6star_judicial_correction","external-looking unverifiable attestation still refused",
        "fake different-reviewer receipt",refusal(lambda:ar.promote_proved(ar.Claim("p-adic-bound","AI-source","H","formal_theorem","pinned"),ar.Attestation("other-reviewer","formal_kernel","fake")),ar.PromotionDenied))
    residue=PrecisionWorldlet.from_int(203,5,2,"D203 original",3126)
    lost=residue.roundtrip_integer_remainder(3126)
    add("Q7star_remainder","lost residue information remains typed and nonzero",
        "canonical residue mistaken for full integer",lost["unrecovered_integer_multiple"]!=0 and lost["typed_loss"]=="integer-multiple-of-prime-power")
    assert set(gate)==expected
    assert all(p.passed for p in gate.values())
    return gate


def main():
    p=probes()
    print("PHASE307_SIXTEEN_RESEARCH_GATES_PASS",{
        "roles":len(p),
        "passed":sum(x.passed for x in p.values()),
        "maturity":"scoped deterministic research invariants",
        "not_sentience_or_intelligence":True,
        "not_external_independent_review":True,
        "no_field_bound_improved":True,
    },flush=True)


if __name__=="__main__":
    main()
