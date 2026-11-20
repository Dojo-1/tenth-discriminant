"""Phase368: structural tests only, not a benchmark or field proof."""
import copy
import unittest
from pathlib import Path
from polybandit import PolyBandit, ContractError, Receipt, dominates, load

M = load(Path(__file__).with_name("manifest.json"))
S = M["frozen_source"]

class Controls(unittest.TestCase):
    def test_declared_worldlets_and_higher_edges(self):
        b = PolyBandit(M)
        self.assertEqual((len(b.worldlets),len(b.arms),len(b.hyperedges)),(8,8,5))
        self.assertFalse("promoted_claims" in b.export())

    def test_refuse_single_clock(self):
        m = copy.deepcopy(M)
        for w in m["worldlets"]: w["clocks"] = ["fast"]
        with self.assertRaises(ContractError): PolyBandit(m)

    def test_refuse_binary_hyperedge(self):
        m = copy.deepcopy(M)
        m["hyperedges"][0]["participants"] = ["logic.prolog","source.original"]
        with self.assertRaises(ContractError): PolyBandit(m)

    def test_refuse_d203_substitution(self):
        m = copy.deepcopy(M)
        m["arms"][2]["source"] = "maximal-order-D203-phase306"
        with self.assertRaises(ContractError): PolyBandit(m)

    def test_refuse_nonzero_remainder_as_exact(self):
        m = copy.deepcopy(M)
        m["arms"][1]["transport"] = "exact"
        with self.assertRaises(ContractError): PolyBandit(m)

    def test_clock_permissions_and_contrast_opt_in(self):
        b = PolyBandit(M)
        fast = {a.id for a in b.eligible(10,phase="fast")}
        review = {a.id for a in b.eligible(10,phase="review")}
        self.assertNotIn("external_field_chart_reconstruction",fast)
        self.assertIn("external_field_chart_reconstruction",review)
        self.assertNotIn("d203_worldlet_contrast",review)
        self.assertIn("d203_worldlet_contrast",
                      {a.id for a in b.eligible(10,phase="review",include_contrast=True)})

    def test_budget_and_initial_coverage(self):
        b = PolyBandit(M)
        self.assertEqual({a.id for a in b.eligible(1)},{"source_anchor_mutation"})
        feasible = b.eligible(4)
        self.assertEqual({b.choose(4).id for _ in range(len(feasible))},
                         {a.id for a in feasible})
        with self.assertRaises(ContractError): b.choose(0)

    def test_vector_not_universal_scalar(self):
        self.assertTrue(dominates((.8,.8,-2),(.7,.7,-3)))
        self.assertFalse(dominates((.9,.2,-2),(.2,.9,-2)))

    def test_reject_unapproved_and_repeated_outcomes(self):
        r = Receipt("fixture-1","prolog_clock_counterworld",S,
                    "matrix_general","fixture",True,False)
        with self.assertRaises(ContractError): PolyBandit(M).observe(r)
        b = PolyBandit(M,{"fixture-1":r})
        b.observe(r)
        self.assertEqual(b.state[r.arm].diagnostic_hits,1)
        with self.assertRaises(ContractError): b.observe(r)
        self.assertNotIn("promoted_claims",b.export())

    def test_reject_bounded_prolog_as_proof(self):
        r = Receipt("bad","prolog_clock_counterworld",S,
                    "matrix_general","prolog_exact",True,True)
        b = PolyBandit(M,{"bad":r})
        with self.assertRaises(ContractError): b.observe(r)

    def test_reject_formal_ci_as_external_field_review(self):
        r = Receipt("ci","external_field_chart_reconstruction",S,
                    "field_301_semantic","lean_kernel",True,False)
        b = PolyBandit(M,{"ci":r})
        with self.assertRaises(ContractError): b.observe(r)

    def test_reject_tampered_receipt(self):
        r = Receipt("good","source_anchor_mutation",S,"source_contract",
                    "fixture",True,False)
        altered = Receipt("good",r.arm,"maximal-order-D203-phase306",r.scope,
                          r.validator,r.diagnostic,r.closure)
        b = PolyBandit(M,{"good":r})
        with self.assertRaises(ContractError): b.observe(altered)
        self.assertEqual(b.state[r.arm].observations,0)

    def test_optimism_recalibrated_by_failure_records(self):
        arm="prolog_clock_counterworld"
        receipts={f"r{i}":Receipt(f"r{i}",arm,S,"matrix_general",
                                   "fixture",False,False) for i in range(30)}
        b=PolyBandit(M,receipts)
        initial=b.objectives(b.arms[arm])[0]
        for r in receipts.values(): b.observe(r)
        self.assertLess(b.objectives(b.arms[arm])[0],initial)
        self.assertEqual(b.state[arm].closure_hits,0)

if __name__=="__main__":
    unittest.main()
