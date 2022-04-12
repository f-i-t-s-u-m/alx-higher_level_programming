#!/usr/bin/node

const req = require('request');
const argv = process.argv.slice(2);

req(argv[0], (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
