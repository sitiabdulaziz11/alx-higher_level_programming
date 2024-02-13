#!/usr/bin/node
// script that display the status code of a GET request.

const reqst = require('request');

reqst(process.argv[2], function (_error, response) {
  console.log('code:', response.statusCode);
});
