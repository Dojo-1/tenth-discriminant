// Exact original-ellipse ordinary-jet Gram from mixed and radial moments.
// Rust std only; no change of nodes, derivative slots or trace pairing.
// D=19, rho=5, R=8, S=J=4; the original E has 32 rows.
const D:i128=19;const R:i32=8;const S:i32=4;const J:i32=4;
type Z=(i128,i128);
fn mul(a:Z,b:Z)->Z{(a.0*b.0-D*a.1*b.1,a.0*b.1+a.1*b.0)}
fn pow(a:Z,n:i32)->Z{let mut z=(1,0);for _ in 0..n{z=mul(z,a)}z}
fn pts()->Vec<Z>{let mut v=vec![];for x in -5..=5{for y in -5..=5{
 if x*x+19*y*y<=25{v.push((x,y))}}}v}
fn fall(n:i32,j:i32)->i128{let mut x=1;for k in 0..j{x*=(n-k) as i128;}x}
fn jet(r:i32,s:i32,j:i32,z:Z)->Z{if j>r{return (0,0)}
 let a=mul(pow(z,r-j),pow((z.0,-z.1),s));let f=fall(r,j);(f*a.0,f*a.1)}
fn moment(q:&[Z],a:i32,b:i32)->Z{let mut v=(0,0);
 for &z in q{let x=mul(pow(z,a),pow((z.0,-z.1),b));v.0+=x.0;v.1+=x.1;}v}
fn radial(q:&[Z],k:i32)->i128{q.iter().map(|z|(z.0*z.0+D*z.1*z.1).pow(k as u32)).sum()}
fn direct(q:&[Z],r:i32,s:i32,t:i32,u:i32)->i128{
 let mut v=0;for &z in q{for j in 0..J{
 let a=jet(r,s,j,z);let b=jet(t,u,j,z);
 v+=2*(a.0*b.0+D*a.1*b.1);}}v}
fn reconstructed(q:&[Z],r:i32,s:i32,t:i32,u:i32)->i128{
 let mut v=0;for j in 0..J{if j>r||j>t{continue}
 let m=moment(q,r-j+u,s+t-j);
 assert_eq!(m.1,0);v+=2*fall(r,j)*fall(t,j)*m.0;}v}
fn radial_block(q:&[Z],r:i32,s:i32,t:i32,u:i32)->i128{
 assert_eq!(r-s,t-u);let d=(r-s).abs();let m=r.min(s);let n=t.min(u);
 let mut v=0;for j in 0..J{if j>r||j>t{continue}
 v+=2*fall(r,j)*fall(t,j)*radial(q,d+m+n-j)}v}
// A single angular order ell=|(r-s)-(t-u)| suffices for each
// cross-grade pair, independent of the ordinary derivative order.
fn angular_harmonic(q:&[Z],ell:i32,k:i32)->i128{
 q.iter().map(|z|{
   let t=z.0*z.0+D*z.1*z.1;
   pow(*z,ell).0*t.pow(k as u32)
 }).sum()
}
fn angular_entry(q:&[Z],r:i32,s:i32,t:i32,u:i32)->i128{
 let ell=(r-s-t+u).abs();let mut total=0;
 for j in 0..J{if j>r||j>t{continue}
 let a=r-j+u;let b=s+t-j;
 total+=2*fall(r,j)*fall(t,j)*angular_harmonic(q,ell,a.min(b));
 }total
}
#[test] fn whole_original_gram_equals_moment_reconstruction(){
 let q=pts();assert_eq!(q.len(),21);
 let mut nonzero_even=0;let mut odd_pairs=0;
 for r in 0..R{for s in 0..S{for t in 0..R{for u in 0..S{
 let x=direct(&q,r,s,t,u);
 assert_eq!(x,reconstructed(&q,r,s,t,u));
 if r-s==t-u{assert_eq!(x,radial_block(&q,r,s,t,u));}
 if (r-s-t+u)%2!=0{assert_eq!(x,0);odd_pairs+=1;}
 else if r-s!=t-u&&x!=0{nonzero_even+=1;}
 }}}}
 assert!(nonzero_even>0&&odd_pairs>0);
}
#[test] fn exact_values_and_derivative_falsifier(){
 let q=pts();
 assert_eq!([radial(&q,0),radial(&q,1),radial(&q,2),radial(&q,3)],
            [21,320,6396,135416]);
 assert_eq!(moment(&q,2,0),(-60,0));
 assert_eq!(moment(&q,1,0),(0,0));
 let a=direct(&q,0,0,0,0);let b=direct(&q,0,0,2,0);
 let c=direct(&q,2,0,2,0);
 assert_eq!((a,b,c),(42,-120,15520));
 assert_eq!(a*c-b*b,637440);
 assert_ne!(c,2*radial(&q,2)); // Dropped derivatives are wrong.
}
#[test] fn angular_orders_and_signed_cross_grade_controls(){
 let q=pts();
 for r in 0..R{for s in 0..S{for t in 0..R{for u in 0..S{
   assert_eq!(angular_entry(&q,r,s,t,u),direct(&q,r,s,t,u));
 }}}}
 assert_eq!(angular_harmonic(&q,0,2),radial(&q,2));
 assert_eq!(angular_harmonic(&q,1,0),0);
 assert_eq!(angular_harmonic(&q,2,0),-60);
 assert_eq!(angular_harmonic(&q,2,1),-1584);
 assert_eq!(angular_harmonic(&q,4,0),3356);
 assert_ne!(angular_harmonic(&q,4,0),0);
 // Triangle bound for even angular order: |Re(z^ell)|<=norm(z)^(ell/2).
 for ell in [2,4,6]{for k in 0..4{
   assert!(angular_harmonic(&q,ell,k).abs()<=radial(&q,k+ell/2));
 }}
}
#[test] fn rational_real_shear_preserves_exact_integer_determinant(){
 let q=pts();let a=direct(&q,0,0,0,0);
 let b=direct(&q,0,0,2,0);let c=direct(&q,2,0,2,0);
 // t=b/a=-20/7; new row is old row - t*constant row.
 let den=7;let numerator=-20;
 assert_eq!(a*numerator,b*den);
 let c_new_num=den*den*c-2*den*numerator*b+numerator*numerator*a;
 assert_eq!(a*c_new_num,den*den*(a*c-b*b));
 assert_eq!(c_new_num,743680);
 assert!(c_new_num<den*den*c);
 assert_ne!(b%a,0); // This real frame is not integral.
}
