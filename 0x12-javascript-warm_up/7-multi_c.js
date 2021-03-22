#!/usr/bin/node

if (process.argv[2] && Number(process.argv[2])) {
  for (let itr = 0; itr < Number(process.argv[2]); itr++) {
    console.log('C is fun');
  }
}
