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
console.log(cleanUp(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix"));
console.log(cleanUp(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix"));
console.log(cleanUp(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix"));
console.log(cleanUp(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix"));
console.log(cleanUp(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix"));