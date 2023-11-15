#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let h = (list.length - 1); h >= 0; h--) {
    reversedList.push(list[h]);
  }
  return reversedList;
};
