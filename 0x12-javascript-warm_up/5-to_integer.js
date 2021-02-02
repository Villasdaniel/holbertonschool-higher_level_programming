#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const MyVar = parseInt(process.argv[2]);
if (!MyVar) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + MyVar);
}
