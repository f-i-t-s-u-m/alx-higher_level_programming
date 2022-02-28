#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv[0] === undefined) console.log('Missing number of occurrences');
else {
  let n = argv[0];
  while (n) {
    console.log('C is fun');
    n--;
  }
}
