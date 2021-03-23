#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = 0;

  for (i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
