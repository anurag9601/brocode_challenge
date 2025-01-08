function paths(n: number): number {
    if (n == 1 || n == 0) {
        return 1
    }
    return n * paths(n - 1);
}

// console.log(paths(4))
// console.log(paths(9))

function sumNumber(n: number): number {
    if (n == 0 || n == 1) {
        return n
    }

    return n + sumNumber(n - 1)
}

// console.log(sumNumber(5))

function multiSum(n: number, index: number = 1): number {
    if (index > 10) {
        return 0;
    }

    return n * index + multiSum(n, index + 1)
}

// console.log(multiSum(6))
// console.log(multiSum(10))

function reverse(input_str: string): string {
    if (input_str.length == 1 || input_str.length == 0) {
        return input_str;
    }

    return reverse(input_str.slice(1)) + input_str[0]
}

// console.log(reverse("hello"))

function fibo(n: number): number {
    if (n == 0 || n == 1) {
        return n
    }

    return fibo(n - 2) + fibo(n - 1)
}

// console.log(fibo(8))
// console.log(fibo(2))
// console.log(fibo(1))
// console.log(fibo(0))

function GCD(n1: number, n2: number, range: number = 0) {
    if (range == 0) {
        if (n1 > n2) {
            range = n2
        } else {
            range = n1
        }
    }

    if (n1 % range == 0 && n2 % range == 0) {
        return range
    } else {
        return GCD(n1, n2, range - 1)
    }
}

// console.log(GCD(32,8));
// console.log(GCD(17,13));
// console.log(GCD(8, 12));

function findHeighest(nums: number[]): number {
    if (nums.length == 0) {
        return 0;
    } else if (nums.length == 1) {
        return nums[0]
    } else {
        let max = findHeighest(nums.slice(1));
        return max > nums[0] ? max : nums[0]
    }
}

// console.log(findHeighest([-1, 3, 5, 6, 99, 12, 2]))
// console.log(findHeighest([0, 12, 4, 87]))
// console.log(findHeighest([8]))
// console.log(findHeighest([]))

function vowels(input_str: string, count: number = 0): number {
    const Vowels = "aeiou"
    if (input_str == "") {
        return count;
    }

    if (Vowels.includes(input_str[0])) {
        return vowels(input_str.slice(1), count + 1)
    } else {
        return vowels(input_str.slice(1), count)
    }
}

// console.log(vowels("apple"))
// console.log(vowels("cheesecake"))
// console.log(vowels("bbb"))