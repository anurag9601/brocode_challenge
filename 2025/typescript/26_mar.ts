// problem
let nestedList = [1, [2, 3], [4, 5]]

type nestedNumberArray = number | nestedNumberArray[]

//Using recursion
function sumOfNestedList(list: nestedNumberArray): number {
    if (typeof list === "number") return list

    let sum: number = 0;

    for (let ele of list) {
        sum += Array.isArray(ele) ? sumOfNestedList(ele) : ele
    }

    return sum
}

// console.log(sumOfNestedList(nestedList))

//Using build in functions
// console.log(nestedList.flat(2).reduce((a,b) => a + b, 0))

function partitionString(s: string): number {
    let listStr = []
    let tempStr = ""
    for (let char of s) {
        if (!tempStr.includes(char)) {
            tempStr += char
        } else {
            listStr.push(tempStr)
            tempStr = ""
            tempStr += char
        }
    }
    listStr.push(tempStr)
    return listStr.length
}

// console.log(partitionString("abacaba"))

function findDuplicates(arr: number[]) {
    let seen = new Set()
    let duplicates = new Set()

    for (let num of arr){
        if(seen.has(num)){
            duplicates.add(num)
        }
        seen.add(num)
    }

    return Array.from(duplicates)
}

// console.log(findDuplicates([2, 3, 1, 2, 3]))