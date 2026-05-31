import random

class play_sudoku:
    def __init__(self):
        self.board = []
        self.board_result = []
        self.grid_size = 3
        self.space_length = 1
        self.game_level = "easy"

    def generate_dummy_board(self):
        box_length = self.grid_size * 3
        self.board = [[0 for _ in range(box_length)] for _ in range(box_length)]

    def is_valid(self, row, col, num):

        if num in self.board[row]:
            return False
        
        for r in range(len(self.board)):
            if self.board[r][col] == num:
                return False
        
        box_row = (row // self.grid_size) * self.grid_size
        box_col = (col // self.grid_size) * self.grid_size

        for r in range(box_row, box_row + self.grid_size):
            for c in range(box_col, box_col + self.grid_size):
                if self.board[r][c] == num:
                    return False
                
        return True

    def generate_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                nums = list(range(1, self.grid_size * 3 + 1))
                random.shuffle(nums)

                for num in nums:
                    if self.is_valid(row, col, num) == True:
                        self.board[row][col] = num
                        break
    
    def print_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(" " * self.space_length + str(self.board[row][col]) + " " * self.space_length , end="")
                if (col + 1) % self.grid_size == 0 and col != (self.grid_size * 3) - 1:
                    print("|", end="")
            print()
            if (row + 1) % self.grid_size == 0 and row != (self.grid_size * 3) - 1:
                print("-" * ((self.grid_size * (self.grid_size * 3)) + 2))

    def play(self):
        self.generate_dummy_board()
        self.generate_board()
        self.print_board()

sudoku = play_sudoku()

sudoku.play()
        
        
        
