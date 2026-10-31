// Phase137: integer Chebyshev-like moving frame on the EXACT same ordinary jets.
//
// Experiment: D=19, rho=5, R=8, S=J=4, 21 original ellipse nodes.
// Controlled test of the whole 32-row trace-Gram, not a discriminant bound.
// No external crates: rustc --edition=2021 --test phase137_chebyshev_frame.rs
//
// Two genuinely different implementations of ordinary derivatives:
// (1) expansion into original Z^r W^s monomials; (2) Leibniz + derivative
//     of the one-variable recurrence polynomial in u=ZW.
//
// The integer unipotent frame is compared entrywise on ALL columns, then
// its Gram is compared as U G U^T with the unchanged factor-two trace B.

const D: i128 = 19;
const RHO: i128 = 5;
const R: usize = 8;
const S: usize = 4;
const J: usize = 4;
const N: usize = R * S;

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
struct Q { a: i128, b: i128 }
impl Q {
    fn zero() -> Self { Self { a: 0, b: 0 } }
    fn one() -> Self { Self { a: 1, b: 0 } }
    fn conj(self) -> Self { Self { a: self.a, b: -self.b } }
    fn mul(self, x: Self) -> Self {
        Self { a: self.a*x.a - D*self.b*x.b, b: self.a*x.b + self.b*x.a }
    }
    fn scale(self, c: i128) -> Self { Self { a: self.a*c, b: self.b*c } }
    fn add(self, x: Self) -> Self { Self { a: self.a+x.a, b: self.b+x.b } }
    fn pow(self, n: usize) -> Self {
        let mut z = Self::one();
        for _ in 0..n { z = z.mul(self); }
        z
    }
    fn normsq(self) -> i128 { self.a*self.a + D*self.b*self.b }
}

fn points() -> Vec<Q> {
    let mut q = Vec::new();
    for x in -RHO..=RHO {
        for y in -RHO..=RHO {
            if x*x + D*y*y <= RHO*RHO {
                q.push(Q { a: x, b: y });
            }
        }
    }
    q
}

fn fall(n: usize, j: usize) -> i128 {
    if j>n { return 0; }
    (0..j).map(|k|(n-k) as i128).product()
}
fn choose(n: usize, k: usize) -> i128 {
    if k>n {return 0;}
    let k = k.min(n-k);
    let mut a=1i128;
    for t in 0..k {a=a*((n-t) as i128)/((t+1) as i128);}
    a
}
fn mul_u_minus_a(p: &[i128], a: i128)->Vec<i128>{
    let mut v=vec![0;p.len()+1];
    for (i,c) in p.iter().enumerate(){ v[i]-=a*c; v[i+1]+=c; }
    v
}

// The classical Chebyshev recurrence has P_0=2 (as a recurrence seed);
// the MONIC frame has P_0=1 (the unchanged constant row), P_1=u-a,
// P_2=(u-a)^2-2b, and P_{s+1}=(u-a)P_s-b P_{s-1} for s>=2.
// All coefficients are integral; the leading coefficient is exactly one.
fn polynomial_frames() -> (Vec<Vec<i128>>,Vec<Vec<i128>>,i128,i128) {
    let l=RHO*RHO;
    let a=l/2;
    let extent=a.max(l-a);
    let b=(extent*extent+3)/4; // ceil(max(a,L-a)^2 / 4)
    let mut centered=vec![vec![1]];
    let mut cheb=vec![vec![1]];
    for s in 1..S {
        centered.push(mul_u_minus_a(centered.last().unwrap(),a));
        let mut q=mul_u_minus_a(cheb.last().unwrap(),a);
        if s==2 {q[0]-=2*b;}
        if s>=3 {
            let two_before=&cheb[s-2];
            for (i,c) in two_before.iter().enumerate(){q[i]-=b*c;}
        }
        cheb.push(q);
    }
    (centered,cheb,a,b)
}

fn monomial_jet(r:usize,s:usize,j:usize,z:Q)->Q {
    if j>r { return Q::zero(); }
    z.pow(r-j).mul(z.conj().pow(s)).scale(fall(r,j))
}

// Via original integer monomial rows; W is held constant on differentiation.
fn expansion_jet(r:usize,s:usize,j:usize,z:Q,p:&[i128])->Q {
    let m=r.min(s);
    assert_eq!(p.len(),m+1);
    let mut out=Q::zero();
    for (t,c) in p.iter().enumerate(){
        let newr=r-m+t;let news=s-m+t;
        out=out.add(monomial_jet(newr,news,j,z).scale(*c));
    }
    out
}

fn ordinary_poly_deriv_at(p:&[i128],j:usize,u:i128)->i128{
    p.iter().enumerate().filter(|(t,_)|*t>=j)
        .map(|(t,c)|c*fall(t,j)*u.pow((t-j) as u32)).sum()
}

// Independently via Leibniz on Z^(r-m) W^(s-m) P_m(ZW).
fn factorized_jet(r:usize,s:usize,j:usize,z:Q,p:&[i128])->Q {
    let m=r.min(s);let a=r-m;let b=s-m;
    let mut out=Q::zero();
    for k in 0..=j.min(m) {
        if j-k>a {continue;}
        let c=choose(j,k)*fall(a,j-k)*
            ordinary_poly_deriv_at(p,k,z.normsq());
        let term=z.pow(a-(j-k)).mul(z.conj().pow(b+k)).scale(c);
        out=out.add(term);
    }
    out
}

fn frame_matrix(polys:&[Vec<i128>])->Vec<Vec<i128>> {
    let mut u=vec![vec![0;N];N];
    for r in 0..R {
        for s in 0..S {
            let m=r.min(s);let i=r*S+s;
            for (t,c) in polys[m].iter().enumerate(){
                let rr=r-m+t;let ss=s-m+t;let dst=rr*S+ss;
                assert!(dst<=i); // integer lower triangular, exact same rows
                u[i][dst]+=c;
            }
            assert_eq!(u[i][i],1); // det(U)=1 over Z
            for j in i+1..N {assert_eq!(u[i][j],0);}
        }
    }
    u
}

fn observation_matrix(original:bool,polys:&[Vec<i128>],pts:&[Q])->Vec<Vec<i128>> {
    let mut e=Vec::new();
    for r in 0..R {
        for s in 0..S {
            let m=r.min(s);let mut row=Vec::new();
            for z in pts {
                for j in 0..J {
                    let v=if original {monomial_jet(r,s,j,*z)}
                        else { expansion_jet(r,s,j,*z,&polys[m]) };
                    row.push(v.a);
                    row.push(v.b);
                    if !original {
                        assert_eq!(v,factorized_jet(r,s,j,*z,&polys[m]));
                    }
                }
            }
            e.push(row);
        }
    }
    e
}

fn row_times(u:&[Vec<i128>],e:&[Vec<i128>])->Vec<Vec<i128>> {
    let n=u.len();let cols=e[0].len();
    let mut out=vec![vec![0;cols];n];
    for i in 0..n {
        for k in 0..n {
            if u[i][k]==0 {continue;}
            for col in 0..cols {out[i][col]+=u[i][k]*e[k][col];}
        }
    }
    out
}

fn gram(e:&[Vec<i128>])->Vec<Vec<i128>> {
    let n=e.len();let mut out=vec![vec![0i128;n];n];
    for i in 0..n {
        for k in 0..n {
            for col in 0..e[0].len(){
                let weight=if col%2==0 {2}else{2*D};
                out[i][k]+=weight*e[i][col]*e[k][col];
            }
        }
    }
    out
}

fn congruence(u:&[Vec<i128>],g:&[Vec<i128>])->Vec<Vec<i128>> {
    let n=g.len();let mut ug=vec![vec![0;n];n];
    for i in 0..n {for k in 0..n {for j in 0..n {
        ug[i][j]+=u[i][k]*g[k][j];
    }}}
    let mut out=vec![vec![0;n];n];
    for i in 0..n {for j in 0..n {for k in 0..n {
        out[i][j]+=ug[i][k]*u[j][k];
    }}}
    out
}

#[derive(Debug)]
struct Report {
    node_count:usize, row_count:usize, observation_cols:usize,
    point_guard:bool, improved_rows:usize, worsened_rows:usize,
    unchanged_rows:usize, log_product_gain:f64,
    new_diag_product_over_old:f64,
}

fn run()->Report {
    let pts=points();
    let (centered,cheb,a,b)=polynomial_frames();
    assert_eq!((a,b),(12,43));
    assert_eq!(pts.len(),21);
    assert_eq!(centered[2],vec![144,-24,1]);
    assert_eq!(cheb[2],vec![58,-24,1]);
    assert_eq!(cheb[3],vec![-180,303,-36,1]);
    let original=observation_matrix(true,&[],&pts);
    let ep=observation_matrix(false,&centered,&pts);
    let ec=observation_matrix(false,&cheb,&pts);
    let up=frame_matrix(&centered);
    let uc=frame_matrix(&cheb);
    assert_eq!(row_times(&up,&original),ep);
    assert_eq!(row_times(&uc,&original),ec);
    let g=gram(&original);
    let gp=gram(&ep);
    let gc=gram(&ec);
    assert_eq!(congruence(&up,&g),gp);
    assert_eq!(congruence(&uc,&g),gc);
    assert_eq!((gp[2*S+2][2*S+2],gc[2*S+2][2*S+2]),(666616,378688));
    assert_eq!((gp[3*S+3][3*S+3],gc[3*S+3][3*S+3]),(163129320,87348528));
    let mut better=0;let mut worse=0;let mut same=0;let mut log_gain=0f64;
    for i in 0..N {
        assert!(gp[i][i]>0 && gc[i][i]>0);
        let s=i%S;let r=i/S;let m=r.min(s);
        if gc[i][i]<gp[i][i] {better+=1;}
        else if gc[i][i]>gp[i][i] {worse+=1;}
        else {same+=1;}
        if m<2 {assert_eq!(gc[i][i],gp[i][i]);}
        log_gain+=(gc[i][i] as f64).ln()-(gp[i][i] as f64).ln();
    }
    assert_eq!((better,worse,same),(12,0,20));
    // Negative control: pointwise squared jet norms do NOT always shrink.
    let z=Q{a:-4,b:0};
    let old=expansion_jet(2,2,0,z,&centered[2]).normsq();
    let new=expansion_jet(2,2,0,z,&cheb[2]).normsq();
    assert_eq!((old,new),(256,4900));
    assert!(new>old);
    assert!(log_gain < -5.80 && log_gain > -5.81);
    Report{node_count:pts.len(),row_count:N,observation_cols:2*J*pts.len(),
        point_guard:2*(R-1)+(S-1)<pts.len(),
        improved_rows:better,worsened_rows:worse,unchanged_rows:same,
        log_product_gain:log_gain,new_diag_product_over_old:log_gain.exp()}
}

fn main() {
    let v=run();
    println!("{v:?}");
    assert!(v.point_guard);
}

#[cfg(test)]
mod tests{
    use super::*;
    #[test]fn same_matrix_all_ordinary_jets_and_full_gram(){main();}
    #[test]fn changed_rows_preserve_integral_unipotent_lattice(){
        let(c,t,_,_)=polynomial_frames();
        let uc=frame_matrix(&c);let ut=frame_matrix(&t);
        assert_eq!(uc.len(),R*S);
        assert_eq!(ut.len(),R*S);
        assert!((0..N).all(|i|uc[i][i]==1&&ut[i][i]==1));
    }
    #[test]fn independent_leibniz_implementation(){
        let(c,t,_,_)=polynomial_frames();let q=points();
        for p in [&c,&t] {
            for r in 0..R {for s in 0..S {let m=r.min(s);
                for z in &q {for j in 0..J {
                    assert_eq!(expansion_jet(r,s,j,*z,&p[m]),
                               factorized_jet(r,s,j,*z,&p[m]));
                }}
            }}
        }
    }
    #[test]fn false_pointwise_improvement_is_rejected(){
        let(c,t,_,_)=polynomial_frames();let z=Q{a:-4,b:0};
        assert!(expansion_jet(2,2,0,z,&t[2]).normsq() >
            expansion_jet(2,2,0,z,&c[2]).normsq());
    }
}
