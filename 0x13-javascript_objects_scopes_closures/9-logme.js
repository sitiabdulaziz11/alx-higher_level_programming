#!/usr/bin/node

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
let count = 0;
