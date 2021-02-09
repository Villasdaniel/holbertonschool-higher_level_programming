#!/usr/bin/node
/* prints the title of a Star Wars movie
where the episode number matches a given integer */

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
