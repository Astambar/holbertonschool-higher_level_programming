#!/usr/bin/env node

function factorial (x) {
    let result = 1;
    if (x > 0) {
      result = factorial(x - 1) * x;
    }
    return result;
  }
  const args = process.argv;
  console.log(factorial(parseInt(args[2])));
