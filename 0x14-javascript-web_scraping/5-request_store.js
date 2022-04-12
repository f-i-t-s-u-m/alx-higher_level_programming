#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');
const req = require('request');

req(argv[0], (err, response, body) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(argv[1], body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
