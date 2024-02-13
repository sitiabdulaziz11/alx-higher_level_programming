#!/usr/bin/node
// script that prints the title of a Star Wars movie

const reqst = require('request');
const movieId = process.argv[2];
const urlStarWar = `https://swapi-api.alx-tools.com/api/films/${movieId}`;// .concat(process.argv[2]);

reqst(urlStarWar, function (_error, response, value) {
  value = JSON.parse(value);
  console.log(value.title);
});
