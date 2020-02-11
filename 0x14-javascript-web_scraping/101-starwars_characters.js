#!/usr/bin/node
const request = require('request');
request('https://swapi.co/api/films/', function (err, res, body) {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body).results;
    let film;
    for (const movie of movies) {
      if (movie.url.includes(process.argv[2])) {
        film = movie;
        break;
      }
    }
    for (const character of film.characters) {
      request(character, function (err, res, body) {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
