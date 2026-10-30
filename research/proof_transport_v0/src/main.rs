fn main() {
    match tenth_proof_transport::pilot() {
        Ok(p) => {
            println!("fixture=D19 p3 R5 S2 J2 rho2; finite exact-arithmetic check, not a new proof");
            println!("Q={} F={} p^(2F)={} det={} quotient={}", p.n_points, p.f, p.p2f, p.det, p.quotient);
            println!("(T U)[8,0]={}; (U T)[8,0]={}; rank_mod3={}", p.diff_tu, p.diff_ut, p.mod_rank);
            println!("Hadamard diagonal products: G={} T={} TU={} UT={}", p.diag_original, p.diag_radial, p.diag_tu, p.diag_ut);
            println!("evidence=M on this bounded pilot only; no cutoff claim");
        }
        Err(e) => { eprintln!("pilot FAILED: {e}"); std::process::exit(1); }
    }
}
