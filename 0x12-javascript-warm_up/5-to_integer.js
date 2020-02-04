#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) === false) {
  console.log('My number: '.concat(parseInt(process.argv[2])));
} else {
  console.log('Not a number');
}
