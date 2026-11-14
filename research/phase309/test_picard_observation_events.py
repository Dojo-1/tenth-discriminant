#!/usr/bin/env python3
"""Phase309-C controls for exact original observation-filtration Picard events."""
import unittest
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import picard_observation_events as p
import original_source_picard as source


class PicardObservationEventsTests(unittest.TestCase):
    def test_original_observation_ideal_history(self):
        data=p.original_source_event_chain()
        log=data["event_log"]
        self.assertEqual([x["num_observations"] for x in log],[2,3,4])
        self.assertEqual([x["maximal_minor_Z_index_Norm"] for x in log],[9,3,1])
        self.assertEqual(data["Picard_event_class_orders"],[1,4,1])
        self.assertEqual([x["original_restricted_integer_Gram_det"] for x in log],
                         [36,671,895])
        self.assertEqual(data["different_original_trace_Gram_v3"],[2,0,0])

    def test_strict_fractional_ideal_shrinkage(self):
        ordered=((0,0),(3,0),(0,1),(1,0))
        self.assertTrue(p.coeff_allowed((1,0),3,ordered[:2],203))
        self.assertFalse(p.coeff_allowed((1,0),3,ordered[:3],203))
        self.assertTrue(p.coeff_allowed((1,-1),3,ordered[:3],203))
        self.assertFalse(p.coeff_allowed((1,-1),3,ordered[:4],203))

    def test_existing_source_points_and_no_new_global_bound(self):
        ps,q=source.patch_source(203,3,0)
        self.assertTrue(all(z in q for z in ((0,0),(3,0),(0,1),(1,0))))
        data=p.original_source_event_chain()
        self.assertTrue(data["all_original_observations_genuine"])
        self.assertTrue(data["no_full_100_row_Picard_persistence"])
        self.assertTrue(data["no_field_bound_improved"])

    def test_wrong_fractional_coefficient_type_rejected(self):
        with self.assertRaises(ValueError):
            p.coeff_allowed((1,0),0,((0,0),(3,0)),203)


if __name__=="__main__":
    unittest.main(verbosity=2)
