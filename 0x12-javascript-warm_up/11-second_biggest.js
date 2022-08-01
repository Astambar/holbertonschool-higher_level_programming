#!/usr/bin/node
const args = process.argv;
const x = args.length;
let max = parseInt(args[2]);
let secmax = 0;
if (x > 3) {
  for (let i = 2; i < x; i++) {
    if (max < parseInt(args[i])) {
      max = parseInt(args[i]);
    }
  }
  for (let i = 2; i < x; i++) {
    if (secmax < parseInt(args[i]) && parseInt(args[i]) < max) {
      secmax = parseInt(args[i]);
    }
  }
}
console.log(secmax);
