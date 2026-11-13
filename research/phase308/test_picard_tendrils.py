#!/usr/bin/env python3
"""Phase308: exact hostile controls of arithmetic Picard tendrils."""
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(HERE.parent/"phase306"))

import picard_tendrils as p
import arithmetic_fabric as ar


class PicardTendrilTests(unittest.TestCase):
    def test_actual_d203_fourth_power_generator_and_index(self):
        cert=p.alpha_fourth_power_certificate()
        self.assertEqual(cert["class_exact_order"],4)
        self.assertEqual(cert["ideal_powers_Z_lattice_indices"],[3,9,27,81])
        self.assertEqual(cert["power4_norm"],81)
        self.assertEqual(cert["all_five_exact_ideal_generator_quotients"],
            [(-5,-1),(17,-2),(34,5),(-85,13),(-221,-24)])

    def test_coherent_hensel_tower_and_wrong_branch_rejection(self):
        x=p.ideal_power_hensel_certificate(203,3,0,5)
        self.assertEqual([t.root for t in x],[0,6,6,6,87])
        for k in range(1,5):
            self.assertEqual(x[k].reduce(k),x[k-1])
        self.assertEqual(x[1].residue((3,0)),3)
        self.assertEqual(x[3].residue((-6,1)),0)
        other=p.HenselWorldlet(203,3,1,1)
        self.assertNotEqual(other.residue((-6,1)),0)
        with self.assertRaises(p.InvalidTransport):
            p.HenselWorldlet(203,3,2,0)
        with self.assertRaises(p.InvalidTransport):
            x[0].reduce(2)

    def test_real_two_open_picard_cocycle_not_global_unit(self):
        c=p.nontrivial_picard_cocycle_d203()
        self.assertEqual(c["one_cocycle_transition"],3)
        self.assertEqual(c["fourfold_transition"],81)
        self.assertTrue(c["one_cocycle_nontrivial_by_norm_obstruction"])
        self.assertTrue(c["fourfold_transition_is_explicit_coboundary"])
        self.assertNotEqual(p.norm((3,0),203),1)
        self.assertEqual(p.PicardTendril(203,3).overlap_inverse_numerator(),-17)
        self.assertEqual(p.mul((0,1),(-1,1),203),(-51,0))

    def test_principal_boundary_has_coboundary(self):
        c=p.principal_boundary_d163()
        self.assertEqual(c["transition"],41)
        self.assertEqual(c["principal_norm"],41)
        self.assertTrue(c["not_a_nonprincipal_class"])
        self.assertEqual(p.mul((0,1),(-1,1),163),(-41,0))

    def test_reduced_form_class_number_cross_control(self):
        self.assertEqual(p.reduced_positive_forms(203),
            ((1,1,51),(3,-1,17),(3,1,17),(7,7,9)))
        self.assertEqual(p.reduced_positive_forms(163),((1,1,41),))

    def test_determinant_forgets_labels_without_replacing_source(self):
        for n in (4,8,100):
            x=p.twisted_module_class(n)
            self.assertTrue(x["determinant_line_trivial"])
            self.assertTrue(x["abstract_module_free_BY_STEINITZ"])
            self.assertTrue(x["every_named_line_summand_nonprincipal"])
            self.assertTrue(x["ORIGINAL_integer_source_is_UNCHANGED"])
        for n in (1,2,3,5,99):
            self.assertFalse(p.twisted_module_class(n)["determinant_line_trivial"])
        with self.assertRaises(p.InvalidTransport):
            p.twisted_module_class(0)

    def test_wrong_localization_and_fractional_transport_refused(self):
        with self.assertRaises(p.InvalidTransport):
            p.PicardTendril(203,5)
        with self.assertRaises(p.InvalidTransport):
            p.divide_by_element_integrally((1,0),(-6,1),203)
        with self.assertRaises(p.InvalidTransport):
            p.HenselWorldlet(203,3,2,3) # f(3) not 0 mod 9

    def test_original_D203_jet_gram_is_invariant_to_new_twisted_probe(self):
        e=ar.exact_original_jet_rows(ar.actual_d203_points(),
                                     degrees=(0,1,2),jets=2,d=203)
        original=ar.trace_gram(e,203)
        _=(p.alpha_fourth_power_certificate(),
           p.nontrivial_picard_cocycle_d203(),
           p.twisted_module_class(100))
        self.assertEqual(original,ar.trace_gram(e,203))
        self.assertEqual(ar.det(original),ar.det(ar.trace_gram(e,203)))


if __name__=="__main__":
    unittest.main(verbosity=2)
