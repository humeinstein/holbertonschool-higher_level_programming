#!/usr/bin/node
// defines square inheirs from square from #5 char print
const SquareBefore = require('./5-square.js');

const Square = class Square extends SquareBefore {
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let iter = 0; iter < this.width; iter++) { console.log(c.repeat(this.height)); }
    }
  }
};
module.exports = Square;
