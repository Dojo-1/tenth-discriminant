#!/usr/bin/env python3
"""Phase316-C: globally unrealizable norm164 ray classes despite local norm125."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import realization_obstruction as o

class ExactRealizationObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=o.first_global_realization_obstruction()

    def test_first_exact_global_fibre_is_norm164_not_small_rational_region(self):
        x=self.data
        self.assertEqual(x["first_changed_exact_norm"],164)
        self.assertEqual(x["exact_original_norm164_integer_solutions"],
                         [(-1,-1),(-1,1),(1,-1),(1,1)])
        self.assertEqual(x["signed_actual_ideals_norm164"],2)
        self.assertEqual(x["signed_synthetic_ideals_norm164"],2)

    def test_both_synthetic_tags_have_correct_local_norm_but_no_global_generator(self):
        x=self.data
        self.assertTrue(x["all_synthetic_norm164_tags_OUTSIDE_actual_exact_fibre"])
        rays=x["synthetic_norm164_rays_locally_realizable_at_conductor250"]
        self.assertEqual(len(rays),2)
        for r in rays:
            self.assertEqual(r["local_norm_mod125"],164%125)
            self.assertFalse(r["actual_exact_norm164_integer_generator_exists"])
            self.assertTrue(all(n%2==0 for n in
                         r["conductor2_even_coordinate_integral_lift"]))

    def test_exact_original_Gram_change_is_reconciled_to_norm_fibre(self):
        x=self.data
        self.assertEqual(x["native_integer_order_Q"],109)
        self.assertTrue(x["same_original_primitive_G_mod5"])
        self.assertEqual(x["changed_primitive_Gram_cells_mod25"],363)
        self.assertEqual(x["changed_Gram_entry_first"],[0,26,15])
        self.assertTrue(x["all_Gram_changes_explained_by_norm164_fibre_only"])
        self.assertEqual(x["other_original_norm_shells_changed_if_any"],[])

    def test_strict_evidence_boundary(self):
        self.assertTrue(self.data["global_realization_obstruction_not_deduced_from_local_norm_only"])
        self.assertTrue(self.data["no_new_field_or_cutoff_claim"])

if __name__=="__main__":
    unittest.main(verbosity=2)
