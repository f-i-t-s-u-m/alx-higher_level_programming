#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');

fs.readFile(argv[0], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
