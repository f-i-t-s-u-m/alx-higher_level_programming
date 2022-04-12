#!/usr/bin/node

const req = require('request');
const argv = process.argv.slice(2);

req(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
