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