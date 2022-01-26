/*
    A number is said to be Disarium if the sum of its 'digits raised to their respective positions' is the number itself.

    Create a function that determines whether a number is a Disarium or not.

    Examples:
    isDisarium(75) ➞ false
    // 7^1 + 5^2 = 7 + 25 = 32

    isDisarium(135) ➞ true
    // 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

    isDisarium(518) ➞ false

    isDisarium(518) ➞ true

    isDisarium(544) ➞ false

    isDisarium(8) ➞ true

    isDisarium(466) ➞ false

    Notes:
    Position of the digit is 1-indexed.
*/

//this function assumes the input is a valid int
function isDisarium(input) {
    input = String(input);

    let disariumSum = 0;
    let pos = 1; //tracks the position of the digit
    for (let digit of input) {
        //raise character to the poswer of the position than add it to the sum
        disariumSum += parseInt(digit) ** pos;
        pos++;
    }
    return input == disariumSum;
}

console.log(isDisarium(75)); //false
console.log(isDisarium(135)); //true
console.log(isDisarium(12)); //false
console.log(isDisarium(518)); //true
console.log(isDisarium(544)); //false
console.log(isDisarium(8)); //true
console.log(isDisarium(466)); //false