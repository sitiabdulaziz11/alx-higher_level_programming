#!/usr/bin/node

function add(a, b) {
  return a + b;
}
a = parseInt(process.argv[2]);
b = parseInt(process.argv[3]);
console.log(add(a, b));
