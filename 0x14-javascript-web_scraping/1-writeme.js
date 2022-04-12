#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');

fs.writeFile(argv[0], argv[1], 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
