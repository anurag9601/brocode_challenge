function sevenBoom(input_arr: number[]): string {
    for (let num of input_arr) {
        const str_num = num.toString();
        if (str_num.includes("7")) {
            return "Boom!"
        }
    }

    return "there is no 7 in the array"
}

console.log(sevenBoom([1, 2, 3, 4, 5, 6, 7]))
console.log(sevenBoom([8, 6, 33, 100]))
console.log(sevenBoom([2, 55, 60, 97, 86]))