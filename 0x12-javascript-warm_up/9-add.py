#!/usr/bin/node
const firstInt = process.argv[2];
const secondInt = process.argv[3];
function add (a, b) {
  const c = parseInt(a) + parseInt(b);
  return (c);
}
console.log(add(firstInt, secondInt));
