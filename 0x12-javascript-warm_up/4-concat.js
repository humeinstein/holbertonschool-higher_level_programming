#!/usr/bin/node
const first = process.argv[2];
if (first === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(first.concat(' is ', process.argv[3]));
}
