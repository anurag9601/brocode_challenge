function fibStr(n: number, arrStr: string[]): string[] {
    if (n > 2) {
        for (let i = 1; i < n - 1; i++) {
            arrStr.push(arrStr[i] + arrStr[i - 1])
        }
    }
    return arrStr
}

// console.log(fibStr(3, ["j", "h"]));
// console.log(fibStr(5, ["e", "a"]));
// console.log(fibStr(6, ["n", "k"]));

//using recursion

function fibStrRecur(n: number, arrStr: string[], index: number = 1): string[] {
    if (index == n - 1) {
        return arrStr
    } else {
        arrStr.push(arrStr[index] + arrStr[index - 1])
        return fibStrRecur(n, arrStr, index + 1)
    }
}

// console.log(fibStrRecur(3, ["j", "h"]));
// console.log(fibStrRecur(5, ["e", "a"]));
// console.log(fibStrRecur(6, ["n", "k"]));

function sentence(arrStr: string[]): string {
    function isVowel(str: string): boolean {
        const vowel: string = "aeiou"
        if (vowel.includes(str[0].toLowerCase())) {
            return true;
        }
        return false;
    }
    if (arrStr.length == 1) {
        const firstLetterVowel: boolean = isVowel(arrStr[0]);

        if (firstLetterVowel) {
            return `An ${arrStr[0]}.`
        }

        return `A ${arrStr[0]}.`
    }

    let returnStr: string = ""
    for (let i = 0; i < arrStr.length; i++) {
        const firstLetterVowel: boolean = isVowel(arrStr[i][0])
        if (firstLetterVowel) {
            if (i == 0) {
                returnStr += "An "
            }
            if (i != 0) {
                returnStr += "an "
            }
        } else if (!firstLetterVowel) {
            if (i == 0) {
                returnStr += "A "
            }
            if (i != 0) {
                returnStr += "a "
            }
        }
        returnStr += arrStr[i]
        if (i == arrStr.length - 2) {
            returnStr += " and "
        }
        if (i == arrStr.length - 1) {
            returnStr += "."
        }
        if (i < arrStr.length - 2) {
            returnStr += ", "
        }
    }

    return returnStr
}

// console.log(sentence(["orange", "apple", "pear"]));
// console.log(sentence(["keyboard", "mouse"]));
// console.log(sentence(["keyboard"]));
// console.log(sentence(["car", "plane", "truck", "boat"]));


function isShuffledWell(arrNums: number[]) {
    let notWell = 0;
    let prev = 0;
    for (let num of arrNums) {
        if (notWell == 3) {
            return false;
        }
        if (num == prev + 1 || num == prev - 1) {
            if (notWell == 0) {
                notWell = notWell + 2
            } else {
                notWell++;
            }
            prev = num;
        } else {
            prev = num
            notWell = notWell > 0 ? 0 : notWell
        }
    }

    return true;
}

// console.log(isShuffledWell([9, 2, 3, 4, 8, 6, 1, 10, 7, 5]));
// console.log(isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]));
// console.log(isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]));
// console.log(isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]));

function block(arrRows: number[][]): number {
    let blockedPeople = 0;
    for (let row = 0; row < arrRows.length; row++) {
        for (let col = 0; col < arrRows[row].length; col++) {
            if (arrRows[row][col] == 2) {
                blockedPeople += (arrRows.length - 1) - row
            }
        }
    }

    return blockedPeople
}

// console.log(block([
//     [1, 1, 1, 1, 1],
//     [1, 1, 1, 1, 1],
//     [1, 1, 1, 1, 2],
//     [1, 1, 1, 1, 1],
//     [1, 1, 1, 1, 1]
// ]));
// console.log(block([
//     [1, 2, 1, 1],
//     [1, 1, 1, 2],
//     [1, 1, 1, 1],
//     [1, 1, 1, 1],
// ]));
// console.log(block([
//     [1, 1, 1, 1],
//     [2, 1, 1, 2],
//     [1, 1, 1, 1],
//     [1, 1, 1, 1],
// ]));

function doesTriangleFit(arr1: number[], arr2: number[]) {
    function validTriangle(arr: number[]) {
        if ((arr[0] + arr[1]) <= arr[2]) {
            return false
        } else if ((arr[0] + arr[2]) <= arr[1]) {
            return false
        } else if ((arr[1] + arr[2]) <= arr[0]) {
            return false
        }
        return true
    }

    const arr1IsValid = validTriangle(arr1);
    const arr2IsValid = validTriangle(arr2);

    if (!arr1IsValid || !arr2IsValid) {
        return false;
    }

    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] > arr2[i]) {
            return false;
        }
    }

    return true;
}

// console.log(doesTriangleFit([1, 1, 1], [1, 1, 1]));
// console.log(doesTriangleFit([1, 1, 1], [2, 2, 2]));
// console.log(doesTriangleFit([1, 2, 3], [1, 2, 2]));
// console.log(doesTriangleFit([1, 2, 4], [1, 2, 6]));

interface objectDataType {
    color: string,
    number: number,
    shade: string,
    shape: string,
}

function isSet(arrObject: objectDataType[]) {
    for (let key of Object.keys(arrObject[0]) as (keyof objectDataType)[]) {
        let setOfValues = new Set();
        for (let i = 0; i < arrObject.length; i++) {
            setOfValues.add(arrObject[i][key])
        }
        if (setOfValues.size !== 1 && setOfValues.size !== arrObject.length) {
            return false
        }
    }
    return true
};

// console.log(isSet([
//     { color: "green", number: 1, shade: "empty", shape: "squiggle" },
//     { color: "green", number: 2, shade: "empty", shape: "diamond" },
//     { color: "green", number: 3, shade: "empty", shape: "oval" }
// ]));
// console.log(isSet([
//     { color: "purple", number: 1, shade: "full", shape: "oval" },
//     { color: "green", number: 1, shade: "full", shape: "oval" },
//     { color: "red", number: 1, shade: "full", shape: "oval" }
// ]));
// console.log(isSet([
//     { color: "purple", number: 3, shade: "full", shape: "oval" },
//     { color: "green", number: 1, shade: "full", shape: "oval" },
//     { color: "red", number: 3, shade: "full", shape: "oval" }
// ]))

function lowestElement(arr: number[][], x: number, y: number): number {
    let currentLowest: number = arr[x][y]

    if (x != 0) {
        currentLowest = currentLowest > arr[x - 1][y] ? arr[x - 1][y] : currentLowest

        if (y != 0) {
            currentLowest = currentLowest > arr[x - 1][y - 1] ? arr[x - 1][y - 1] : currentLowest
        }

        if (y != arr[0].length) {
            currentLowest = currentLowest > arr[x - 1][y + 1] ? arr[x - 1][y + 1] : currentLowest
        }
    }

    if (x != arr.length - 1) {
        currentLowest = currentLowest > arr[x + 1][y] ? arr[x + 1][y] : currentLowest

        if (y != 0) {
            currentLowest = currentLowest > arr[x + 1][y - 1] ? arr[x + 1][y - 1] : currentLowest
        }

        if (y != arr[0].length) {
            currentLowest = currentLowest > arr[x + 1][y + 1] ? arr[x + 1][y + 1] : currentLowest
        }
    }

    if (y != 0) {
        currentLowest = currentLowest > arr[x][y - 1] ? arr[x][y - 1] : currentLowest
    }

    if (y != arr[0].length) {
        currentLowest = currentLowest > arr[x][y + 1] ? arr[x][y + 1] : currentLowest
    }

    return currentLowest
}

// console.log(lowestElement([
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9]
// ], 1, 1));

// console.log(lowestElement([
//     [9, 8, 7],
//     [0, -1, -3],
//     [-5, -9, 54]
// ], 0, 0));

function majorityVote(arr: string[]) {
    let voteObj: { [key: string]: number } = {};
    for (let x of arr) {
        if (!voteObj[x]) {
            let voteCount = 0;
            for (let y of arr) {
                if (x == y) {
                    voteCount++;
                }
            }
            voteObj[x] = voteCount;
        }
    }

    let maxVote = 0;
    let letter: string | null = null;
    for (let key of Object.keys(voteObj)) {
        if (voteObj[key] > maxVote) {
            maxVote = voteObj[key];
            letter = key;
        } else if (maxVote == voteObj[key]) {
            letter = null;
        }
    }

    return letter;
}

// console.log(majorityVote(["A", "A", "B"]));
// console.log(majorityVote(["A", "A", "A", "B", "C", "A"]));
// console.log(majorityVote(["A", "B", "B", "A", "C", "C"]));
// console.log(majorityVote(["X", "X", "X", "Y", "Y"]));
// console.log(majorityVote(["Z", "Z", "Z", "Z", "Y", "Y", "Y"]));
// console.log(majorityVote(["M", "N", "M", "N", "M", "N", "M"]));
// console.log(majorityVote(["A"]));
// console.log(majorityVote(["A", "B", "C", "D", "E", "F"]));
// console.log(majorityVote([]));
// console.log(majorityVote(["A", "A", "A", "B", "B", "B", "A"]));
