function paths(n: number): number {
    if (n == 1 || n == 0) {
        return 1
    }
    return n * paths(n - 1);
}

// console.log(paths(4))
// console.log(paths(9))

function sum_number(n: number): number {
    if (n == 0 || n == 1) {
        return n
    }

    return n + sum_number(n - 1)
}

// console.log(sum_number(5))

function multi_sum(n: number, index: number = 1): number {
    if (index > 10) {
        return 0;
    }

    return n * index + multi_sum(n, index + 1)
}

// console.log(multi_sum(6))
// console.log(multi_sum(10))

function reverse(input_str:string): string{
    if(input_str.length == 1 || input_str.length == 0){
        return input_str;
    }

    return reverse(input_str.slice(1)) + input_str[0]
}

// console.log(reverse("hello"))

function fibo(n:number): number{
    if(n == 0 || n == 1){
        return n
    }

    return fibo(n - 2) + fibo(n - 1)
}

// console.log(fibo(8))
// console.log(fibo(2))
// console.log(fibo(1))
// console.log(fibo(0))