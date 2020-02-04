#!/usr/bin/node
const lengthOfList = (process.argv.length - 2);
const position = process.argv;
function sortedFor (position, lengthOfList) {
  const hold = [];
  for (let iter = 0; iter < lengthOfList; iter++) {
    if (position[iter] < 0) { hold.push([Math.abs(iter + 2)]); }
    hold.push(position[iter + 2]);
  }
  const sortedList = hold.sort();
  const sortedLength = sortedList.length;
  const max = sortedList[sortedLength - 2];
  return (max);
}
if (process.argv.length < 4) { console.log(0); } else {
  console.log(sortedFor(position, lengthOfList));
}
