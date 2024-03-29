#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  n = parseInt(n);

  if (n < 0) {
    return 'Invalid input. Please provide a non-negative integer.';
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const input = process.argv[2];
const result = factorial(input);

console.log(result);
