#!/usr/bin/node
// script reads and prints contents of a file

const fs = require('fs');
const fileCheck = process.argv[2];
fs.readFile(fileCheck, 'utf-8', function (err, data) {
  if (err) { console.log(err); } else { console.log(data); }
});
