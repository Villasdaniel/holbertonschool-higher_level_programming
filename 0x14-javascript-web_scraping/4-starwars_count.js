#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const i in films) {
      for (const x in films[i].characters) {
        if (films[i].characters[x] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count = count + 1;
        }
      }
    }
  }
  return console.log(count);
});
