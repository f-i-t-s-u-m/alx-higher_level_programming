#!/usr/bin/node

const req = require('request');
const argv = process.argv.slice(2);

req(argv[0], (error, response, body) => {
  if (error) {
    console.log(error);
  }

  let i = 0;
  let c = 0;
  while (JSON.parse(body).results[i]) {
    let n = 0;
    const ch = JSON.parse(body).results[i].characters;
    while (ch[n]) {
      if (ch[n] === 'https://swapi-api.hbtn.io/api/people/18/') {
        c++;
      }
      n++;
    }
    i++;
  }
  console.log(c);
});
