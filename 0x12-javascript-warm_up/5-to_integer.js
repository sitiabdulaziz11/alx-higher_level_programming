#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const FirstArg = parseInt(process.argv[2]);
  if (!isNaN(FirstArg)) {
    console.log(`My number: ${FirstArg}`);
  } else {
    console.log('Not a number');
  }
}
