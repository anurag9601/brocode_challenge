//For running typescipt file in the terminal use command 
// ts-node <file_name>.ts

// Problem 1
// Create a function which returns the number of true values there are in an array.

// Examples
// countTrue([true, false, false, true, false]) ➞ 2
// countTrue([false, false, false, false]) ➞ 0
// countTrue([]) ➞ 0

//code
function numberOfTrue(arr: boolean[]) {
    let count = 0;
    for (let i of arr) {
        if (i == true) {
            count++;
        }
    }
    return count;
}

console.log(numberOfTrue([true, false, false, true, false]))
console.log(numberOfTrue([false, false, false, false]))
console.log(numberOfTrue([]))

// Problem 2
// Write a function that converts an object into an array of keys and values.

// Examples
// objectToArray({
//     D: 1,
//     B: 2,
//     C: 3
//   }) ➞ [["D", 1], ["B", 2], ["C", 3]]

//   objectToArray({
//     likes: 2,
//     dislikes: 3,
//     followers: 10
//   }) ➞ [["likes", 2], ["dislikes", 3], ["followers", 10]]

const objectToArray = (obj: Record<string, number>) => {
    const result: [string, number][] = [];
    for (let i in obj) {
        result.push([i, obj[i]])
    }

    return result;
}

console.log(objectToArray({
    D: 1,
    B: 2,
    C: 3
}));

console.log(objectToArray({
    likes: 2,
    dislikes: 3,
    followers: 10
}));
