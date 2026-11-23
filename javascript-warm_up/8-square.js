#!/usr/bin/node
const size = parseInt(process.argv[2], 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let col = 0; col < size; col += 1) {
    row += 'X';
  }
  for (let line = 0; line < size; line += 1) {
    console.log(row);
  }
}
