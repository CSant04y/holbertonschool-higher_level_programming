#!/usr/bin/node

// This script prints "My number: <first argument converted in integer>"

if (process.argv[2] && Number(process.argv[2])) {
  console.log('My number: %d2f', process.argv[2]);
} else {
  console.log('Not a number');
}
