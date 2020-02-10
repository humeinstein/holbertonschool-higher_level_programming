#!/usr/bin/node
// define rectangle height and width in class desc

const Rectangle = class Rectangle {
  constructor (wide, high) {
    this.width = wide;
    this.height = high;
  }
};
module.exports = Rectangle;
