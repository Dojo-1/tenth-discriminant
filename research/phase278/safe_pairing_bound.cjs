'use strict';
// Six registered abstract trace-metric controls; never a production jet source.
const assert = require('node:assert/strict');
const p = 3n, weights = [2n, 14n, 2n, 14n];
const w = [1n, 0n, 1n, 1n], z = [1n, 0n, 0n, 0n];
const mod = x => (x % p + p) % p;
const gram = (C, B = weights) => C.map(a => C.map(b =>
  a.reduce((sum, x, j) => sum + x * B[j] * b[j], 0n)));
const det = A => A.length === 1 ? A[0][0] :
  A[0][0] * A[1][1] - A[0][1] * A[1][0];
function valuation(x) {
  assert.notEqual(x, 0n, 'zero valuation is not a finite integer');
  let v = 0;
  while (x % p === 0n) { x /= p; v++; }
  return v;
}
function rank(C) {
  const A = C.map(row => row.map(mod));
  let k = 0;
  for (let j = 0; j < A[0].length && k < A.length; j++) {
    const i = A.findIndex((row, h) => h >= k && row[j] !== 0n);
    if (i < 0) continue;
    [A[k], A[i]] = [A[i], A[k]];
    const inverse = A[k][j] === 1n ? 1n : 2n; // only F_3
    A[k] = A[k].map(x => mod(x * inverse));
    for (let h = k + 1; h < A.length; h++) {
      const factor = A[h][j];
      A[h] = A[h].map((x, t) => mod(x - factor * A[k][t]));
    }
    k++;
  }
  return k;
}
const cases = [
  {name: 'primitive_isotropic_line', C: [w], exponents: [0], value: 2, r: 1, q: 0},
  {name: 'scaled_isotropic_line', C: [w], exponents: [1], value: 4, r: 0, q: 0},
  {name: 'primitive_plane', C: [w, z], exponents: [0, 0], value: 0, r: 2, q: 2},
  {name: 'false_addition_killer', C: [w, z], exponents: [0, 1], value: 2, r: 1, q: 0},
  {name: 'other_scaled_row', C: [w, z], exponents: [1, 0], value: 2, r: 1, q: 1},
  {name: 'both_scaled_rows', C: [w, z], exponents: [1, 1], value: 4, r: 0, q: 0},
];
const results = [];
for (const c of cases) {
  const E = c.C.map((row, i) => row.map(x => x * p ** BigInt(c.exponents[i])));
  const H = gram(c.C), G = gram(E), n = E.length;
  assert.equal(rank(c.C), n, 'primitive residue rows must be independent');
  const index = c.exponents.reduce((a, b) => a + b, 0);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++)
    assert.equal(G[i][j], p ** BigInt(c.exponents[i] + c.exponents[j]) * H[i][j]);
  assert(det(G) > 0n);
  const value = valuation(det(G)), residual = valuation(det(H));
  const r = rank(E), q = rank(G), d = n - r, radical = r - q;
  const bound = Math.max(2 * d, n - q);
  assert.deepEqual([value, r, q], [c.value, c.r, c.q]);
  assert.equal(value, 2 * index + residual);
  assert(value >= bound);
  assert(residual >= n - rank(H));
  // The actual row shear has determinant one; do not change channel weights.
  const sheared = n === 1 ? E : [E[0].map((x, j) => x + E[1][j]), E[1]];
  assert.equal(det(gram(sheared)), det(G));
  assert.equal(rank(sheared), r);
  assert.equal(rank(gram(sheared)), q);
  results.push({name: c.name, n, r, q, d, radical, index, residual,
    value, bound, determinant: det(G).toString()});
}
const killer = results[3];
assert(2 * killer.d + killer.radical > killer.value);
assert(results[0].residual > 1 - rank(gram([w])));
assert.equal(valuation(det(gram([w], [2n, 2n, 2n, 2n]))), 1);
assert.equal(results[0].residual, 2); // wrong metric loses a real valuation layer
// Phase277 data are read as published finite inputs, not recomputed here.
const publishedPanel = [[3, 140, 36, 10], [5, 140, 60, 32], [7, 140, 28, 28]]
  .map(([prime, n, r, q]) => ({prime, d: n-r, radical: r-q,
    safeAdditionalBound: Math.max(2*(n-r), n-q),
    radicalBeyondIndexBound: Math.max(0, (r-q)-(n-r))}));
assert.deepEqual(publishedPanel.map(c => c.radicalBeyondIndexBound), [0, 0, 0]);
console.log(JSON.stringify({status: 'PASS', evidence: 'six abstract finite controls',
  prime: 3, D: 7, cases: results, publishedPanel,
  limits: 'No production-source replay, Lean theorem, new cutoff or independent review.'}, null, 2));
