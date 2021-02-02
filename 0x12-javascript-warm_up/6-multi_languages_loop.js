#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const MyVar = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let i;
for (i in MyVar) {
  console.log(MyVar[i]);
}
