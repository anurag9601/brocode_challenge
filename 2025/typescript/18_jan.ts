function rootDigit(n: number, sum: number = 0) {
    let lstNum = n % 10
    sum = sum + lstNum
    let strSum = sum.toString()
    if (n == 0 && strSum.length == 1) return sum
    else if (n == 0 && strSum.length > 1) {
        n = parseInt(strSum)
        return rootDigit(n, sum = 0)
    }
    return rootDigit(Math.floor(n / 10), sum)
}

// console.log(rootDigit(123))
// console.log(rootDigit(999888777))
// console.log(rootDigit(1238763636555555555555))

