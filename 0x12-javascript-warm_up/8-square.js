#!/usr/bin/node
//comment
const args = process.argv;
const x = parseInt(args[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
