#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const reqst = require('request');
const urlStarwar = process.argv[2];
let count = 0;

reqst(urlStarwar, function (_error, resours, value) {
  value = JSON.parse(value).results;

  for (let i = 0; i < value.length; i++) {
    const characters = value[i].characters;

    for (let k = 0; k < characters.length; k++) {
      const val = characters[k];
      const chrId = val.split('/')[5];

      if (chrId === '18') {
        count += 1;
      }
    }
  }

  console.log(count);
});
