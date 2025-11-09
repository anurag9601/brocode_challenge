function longestPalindrom(inputString: string, longPali: string = ""): string {
    if (inputString.length === 0) {
        return longPali;
    };

    let currentLongestPalindrom: string = "";

    for (let char of inputString) {
        currentLongestPalindrom += char;
        const currentReversedString = currentLongestPalindrom.split("").reverse().join("");
        if (currentReversedString === currentLongestPalindrom && currentReversedString.length > longPali.length) {
            longPali = currentLongestPalindrom;
        }
    };

    return longestPalindrom(inputString.slice(1), longPali);
}

// console.log(longestPalindrom("babad"))
// console.log(longestPalindrom("ac"))
// console.log(longestPalindrom("racecarannakayak"))

function leftSlide(inputList: number[]) {
    const operationList = inputList.filter((e) => e > 0);
    let result: number[] = [];
    let index: number = 0;

    for (let i = 0; i < inputList.length; i++) {
        if (index === operationList.length) {
            result.push(0);
        } else {
            while (true) {
                if (index !== operationList.length - 1 && operationList[index] === operationList[index + 1]) {
                    result.push(operationList[index] + operationList[index + 1]);
                    index += 2;
                    break;
                } else {
                    result.push(operationList[index]);
                    index += 1;
                    break;
                }
            }
        }
    };

    return result;
}

// console.log(leftSlide([2, 2, 2, 0]));
// console.log(leftSlide([2, 2, 4, 4, 8, 8]));
// console.log(leftSlide([0, 2, 0, 2, 4]));
// console.log(leftSlide([0, 2, 2, 8, 8, 8]));