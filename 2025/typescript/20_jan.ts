function getHashTags(inputStr: string): string[] {
    let result: string[] = [];
    let sortWordLength: number[] = [];
    let lstInputStr: string[] = inputStr.split(" ");
    let splitInputStr: string[] = inputStr.split(" ");

    for (let i = 0; i < lstInputStr.length; i++) {
        let mini_i: number = i;
        for (let j = i; j < lstInputStr.length; j++) {
            if (lstInputStr[j].length < lstInputStr[mini_i].length) {
                mini_i = j;
            }
        }
        sortWordLength.splice(0, 0, lstInputStr[mini_i].length);
        [lstInputStr[mini_i], lstInputStr[i]] = [lstInputStr[i], lstInputStr[mini_i]];
    }

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < splitInputStr.length; j++) {
            if (sortWordLength[i] === splitInputStr[j].length && !result.includes(("#" + splitInputStr[j]).toLowerCase())) {
                result.push(("#" + splitInputStr[j]).toLowerCase());
                break;
            }
        }
    }

    return result;
}

// console.log(getHashTags("How the Avocado Became the Fruit of the Global Trade"));
// console.log(getHashTags("Why You Will Probably Pay More for Your Christmas Tree This Year"));
// console.log(getHashTags("Hey Parents, Surprise, Fruit Juice Is Not Fruit"));
// console.log(getHashTags("Visualizing Science"));

