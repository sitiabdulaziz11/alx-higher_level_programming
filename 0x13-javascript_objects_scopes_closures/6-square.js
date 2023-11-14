#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let t = 0; t < this.height; t++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
