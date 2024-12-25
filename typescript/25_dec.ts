function saveBoom(inputLstObj: number[]): string {
    for (let numI: number = 0; numI < inputLstObj.length; numI++) {
        const strInt: string = inputLstObj[numI].toString();
        if (strInt.includes("7")) {
            return "Boom!"
        };
    }

    return "There is no 7 in the array"
}

// console.log(saveBoom([1, 2, 3, 4, 5, 6, 7]));
// console.log(saveBoom([8, 6, 33, 100]));

function countBoomerangs(inputLst: number[]): number {
    let noOfBoomerangs: number = 0

    for (let i = 0; i < inputLst.length; i++) {
        let tempLst: number[] = []
        for (let j = i; j < inputLst.length; j++) {
            tempLst.push(inputLst[j])
            if (tempLst.length == 3) {
                if (tempLst[0] == tempLst[2] && tempLst[1] !== tempLst[0]) {
                    noOfBoomerangs++;
                }
                break
            }
        }
    }

    return noOfBoomerangs;
}

// console.log(countBoomerangs([9, 5, 9, 5, 1, 1, 1]))
// console.log(countBoomerangs([3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]))
// console.log(countBoomerangs([4, 4, 4, 9, 9, 9, 9]))
// console.log(countBoomerangs([5, 6, 6, 7, 6, 3, 9]))

function getLength(nestedList: unknown[]): number {
    let lengthCount: number = 0

    for (let element of nestedList) {
        if (Array.isArray(element)) {
            lengthCount += getLength(element)
        } else {
            lengthCount++;
        }
    }

    return lengthCount
}

// console.log(getLength([1, [2, [3, [4, [5, 6]]]]]))
// console.log(getLength([1, [2], 1, [2], 1]))

function invert(inputStr: string): string {
    if (inputStr == "") {
        return ""
    }
    const currentString: string = inputStr[0].toLowerCase() == inputStr[0] ? inputStr[0].toUpperCase() : inputStr[0].toLowerCase()
    return invert(inputStr.slice(1)) + currentString
}

// console.log(invert("dLROW YM sI HsEt"))
// console.log(invert("ytInIUgAsnOc"))

function numInStr(inputLst: string[]): string[] {
    const result: string[] = []

    const numLst: string[] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for (let str of inputLst) {
        for (let letter of str) {
            if (letter in numLst) {
                result.push(str);
                break
            }
        }
    }

    return result
}

// console.log(numInStr(["1a", "a", "2b", "b"]))
// console.log(numInStr(["abc", "abc10"]))
// console.log(numInStr(["abc", "ab10c", "a10bc", "bcd"]))
// console.log(numInStr(["this is a test", "test1"]))