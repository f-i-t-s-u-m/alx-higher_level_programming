#!/usr/bin/node

const req = require('request');
const argv = process.argv.slice(2);

req(argv[0], (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const data = JSON.parse(body).reduce((p, c) => {
    if (c.completed) {
      if (p[c.userId]) {
        p[c.userId]++;
      } else {
        p[c.userId] = 1;
      }
    }

    return p;
  }, {});
  console.log(data);
});
