function sevenBoom(input_arr: number[]): string {
    for (let num of input_arr) {
        const str_num = num.toString();
        if (str_num.includes("7")) {
            return "Boom!"
        }
    }

    return "there is no 7 in the array"
}

// console.log(sevenBoom([1, 2, 3, 4, 5, 6, 7]))
// console.log(sevenBoom([8, 6, 33, 100]))
// console.log(sevenBoom([2, 55, 60, 97, 86]))

function coinsCombinations(total: number, coin_arr: number[], index = 0): number {
    if (total == 0) {
        return 1;
    }

    if (total < 0 || index === coin_arr.length) {
        return 0;
    }

    let includeCurrentCoin: number = coinsCombinations(total - coin_arr[index], coin_arr, index);

    let skipCurrentCoin: number = coinsCombinations(total, coin_arr, index + 1);

    return includeCurrentCoin + skipCurrentCoin
}

// console.log(coinsCombinations(4, [1, 2]));
// console.log(coinsCombinations(10, [5, 2, 3]));
// console.log(coinsCombinations(11, [5, 7]))

function charAtPos(input: unknown[] | string, condition: string): unknown[] | string {
    let indexCount: number = 1
    const filtered_arr: unknown[] | string = []
    for (let i = input.length - 1; i >= 0; i--) {
        if (condition == "even" && indexCount % 2 == 0) {
            filtered_arr.splice(0, 0, input[i])
        } else if (condition == "odd" && indexCount % 2 != 0) {
            filtered_arr.splice(0, 0, input[i])
        }
        indexCount++;
    }
    if (Array.isArray(input)) {
        return filtered_arr;
    } else {
        return filtered_arr.join("")
    }
}

// console.log(charAtPos([2, 4, 6, 8, 10], "even"));
// console.log(charAtPos("EDABIT", "odd"));
// console.log(charAtPos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd"));

function zeroesToEnd(input_arr: number[]) {
    if (!input_arr.includes(0)) {
        return input_arr;
    };

    let itretion = 0;
    let shortLength = 0;
    while (itretion < input_arr.length - shortLength) {
        for (let i = 0; i < input_arr.length - shortLength; i++) {
            if (input_arr[i] == 0) {
                input_arr.splice(i, 1)
                input_arr.push(0)
                shortLength++;
            }
        }
        itretion++;
    }
    return input_arr
}

// console.log(zeroesToEnd([1, 2, 0, 0, 4, 0, 5]));
// console.log(zeroesToEnd([0, 0, 2, 0, 5]));
// console.log(zeroesToEnd([4, 4, 5]));
// console.log(zeroesToEnd([0, 0]));


function zeroesShiftToEnd(arrNums: number[]) {
    let zero_num_count = 0
    for (let i = 0; i < arrNums.length; i++) {
        if (arrNums[i] != 0) {
            [arrNums[i], arrNums[zero_num_count]] = [arrNums[zero_num_count], arrNums[i]]
            zero_num_count++;
        }
    }

    return arrNums
}

// console.log(zeroesShiftToEnd([1, 2, 0, 0, 4, 0, 5]));
// console.log(zeroesShiftToEnd([0, 0, 2, 0, 5]));