function is_happy(n: number) {
    let result = 0;
    while (n !== 0) {
        const lastInt = n % 10
        n = Math.floor(n / 10)
        result += lastInt ** 2
    }

    if (result == 1 || result == 4) {
        return result === 1 ? true : false;
    } else {
        return is_happy(result)
    }
}

// console.log(is_happy(67))
// console.log(is_happy(89))
// console.log(is_happy(139))
// console.log(is_happy(3970))