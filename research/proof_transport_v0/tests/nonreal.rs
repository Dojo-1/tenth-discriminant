//! Regression for the *nonreal* observation fiber missing from the original pilot.
//! These are known-answer/metamorphic tests, not independent mathematical evidence.
use tenth_proof_transport::{
    arithmetic_frame, ellipse_points, gram, inert_nonsquare, normalized_integer_jets,
    observation_matrix, radial_frame, Check,
};

#[test]
fn full_nonreal_ellipse_exercises_metric_and_point_count_guard() -> Check<()> {
    let (d, r, s, j, p) = (1i128, 4usize, 2usize, 2usize, 3usize);
    assert!(inert_nonsquare(d, p)); // -1 is nonsquare modulo 3.
    let q = ellipse_points(d, 2)?;
    assert_eq!(q.len(), 13);
    assert!(2 * (r - 1) + (s - 1) < q.len());
    assert!(q.iter().any(|z| z.im != 0));

    let e = observation_matrix(d, r, s, j, &q)?;
    assert!((0..e.rows).any(|i| (1..e.cols).step_by(2).any(|k| e.at(i, k) != 0)));
    let g = gram(&e, d)?;
    let det = g.determinant()?;
    assert_eq!(det, 2690908182187868160);
    assert!(det > 0);
    // Keep the same actual observations but corrupt the imaginary-coordinate weight:
    // this must NOT be an unnoticed change of representation.
    assert_ne!(gram(&e, 2)?, g);

    let u = arithmetic_frame(r, s, p)?;
    let t = radial_frame(r, s, 1)?;
    let ue = u.times(&e)?;
    let (delta, ehat, f) = normalized_integer_jets(&ue, r, s, p)?;
    assert_eq!(f, 1);
    assert_eq!(u.congruence(&g)?, delta.congruence(&gram(&ehat, d)?)?);
    assert_eq!(u.congruence(&g)?, gram(&ue, d)?);
    assert_eq!(t.congruence(&g)?, gram(&t.times(&e)?, d)?);

    for frame in [&u, &t, &t.times(&u)?, &u.times(&t)?] {
        let h = frame.congruence(&g)?;
        assert_eq!(h.determinant()?, det);
        assert_eq!(h.rank_mod_prime(p as i128)?, g.rank_mod_prime(p as i128)?);
    }
    assert_eq!(det % 9, 0);
    Ok(())
}

#[test]
fn nonreal_split_prime_rejects_integer_quotient() -> Check<()> {
    let (d, r, s, j, p) = (2i128, 4usize, 2usize, 2usize, 3usize);
    let q = ellipse_points(d, 2)?;
    assert!(q.iter().any(|z| z.im != 0));
    assert!(!inert_nonsquare(d, p)); // -2 is a square modulo 3.
    let e = observation_matrix(d, r, s, j, &q)?;
    let ue = arithmetic_frame(r, s, p)?.times(&e)?;
    assert!(normalized_integer_jets(&ue, r, s, p).is_err());
    Ok(())
}
