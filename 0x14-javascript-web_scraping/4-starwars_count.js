#!/usr/bin/node

const req = require('request');
const argv = process.argv.slice(2);

req(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const ch = JSON.parse(body).results.filter(result => {
    return result.characters.filter(data => data.includes('18')).length;
  }).length;
  console.log(ch);
});
