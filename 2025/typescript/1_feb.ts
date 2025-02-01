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