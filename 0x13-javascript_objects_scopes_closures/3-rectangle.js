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

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
