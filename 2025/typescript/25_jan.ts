function plusSign(inputStr: string): boolean {
    let character = /^[ A-Za-z0-9_@./#&+-]*$/
    let charCount = 0;

    if (inputStr[0] !== "+" || inputStr.slice(-1) !== "+") {
        return false;
    }

    for (let i = 1; i < inputStr.length - 1; i++) {
        if (inputStr[i] == "+") {
            if (charCount == 1) {
                charCount = 0
            } else {
                return false;
            }
        } else if (character.test(inputStr[i])) {
            charCount++;
        }
    }

    return true;
}

// console.log(plusSign("+f+d+c+#+f+"));
// console.log(plusSign("+d+=3=+s+"));
// console.log(plusSign("f++d+g+8+"));
// console.log(plusSign("+s+7+fg+r+8+"));


function pigLatinSentence(inputStr: string): string {
    let arrInputStr = inputStr.split(" ");
    let vowel = "aeiou"
    for (let i = 0; i < arrInputStr.length; i++) {
        if (vowel.includes(arrInputStr[i][0])) {
            arrInputStr[i] = arrInputStr[i] + "way"
        } else {
            for (let j = 0; j < arrInputStr[i].length; j++) {
                if (vowel.includes(arrInputStr[i][j])) {
                    arrInputStr[i] = arrInputStr[i].slice(j) + arrInputStr[i].slice(0, j) + "ay"
                }
            }
        }
    }

    return arrInputStr.join(" ")
}

// console.log(pigLatinSentence("this is pig latin"));
// console.log(pigLatinSentence("wall street journal"));
