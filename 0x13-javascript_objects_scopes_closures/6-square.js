#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (a = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(a.repeat(this.width));
    }
  }
};
