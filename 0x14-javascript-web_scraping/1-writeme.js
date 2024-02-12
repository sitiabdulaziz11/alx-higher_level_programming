#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
	if (err) {
		console.log(err);
	} else {
		process.stdout.write(data);
	}
})
