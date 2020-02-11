#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      if (movie.characters.indexOf('https://swapi.co/api/people/18/') >= 0) count++;
    }
    console.log(count);
  }
});
