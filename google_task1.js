// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    
    const inputArray = A;
    let levels = [];
    let levelIndicator = 1;
    let count = 0;
    
    // condition checking 
    
    if(A.length < 1 || A.length > 1000) {
        return false;
    }
    
    A.map((item) => {
        if(item < -100000 || item > 100000) {
            return false;
        }
    })
    
    
    // logic starts
    for(let i = 0; i < inputArray.length; i++) {
        if(count < levelIndicator) {
            levels.push(inputArray[i].toString());
        } else {
            levels.push("*")            
            levels.push(inputArray[i].toString());
            levelIndicator = levelIndicator*2;
            count = 0;
        }
        count++;
    }
    let array = levels.join().split("*");
    let commonArray = []
    array.map(item => {
      let temp = 0;
      item.split(",").map((item) => {
          temp += Number(item)
      })
      commonArray.push(temp)
    })
    let max = Math.max(...commonArray)
    let output = commonArray.indexOf(max) + 1;
    // logic ends 
    
    // throws output
    return output;
    
}