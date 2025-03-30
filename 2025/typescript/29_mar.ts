function pascalsTrangle(n: number) {
    let result = [1, 1, 1];
    let sumIndex = 0

    if (n <= 2) return result.splice(0, n)

    for (let i = 3; i < n + 1; i++) {
        sumIndex += 1;
        result.push(1);
        for (let j = 0; j < (i - 2); j++) {
            result.push((result[sumIndex] + result[sumIndex + 1]))
            sumIndex += 1
        }
        result.push(1);
    }
    return result;
}

// console.log(pascalsTrangle(3))
// console.log(pascalsTrangle(4))
// console.log(pascalsTrangle(5))

