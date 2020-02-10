#!/usr/bin/node
// logs printed and new value
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
