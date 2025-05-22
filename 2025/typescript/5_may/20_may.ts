//Javascript curry 

function addThreeNum(a: number) {
    return function (b: number) {
        return function (c: number) {
            return a + b + c
        }
    }
}

// console.log(addThreeNum(1)(2)(3))

function maximumSeating(seats: number[]) {
    let index = 0;

    let availableSeats = 0;

    while (index < seats.length) {
        if (seats[index] === 0 && index === 0) {
            if (seats[index + 1] === 0 && seats[index + 2] === 0) {
                availableSeats += 1
                seats[index] = 1
            }
        } else if (seats[index] === 0 && index === seats.length - 2) {
            if (seats[index - 1] === 0 && seats[index - 2] === 0 && seats[index + 1] === 0) {
                availableSeats += 1
                seats[index] = 1
            }
        } else if (seats[index] === 0 && index === seats.length - 1) {
            if (seats[index - 1] === 0 && seats[index - 2] === 0) {
                availableSeats += 1
                seats[index] = 1
            }
        } else if (seats[index] === 0) {
            if (seats[index - 1] === 0 && seats[index - 2] === 0 && seats[index + 1] === 0 && seats[index + 2] === 0) {
                availableSeats += 1
                seats[index] = 1
            }
        }
        index += 1
    }

    return availableSeats;
}

// console.log(maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
// console.log(maximumSeating([0, 0, 0, 0]))
// console.log(maximumSeating([1, 0, 0, 0, 0, 1]))

function generateNonconsecutive(n: number): string {
    const result: string[] = [];

    let startStr: string[] = Array.from<string>({ length: n }).fill("0");

    result.push(startStr.join(""))
    for (let i = n - 1; i > -1; i--) {
        let currentStr = [...startStr]
        currentStr[i] = "1"
        result.push(currentStr.join(""))
    }

    if (n >= 2) {
        for (let i = 0; i < n + 1; i++) {
            if (result[i][0] === "0" && result[i][1] === "0") {
                let currentStr: string[] = [...result[i].split("")]
                currentStr[0] = "1"
                if (!result.includes(currentStr.join(""))) {
                    result.push(currentStr.join(""))
                }
            } else if (result[i].slice(-1)[0] === "0" && result[i].slice(-2)[0] === "0") {
                let currentStr: string[] = [...result[i].split("")]
                currentStr.pop()
                currentStr.push("1")
                if (!result.includes(currentStr.join(""))) {
                    result.push(currentStr.join(""))
                }
            }
        }
    }

    return result.join(" ")
}

// console.log(generateNonconsecutive(1))
// console.log(generateNonconsecutive(2))
// console.log(generateNonconsecutive(3))
// console.log(generateNonconsecutive(4))
// console.log(generateNonconsecutive(5))     

function lessEqual(nums: number[], k: number): number | null {
    if (k == 0) return 1;

    const numsLength = nums.length;

    for (let i = 0; i < numsLength; i++) {
        let min_i = i
        for (let j = i; j < nums.length; j++) {
            if (nums[min_i] > nums[j]) {
                min_i = j
            }
        }
        [nums[i], nums[min_i]] = [nums[min_i], nums[i]]
    }

    const finalList = nums.slice(0, k);
    const remainList = nums.slice(k);

    const result = finalList.slice(-1)[0]

    return finalList.slice(0, -1).includes(result) || remainList.includes(result) ? null : result;

}

// console.log(lessEqual([3, 7, 6, 1, 10, 3, 20], 4))
// console.log(lessEqual([3, 7, 6, 1, 10, 3, 20], 2))
// console.log(lessEqual([3, 7, 5, 1, 10, 3, 20], 4))
// console.log(lessEqual([10, 15, 20, 25], 0))

function simplePair(nums: number[], n: number): number[] | null {
    //for solving this problem we will use two pointer search algorithm

    let x = 0;
    let y = nums.length - 1;

    while (x < y) {
        const currentMulti = nums[x] * nums[y]
        if (currentMulti === n) {
            return [nums[x], nums[y]]
        } else if (currentMulti > n) {
            y -= 1
        } else if (currentMulti < n) {
            x += 1
        } else {
            x += 1
        }
    }

    return null
}

// console.log(simplePair([1, 2, 3], 3));
// console.log(simplePair([1, 2, 3], 6));
// console.log(simplePair([1, 2, 3], 9));

//Now what is this primorial number right 
//In mathematics, primorial, denoted by “#”, is a function from natural numbers to natural numbers similar to the factorial function, but rather than successively multiplying positive integers, the function only multiplies prime numbers.

function primorial(n: number): number {
    function isPrime(num: number) {
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 === 0 || num % 3 === 0) return false;
        for (let i = 5; i < num; i++) {
            if (num % i === 0) return false;
        }
        return true;
    }

    let primeNums: number[] = []
    let result = 1

    let num = 2;

    while (primeNums.length < n) {
        if (isPrime(num) === true) {
            result *= num
            primeNums.push(num)
        }
        num += 1
    }

    return result
}

// console.log(primorial(2))
// console.log(primorial(6))


function simpleCheck(a: number, b: number) {
    let divisbleCount = 0;
    let max: number = a > b ? a : b;
    let min: number = a > b ? b : a;
    while (min !== 0) {
        if (max % min === 0) divisbleCount += 1;
        min -= 1
        max -= 1
    }

    return divisbleCount;
}

// console.log(simpleCheck(3, 5))
// console.log(simpleCheck(8, 4))
// console.log(simpleCheck(54, 17))

function makeTranspose(matrix: unknown[][]): unknown[][] {
    let result: unknown[][] = []
    for (let row = 0; row < matrix[0].length; row++) {
        let tempRow: unknown[] = []
        for (let col = 0; col < matrix.length; col++) {
            tempRow.push(matrix[col][row])
        }
        result.push(tempRow)
    }
    return result
}

// console.log(makeTranspose([
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9]
// ]))
// console.log(makeTranspose([
//     [1, 2],
//     [3, 4],
//     [5, 6]
// ]))
// console.log(makeTranspose([
//     ["a", "b"]
// ]))


function cupSwapping(swaps: string[]) {
    let ballHoldCup = "B";

    for (let swap of swaps) {
        if (swap.includes(ballHoldCup)) {
            if (swap[0] === ballHoldCup) {
                ballHoldCup = swap[1]
            } else if (swap[1] === ballHoldCup) {
                ballHoldCup = swap[0]
            }
        }
    }

    return ballHoldCup;
}

// console.log(cupSwapping(["AB", "CA"]))
// console.log(cupSwapping(["AC", "CA", "CA", "AC"]))
// console.log(cupSwapping(["BA", "AC", "CA", "BC"]))

//Check number is prime or not using binary search algorithm

function isPrime(target: number): string {
    const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

    let low = 0;
    let high = primes.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        if (primes[mid] === target) {
            return "yes"
        } else if (primes[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return "no"
}

// console.log(isPrime(3))
// console.log(isPrime(4))
// console.log(isPrime(67))
// console.log(isPrime(36))

function simpleComp(arr1: number[], arr2: number[]) {
    for (let num of arr1) {
        const numSquare = num ** 2;
        if (!arr2.includes(numSquare)) return false;
    }
    return true;
}

// console.log(simpleComp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]));
// console.log(simpleComp([4, 4], [1, 31]));
// console.log(simpleComp([2, 2, 3], [4, 4, 9]));