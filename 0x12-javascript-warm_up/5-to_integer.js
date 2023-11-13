#!/usr/bin/node
const FirstArg = parseInt(process.argv[2]);

if (!FirstArg) {
  console.log('Not a number');
} else {
  console.log('My number: ', FirstArg);
}
