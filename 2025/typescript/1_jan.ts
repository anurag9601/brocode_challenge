function reorderDigits(nums_lst: number[], order_code: string): number[] {
    let result: number[] = []
    for (let num of nums_lst) {
        let lst_num: string[] = num.toString().split("");
        for (let i = 0; i < lst_num.length; i++) {
            let mini_max_i: number = i
            for (let j = i; j < lst_num.length; j++) {
                if (order_code == "asc") {
                    if (parseInt(lst_num[j]) < parseInt(lst_num[mini_max_i])) {
                        mini_max_i = j
                    }
                } else {
                    if (parseInt(lst_num[j]) > parseInt(lst_num[mini_max_i])) {
                        mini_max_i = j
                    }
                }
            }
            [lst_num[mini_max_i], lst_num[i]] = [lst_num[i], lst_num[mini_max_i]];
        }
        result.push(parseInt(lst_num.join("")))
    }

    return result;
}

// console.log(reorderDigits([515, 341, 98, 44, 211], "asc"))
// console.log(reorderDigits([515, 341, 98, 44, 211], "desc"))
// console.log(reorderDigits([63251, 78221], "asc"))
// console.log(reorderDigits([63251, 78221], "desc"))
// console.log(reorderDigits([1, 2, 3, 4], "asc"))
// console.log(reorderDigits([1, 2, 3, 4], "desc"))

function countDigits(numsLst: number[], find: string): number[] {
    let conditionCountLst: number[] = []
    for (let num of numsLst) {
        const numLst = num.toString().split("")
        let conditionCount = 0
        for (let n of numLst) {
            if (find === "odd") {
                if (parseInt(n) % 2 !== 0) {
                    conditionCount++;
                }
            }
            else if (find === "even") {
                if (parseInt(n) % 2 == 0) {
                    conditionCount++;
                }
            }
        }
        conditionCountLst.push(conditionCount)
    }

    return conditionCountLst;
}

// console.log(countDigits([22, 53, 99, 61, 777, 8], "odd"))
// console.log(countDigits([22, 53, 99, 61, 777, 8], "even"))
// console.log(countDigits([54, 113, 89, 10], "odd"))
// console.log(countDigits([54, 113, 89, 10], "even"))


function product(a: number, b: number) {
    return function (c: number, d: number) {
        return function (e: number, f: number) {
            return a * c * e + b * d * f
        };
    };
};

// console.log(product(1,2)(1,1)(2,3));
// console.log(product(10,2)(5,0)(2,3));
// console.log(product(1,2)(0,3)(3,0));

function checkScore(input_lst: string[][]) {
    const signs = ["#", "O", "X", "!", "!!", "!!!"];
    const signValue = [5, 3, 1, -1, -3, -5];

    let totalSum = 0

    for (let lst of input_lst) {
        for (let i = 0; i < lst.length; i++) {
            const valueIndex = signs.indexOf(lst[i]);
            totalSum += signValue[valueIndex]
        }
    }
    return totalSum > 0 ? totalSum : 0
}

console.log(checkScore([
    ["#", "!"],
    ["!!", "X"]
]));

console.log(checkScore([
    ["!!!", "O", "!"],
    ["X", "#", "!!!"],
    ["!!", "X", "O"]
]));

console.log(checkScore([
    ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
    ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
    ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
    ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
    ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
    ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
    ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
    ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
    ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
    ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
    ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
    ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
    ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
    ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))