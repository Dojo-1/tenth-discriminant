#!/usr/bin/env python3
"""Phase328 tapestry: exact finite cross-fiber group relations + evidence gates.

This module does not equate contexts merely because they share a
notation. Its small semidirect group is a separate, explicitly typed
toy model. The actual three-field Frobenius computations remain in
phase325; no induced action of those ray groups on the original Gram
is asserted.

The toy group is G=C4 x C6 with sigma(a,b)=(-a,b).
The semidirect product H=G rtimes_sigma C2 distinguishes the
rational Frobenius coset from its (norm-twisted) square.
The quaternion Q8 factor commutes with H *externally*
inside the signed one-generator tensor algebra; this provides
a mathematical tapestry of relations without altering source jets.
"""
from __future__ import annotations

from dataclasses import dataclass

from stabilized_return import (
    Q8, H_ONE, H_NEG_ONE, quaternion_product, identity,
    original_integer_trace_gram, verify_stable_return,
)

G = tuple((a,b) for a in range(4) for b in range(6))
GroupElement = tuple[tuple[int,int], int]
H = tuple((g,e) for g in G for e in (0,1))
HE: GroupElement = ((0,0),0)


def g_add(x:tuple[int,int],y:tuple[int,int])->tuple[int,int]:
    return ((x[0]+y[0])%4,(x[1]+y[1])%6)


def sigma(g:tuple[int,int])->tuple[int,int]:
    return ((-g[0])%4,g[1])


def h_mul(x:GroupElement,y:GroupElement)->GroupElement:
    (g,e),(k,f)=x,y
    return (g_add(g,sigma(k) if e else k),(e+f)%2)


def tensor_multiply(
    x:tuple[tuple[int,int,int,int],GroupElement],
    y:tuple[tuple[int,int,int,int],GroupElement],
)->tuple[tuple[int,int,int,int],GroupElement]:
    return (quaternion_product(x[0],y[0]),h_mul(x[1],y[1]))


def h_conjugate(a:GroupElement,b:GroupElement)->GroupElement:
    """Conjugate b by a using the finite semidirect group inverse."""
    (g,e)=a
    # inverse of g*sigma^e is sigma^e(-g)*sigma^e.
    ginv=((-g[0])%4,(-g[1])%6)
    ainv=((sigma(ginv) if e else ginv),e)
    return h_mul(h_mul(a,b),ainv)


def frobenius_square_from_inert_lift(g:tuple[int,int])->GroupElement:
    return h_mul((g,1),(g,1))


@dataclass(frozen=True)
class EvidenceNode:
    name: str
    status: str     # algebra, finite, open, semantic, rejected
    provenance: str


@dataclass(frozen=True)
class TypedBridge:
    source: str
    target: str
    kind: str       # exact, conditional, forgetful, blocked
    detail: str


NODES = (
    EvidenceNode("F1_signed_monoid","semantic","research/phase327/README.md"),
    EvidenceNode("integral_quaternion_ring","algebra","research/phase327/README.md"),
    EvidenceNode("coefficient_characteristic_2","finite","research/phase327/test_interleaved_f1_prime.py"),
    EvidenceNode("coefficient_characteristic_7","finite","research/phase327/test_interleaved_f1_prime.py"),
    EvidenceNode("ray_class_groups","finite","research/phase321/README.md"),
    EvidenceNode("exact_conductor_characters","finite","research/phase322/PHASE322_RESULTS.md"),
    EvidenceNode("norm_twisted_representations","finite","research/phase324/README.md"),
    EvidenceNode("rational_frobenius_classes","finite","research/phase325/README.md"),
    EvidenceNode("original_integer_jet_gram","algebra","lean/TenthDiscriminant/IntegerTraceGram.lean"),
    EvidenceNode("stabilized_quaternionic_jet","algebra","research/phase328/stabilized_return.py"),
    EvidenceNode("integral_moving_gram_return","finite","research/phase328/test_stabilized_return.py"),
    EvidenceNode("joint_original_binary_jet_factor","open","lean/TenthDiscriminant/BinaryNullBidirectionalBasisMatrix.lean"),
    EvidenceNode("315_odd_prime_log_bridge","open","lean/TenthDiscriminant/Phase323OddPrimeProduct.lean"),
    EvidenceNode("315_analytic_upper_and_field_bridge","open","lean/TenthDiscriminant/Phase323ThinUpper315.lean"),
    EvidenceNode("315_field_uniform_bound","open","research/phase327/README.md"),
    EvidenceNode("integral_ray_action_original_jet","open","research/phase324/README.md"),
    EvidenceNode("global_one_element_gluing","open","research/phase327/README.md"),
)

EDGES = (
    TypedBridge("F1_signed_monoid","integral_quaternion_ring","conditional",
                "Proposed signed F1-prime presentation, not a conventional field"),
    TypedBridge("integral_quaternion_ring","coefficient_characteristic_2","forgetful",
                "Reduction is exact but identifies +1 with -1"),
    TypedBridge("integral_quaternion_ring","coefficient_characteristic_7","exact",
                "Coefficient reduction modulo seven preserves signed products"),
    TypedBridge("ray_class_groups","exact_conductor_characters","exact",
                "Finite group duality with rational character projectors"),
    TypedBridge("ray_class_groups","norm_twisted_representations","exact",
                "Semidirect product conjugation uses norm twist"),
    TypedBridge("norm_twisted_representations","rational_frobenius_classes","conditional",
                "Class-field interpretation and unramified arithmetic Artin map"),
    TypedBridge("rational_frobenius_classes","integral_quaternion_ring","exact",
                "External tensor factor commutes with quaternionic coefficient factor"),
    TypedBridge("original_integer_jet_gram","stabilized_quaternionic_jet","exact",
                "Integral direct-summand embedding into four copies"),
    TypedBridge("stabilized_quaternionic_jet","integral_moving_gram_return","exact",
                "Moving metric returns original B and determinant after projection"),
    TypedBridge("integral_moving_gram_return","original_integer_jet_gram","exact",
                "Pi_u Iota_u=identity and Iota_u^T B_u Iota_u=B"),
    TypedBridge("coefficient_characteristic_2","original_integer_jet_gram","blocked",
                "Reduced nilpotence cannot increase original integer valuation"),
    TypedBridge("coefficient_characteristic_7","original_integer_jet_gram","blocked",
                "Modular M2 action does not produce a rational quaternion action"),
    TypedBridge("norm_twisted_representations","integral_ray_action_original_jet","blocked",
                "No source-preserving integral action of ray class group on ordinary-Z jets"),
    TypedBridge("integral_moving_gram_return","315_field_uniform_bound","blocked",
                "Gauge transport is determinant equality, not new divisibility"),
    TypedBridge("integral_ray_action_original_jet","315_field_uniform_bound","conditional",
                "Would require an actual source-Jet valuation theorem"),
    TypedBridge("joint_original_binary_jet_factor","315_field_uniform_bound","conditional",
                "Joint binary 2-adic original jet theorem remains needed"),
    TypedBridge("315_odd_prime_log_bridge","315_field_uniform_bound","conditional",
                "Odd-prime logarithmic mass transport remains needed"),
    TypedBridge("315_analytic_upper_and_field_bridge","315_field_uniform_bound","conditional",
                "Same-Gram upper and actual-field synthesis remain needed"),
    TypedBridge("integral_moving_gram_return","global_one_element_gluing","conditional",
                "Local source retractions do not supply sheaf descent or a global generator"),
)


REQUIRED_315 = frozenset({
    "joint_original_binary_jet_factor",
    "315_odd_prime_log_bridge",
    "315_analytic_upper_and_field_bridge",
})


def validate_tapestry() -> None:
    nodes={n.name:n for n in NODES}
    assert len(nodes)==len(NODES)
    assert all(n.status in {"algebra","finite","open","semantic","rejected"}
               for n in NODES)
    assert all(bridge.source in nodes and bridge.target in nodes
               and bridge.kind in {"exact","conditional","forgetful","blocked"}
               for bridge in EDGES)
    assert all(nodes[name].status=="open" for name in REQUIRED_315)
    assert nodes["315_field_uniform_bound"].status=="open"
    assert any(edge.kind=="blocked" and edge.target=="315_field_uniform_bound"
               for edge in EDGES)
    assert any(edge.kind=="forgetful" for edge in EDGES)


def eligible_to_claim_315(evidence:dict[str,bool])->bool:
    """Safety gate: each required independent proof obligation."""
    return all(evidence.get(name,False) for name in REQUIRED_315)


def sample_tapestry() -> dict:
    """Small source-exact intersection; actual ray groups are NOT inferred."""
    validate_tapestry()
    B = original_integer_trace_gram(
        ((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1)),
        D=7,J=2,R=2,S=2)
    frame = verify_stable_return(B,(0,1,0,0))
    g=(1,1)
    f=(g,1)
    square=frobenius_square_from_inert_lift(g)
    assert square==(g_add(g,sigma(g)),0)==((0,2),0)
    assert square!=HE
    assert h_conjugate((G[7],0),square)==square
    # External quaternion and toy H actions commute exactly.
    u=(0,1,0,0)
    one=(H_ONE,HE)
    left=(u,HE)
    frob=(H_ONE,f)
    assert tensor_multiply(left,frob)==tensor_multiply(frob,left)
    return {
        "phase":"328",
        "toy_semidirect_order":len(H),
        "toy_inert_frob_square":square,
        "source_D":7,
        "source_dimension":len(B),
        "original_determinant":frame["det_source"],
        "stabilized_moving_determinant":frame["det_moving"],
        "tensor_actions_commute":True,
        "claimed_315_bound":eligible_to_claim_315({}),
    }


if __name__=="__main__":
    import json
    print("PHASE328_TYPED_TAPESTRY",json.dumps(sample_tapestry(),sort_keys=True))
