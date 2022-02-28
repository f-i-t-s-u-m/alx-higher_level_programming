#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv === undefined || isNaN(parseInt(argv[0]))) console.log('Not a number');
else console.log(parseInt(argv[0]));
