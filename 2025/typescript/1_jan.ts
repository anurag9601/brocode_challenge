function reorderDigits(nums_lst: number[], order_code: string): unknown[] {
    let result: unknown[] = []
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