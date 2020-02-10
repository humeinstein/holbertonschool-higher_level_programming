#!/usr/bin/node
// class Rectangle with some bs inside it that says what it is and does

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

  rotate () {
    const rotates = this.width;
    this.width = this.height;
    this.height = rotates;
  }

  double () {
    this.widht *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;
