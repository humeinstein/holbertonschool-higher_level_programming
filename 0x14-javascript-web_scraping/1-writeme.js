#!/usr/bin/node
// script writes string to file 

const fs = require('fs');
const fileCheck = process.argv[2];
const contentToFile = process.argv[3];
fs.writeFile(fileCheck, contentToFile, 'utf-8', function (err, data) {
    if (err) { console.log(err) }
});

