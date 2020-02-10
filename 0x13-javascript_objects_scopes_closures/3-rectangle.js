#!/usr/bin/node
// same thing but print it visually

const Rectangle = class Rectangle {
  constructor (wide, high) {
    if (wide > 0 && high > 0) {
      this.width = wide;
      this.height = high;
    }
  }

  print () {
    for (let iter = 0; iter < this.height; iter++) { console.log('X'.repeat(this.width)); }
  }
};
module.exports = Rectangle;
