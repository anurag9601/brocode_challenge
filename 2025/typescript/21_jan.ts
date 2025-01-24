function product(numLst: number[], maxOrMin: string) {
    function maxProduct(numLst: number[]) {
        let maxProduct: number = -Infinity;
        for (let i = 0; i < numLst.length; i++) {
            let tempLst = [...numLst];
            tempLst.splice(i, 1)
            for (let j = 0; j < tempLst.length - 1; j++) {
                let currentSum = numLst[i] * tempLst[j] * tempLst[j + 1];
                if (currentSum > maxProduct) {
                    maxProduct = currentSum
                }
            }
        }
        return maxProduct
    }

    function minProduct(numLst: number[]) {
        let minProduct: number = Infinity;
        for (let i = 0; i < numLst.length; i++) {
            let tempLst = [...numLst];
            tempLst.splice(i, 1)
            for (let j = 0; j < tempLst.length - 1; j++) {
                let currentSum = numLst[i] * tempLst[j] * tempLst[j + 1];
                if (currentSum < minProduct) {
                    minProduct = currentSum
                }
            }
        }
        return minProduct
    }

    if (maxOrMin == "max") {
        return maxProduct(numLst);
    } else {
        return minProduct(numLst);
    }
}

// console.log(product([-8, -9, 1, 2, 7], "max"))
// console.log(product([-8, 1, 2, 7, 9], "max"))
// console.log(product([1, -1, 1, 1], "min"))
// console.log(product([-5, -3, -1, 0, 4], "min"))


function minLength(numLst: number[], num: number) {
    let sortestLength: number = Infinity;
    for (let i = 0; i < numLst.length - 1; i++) {
        let arrCount = 0;
        let currentSum = 0;
        for (let j = i; j < numLst.length; j++) {
            currentSum += numLst[j]
            arrCount++;
            if (currentSum > num) {
                if (arrCount < sortestLength) {
                    sortestLength = arrCount
                }
                break;
            }
        }
    }
    return sortestLength === Infinity ? -1 : sortestLength
}

// console.log(minLength([5, 8, 2, -1, 3, 4], 9));
// console.log(minLength([3, -1, 4, -2, -7, 2], 4));
// console.log(minLength([1, 0, 0, 0, 1], 1));
// console.log(minLength([0, 1, 1, 0], 2));