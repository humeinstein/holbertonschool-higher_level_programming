#!/usr/bin/node
// returns # of occrences

exports.nbOccurences = function (list, searchElement) {
  let countOcc = 0;
  for (const iter in list) { if (list[iter] === searchElement) { countOcc++; } }
  return countOcc;
};
