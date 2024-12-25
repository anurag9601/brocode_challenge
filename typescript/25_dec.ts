function saveBoom(inputLstObj: number[]) {
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

function countBoomerangs(inputLst: number[]) {
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
