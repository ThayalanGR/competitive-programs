// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, K) {
    // write your code in JavaScript (Node.js 8.9.4)

    // condition checking
    if (K < 1 || K > 300000 || S.length < 1 || S.length > 300000 || !S.match(/^[0-9a-zA-Z-]+$/)) {
        return false;
    }

    // variable declaration
    let inputStringArr = [];
    let inputString = S.replace(/-/gi, "").toUpperCase();
    let outputString = "";
    let masterCount = 0;
    // logic starts
    inputStringArr = inputString.split("").reverse();
    for (var i = 0; i < inputStringArr.length; i++) {
        if (masterCount == K) {
            outputString = "-" + outputString;
            masterCount = 0;
        }
        outputString = inputStringArr[i] + outputString;
        masterCount++;
    }
    // logic ends

    // throws output
    return outputString;
}

console.log(solution("a42923d235-@23", 1));
console.log(solution("a429-23d235-2as233", 3));
console.log(solution("a429-23d235-23$23", 6));
console.log(solution("a429-23d235-23afsd-asf324-rasfd", 4));