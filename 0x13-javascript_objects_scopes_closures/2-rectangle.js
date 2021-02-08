#!/usr/bin/node
/* class Rectangle that defines a rectangle
If w or h >= 0 so empty object */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
