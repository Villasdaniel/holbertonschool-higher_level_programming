#!/usr/bin/node
// display the status code of a GET request.

const request = require('request');

request(process.argv[2], (err, resp) => {
  if (err) {
    console.error('code: ', err);
  } else {
    console.log('code:', resp && resp.statusCode);
  }
});
