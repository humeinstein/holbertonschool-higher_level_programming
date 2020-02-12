#!/usr/bin/node
// script uses starwars api
const request = require('request');
const url = process.argv[2];
let count = 0;
request.get(url, function (err, response, body) {
  if (err) {
    return;
  }
  for (const movie of JSON.parse(body).results) {
    for (const people of movie.characters) {
      if (people.indexOf('/18/') >= 0) { count += 1; }
    }
  }
  console.log(count);
});
