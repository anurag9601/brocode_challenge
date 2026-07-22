// fibonacci using recursion

function fibonacci(n: number): number {
    if(n <= 1){
        return n;
    }

    return fibonacci(n - 2) + fibonacci(n - 1);
}

console.log(fibonacci(5))