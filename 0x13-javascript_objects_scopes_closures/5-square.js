#!/usr/bin/node
// make class square that inherits rectangle
const Rectangle = require('./4-rectangle.js');
const Square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = Square;
