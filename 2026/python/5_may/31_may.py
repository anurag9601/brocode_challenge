import random

class sudoku:
    def __init__(self, grid_length = 3):
        self.grid_length = grid_length
        self.length = grid_length * 3
        self.board = [[0 for _ in range(grid_length * 3)] for _ in range(grid_length * 3)]
        self.level = "easy"

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False
        
        for r in range(len(self.board)):
            if self.board[r][col] == num:
                return False
            
        box_row = ( row // self.grid_length ) * self.grid_length
        box_col = ( col // self.grid_length ) * self.grid_length

        for r in range(box_row, box_row + self.grid_length):
            for c in range(box_col, box_col + self.grid_length):
                if self.board[r][c] == num:
                    return False
        
        return True

    def generate_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                nums = list(range(1, self.length + 1))
                random.shuffle(nums)
                for num in nums:
                    if self.is_valid(row, col, num) == True:
                        self.board[row][col] = num
                        break

    def hide_nums(self):
        hide_count = self.length * 2 if self.level == "easy" else self.length * 4
        iteration_count = 0

        while iteration_count < hide_count:
            random_y = random.randint(0, self.length - 1)
            random_x = random.randint(0, self.length - 1)

            if self.board[random_y][random_x] != " ":
                self.board[random_y][random_x] = " "
                iteration_count += 1
    
    def print_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(self.board[row][col], end=" ")
                if (col + 1) % self.grid_length == 0 and col != self.length - 1:
                    print("|", end=" ")
            print()
            if (row + 1) % self.grid_length == 0 and row != self.length - 1:
                print("-" * ((self.length * 2) + 3))
            


    def play(self):
        self.generate_board()
        self.hide_nums()
        self.print_board()

sudoku_game = sudoku()
sudoku_game.play()
