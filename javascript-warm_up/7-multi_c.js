#!/usr/bin/node
const count = parseInt(process.argv[2], 10);

if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i += 1;
  }
}
