#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv[0] === undefined || isNaN(parseInt(argv[0]))) console.log('Missing size');
else {
  let n = parseInt(argv[0]);
  while (n) {
    console.log('X'.repeat(parseInt(argv[0])));
    --n;
  }
}
