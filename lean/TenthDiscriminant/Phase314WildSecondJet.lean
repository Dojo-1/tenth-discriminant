import Mathlib

/-!
# Phase314: polynomial certificate for the wild second-jet quotient

If a source evaluation is affine in the wild (F5)^2 coordinates,
its trace Gram is at most quadratic; all THIRD additive differences
vanish. Kernel checked here in arbitrary commutative rings.

The six-moment algebra multiplication encodes the exact binomial
formulas for mass, first and second moments under group convolution.
This file does NOT formalize the full number field ray group, original
Gram source, quotient by J^3, or class number one.
-/

namespace TenthDiscriminant.Phase314

variable {R : Type*} [CommRing R]

def quadratic (a0 ax ay axx axy ayy x y : R) : R :=
  a0 + ax*x + ay*y + axx*x^2 + axy*x*y + ayy*y^2

/-- Every cubic mixed forward difference of an affine-evaluation Gram
is zero, independently of the choice of three wild increments. -/
theorem quadratic_third_difference
    (a0 ax ay axx axy ayy x y hx hy kx ky lx ly : R) :
    quadratic a0 ax ay axx axy ayy (x+hx+kx+lx) (y+hy+ky+ly)
      - quadratic a0 ax ay axx axy ayy (x+hx+kx) (y+hy+ky)
      - quadratic a0 ax ay axx axy ayy (x+hx+lx) (y+hy+ly)
      - quadratic a0 ax ay axx axy ayy (x+kx+lx) (y+ky+ly)
      + quadratic a0 ax ay axx axy ayy (x+hx) (y+hy)
      + quadratic a0 ax ay axx axy ayy (x+kx) (y+ky)
      + quadratic a0 ax ay axx axy ayy (x+lx) (y+ly)
      - quadratic a0 ax ay axx axy ayy x y = 0 := by
  unfold quadratic
  ring

/-- Six raw moments: mass, x, y, x-square, xy, y-square. -/
@[ext] structure SixMoments (R : Type*) [CommRing R] where
  mass : R
  x : R
  y : R
  xx : R
  xy : R
  yy : R

def momentAtom (x y : R) : SixMoments R :=
  ⟨1, x, y, x*x, x*y, y*y⟩

/-- Convolution is closed in the six-moment quotient.
The crossed terms are essential and cannot be discarded. -/
def momentConvolution (a b : SixMoments R) : SixMoments R :=
  ⟨a.mass*b.mass,
   a.x*b.mass+a.mass*b.x,
   a.y*b.mass+a.mass*b.y,
   a.xx*b.mass+2*a.x*b.x+a.mass*b.xx,
   a.xy*b.mass+a.x*b.y+a.y*b.x+a.mass*b.xy,
   a.yy*b.mass+2*a.y*b.y+a.mass*b.yy⟩

/-- Atoms multiply by adding their two additive wild coordinates. -/
theorem momentConvolution_atoms (x y u v : R) :
    momentConvolution (momentAtom x y) (momentAtom u v) =
      momentAtom (x+u) (y+v) := by
  apply SixMoments.ext <;> simp [momentConvolution, momentAtom] <;> ring

/-- This is a genuine 2nd-order moment, not just an affine quotient:
the second additive difference of x-square is 2. -/
theorem nonzero_quadratic_second_difference
    (x : ZMod 5) :
    (x+1)^2-2*x^2+(x-1)^2 = 2 := by
  ring

end TenthDiscriminant.Phase314
