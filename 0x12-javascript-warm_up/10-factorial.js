#!/usr/bin/node
const toCheck = process.argv[2];
function factorial (n) {
  const f = [];
  if (n === 0 || n === 1) { return 1; }
  if (f[n] > 0) { return f[n]; }
  if (isNaN(n)) { return (1); }
  return (f[n] = factorial(n - 1) * n);
}
console.log(factorial(toCheck));
