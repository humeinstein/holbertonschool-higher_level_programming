#!/usr/bin/node
// script uses starwars api
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else { }
});
