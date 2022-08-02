#!/usr/bin/node
// comment
const args = process.argv;
const x = parseInt(args[2]);
if (Number.isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[2]);
}
