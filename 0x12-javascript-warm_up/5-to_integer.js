#!/usr/bin/node
if (process.argv[2] === undefined) {
	console.log('Not a number');}
else if (isNaN(Math.trunc(process.argv[2]))){
	console.log('Not a number');}
else {
	console.log(Math.trunc(process.argv[2]));}
