// Function that generates a list of random numbers

function generateRandomNumbers(n, start, end) {
    return Array.from({length: n}, () => Math.floor(Math.random() * (end - start + 1)) + start);
}

// Ask user for the number of random numbers and the range
const n = parseInt(prompt("Enter the number of random numbers: "));
const start = parseInt(prompt("Enter the start of the range: "));
const end = parseInt(prompt("Enter the end of the range: "));

// Generate and print the list of random numbers
const randomNumbers = generateRandomNumbers(n, start, end);
console.log('The list of '+ n + ' random numbers between ' + start + ' and ' + end + ' is: ' + randomNumbers)