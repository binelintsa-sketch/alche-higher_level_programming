#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstNum = parseInt(process.argv[2], 10);
const secondNum = parseInt(process.argv[3], 10);

console.log(add(firstNum, secondNum));
