#!/usr/bin/node
// prints a square

const MyVar = parseInt(process.argv[2]);
if (!MyVar) {
  console.log('Missing size');
}
for (let i = 0; i < MyVar; i++) {
  console.log('X'.repeat(MyVar));
}
