#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const reqst = require('request');
const fileSm = require('fs');

reqst(process.argv[2], function (_error, resours, value) {
  fileSm.writeFile(process.argv[3], value, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
