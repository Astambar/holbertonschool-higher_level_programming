#!/usr/bin/node
//comment
function add (a, b) {
    if (Number.isNaN(a, b)) {
      console.log('NaN');
    } else {
      console.log(a + b);
    }
  }
  const args = process.argv;
  const a = parseInt(args[2]);
  const b = parseInt(args[3]);
  add(a, b);
