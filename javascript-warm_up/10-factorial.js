#!/usr/bin/node

function factorial (n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

const n = parseInt(process.argv[2]);

console.log(factorial(isNaN(n) ? 0 : n));
