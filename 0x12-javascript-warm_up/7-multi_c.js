#!/usr/bin/node
const x = 'C is fun';
const aoTimes = process.argv[2];
if (isNaN(parseInt(aoTimes)) === false) {
  let iter = 0;
  while (iter < aoTimes) {
    console.log(x);
    iter++;
  }
} else {
  console.log('Missing number of occurrences');
}
