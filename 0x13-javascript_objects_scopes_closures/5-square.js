#!/usr/bin/node
/*
la classe Carré qui définit un carré et hérite
de Rectangle de 4-rectangle.js
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
