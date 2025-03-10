function longestPalindrome(s: string) {
    let longestPali: string = ""

    for (let i = 0; i < s.length; i++) {
        if (s.length - i > longestPali.length) {
            let currentPali = ""
            for (let j = i; j < s.length; j++) {
                currentPali += s[j]
                if (currentPali == [...currentPali].reverse().join("")) {
                    if (currentPali.length > longestPali.length) {
                        longestPali = currentPali
                    }
                }
            }
        } else {
            return longestPali
        }
    }

    return longestPali
}

// console.log(longestPalindrome("forgeeksskeegfor"))
// console.log(longestPalindrome("Geeks"))
// console.log(longestPalindrome("abc"))

function isValidIP(s: string) {
    let splitIP = s.split(".")
    if (splitIP.length > 4 || splitIP.length < 4 || splitIP.includes("")) return false;

    let isZero = false;

    for (let i = 0; i < splitIP.length; i++) {
        let intIPChunk = parseInt(splitIP[i])
        if (intIPChunk > 255 || intIPChunk < 0) {
            return false;
        } else if (intIPChunk == 0) {
            if (isZero) return false
            isZero = true
        }
    }

    return true
}

// console.log(isValidIP("5555..555"))
// console.log(isValidIP("222.111.111.111"))
// console.log(isValidIP("0.0.0.255"))