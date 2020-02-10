#!/usr/bin/node
// class Rectangle : width & height: w or h == 0 make positive

const Rectangle = class Rectangle {
  constructor (wide, high) {
    if (wide > 0 && high > 0) {
      this.width = wide;
      this.height = high;
    }
  }
};
module.exports = Rectangle;
