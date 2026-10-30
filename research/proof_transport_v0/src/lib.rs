//! Exact, bounded observation-frame pilot for the tenth-discriminant project.
//! No float, no external crates, no extrapolation to the production rectangle.
//! Source correspondence: RectangularBasisMatrix.lean / RadialOperator.lean / IntegerTraceGram.lean.

pub type Check<T> = Result<T, String>;
const MAX_ROWS: usize = 64;

fn err(msg: &str) -> String { msg.to_owned() }
fn add(a: i128, b: i128) -> Check<i128> {
    a.checked_add(b).ok_or_else(|| err("i128 addition overflow"))
}
fn sub(a: i128, b: i128) -> Check<i128> {
    a.checked_sub(b).ok_or_else(|| err("i128 subtraction overflow"))
}
fn mul(a: i128, b: i128) -> Check<i128> {
    a.checked_mul(b).ok_or_else(|| err("i128 multiplication overflow"))
}
fn pow(mut a: i128, mut n: usize) -> Check<i128> {
    let mut v = 1i128;
    while n > 0 {
        if n & 1 != 0 { v = mul(v, a)?; }
        n >>= 1;
        if n > 0 { a = mul(a, a)?; }
    }
    Ok(v)
}
fn choose(n: usize, k: usize) -> Check<i128> {
    if k > n { return Ok(0); }
    let k = k.min(n - k);
    let mut c = 1i128;
    for j in 1..=k {
        let numer = mul(c, (n - j + 1) as i128)?;
        if numer % (j as i128) != 0 { return Err(err("binomial division")); }
        c = numer / (j as i128);
    }
    Ok(c)
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Mat {
    pub rows: usize,
    pub cols: usize,
    cells: Vec<i128>,
}
impl Mat {
    pub fn zero(rows: usize, cols: usize) -> Check<Self> {
        let size = rows.checked_mul(cols).ok_or_else(|| err("dimension overflow"))?;
        if rows > MAX_ROWS || cols > 1024 { return Err(err("pilot dimension cap")); }
        Ok(Self { rows, cols, cells: vec![0; size] })
    }
    pub fn eye(n: usize) -> Check<Self> {
        let mut a = Self::zero(n, n)?;
        for i in 0..n { a.put(i, i, 1); }
        Ok(a)
    }
    pub fn from_rows(rows: &[&[i128]]) -> Check<Self> {
        let n = rows.len();
        let m = rows.first().map_or(0, |r| r.len());
        if rows.iter().any(|r| r.len() != m) { return Err(err("ragged matrix")); }
        let mut v = Self::zero(n, m)?;
        for (i, row) in rows.iter().enumerate() {
            for (j, x) in row.iter().enumerate() { v.put(i, j, *x); }
        }
        Ok(v)
    }
    pub fn at(&self, i: usize, j: usize) -> i128 { self.cells[i * self.cols + j] }
    fn put(&mut self, i: usize, j: usize, v: i128) {
        self.cells[i * self.cols + j] = v;
    }
    fn accumulate(&mut self, i: usize, j: usize, v: i128) -> Check<()> {
        self.put(i, j, add(self.at(i, j), v)?);
        Ok(())
    }
    pub fn transpose(&self) -> Check<Self> {
        let mut t = Self::zero(self.cols, self.rows)?;
        for i in 0..self.rows { for j in 0..self.cols { t.put(j, i, self.at(i, j)); } }
        Ok(t)
    }
    pub fn times(&self, b: &Self) -> Check<Self> {
        if self.cols != b.rows { return Err(err("matrix shape mismatch")); }
        let mut ans = Self::zero(self.rows, b.cols)?;
        for i in 0..self.rows {
            for k in 0..self.cols {
                let aik = self.at(i, k);
                if aik == 0 { continue; }
                for j in 0..b.cols {
                    ans.accumulate(i, j, mul(aik, b.at(k, j))?)?;
                }
            }
        }
        Ok(ans)
    }
    pub fn congruence(&self, g: &Self) -> Check<Self> {
        self.times(g)?.times(&self.transpose()?)
    }
    /// Fraction-free Bareiss determinant, exact divisions and checked arithmetic.
    pub fn determinant(&self) -> Check<i128> {
        if self.rows != self.cols { return Err(err("non-square determinant")); }
        let n = self.rows;
        if n == 0 { return Ok(1); }
        let mut a = self.clone();
        let mut sign = 1i128;
        let mut prev = 1i128;
        for k in 0..n - 1 {
            if a.at(k, k) == 0 {
                let pivot = (k + 1..n).find(|&i| a.at(i, k) != 0);
                let Some(pivot) = pivot else { return Ok(0); };
                for j in 0..n {
                    let x = a.at(k, j);
                    a.put(k, j, a.at(pivot, j));
                    a.put(pivot, j, x);
                }
                sign = -sign;
            }
            let v = a.at(k, k);
            for i in k + 1..n {
                let aik = a.at(i, k);
                for j in k + 1..n {
                    let top = sub(mul(v, a.at(i, j))?, mul(aik, a.at(k, j))?)?;
                    if top % prev != 0 { return Err(err("non-exact Bareiss division")); }
                    a.put(i, j, top / prev);
                }
                a.put(i, k, 0);
            }
            prev = v;
        }
        mul(sign, a.at(n - 1, n - 1))
    }
    pub fn diagonal_product(&self) -> Check<i128> {
        if self.rows != self.cols { return Err(err("non-square diagonal product")); }
        let mut x = 1i128;
        for i in 0..self.rows { x = mul(x, self.at(i, i))?; }
        Ok(x)
    }
    pub fn invert_unit_lower(&self) -> Check<Self> {
        if self.rows != self.cols { return Err(err("non-square inverse")); }
        let n = self.rows;
        for i in 0..n {
            if self.at(i, i) != 1 { return Err(err("not unit-diagonal")); }
            for j in i + 1..n {
                if self.at(i, j) != 0 { return Err(err("not lower triangular")); }
            }
        }
        let mut inv = Self::eye(n)?;
        for i in 0..n {
            for j in 0..i {
                let mut acc = 0i128;
                for k in j..i { acc = add(acc, mul(self.at(i, k), inv.at(k, j))?)?; }
                inv.put(i, j, acc.checked_neg().ok_or_else(|| err("inverse overflow"))?);
            }
        }
        if self.times(&inv)? != Self::eye(n)? || inv.times(self)? != Self::eye(n)? {
            return Err(err("failed exact inverse"));
        }
        Ok(inv)
    }
    pub fn rank_mod_prime(&self, p: i128) -> Check<usize> {
        if p <= 1 || p > 101 || !is_prime(p as usize) { return Err(err("rank requires small prime")); }
        let mut a = self.clone();
        for x in &mut a.cells { *x = x.rem_euclid(p); }
        let mut r = 0usize;
        for c in 0..self.cols {
            if r == self.rows { break; }
            let Some(k) = (r..self.rows).find(|&i| a.at(i, c) != 0) else { continue; };
            for j in 0..self.cols {
                let x = a.at(r, j); a.put(r, j, a.at(k, j)); a.put(k, j, x);
            }
            let pivot = a.at(r, c);
            let inv = (1..p).find(|&t| (t * pivot).rem_euclid(p) == 1)
                .ok_or_else(|| err("noninvertible pivot"))?;
            for j in c..self.cols { a.put(r, j, (a.at(r, j) * inv).rem_euclid(p)); }
            for i in r + 1..self.rows {
                let f = a.at(i, c);
                for j in c..self.cols {
                    a.put(i, j, (a.at(i, j) - f * a.at(r, j)).rem_euclid(p));
                }
            }
            r += 1;
        }
        Ok(r)
    }
}
pub fn is_prime(p: usize) -> bool {
    p >= 2 && !(2..=p / 2).any(|q| p % q == 0)
}
pub fn inert_nonsquare(d: i128, p: usize) -> bool {
    if p == 2 || !is_prime(p) { return false; }
    let modulus = p as i128;
    let target = (-d).rem_euclid(modulus);
    !(0..modulus).any(|x| (x * x).rem_euclid(modulus) == target)
}
pub fn exponent(r: usize, s: usize, s_width: usize, p: usize) -> usize {
    (r / p).min(s_width - 1 - s)
}
pub fn arithmetic_frame(r_width: usize, s_width: usize, p: usize) -> Check<Mat> {
    if p == 0 { return Err(err("zero prime")); }
    let n = r_width.checked_mul(s_width).ok_or_else(|| err("size overflow"))?;
    let mut u = Mat::zero(n, n)?;
    for r in 0..r_width {
        for s in 0..s_width {
            let k = exponent(r, s, s_width, p);
            for t in 0..=k {
                let j = (r - p * t) * s_width + (s + t);
                let coeff = mul(if t % 2 == 0 { 1 } else { -1 }, choose(k, t)?)?;
                u.accumulate(r * s_width + s, j, coeff)?;
            }
        }
    }
    Ok(u)
}
pub fn radial_frame(r_width: usize, s_width: usize, a: i128) -> Check<Mat> {
    let n = r_width.checked_mul(s_width).ok_or_else(|| err("size overflow"))?;
    let mut tframe = Mat::zero(n, n)?;
    let neg = a.checked_neg().ok_or_else(|| err("radial parameter overflow"))?;
    for r in 0..r_width {
        for s in 0..s_width {
            let m = r.min(s);
            for t in 0..=m {
                let j = (r - t) * s_width + (s - t);
                let coeff = mul(pow(neg, t)?, choose(m, t)?)?;
                tframe.accumulate(r * s_width + s, j, coeff)?;
            }
        }
    }
    Ok(tframe)
}
#[derive(Clone, Copy, Debug)]
pub struct Pair { pub re: i128, pub im: i128 }
impl Pair {
    fn times(self, b: Self, d: i128) -> Check<Self> {
        Ok(Self {
            re: sub(mul(self.re, b.re)?, mul(d, mul(self.im, b.im)?)?)?,
            im: add(mul(self.re, b.im)?, mul(self.im, b.re)?)?,
        })
    }
    fn power(self, k: usize, d: i128) -> Check<Self> {
        let mut x = Self { re: 1, im: 0 };
        for _ in 0..k { x = x.times(self, d)?; }
        Ok(x)
    }
    fn conjugate(self) -> Self { Self { re: self.re, im: -self.im } }
}
fn falling(r: usize, j: usize) -> Check<i128> {
    if j > r { return Ok(0); }
    let mut ans = 1;
    for x in r - j + 1..=r { ans = mul(ans, x as i128)?; }
    Ok(ans)
}
fn derivative_jet(d: i128, r: usize, s: usize, j: usize, z: Pair) -> Check<Pair> {
    if j > r { return Ok(Pair { re: 0, im: 0 }); }
    let f = falling(r, j)?;
    let v = z.power(r - j, d)?.times(z.conjugate().power(s, d)?, d)?;
    Ok(Pair { re: mul(f, v.re)?, im: mul(f, v.im)? })
}
pub fn ellipse_points(d: i128, rho: i64) -> Check<Vec<Pair>> {
    if d <= 0 || !(0..=32).contains(&rho) { return Err(err("ellipse pilot guard")); }
    let mut points = Vec::new();
    let radius_sq = mul(rho as i128, rho as i128)?;
    for x in -rho..=rho {
        for y in -rho..=rho {
            let norm = add(mul(x as i128, x as i128)?, mul(d, mul(y as i128, y as i128)?)?)?;
            if norm <= radius_sq { points.push(Pair { re: x as i128, im: y as i128 }); }
        }
    }
    Ok(points)
}
pub fn observation_matrix(d: i128, r_width: usize, s_width: usize,
                          j_count: usize, q: &[Pair]) -> Check<Mat> {
    let n = r_width.checked_mul(s_width).ok_or_else(|| err("rows overflow"))?;
    let slots = q.len().checked_mul(j_count).and_then(|x| x.checked_mul(2))
        .ok_or_else(|| err("columns overflow"))?;
    let mut e = Mat::zero(n, slots)?;
    for r in 0..r_width {
        for s in 0..s_width {
            for (point_id, &z) in q.iter().enumerate() {
                for j in 0..j_count {
                    let v = derivative_jet(d, r, s, j, z)?;
                    let col = 2 * (point_id * j_count + j);
                    e.put(r * s_width + s, col, v.re);
                    e.put(r * s_width + s, col + 1, v.im);
                }
            }
        }
    }
    Ok(e)
}
pub fn gram(e: &Mat, d: i128) -> Check<Mat> {
    if d <= 0 || e.cols % 2 != 0 { return Err(err("invalid trace metric")); }
    let mut g = Mat::zero(e.rows, e.rows)?;
    for i in 0..e.rows {
        for j in 0..e.rows {
            let mut v = 0i128;
            for col in 0..e.cols {
                let metric = if col % 2 == 0 { 2 } else { mul(2, d)? };
                v = add(v, mul(metric, mul(e.at(i, col), e.at(j, col))?)?)?;
            }
            g.put(i, j, v);
        }
    }
    Ok(g)
}
pub fn normalized_integer_jets(ue: &Mat, r_width: usize, s_width: usize,
                               p: usize) -> Check<(Mat, Mat, usize)> {
    if p == 0 || ue.rows != r_width * s_width { return Err(err("quotient size")); }
    let mut delta = Mat::zero(ue.rows, ue.rows)?;
    let mut ehat = Mat::zero(ue.rows, ue.cols)?;
    let mut f = 0usize;
    for i in 0..ue.rows {
        let k = exponent(i / s_width, i % s_width, s_width, p);
        f += k;
        let power = pow(p as i128, k)?;
        delta.put(i, i, power);
        for j in 0..ue.cols {
            if ue.at(i, j) % power != 0 { return Err(err("nonintegral jet quotient")); }
            ehat.put(i, j, ue.at(i, j) / power);
        }
    }
    Ok((delta, ehat, f))
}
pub fn weighted_exterior_sum(e: &Mat, diagonal: &[i128]) -> Check<i128> {
    if e.cols != diagonal.len() || e.rows > 3 || e.cols > 10 {
        return Err(err("bounded exterior comparator guard"));
    }
    fn rec(e: &Mat, diagonal: &[i128], pick: &mut Vec<usize>, start: usize,
           total: &mut i128) -> Check<()> {
        if pick.len() == e.rows {
            let mut minor = Mat::zero(e.rows, e.rows)?;
            let mut weight = 1i128;
            for (j, &col) in pick.iter().enumerate() {
                weight = mul(weight, diagonal[col])?;
                for i in 0..e.rows { minor.put(i, j, e.at(i, col)); }
            }
            let det = minor.determinant()?;
            *total = add(*total, mul(weight, mul(det, det)?)?)?;
            return Ok(());
        }
        for j in start..e.cols {
            pick.push(j);
            rec(e, diagonal, pick, j + 1, total)?;
            pick.pop();
        }
        Ok(())
    }
    let mut sum = 0;
    rec(e, diagonal, &mut Vec::new(), 0, &mut sum)?;
    Ok(sum)
}
#[derive(Debug)]
pub struct Pilot {
    pub n_points: usize, pub f: usize, pub det: i128,
    pub p2f: i128, pub quotient: i128, pub diff_tu: i128, pub diff_ut: i128,
    pub diag_original: i128, pub diag_radial: i128,
    pub diag_tu: i128, pub diag_ut: i128, pub mod_rank: usize,
}
pub fn pilot() -> Check<Pilot> {
    let (d, p, r, s, j, rho, a) = (19i128, 3usize, 5usize, 2usize, 2usize, 2i64, 1i128);
    if !inert_nonsquare(d, p) { return Err(err("inertness guard failed")); }
    let q = ellipse_points(d, rho)?;
    let e = observation_matrix(d, r, s, j, &q)?;
    let g = gram(&e, d)?;
    let u = arithmetic_frame(r, s, p)?;
    let t = radial_frame(r, s, a)?;
    let tu = t.times(&u)?;
    let ut = u.times(&t)?;
    let ug = u.congruence(&g)?;
    let ue = u.times(&e)?;
    let (delta, ehat, f) = normalized_integer_jets(&ue, r, s, p)?;
    let k = gram(&ehat, d)?;
    if ug != delta.congruence(&k)? || ug != gram(&ue, d)? {
        return Err(err("arithmetic/Gram commuting square failed"));
    }
    let tg = t.congruence(&g)?;
    if tg != gram(&t.times(&e)?, d)? { return Err(err("radial jet action mismatch")); }
    let tug = tu.congruence(&g)?;
    let utg = ut.congruence(&g)?;
    let det = g.determinant()?;
    if det <= 0 { return Err(err("nonpositive finite determinant")); }
    for h in [&ug, &tg, &tug, &utg] {
        if h.determinant()? != det { return Err(err("same determinant failure")); }
        if h.rank_mod_prime(p as i128)? != g.rank_mod_prime(p as i128)? {
            return Err(err("residue-rank invariance failure"));
        }
    }
    let p2f = pow(p as i128, 2 * f)?;
    if det % p2f != 0 { return Err(err("prime-power divisibility failure")); }
    let diag_original = g.diagonal_product()?;
    let diag_radial = tg.diagonal_product()?;
    let diag_tu = tug.diagonal_product()?;
    let diag_ut = utg.diagonal_product()?;
    for ceiling in [diag_original, diag_radial, diag_tu, diag_ut] {
        if ceiling < det { return Err(err("Hadamard ceiling violation")); }
    }
    Ok(Pilot {
        n_points: q.len(), f, det, p2f, quotient: det / p2f,
        diff_tu: tu.at(8, 0), diff_ut: ut.at(8, 0),
        diag_original, diag_radial, diag_tu, diag_ut,
        mod_rank: g.rank_mod_prime(p as i128)?,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sealed_training_fixture_and_both_orders() -> Check<()> {
        let x = pilot()?;
        assert_eq!(x.n_points, 5);
        assert_eq!(x.f, 2);
        assert_eq!(x.det, 112717121716224);
        assert_eq!(x.p2f, 81);
        assert_eq!(x.quotient, 1391569403904);
        assert_eq!((x.diff_tu, x.diff_ut), (0, 1));
        assert_eq!(x.diag_original, 13015635040576930578432000);
        assert_eq!(x.diag_radial, 2306514694562388295680000);
        assert_eq!(x.diag_tu, 1673467584363003985920000);
        assert_eq!(x.diag_ut, 1664348262452655575040000);
        assert!(x.diag_radial < x.diag_original);
        assert_ne!(x.diag_tu, x.diag_ut);
        Ok(())
    }

    #[test]
    fn frame_group_laws_and_unitriangular_inverses() -> Check<()> {
        for r in 0..=6 {
            for s in 0..=3 {
                let id = Mat::eye(r * s)?;
                for a in -2i128..=2 {
                    let ta = radial_frame(r, s, a)?;
                    let tinv = radial_frame(r, s, -a)?;
                    assert_eq!(ta.times(&tinv)?, id);
                    assert_eq!(ta.invert_unit_lower()?, tinv);
                    assert_eq!(ta.determinant()?, 1);
                    for b in -1i128..=1 {
                        assert_eq!(ta.times(&radial_frame(r, s, b)?)?,
                            radial_frame(r, s, a + b)?);
                    }
                }
                for p in [3, 5, 7] {
                    let u = arithmetic_frame(r, s, p)?;
                    let ui = u.invert_unit_lower()?;
                    assert_eq!(u.times(&ui)?, id);
                    assert_eq!(ui.times(&u)?, id);
                    assert_eq!(u.determinant()?, 1);
                }
            }
        }
        Ok(())
    }

    #[test]
    fn negative_controls_are_rejected() -> Check<()> {
        assert!(inert_nonsquare(19, 3));
        assert!(!inert_nonsquare(2, 3));
        let z = Pair { re: 0, im: 1 };
        let h = z.power(3, 2)?;
        // z^3 - conjugate(z) = -t, nonzero modulo 3.
        assert_eq!(sub(h.im, z.conjugate().im)?.rem_euclid(3), 2);
        // d^3/dZ^3 Z^3 = 6 but HasseDeriv_3 Z^3 = 1.
        assert_eq!(falling(3, 3)? % 3, 0);
        assert_ne!(1 % 3, 0);
        let e = Mat::eye(2)?;
        let b = Mat::from_rows(&[&[2, 0], &[0, 38]])?;
        let a = Mat::from_rows(&[&[1, 1], &[0, 1]])?;
        let ai = Mat::from_rows(&[&[1, -1], &[0, 1]])?;
        let metric_transport = ai.times(&b)?.times(&ai.transpose()?)?;
        let ea = e.times(&a)?;
        assert_eq!(ea.times(&metric_transport)?.times(&ea.transpose()?)?, b);
        assert_ne!(ea.times(&b)?.times(&ea.transpose()?)?, b);
        let rank_example = Mat::from_rows(&[&[3, 0], &[0, 1]])?;
        assert_eq!(rank_example.determinant()?, 3);
        assert_eq!(rank_example.rank_mod_prime(3)?, 1);
        Ok(())
    }

    #[test]
    fn independent_exterior_formula_on_a_smaller_matrix() -> Check<()> {
        let e = Mat::from_rows(&[&[1, 2, 0, 1], &[0, 1, 3, -1]])?;
        let weights = [2i128, 38, 2, 38];
        let mut b = Mat::zero(4, 4)?;
        for i in 0..4 { b.put(i, i, weights[i]); }
        let g = e.times(&b)?.times(&e.transpose()?)?;
        assert_eq!(g.determinant()?, weighted_exterior_sum(&e, &weights)?);
        Ok(())
    }

    #[test]
    fn explicit_overflow_refusal_not_wrapping() {
        assert!(pow(i128::MAX, 2).is_err());
        assert!(radial_frame(3, 3, i128::MIN).is_err());
        assert!(arithmetic_frame(3, 3, 0).is_err());
        assert!(Mat::zero(65, 65).is_err());
    }
}
