#!/usr/bin/node
// return reverse list

exports.esrever = function (list) {
  const reverse = [];
  for (let iter = 0; iter < list.length; iter++) { reverse.unshift(list[iter]); }
  return reverse;
};
