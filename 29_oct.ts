//Problem 1 map 
// Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
// The returned array should be created such that returnedArray[i] = fn(arr[i], i).
// Please solve it without the built-in Array.map method.

// Example 1:
// Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
// Output: [2,3,4]
// Explanation:
// const newArray = map(arr, plusone); // [2,3,4]
// The function increases each value in the array by one. 

// Example 2:
// Input: arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
// Output: [1,3,5]
// Explanation: The function increases each value by the index it resides in.

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const result = []
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i))
    }
    return result
};

// const arr: number[] = [1, 2, 3];
// const fn = function (n: number, i: number) { return n + i };
// console.log(map(arr, fn))

//Problem 2 filter
// Given an integer array arr and a filtering function fn, return a filtered array filteredArr.
// The fn function takes one or two arguments:
// arr[i] - number from the arr
// i - index of arr[i]
// filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.
// Please solve it without the built-in Array.filter method.

// Example 1:
// Input: arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
// Output: [20,30]
// Explanation:
// const newArray = filter(arr, fn); // [20, 30]
// The function filters out values that are not greater than 10

// Example 2:
// Input: arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
// Output: [1]
// Explanation:
// fn can also accept the index of each element
// In this case, the function removes elements not at index 0

const filter = (arr: number[], fn: (n: number, i: number) => boolean): number[] => {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        const isValid = fn(arr[i], i);
        if (isValid == true) {
            result.push(arr[i])
        };
    }
    return result;
}

//Example
// const arr = [0, 10, 20, 30];
// const fn = function greaterThan10(n:number) { return n > 10; };
// console.log(filter(arr, fn));





