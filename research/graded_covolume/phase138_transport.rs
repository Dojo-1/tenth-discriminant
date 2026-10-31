// Phase138 small 4-dimensional, all-integer noncommuting frame test.
// This is a typed algebraic CONTROL, not the production ellipse or a
// proof of an improved discriminant bound. It checks that a moving
// integral frame and its compensated inverse preserve the ORIGINAL
// p-local extraction and the full positive trace Gram.
//
// Run: rustc --edition=2021 --test research/graded_covolume/phase138_transport.rs
// All matrices are fixed 4x4 and fit in i128.
type M = [[i128; 4]; 4];

fn eye() -> M {
    let mut o = [[0;4];4];
    for i in 0..4 {o[i][i]=1;}
    o
}
fn mm(a: &M, b: &M) -> M {
    let mut o = [[0;4];4];
    for i in 0..4 {
        for k in 0..4 {
            for j in 0..4 {o[i][j] += a[i][k]*b[k][j];}
        }
    }
    o
}
fn tr(a: &M)->M {
    let mut o=[[0;4];4];
    for i in 0..4 {for j in 0..4 {o[j][i]=a[i][j];}}
    o
}
fn congruence(h:&M,g:&M)->M {mm(&mm(h,g),&tr(h))}
fn gram(e:&M,b:&[i128;4])->M {
    let mut o=[[0;4];4];
    for i in 0..4 {for j in 0..4 {
        for k in 0..4 {o[i][j]+=e[i][k]*e[j][k]*b[k];}
    }}
    o
}
fn det4(a:&M)->i128 {
    // Exact fraction-free Bareiss with integer pivots.
    let mut b=*a;let mut den=1i128;let mut sign=1;
    for k in 0..3 {
        if b[k][k]==0 {
            let t=((k+1)..4).find(|&i|b[i][k]!=0);
            let Some(t)=t else{return 0};
            b.swap(k,t);sign=-sign;
        }
        let pivot=b[k][k];
        for i in k+1..4 {for j in k+1..4 {
            let n=b[i][j]*pivot-b[i][k]*b[k][j];
            assert_eq!(n%den,0,"exact Bareiss pivot division");
            b[i][j]=n/den;
        }}
        for i in k+1..4 {b[i][k]=0;}
        den=pivot;
    }
    sign*b[3][3]
}
fn shear(row:usize,col:usize,coefficient:i128)->M {
    assert!(row>col&&row<4);
    let mut a=eye();a[row][col]=coefficient;a
}
fn matmul3(a:&M,b:&M,c:&M)->M{mm(&mm(a,b),c)}

#[cfg(test)]
mod tests {
    use super::*;
    fn sample()->(M,[i128;4],M) {
        // Integer coordinates with the same weight pattern as Q(sqrt(-19)).
        // First two observation rows have a p=2 integral row factor.
        let e:M=[[2,0,0,0],[0,2,0,0],[5,0,1,0],[0,5,0,1]];
        let b=[2,38,2,38];
        let g=gram(&e,&b);
        (e,b,g)
    }
    #[test]
    fn fractional_sobolev_projection_has_positive_integral_remainder() {
        let (_,_,g)=sample();
        // A=diag(8,152); C=diag(20,380);
        // real minimizing K*=diag(5/2,5/2), with
        // Schur S=diag(2,38).
        assert_eq!([g[0][0],g[1][1],g[2][2],g[3][3]],[8,152,52,988]);
        assert_eq!([g[0][2],g[1][3],g[0][3],g[1][2]],[20,380,0,0]);
        let h=mm(&shear(3,1,-2),&shear(2,0,-2));
        let newer=congruence(&h,&g);
        // Correct integer rounding K=diag(2,2):
        // D_K=Schur + RoundingDefect=diag(2,38)+diag(2,38).
        assert_eq!([newer[2][2],newer[3][3]],[4,76]);
        assert!(newer[2][2]<g[2][2]&&newer[3][3]<g[3][3]);
        assert_eq!(det4(&g),92416);
        assert_eq!(det4(&newer),92416);
        assert_eq!(det4(&h),1);
        // A tempting claim that integral rounding achieves the
        // continuous Schur optimum is FALSE in this exact example.
        assert_ne!([newer[2][2],newer[3][3]],[2,38]);
    }
    #[test]
    fn noncommuting_frames_need_corrected_paths() {
        let (e,b,g)=sample();
        let h1=shear(2,0,-2);
        let h2=shear(3,2,-1);
        let left=mm(&h2,&h1);
        let right=mm(&h1,&h2);
        assert_ne!(left,right);
        assert_eq!(det4(&left),det4(&right));
        let inv=mm(&shear(2,0,2),&shear(3,2,1));
        assert_eq!(mm(&left,&inv),eye());
        assert_eq!(mm(&inv,&left),eye());
        let e_new=mm(&left,&e);
        let g_new=congruence(&left,&g);
        assert_eq!(mm(&inv,&e_new),e);
        assert_eq!(congruence(&inv,&g_new),g);
        assert_eq!(gram(&e_new,&b),g_new);
    }
    #[test]
    fn p_local_row_extraction_survives_integral_gauge() {
        let (e,b,g)=sample();
        let delta:M=[[2,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]];
        let normalized:M=[[1,0,0,0],[0,1,0,0],[5,0,1,0],[0,5,0,1]];
        assert_eq!(mm(&delta,&normalized),e);
        let k=gram(&normalized,&b);
        assert_eq!(congruence(&delta,&k),g);
        let h1=shear(2,0,-2);
        let h2=shear(3,2,-1);
        let moving=mm(&h2,&h1);
        let compensated=mm(&shear(2,0,2),&shear(3,2,1));
        let em=mm(&moving,&e);
        let gm=congruence(&moving,&g);
        assert_eq!(mm(&compensated,&em),mm(&delta,&normalized));
        assert_eq!(congruence(&compensated,&gm),
                   congruence(&delta,&k));
        assert_eq!(det4(&g),16*det4(&k));
        assert!(det4(&g)>0);
        // The raw order-swap is a counterworld; identical det
        // does not establish equality of transported matrices.
        assert_ne!(matmul3(&h1,&h2,&e),matmul3(&h2,&h1,&e));
    }
}
