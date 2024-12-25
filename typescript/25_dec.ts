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

function isPositiveDominant(numLst: number[]): boolean {
    let positiveInt = 0
    let nagativeInt = 0

    const passedInt: number[] = []

    for (let num of numLst) {
        if (num in passedInt) {
            continue;
        } else {
            if (num > 0) {
                positiveInt++;
            } else if (num < 0) {
                nagativeInt++;
            }
            passedInt.push(num)
        }
    }

    return positiveInt > nagativeInt ? true : false;
}

// console.log(isPositiveDominant([1, 1, 1, 1, -3, -4]))
// console.log(isPositiveDominant([5, 99, 832, -3, -4]))

function getFrequencies(input_lst: any[]) {
    const frequencDict: { [key: string]: number } = {}

    for (let i of input_lst) {
        let count = 0
        for (let j of input_lst) {
            if (i.toString() == j.toString()) {
                count++;
            }
        }
        frequencDict[i.toString()] = count
    }

    return frequencDict
}

// console.log(getFrequencies([true, false, true, false, false]))
// console.log(getFrequencies(([1, 2, 3, 3, 2])))

function isHeteromecic(num: number, n: number = 0): boolean {
    if (n * (n + 1) == num) {
        return true;
    }
    if (n * (n + 1) > num) {
        return false;
    }

    return isHeteromecic(num, n + 1);
}

console.log(isHeteromecic(136))
console.log(isHeteromecic(156))
console.log(isHeteromecic(2))