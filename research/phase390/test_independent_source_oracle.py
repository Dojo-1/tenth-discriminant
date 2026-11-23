"""Phase390 exact arithmetic regressions of the audit, no external field proof."""
import unittest
from research.phase390.independent_source_oracle import (
    full_gram_chart_test,exact_ellipse_count_at_fourth_root,
    strict_prime_boundary,source_points,maximal_points,chart,
    derivative,trace,gram,det_bareiss,
    local_source_valuation_pilot,predicted_binary_exponent,
    predicted_local_odd_exponent)

class Phase390IndependentSourceTests(unittest.TestCase):
    def test_full_original_integer_gram_in_two_genuinely_distinct_charts(self):
        for D,rho in ((3,4),(7,5),(11,6),(19,7),(43,8),(163,15)):
            with self.subTest(D=D):
                r=full_gram_chart_test(D,rho)
                self.assertTrue(r["same_physical_samples_equal"])
                self.assertTrue(r["enlarged_source_changes_gram"])
                self.assertGreater(r["points_full_order"],r["points_source"])
                self.assertNotEqual(r["original_det"],r["substituted_det"])
        self.assertEqual(full_gram_chart_test(3,4)["original_det"],
                         10368899439910948864)
        self.assertEqual(full_gram_chart_test(163,15)["original_det"],
                         1356200116978473919296852480000)

    def test_index_two_chart_is_not_unimodular_at_two(self):
        # (x,y)->(u,v)=(x-y,2y), determinant=2.
        # T^T [[2,1],[1,(D+1)/2]] T = diag(2,2D) in integers.
        for D in (3,7,11,19,43,163):
            T=((1,-1),(0,2))
            B=((2,1),(1,(D+1)//2))
            m=lambda a,b:[[sum(a[i][k]*b[k][j] for k in range(2))
                         for j in range(2)] for i in range(2)]
            Bt=m(m([[T[k][i] for k in range(2)]for i in range(2)],B),T)
            self.assertEqual(Bt,[[2,0],[0,2*D]])
            self.assertEqual(T[0][0]*T[1][1]-T[0][1]*T[1][0],2)
            # Mod 2 the transition is rank one; mod every odd prime invertible.
            self.assertEqual((T[0][0]*T[1][1]-T[0][1]*T[1][0])%2,0)
            for p in (3,5,7,11):
                self.assertNotEqual(2%p,0)

    def test_complete_maximal_order_sampling_is_a_real_geometry_mutation(self):
        for D,rho in ((3,4),(43,8),(163,15)):
            q=source_points(D,rho)
            transported=set(map(chart,q))
            all_order=set(maximal_points(D,rho))
            self.assertTrue(transported<all_order)
            self.assertTrue(all(v%2==0 for u,v in transported))
            self.assertTrue(any(v%2==1 for u,v in all_order-transported))

    def test_original_held_w_ordinary_derivative_is_not_real_path_derivative(self):
        # derivative_Z(Z*W) with W frozen = W = conj(z).
        # Under real path z->z+t, W->W+t it would be Z+W.
        self.assertEqual(derivative(3,1,1,1,(1,1),"source"),(1,-1))
        self.assertNotEqual(derivative(3,1,1,1,(1,1),"source"),(2,0))
        self.assertEqual(derivative(3,1,1,1,chart((1,1)),"maximal"),
                         chart((1,-1)))

    def test_trace_channel_weights_are_not_replaceable(self):
        for D in (3,11,43):
            self.assertEqual(trace(D,(0,1),(0,1),"source"),2*D)
            self.assertNotEqual(trace(D,(0,1),(0,1),"source"),D)
            self.assertEqual(trace(D,(1,0),(1,0),"maximal"),2)

    def test_exact_302_endpoint_count_is_nonvacuous(self):
        c=exact_ellipse_count_at_fourth_root(302)
        self.assertEqual(c["D"],8318169616)
        self.assertEqual(c["R"],2079542404)
        self.assertEqual(c["S"],83181696)
        self.assertEqual(c["thin_radius"],12119188)
        self.assertEqual(c["original_ellipse_points"],5058469573)
        self.assertEqual(c["interpolation_requirement"],4242266501)
        self.assertEqual(c["strict_margin"],816203072)
        self.assertGreater(c["original_ellipse_points"],c["interpolation_requirement"])

    def test_301_count_can_pass_while_301_scalar_contradiction_fails(self):
        # This is a diagnostic of NON-IMPLICATION: cardinality alone cannot
        # close the arithmetic-plus-analytic proof at 301^4.
        c=exact_ellipse_count_at_fourth_root(301)
        self.assertEqual(c["D"],8208541201)
        self.assertEqual(c["original_ellipse_points"],4992989319)
        self.assertEqual(c["strict_margin"],806633310)
        self.assertGreater(c["strict_margin"],0)

    def test_strict_inert_prime_cutoff_has_actual_split_boundary_witnesses(self):
        for D,p in ((7,2),(11,3),(19,5),(43,11),(67,17),(163,41)):
            b=strict_prime_boundary(D)
            self.assertEqual(b["boundary_prime"],p)
            self.assertTrue(b["boundary_split"])
            self.assertEqual(D,4*p-1)
            # The class-one field D=163 has a principal split prime
            # at p=41: Norm((1+sqrt(-163))/2)=41.
        self.assertEqual(strict_prime_boundary(163)["boundary_prime"],41)

    def test_actual_full_original_gram_odd_binary_valuation_pilot(self):
        # Not a proof of the uniform high-dimensional valuation statement.
        w=local_source_valuation_pilot()
        self.assertEqual(w["Q_cardinality"],87)
        self.assertEqual(w["actual_valuations"],{2:216,3:36,5:21})
        self.assertEqual(w["theorem_required_exponents"],{2:84,3:30,5:10})
        self.assertEqual(predicted_binary_exponent(6,6),84)
        self.assertEqual(predicted_local_odd_exponent(6,6,3),30)
        self.assertEqual(predicted_local_odd_exponent(6,6,5),10)
        self.assertTrue(all(w["actual_valuations"][p]>=w["theorem_required_exponents"][p]
                            for p in (2,3,5)))

    def test_bad_parameters_are_rejected(self):
        with self.assertRaises(AssertionError):
            gram(2,3,2,2,[(0,0)],"source")
        with self.assertRaises(ValueError):
            derivative(3,1,1,1,(1,1),"wrong")

if __name__=="__main__":unittest.main()
