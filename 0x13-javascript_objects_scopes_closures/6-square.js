#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  charPrint (a = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(a.repeat(this.width));
    }
  }
};
