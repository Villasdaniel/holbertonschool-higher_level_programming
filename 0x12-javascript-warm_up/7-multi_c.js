#!/usr/bin/node
//  prints x times “C is fun”

const MyVar = parseInt(process.argv[2]);
if (!MyVar) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < MyVar; i++) {
  console.log('C is fun');
}
