#!/usr/bin/node

var argv = process.argv.slice(2);
var fs =  require('fs');

fs.readFile(argv[0], 'utf8', function (err, data) {
	if(err) {
		return console.log(err)
	}
	console.log(data);
})
