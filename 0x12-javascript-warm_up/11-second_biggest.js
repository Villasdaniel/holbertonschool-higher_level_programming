#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const MyVar = []; let i;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    MyVar.push(parseInt(process.argv[i]));
  }
  MyVar.sort();
  console.log(MyVar[MyVar.length - 2]);
}
