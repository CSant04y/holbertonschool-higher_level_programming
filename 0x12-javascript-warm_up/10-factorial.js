#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
