#!/usr/bin/node
const size = process.argv[2];
let square = '';
if (isNaN(parseInt(size)) === false) {
  for (let across = 0; across < size; across++) {
    square = '';
    for (let down = 0; down < size; down++) {
      square += ('X');
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
