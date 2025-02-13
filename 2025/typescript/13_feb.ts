function majority_element(arr: number[]) {
    if (arr.length == 0) {
        return -1;
    }

    let dict_obj: { [key: number]: number } = {}
    let arrHalf = arr.length / 2
    for (let num of arr) {
        if (!dict_obj[num]) {
            let currentNCount = 0;
            for (let n of arr) {
                if (num == n) {
                    currentNCount++;
                }
            }
            if (currentNCount > arrHalf) {
                return num;
            }
            dict_obj[num] = currentNCount;
        }
    }
    return -1;
}

// console.log(majority_element([3, 1, 3, 3, 2]))
// console.log(majority_element([7]))
// console.log(majority_element([2, 13]))

function kSmallest(arr: number[], k: number) {
    for (let i = 0; i < arr.length; i++) {
        let min_i = i
        for (let j = i; j < arr.length; j++) {
            if (arr[j] < arr[min_i]) {
                min_i = j
            }
        }
        [arr[i], arr[min_i]] = [arr[min_i], arr[i]]
        if (i == k - 1) {
            return arr[k - 1]
        }
    }
}

// console.log(kSmallest([7, 10, 4, 3, 20, 15], 3))
// console.log(kSmallest([2, 3, 1, 20, 15], 4))

//Solving this problem using stack approach first in last out or last in first out
function paranthesisCheck(s: string) {
    let stack: string[] = []
    let breacket_map: { [key: string] : string} = { ")" : "(" , "]" : "[" , "}" : "{"}
    for(let char of s){
        if(Object.values(breacket_map).includes(char)){
            stack.push(char)
        }else if(stack.length == 0 || stack.pop() != breacket_map[char]){
            return false
        }
    }

    return stack.length == 0
}

// console.log(paranthesisCheck("[()()]{}"))
// console.log(paranthesisCheck("([]"))
// console.log(paranthesisCheck("([{]})"))

function inversionCount(arr: number[]){
    let sort_arr = arr.toSorted((a , b) => a - b)
    if(arr == sort_arr){
        return 0;
    }
    let inversionCount = 0;
    for(let i=0; i<arr.length - 1; i++){
        for(let j=i + 1; j<arr.length; j++){
            if(arr[i] > arr[j]){
                inversionCount++;
            }
        }
    }

    return inversionCount;
}

// console.log(inversionCount([2, 4, 1, 3, 5]))
// console.log(inversionCount([2, 3, 4, 5, 6]))
// console.log(inversionCount([10, 10, 10]))

function findEquilibrium(arr: number[]){
    if (arr.length == 0){
        return -1;
    }

    let lsum = 0;
    let rsum = arr.reduce((acc, num) => acc + num , 0) - arr[0]

    for (let i=1; i<arr.length; i++){
        lsum += arr[i - 1]
        rsum -= arr[i]

        if(lsum == rsum){
            return i;
        }
    }

    return -1
}

// console.log(findEquilibrium([1, 2, 0, 3]))
// console.log(findEquilibrium([-7, 1, 5, 2, -4, 3, 0]))

function leaders(arr: number[]){
    let result = []
    for(let i=0; i<arr.length; i++){
        let isLeader = true;
        for(let j=i; j<arr.length; j++){
            if(arr[i] < arr[j]){
                isLeader = false;
                break;
            }
        }
        if(isLeader){
            result.push(arr[i])
        }
    }

    return result;
}

// console.log(leaders([16, 17, 4, 3, 5, 2]))
// console.log(leaders([10, 4, 2, 4, 1]))
// console.log(leaders([5, 10, 20, 40]))
// console.log(leaders([30, 10, 10, 5]))




