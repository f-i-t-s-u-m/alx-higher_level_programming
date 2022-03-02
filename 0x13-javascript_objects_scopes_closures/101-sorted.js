#!/usr/bin/node
const dict = require('./101-data').dict;
const d = {};
Object.entries(dict).map(function ([k, v]) {
  d[v] = Object.entries(dict).filter(([x, y]) => v === y).map(([a, b]) => a);
  return true;
});
console.log(d);
