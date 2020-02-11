#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (data, err) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
