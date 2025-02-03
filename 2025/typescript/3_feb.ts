function XAndO(board: string[] = [" | | ", " |X| ", "X| | "]) {

    function checkPosition(boardLst: string[][]) {
        for (let row = 0; row < boardLst.length; row++) {
            if (boardLst[row][0] == " " && boardLst[row][1] == "X" && boardLst[row][2] == "X") {
                return [row + 1, 1];
            } else if (boardLst[row][0] == "X" && boardLst[row][1] == " " && boardLst[row][2] == "X") {
                return [row + 1, 2];
            } else if (boardLst[row][0] == "X" && boardLst[row][1] == "X" && boardLst[row][2] == " ") {
                return [row + 1, 3];
            }
        }

        for (let col = 0; col < boardLst[0].length; col++) {
            if (boardLst[0][col] == " " && boardLst[1][col] == "X" && boardLst[2][col] == "X") {
                return [1, col + 1];
            } else if (boardLst[0][col] == "X" && boardLst[1][col] == " " && boardLst[2][col] == "X") {
                return [2, col + 1];
            } else if (boardLst[0][col] == "X" && boardLst[1][col] == "X" && boardLst[2][col] == " ") {
                return [3, col + 1];
            }
        }

        if (boardLst[0][0] == " " && boardLst[1][1] == "X" && boardLst[2][2] == "X") {
            return [1, 1];
        } else if (boardLst[0][0] == "X" && boardLst[1][1] == " " && boardLst[2][2] == "X") {
            return [2, 2];
        } else if (boardLst[0][0] == "X" && boardLst[1][1] == "X" && boardLst[2][2] == " ") {
            return [3, 3];
        }

        if (boardLst[0][2] == " " && boardLst[1][1] == "X" && boardLst[2][0] == "X") {
            return [1, 3];
        } else if (boardLst[0][2] == "X" && boardLst[1][1] == " " && boardLst[2][0] == "X") {
            return [2, 2];
        } else if (boardLst[0][2] == "X" && boardLst[1][1] == "X" && boardLst[2][0] == " ") {
            return [3, 1];
        }

        return false;
    }

    let boardLst: string[][] = []
    for (let row of board) {
        boardLst.push(row.split("|"));
    }

    return checkPosition(boardLst)
}

// console.log(XAndO());
// console.log(XAndO(["X|X|O", "O|X| ", "X|O| "]));
// console.log(XAndO(["X|X| ", "O|O|X", "X|O|O"]))
// console.log(XAndO(["O|X|O", "X|X| ", "X|O|O"]))
// console.log(XAndO(["X|O|X", "O|X| ", "X|O|O"]))
// console.log(XAndO(["X| |X", "O|X|O", "O|X|O"]))