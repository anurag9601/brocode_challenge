function validName(nameStr: string) {
    const splitNameStr = nameStr.split(" ");

    if (splitNameStr.length == 1 || splitNameStr.slice(-1)[0].length == 2 && splitNameStr.slice(-1)[0].includes(".") || splitNameStr.length == 3 && splitNameStr[0].length == 2 && splitNameStr[1].length > 2) {
        return false;
    }

    for (let part of splitNameStr) {
        if (part.length == 1) {
            return false;
        } else if (part.length > 2 && part.includes(".") || part.length == 2 && part.includes(".") && part[0].toLowerCase() === part[0]) {
            return false;
        } else if (part.length > 2 && part[0].toLocaleLowerCase() == part[0]) {
            return false;
        }
    }

    return true;
}

// console.log(validName("H. Wells"));
// console.log(validName("H. G. Wells"));
// console.log(validName("Herbert G. Wells"));
// console.log(validName("Herbert"));
// console.log(validName("h. Wells"));
// console.log(validName("H Wells"));
// console.log(validName("H. George Wells"));
// console.log(validName("H. George W."));
// console.log(validName("Herb. George Wells"));

