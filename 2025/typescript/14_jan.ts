function largestEven(numArr:number[], largest=-1){
    if (numArr.length == 0){
        return largest
    }

    if(numArr[0] > largest && numArr[0] % 2 == 0){
        largest = numArr[0]
    }
    return largestEven(numArr.slice(1), largest)
}

console.log(largestEven([3, 7, 2, 1, 7, 9, 10, 13]))