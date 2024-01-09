#!/usr/bin/node
const ComLineArg = process.argv.length - 2;

if (ComLineArg === 0) {
  console.log('No argument');
} else if (ComLineArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
