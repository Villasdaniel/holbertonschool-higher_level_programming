#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const MyVar = []; let i;
for (i = 2; i < process.argv.length; i++) {
  MyVar.push(parseInt(process.argv[i]));
}
if (MyVar.length > 1) {
  MyVar.sort();
  console.log(MyVar[MyVar.length - 2]);
}
console.log(0);
