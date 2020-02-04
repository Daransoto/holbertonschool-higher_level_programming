#!/usr/bin/node
const array = process.argv.slice(2).sort(function (a, b) { return b - a; });
console.log(array[1]);
