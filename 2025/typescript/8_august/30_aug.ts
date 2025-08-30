// For solving this problem we will use stack method.

function validParentheses(parentheses: string): boolean {
    const parenthObj: { [key: string]: string } = {
        '}': '{',
        ']': '[',
        ')': '('
    };

    let stack: string[] = [];

    for (let char of parentheses) {
        if (parenthObj[char]) {
            if (!stack || stack[stack.length - 1] !== parenthObj[char]) {
                return false;
            } else {
                stack.pop();
            }
        } else {
            stack.push(char);
        }
    };

    return true;
};

// console.log(validParentheses("()[]{}"));
// console.log(validParentheses("(]"));

// Rotate Matrix 90°

class Rotate90Degree {
    matrix: number[][] = [];
    matrixLength: number;
    
    constructor(matrix: number[][]) {
        this.matrix = matrix;
        this.matrixLength = matrix[0].length;
    }

    result: number[][] = [];

    get perform(): number[][] {
        for (let i = 0; i < this.matrixLength; i++) {
            let tempList: number[] = [];
            for (let j = this.matrixLength - 1; j > -1; j--) {
                tempList.push(this.matrix[j][i])
            }
            this.result.push(tempList);
        };

        return this.result;
    };
};

// const rotateMatrix = new Rotate90Degree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

// console.log(rotateMatrix.perform);