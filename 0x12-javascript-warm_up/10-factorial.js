#!/usr/bin/node
const argv = process.argv.slice(2);
let n = parseInt(argv[0]);
function f (a) {
  if (argv.length >= 1 && isNaN(n));
  else if (isNaN(n)) console.log(1);
  else if (a === 1) console.log(n);
  else {
    n = n * (a - 1);
    f(a - 1);
  }
}

f(n);
