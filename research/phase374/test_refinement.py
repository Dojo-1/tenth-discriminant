"""Phase374 independent differential and source-version controls.

These are *tests*, not a correctness proof of Python itself or a verifier.
Do not modify the frozen Phase368 selector when running the comparisons.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/"research"/"phase368"))
sys.path.insert(0,str(HERE))
from polybandit import PolyBandit
from gen_refinement import render, git_blob_sha, MANIFEST, OUTPUT, PHASES

RAW=MANIFEST.read_bytes()
M=json.loads(RAW)
W={w["id"]:w for w in M["worldlets"]}
A=M["arms"]
BUDGETS=range(10)


def independent_rule(arm,phase,budget,include_human,include_contrast):
    """Policy contract deliberately not imported from PolyBandit.eligible."""
    native=set(W[arm["worldlet"]]["clocks"])
    phase_native={
        "fast":{"fast"},
        "meso":{"fast","meso"},
        "review":{"fast","meso","review"},
    }[phase]
    return (budget>=arm["cost"] and arm["transport"]!="forbidden"
        and (arm["source"]==M["frozen_source"]
             or (include_contrast and arm["purpose"]=="contrast"))
        and (include_human or arm["execution"]!="human")
        and bool(native & phase_native)
        and (arm["execution"]!="human" or phase=="review"))


class ManifestRefinementTests(unittest.TestCase):
    def test_exact_eight_arm_and_three_clock_snapshot(self):
        self.assertEqual(len(A),8)
        self.assertEqual(len({a["id"] for a in A}),8)
        self.assertEqual({v["id"] for v in M["clocks"]},set(PHASES))
        self.assertEqual(git_blob_sha(RAW),"2e0a7e2e77d674bb0ef978785844914f4040a0c8")

    def test_certificate_regenerates_exactly(self):
        self.assertTrue(OUTPUT.is_file())
        self.assertEqual(render(M,RAW),OUTPUT.read_text(encoding="utf-8"))

    def test_exhaustive_960_source_python_predicate_comparisons(self):
        oracle=PolyBandit(M)
        checks=0
        for phase in PHASES:
            for budget in BUDGETS:
                for include_human in (False,True):
                    for include_contrast in (False,True):
                        result={x.id for x in oracle.eligible(
                            budget,include_human=include_human,
                            phase=phase,include_contrast=include_contrast)}
                        expected={a["id"] for a in A if independent_rule(
                            a,phase,budget,include_human,include_contrast)}
                        self.assertEqual(result,expected,
                           (phase,budget,include_human,include_contrast))
                        checks+=len(A)
        self.assertEqual(checks,960)

    def test_source_native_meso_is_not_fast(self):
        oracle=PolyBandit(M)
        self.assertNotIn("source_anchor_mutation",
            {a.id for a in oracle.eligible(9,phase="fast")})
        self.assertIn("source_anchor_mutation",
            {a.id for a in oracle.eligible(9,phase="meso")})

    def test_fast_prolog_native_is_admitted_during_meso(self):
        oracle=PolyBandit(M)
        self.assertIn("prolog_clock_counterworld",
            {a.id for a in oracle.eligible(9,phase="meso")})

    def test_d203_contrast_requires_explicit_optin(self):
        oracle=PolyBandit(M)
        default={a.id for a in oracle.eligible(9,phase="meso")}
        contrast={a.id for a in oracle.eligible(9,phase="meso",
                                              include_contrast=True)}
        self.assertNotIn("d203_worldlet_contrast",default)
        self.assertIn("d203_worldlet_contrast",contrast)

    def test_human_review_requires_review_phase(self):
        oracle=PolyBandit(M)
        for phase in ("fast","meso"):
            self.assertNotIn("external_field_chart_reconstruction",
                {a.id for a in oracle.eligible(9,phase=phase)})
        self.assertIn("external_field_chart_reconstruction",
            {a.id for a in oracle.eligible(9,phase="review")})
        self.assertNotIn("external_field_chart_reconstruction",
            {a.id for a in oracle.eligible(9,phase="review",
                                          include_human=False)})

    def test_budget_saturates_after_max_cost(self):
        oracle=PolyBandit(M)
        maxcost=max(a["cost"] for a in A)
        self.assertEqual(maxcost,8)
        for phase in PHASES:
            for human in (False,True):
                for contrast in (False,True):
                    ref={a.id for a in oracle.eligible(maxcost,include_human=human,
                             include_contrast=contrast,phase=phase)}
                    for budget in (9,12,99,10000):
                        self.assertEqual(ref,{a.id for a in oracle.eligible(
                            budget,phase=phase,include_human=human,
                            include_contrast=contrast)})

    def test_manifest_clock_mutation_invalidates_certificate(self):
        changed=copy.deepcopy(M)
        next(w for w in changed["worldlets"] if w["id"]=="source.original")["clocks"]=["fast"]
        data=json.dumps(changed,indent=2).encode("utf-8")
        self.assertNotEqual(render(changed,data),OUTPUT.read_text(encoding="utf-8"))

    def test_manifest_cost_mutation_invalidates_certificate(self):
        changed=copy.deepcopy(M)
        next(a for a in changed["arms"] if a["id"]=="source_anchor_mutation")["cost"]=2
        data=json.dumps(changed,indent=2).encode("utf-8")
        self.assertNotEqual(render(changed,data),OUTPUT.read_text(encoding="utf-8"))

    def test_reordered_arm_list_invalidates_certificate(self):
        changed=copy.deepcopy(M)
        changed["arms"].reverse()
        data=json.dumps(changed,indent=2).encode("utf-8")
        self.assertNotEqual(render(changed,data),OUTPUT.read_text(encoding="utf-8"))

    def test_no_claim_promotion_or_field_semantics_in_certificate(self):
        rendered=OUTPUT.read_text(encoding="utf-8")
        self.assertNotIn("theorem classNumber",rendered)
        self.assertNotIn("301^4 is verified",rendered)
        self.assertIn("NOT a proof of arbitrary Python execution",rendered)

if __name__=="__main__":
    unittest.main()
