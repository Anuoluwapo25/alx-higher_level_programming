#!/usr/bin/node

function findSecondLargest(args) {
    if (args.length <= 1) {
        return 0;
    }

    const numbers = args.map(Number).filter(num => !isNaN(num));
    const uniqueNumbers = Array.from(new Set(numbers));

    if (uniqueNumbers.length <= 1) {
        return 0;
    }

    const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);
    return sortedNumbers[1];
}

const argumentsList = process.argv.slice(2);
const result = findSecondLargest(argumentsList);

console.log(result);

