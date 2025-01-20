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

function cleanUp(fileLst: string[], method: string) {
    let result: unknown[] = []
    let doneList: string[] = []
    let currentIndex = 0
    if (method == "suffix") {
        for (let i of fileLst) {
            let tempLst = []
            let extension = i.split(".")[1]
            if (!doneList.includes(extension)) {
                doneList.push(extension)
                for (let j of fileLst) {
                    let currentExtension = j.split(".")[1]
                    if (currentExtension == extension) {
                        tempLst.push(j)
                    }
                }
                result.push(tempLst)
            }
        }
    } else {
        for (let i = 0; i < fileLst.length; i++) {
            let tempLst = [];
            let passedFile: string[] = [];
            if (currentIndex < fileLst.length) {
                for (let j = currentIndex; j < fileLst.length; j++) {
                    let extension = fileLst[j].split(".")[1]
                    if (!passedFile.includes(extension)) {
                        passedFile.push(extension)
                        tempLst.push(fileLst[j])
                        if (j == fileLst.length - 1) {
                            currentIndex = j + 1
                            result.push(tempLst);
                            break
                        }
                    } else {
                        currentIndex = j
                        result.push(tempLst)
                        break;
                    }
                }
            } else {
                break
            }
        }
    }

    return result
}

// console.log(cleanUp(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix"));
// console.log(cleanUp(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix"));
// console.log(cleanUp(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix"));
// console.log(cleanUp(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix"));
// console.log(cleanUp(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix"));

function bandNameSort(bandLst: string[]) {
    let alphabet = "abcdefghijklmnopqrstuvwxyz"
    let bandNameIndexAlpha: { [key: string]: number } = {}
    let skipWord = ["The", "A", "An"]
    for (let band = 0; band < bandLst.length; band++) {
        let splitBandName: string[] = bandLst[band].split(" ")
        for (let chunk of splitBandName) {
            if (!skipWord.includes(chunk)) {
                for (let letter of chunk.toLocaleLowerCase()) {
                    if (!bandNameIndexAlpha[letter]) {
                        bandNameIndexAlpha[letter] = band
                        break
                    }
                }
                break;
            }
        }
    }

    let result: string[] = []

    for (let alpha of alphabet) {
        if (bandNameIndexAlpha[alpha]) {
            result.push(bandLst[bandNameIndexAlpha[alpha]])
        }
    }

    return result
}

// console.log(bandNameSort(["The New Yardbirds", "The Beatles", "The Square Roots", "On A Friday", "An Irony"]));
// console.log(bandNameSort(["The Platters", "A Yard of Yarn", "The Everly Brothers", "A Monster Effect", "The Sex Maggots"]))
// console.log(bandNameSort(["But Myth", "An Old Dog", "Def Leppard", "The Any Glitters", "The Dawn"]))


function countUniqueBooks(stringSequence: string, bookEnd: string) {
    let uniqueBooks: number = 0
    let currentBooks = new Set<string>()
    let addBooks = false
    for (let letter of stringSequence) {
        if (letter == bookEnd) {
            if (!addBooks) {
                addBooks = true
            } else {
                uniqueBooks += currentBooks.size;
                currentBooks.clear();
                addBooks = false
            }
        }
        else if (addBooks == true) {
            currentBooks.add(letter)
        }
    }

    return uniqueBooks
}

// console.log(countUniqueBooks("AZYWABBCATTTA", "A"));
// console.log(countUniqueBooks("$AA$BBCATT$C$$B$", "$"));
// console.log(countUniqueBooks("ZZABCDEF", "Z"))

function spoonerise(inputStr: string) {
    let str1 = "";
    let str2 = "";
    let vowels = "aeiou"
    let splitStr = inputStr.split(" ")
    for (let word = 0; word < splitStr.length; word++) {
        for (let letter = 0; letter < splitStr[word].length; letter++) {
            if (vowels.includes(splitStr[word][letter])) {
                splitStr[word] = splitStr[word].slice(letter)
                break
            } else {
                if (word == 0) {
                    str1 += splitStr[word][letter]
                }else{
                    str2 += splitStr[word][letter]
                }
            }
        }
    }

    splitStr[0] = str2 + splitStr[0]
    splitStr[1] = str1 + splitStr[1]

    return splitStr.join(" ")
}

// console.log(spoonerise("history lecture"));
// console.log(spoonerise("loud noises"))
// console.log(spoonerise("chow mein"))
// console.log(spoonerise("edabit rules!"))