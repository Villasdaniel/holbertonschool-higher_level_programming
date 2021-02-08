#!/usr/bin/node
// class Square inherits from 5-square
const Squareone = require('./5-square.js');
class Square extends Squareone {
  charPrint (C) {
    if (C == null) {
      C = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(C.repeat(this.width));
    }
  }
}
module.exports = Square;
