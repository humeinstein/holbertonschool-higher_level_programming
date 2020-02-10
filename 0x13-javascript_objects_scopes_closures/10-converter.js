#!/usr/bin/node
// converter
exports.converter = function (base) {
  function conversion (number) { return number.toString(base); } return conversion;
};
