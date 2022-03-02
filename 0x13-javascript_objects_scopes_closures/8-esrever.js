#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length;
  const a = [];
  while (list[i - 1]) {
    a.push(list[i - 1]);
    --i;
  }
  return a;
};
