#!/usr/bin/node
/*
classe Rectangle qui définit un rectangle
*/
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && w > 0 && parseInt(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
