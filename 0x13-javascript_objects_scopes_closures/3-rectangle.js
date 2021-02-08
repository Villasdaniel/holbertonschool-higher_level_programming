#!/usr/bin/node
/* class Rectangle that defines a rectangle
method print() prints the rectangle using X */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
