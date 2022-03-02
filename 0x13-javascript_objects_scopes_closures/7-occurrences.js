#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter(d => d === searchElement).length;
};
