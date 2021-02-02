#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  if (n === 0 || !n) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
