function canFind(bigramLst: string[], str_lst: string[]): boolean {
    for (let bigram of bigramLst) {
        let isFind: boolean = false
        for (let str of str_lst) {
            if (str.includes(bigram)) {
                isFind = true
                break
            }
        }
        if (isFind === false) {
            return false;
        }
    }
    return true;
}

// console.log(canFind(["at", "be", "th", "au"], ["beautiful", "the", "hat"]));
// console.log(canFind(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]));
// console.log(canFind(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
// console.log(canFind(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))

const movingPartition = (nums_lst: number[]) : unknown[] => {

    const finalResultOfPartition:unknown[] = []

    for (let i=0; i<nums_lst.length - 1; i++){
        let row:unknown[] = []
        let col:number[] = []
        for (let j=0; j<i+1; j++){
            col.push(nums_lst[j])
        }
        row.push(col)
        row.push(nums_lst.slice(i+1))
        finalResultOfPartition.push(row)
    }

    return finalResultOfPartition;
}

// console.log(movingPartition([-1, -1, -1, -1]))
// console.log(movingPartition([1, 2, 3, 4, 5]))
// console.log(movingPartition([]))

function uniqueAbbrev(abbre_lst:string[], str_lst:string[]):boolean{
    for(let i=0; i<abbre_lst.length; i++){
        for(let j=0; j<abbre_lst.length; j++){
            if(j != i && abbre_lst[j].includes(abbre_lst[i])){
                return false;
            }
        }
    }
    return true;
}

// console.log(uniqueAbbrev(["ho", "h", "ha"], ["house", "hope", "happy"]))
// console.log(uniqueAbbrev(["tr", "tr", "ti"], ["train", "tree", "time"]))
// console.log(uniqueAbbrev(["pl", "pi", "pu"], ["plant", "pilot", "pump"]))