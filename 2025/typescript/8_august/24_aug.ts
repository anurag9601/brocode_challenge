// Printer Ink Levels

// A wireless printer has four ink cartridges (Cyan, Magenta, Yellow, Black). Each page requires at least 1 unit of each color to print.

// Create a function that takes the available ink levels [C, M, Y, K] and returns the maximum number of pages that can be printed before one cartridge runs empty.

function printer(colorList: number[]): number {
    let printedPages: number = 0
    while (!colorList.includes(0)) {
        colorList = colorList.map(c => c - 1);
        printedPages += 1;
    };

    return printedPages;
};

// console.log(printer([10, 5, 7, 8]))
// console.log(printer([3, 3, 3, 3]))

function parking(parkingSpaceList: number[]) {
    let possibleParking: number = 0
    
    if(parkingSpaceList.length < 3){
        return 0;
    }

    for(let i=0; i<parkingSpaceList.length-1; i++) {
        if(i === 0 && parkingSpaceList[i] === 0 && parkingSpaceList[i + 1] === 0 && parkingSpaceList[i + 2] === 0){
            parkingSpaceList[i] = 1;
            possibleParking += 1;
        }else if(i === 1 && parkingSpaceList[i] === 0 && parkingSpaceList[i - 1] === 0 && ((parkingSpaceList.length > 3 && parkingSpaceList[i + 1] === 0 && parkingSpaceList[i + 2] === 0) || parkingSpaceList[i + 1] === 0)){
            parkingSpaceList[i] = 1;
            possibleParking += 1;
        }else if(i === parkingSpaceList.length - 1 && parkingSpaceList[i] === 0 && parkingSpaceList[i - 1] === 0 && parkingSpaceList[i - 2] === 0) {
            parkingSpaceList[i] = 1;
            possibleParking += 1;
        }else if(i === parkingSpaceList.length - 2 && parkingSpaceList[i] === 0 && parkingSpaceList[i + 1] === 0 && (parkingSpaceList.length > 3 && parkingSpaceList[i - 1] === 0 && parkingSpaceList[i - 2] === 0 || parkingSpaceList[i - 1] === 0)){
            parkingSpaceList[i] = 1;
            possibleParking += 1;
        }else if(parkingSpaceList[i] === 0 && parkingSpaceList[i - 1] === 0 && parkingSpaceList[i - 2] === 0 && parkingSpaceList[i + 1] === 0 && parkingSpaceList[i + 2] === 0){
            parkingSpaceList[i] = 1;
            possibleParking += 1;
        }
    };

    return possibleParking;
}

// console.log(parking([0, 0, 1, 0, 0, 0]))
// console.log(parking([1, 0, 0, 1, 0, 0, 0]))