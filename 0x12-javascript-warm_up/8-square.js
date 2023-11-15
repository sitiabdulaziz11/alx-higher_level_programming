#!/usr/bin/node

const FirstArg = process.argv[2];

if (!parseInt(FirstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
