//My_shiritori word problem

class my_shiritori {
    enteredWords: string[] = [];
    isValidShiritori: boolean = false;

    play(word: string) {
        this.enteredWords.push(word);
        this.checkValidShiritori(this.enteredWords);
        console.log(!this.isValidShiritori && this.enteredWords.length > 1 ? "game over" : this.enteredWords);
    };

    checkValidShiritori(words: string[]) {
        let isValid = true;
        for (let i = 0; i < words.length - 1; i++) {
            if (words[i][words[i].length - 1] !== words[i + 1][0]) {
                isValid = false;
                break;
            }
        };
        this.isValidShiritori = isValid;
    };

    restart() {
        this.isValidShiritori = false;
        this.enteredWords = [];
    };
};

// const My_shiritori = new my_shiritori();

// My_shiritori.play("apple");
// My_shiritori.play("ear");
// My_shiritori.play("rhino");
// My_shiritori.play("corn");
// My_shiritori.restart();
