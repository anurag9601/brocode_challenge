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