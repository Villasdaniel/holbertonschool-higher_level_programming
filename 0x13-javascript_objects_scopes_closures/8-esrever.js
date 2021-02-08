#!/usr/bin/node
// returns the reversed version of a list

exports.esrever = function (list) {
  e = [];
  for (let i = list.length - 1; i >= 0; i--) {
    e.push(list[i]);
  }
  return (e);
};
