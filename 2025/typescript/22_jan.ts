function caesarCipher(inputStr: string, jump: number): string {
    let lstInputStr = inputStr.split("")
    let alphabet: string = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < lstInputStr.length; i++) {
        if (alphabet.includes(lstInputStr[i].toLocaleLowerCase())) {
            let isUpper = false;
            let currentLetterIndex = alphabet.indexOf(lstInputStr[i].toLocaleLowerCase());
            if (lstInputStr[i] != alphabet[currentLetterIndex]) {
                isUpper = true;
            }
            currentLetterIndex += jump
            if (currentLetterIndex > alphabet.length) {
                let remainIndex = currentLetterIndex - (alphabet.length);
                if (isUpper == true) {
                    lstInputStr[i] = alphabet[remainIndex].toUpperCase();
                } else {
                    lstInputStr[i] = alphabet[remainIndex]
                }
            } else {
                if (isUpper == true) {
                    lstInputStr[i] = alphabet[currentLetterIndex].toUpperCase();
                } else {
                    lstInputStr[i] = alphabet[currentLetterIndex]
                }
            }
        }
    }

    return lstInputStr.join("")
}

// console.log(caesarCipher("middle-Outz", 2));
// console.log(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5));
// console.log(caesarCipher("A friend in need is a friend indeed", 20));

