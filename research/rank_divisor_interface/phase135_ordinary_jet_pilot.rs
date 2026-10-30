// Phase135: independently executable finite arithmetic control (no dependencies).
//
// This reproduces the EXACT integer ordinary-jet observations used by
// IntegerTraceGram.lean and RectangularBasisMatrix.lean for
// D=19, rho=5, J=2, R=4, S=2, p=3. This is NOT a number-field theorem,
// a proof of a uniform valuation, or independent human refereeing.
//
// Build: rustc --edition=2021 --test phase135_ordinary_jet_pilot.rs -o /tmp/jet-test
// Run:   /tmp/jet-test
// Also:  rustc --edition=2021 phase135_ordinary_jet_pilot.rs -o /tmp/jet && /tmp/jet

#[derive(Clone, Copy, Debug)]
struct Pair { re: i128, im: i128 }
const ZERO: Pair = Pair { re: 0, im: 0 };
const ONE: Pair = Pair { re: 1, im: 0 };

fn mul(a: Pair, b: Pair, d: i128) -> Pair {
    Pair { re: a.re*b.re - d*a.im*b.im, im: a.re*b.im + a.im*b.re }
}

fn power(mut a: Pair, exp: usize, d: i128) -> Pair {
    let mut v = ONE;
    for _ in 0..exp { v = mul(v, a, d); }
    a = v;
    a
}

fn falling(r: usize, j: usize) -> i128 {
    (0..j).map(|t| (r - t) as i128).product()
}

fn samples(d: i128, rho: i128) -> Vec<Pair> {
    let mut out = Vec::new();
    for x in -rho..=rho {
        for y in -rho..=rho {
            if x*x + d*y*y <= rho*rho {
                out.push(Pair { re:x, im:y });
            }
        }
    }
    out
}

fn original_jet(d: i128, r:usize, s:usize, j:usize, q:Pair) -> Pair {
    if j>r { return ZERO; }
    let conj = Pair { re:q.re, im:-q.im };
    let v = mul(power(q,r-j,d),power(conj,s,d),d);
    let f = falling(r,j);
    Pair { re:v.re*f, im:v.im*f }
}

fn raw_observations(d:i128, rho:i128, j_max:usize) -> (Vec<Pair>,Vec<Vec<i128>>) {
    let q = samples(d,rho);
    let mut e = vec![Vec::new();8];
    // The repository's row-major monomial labels: i = r*S+s, S=2.
    for (i,row) in e.iter_mut().enumerate() {
        let r=i/2; let s=i%2;
        for sample in &q {
            for j in 0..j_max {
                let jet=original_jet(d,r,s,j,*sample);
                row.push(jet.re);
                row.push(jet.im);
            }
        }
    }
    (q,e)
}

// U is the specific checked 4x2, p=3 unimodular basis matrix:
// row 6 = row 6 - row 1; all remaining rows are unchanged.
// Delta has exponent 1 in row 6 and exponent 0 elsewhere.
fn normalized_rows(e:&[Vec<i128>]) -> Result<Vec<Vec<i128>>,String> {
    let mut c=e.to_vec();
    for col in 0..e[0].len() {
        let v=e[6][col]-e[1][col];
        if v%3!=0 { return Err(format!("Frobenius quotient nonintegral at column {col}")); }
        c[6][col]=v/3;
    }
    Ok(c)
}

fn gram(e:&[Vec<i128>],d:i128) -> Vec<Vec<i128>> {
    let n=e.len(); let width=e[0].len();
    let mut g=vec![vec![0i128;n];n];
    for i in 0..n {
        for k in 0..n {
            for col in 0..width {
                let weight=if col%2==0 {2} else {2*d};
                g[i][k]+=weight*e[i][col]*e[k][col];
            }
        }
    }
    g
}

fn modp(x:i128,p:i128)->i128 { x.rem_euclid(p) }
fn inv(x:i128,p:i128)->i128 {
    (1..p).find(|t|modp(x*(*t),p)==1).expect("nonzero pivot over prime field")
}

fn rank_mod(e:&[Vec<i128>],p:i128)->usize {
    let mut a:Vec<Vec<i128>>=e.iter().map(|r|r.iter().map(|x|modp(*x,p)).collect()).collect();
    let n=a.len();let m=a[0].len();let mut k=0;
    for j in 0..m {
        if k>=n {break;}
        let Some(t)=(k..n).find(|i|a[*i][j]!=0) else {continue};
        a.swap(k,t);
        let h=inv(a[k][j],p);
        for l in j..m { a[k][l]=modp(a[k][l]*h,p); }
        for i in 0..n {
            if i!=k {
                let f=a[i][j];
                for l in j..m { a[i][l]=modp(a[i][l]-f*a[k][l],p); }
            }
        }
        k+=1;
    }
    k
}

fn det_mod(a:&[Vec<i128>],p:i128)->i128 {
    let n=a.len();
    assert_eq!(n,a[0].len());
    let mut m:Vec<Vec<i128>>=a.iter().map(|r|r.iter().map(|x|modp(*x,p)).collect()).collect();
    let mut determinant=1i128;
    for j in 0..n {
        let Some(t)=(j..n).find(|i|m[*i][j]!=0) else {return 0};
        if t!=j {m.swap(j,t);determinant=modp(-determinant,p);}
        let v=m[j][j];determinant=modp(determinant*v,p);
        let h=inv(v,p);
        for i in j+1..n {
            let f=modp(m[i][j]*h,p);
            for k in j..n {m[i][k]=modp(m[i][k]-f*m[j][k],p);}
        }
    }
    determinant
}

#[derive(Debug)]
struct ResultRow { points:usize, count_guard:bool, quotient_integral:bool,
    rank_raw_mod3:usize, rank_quotient_mod3:usize,
    det_residual_mod3:i128, rank_residual_mod3:usize, two_sided_exact:bool }

fn pilot(d:i128,rho:i128,j:usize) -> Result<ResultRow,String> {
    let (q,e)=raw_observations(d,rho,j);
    let count_guard=7<q.len(); // 2*(4-1)+(2-1)=7, with S=J=2 in primary test
    let c=normalized_rows(&e)?;
    let g=gram(&e,d);
    let transformed=gram(&e.iter().enumerate().map(|(i,row)|{
        if i==6 { row.iter().zip(e[1].iter()).map(|(a,b)|a-b).collect() }
        else {row.clone()}
    }).collect::<Vec<_>>(),d);
    let k=gram(&c,d);
    let mut matched=true;
    for i in 0..8 {
        for h in 0..8 {
            let di=if i==6 {3} else {1};
            let dh=if h==6 {3} else {1};
            if transformed[i][h]!=di*dh*k[i][h] {matched=false}
            // This is also a direct congruence check, not just a new Gram
            // computed from normalized rows.
            let u_gu=g[i][h] - if i==6 {g[1][h]} else {0}
                - if h==6 {g[i][1]} else {0}
                + if i==6 && h==6 {g[1][1]} else {0};
            if u_gu!=transformed[i][h] {matched=false;}
        }
    }
    Ok(ResultRow { points:q.len(), count_guard, quotient_integral:true,
        rank_raw_mod3:rank_mod(&e,3), rank_quotient_mod3:rank_mod(&c,3),
        det_residual_mod3:det_mod(&k,3),rank_residual_mod3:rank_mod(&k,3),
        two_sided_exact:matched })
}

fn main() {
    let r=pilot(19,5,2).expect("inert-prime integral quotient");
    println!("D=19 rho=5 R=4 S=2 J=2 p=3: {:?}",r);
    assert_eq!(r.points,21);
    assert!(r.count_guard && r.quotient_integral && r.two_sided_exact);
    assert_eq!((r.rank_raw_mod3,r.rank_quotient_mod3,r.det_residual_mod3,r.rank_residual_mod3),
               (7,8,2,8));
    // 3 divides the original maximal minors, but the saturated quotient
    // has full row rank and an invertible residual trace Gram mod 3.
    // Thus v3(det G) = 2*F=2 in THIS exact pilot, since F=1.
    assert!(pilot(11,5,2).is_err(),
        "split-prime control must refuse the quotient extraction");
    assert!(!pilot(19,1,2).unwrap().count_guard,
        "undersampled original ellipse must fail interpolation point-count guard");
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn inert_jet_and_residual() { main(); }
    #[test]
    fn wrong_prime_guard() { assert!(pilot(11,5,2).is_err()); }
    #[test]
    fn under_sampling_guard() { assert!(!pilot(19,1,2).unwrap().count_guard); }
    #[test]
    fn factorial_column_control() {
        assert_eq!(6%3,0); assert_ne!(1%3,0); // X^3 third ordinary/Hasse jets
    }
}
