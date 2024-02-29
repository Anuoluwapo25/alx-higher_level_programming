#!/usr/bin/node

exports.esrever = function (list) {
// get the middle value ==> 4 [1, 2, 3, 4, 5]

  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    // move pointers towards each other
    start++;
    end--;
  }
  return list;
};
