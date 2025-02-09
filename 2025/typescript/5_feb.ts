function indexOfSubarray(arr: number[], target: number, index = 0): number[] {
    for (let start = 0; start < arr.length; start++) {
        let currentSum = 0;
        for (let end = start; end < arr.length; end++) {
            currentSum += arr[end];
            if (currentSum === target) {
                return [start + 1, end + 1];
            }

            if (currentSum > target) {
                break;
            }
        }
    }

    return [-1];
}

// console.log(indexOfSubarray([1, 2, 3, 7, 5], 12));

function kadanesAlgo(arr: number[]) {
    let largestSum = -Infinity;

    for (let start = 0; start < arr.length; start++) {
        let currentSum = 0;
        for (let end = start; end < arr.length; end++) {
            currentSum += arr[end]
            if (currentSum > largestSum) {
                largestSum = currentSum
            }
        }
    }
    return largestSum;

}

// console.log(kadanesAlgo([2, 3, -8, 7, -1, 2, 3]))
// console.log(kadanesAlgo([-2, -4]))
// console.log(kadanesAlgo([5, 4, 1, 7, 8]))

function minimumJump(arr: number[]) {
    let minimumJump = 0;
    let index = 0

    while (index < arr.length - 1) {
        if (arr[index] == 0 && index !== arr.length -1 && arr[index + 1] > 0) {
            return -1
        }
        index += arr[index]
        minimumJump += 1;
    }

    return minimumJump == 0 ? -1 : minimumJump;
}

console.log(minimumJump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]));
console.log(minimumJump([1, 4, 3, 2, 6, 7]));
console.log(minimumJump([0, 10, 20]));
// console.log(minimumJump([9, 10, 1, 2, 3, 4, 8, 0, 0, 0, 0, 0, 0, 0, 1]));