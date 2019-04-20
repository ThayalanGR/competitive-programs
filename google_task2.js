// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S1, S2) {
    // write your code in JavaScript (Node.js 8.9.4)
    
    // variables declaration
    const mainString = S1.split("");
    const testString = S2.split("");
    let sampleOutput = 0;
    let output = 0;
    
    // condition checking
    if(mainString.length != 26 || S2.match(/[A-Z]/g) || isExactlyOnce(mainString)) {
        console.log("iamhere")
        return false;        
    }
    
    if(testString.length < 1 || testString.length > 100000 || S2.match(/[A-Z]/g)) {
        return false;        
    }
    
    // logic starts

    testString.map(item => {
        let index = mainString.indexOf(item);
        sampleOutput = Math.abs(index - sampleOutput);
        output += sampleOutput;
    })
    // logic ends
    
    // throws output
    return output;
    
}

// method for checking the input String contains letters will occur exactly once
function isExactlyOnce(array) {
    for(var i = 0; i < array.length - 1; i++) {
        if(array[i] !== array[i+1]) {
            return false;
        }
    }
    return true;
}