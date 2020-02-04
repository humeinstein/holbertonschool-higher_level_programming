#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let iter = 0;
  while (iter < x) {
    theFunction();
    iter++;
  }
};
