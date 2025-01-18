function rootDigit(n: number, sum: number = 0): number {
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

function isPalindrome(str: string): boolean {
    if (str.length <= 1) {
        return true
    } else if (str[0] != str[str.length - 1]) {
        return false
    }
    return isPalindrome(str.slice(1, -1))
}

// console.log(isPalindrome("abcba"))
// console.log(isPalindrome("b"))
// console.log(isPalindrome(""))
// console.log(isPalindrome("ab"))

function bugger(n: number, sum: number = 1, recurCount = 0) {
    let lstNum = n % 10
    sum *= lstNum
    if (n < 10 && sum < 10) {
        return recurCount > 0 ? recurCount + 1 : recurCount
    }
    if (n < 10) {
        return bugger(sum, 1, recurCount+1)
    }
    return bugger(Math.floor(n / 10), sum, recurCount)
}

// console.log(bugger(39))
// console.log(bugger(999))
// console.log(bugger(4))