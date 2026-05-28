import random

def play_sudoku(length = 9):
    board = [[0 for _ in range(length)] for _ in range(length)]
    board_result = [[0 for _ in range(length)] for _ in range(length)]
    game_level = ""
    hide_numbers_length = length

    def is_valid(row, col, num):
        if(num in board[row]):
            return False
        
        for r in range(length):
            if(board[r][col] == num):
                return False
        
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if(board[r][c] == num):
                    return False
        
        return True

    def generate_board():
        for r in range(length):
            for c in range(length):
                nums = list(range(1, length + 1))
                random.shuffle(nums)

                for num in nums:
                    is_valid_num = is_valid(r, c, num)
                    if is_valid_num == True:
                        board[r][c] = num
                        board_result[r][c] = num
                        break
        hide_numbers()

    def set_level():
        nonlocal hide_numbers_length
        if game_level == "easy":
            hide_numbers_length = length
            return True
        elif game_level == "medium":
            hide_numbers_length = length * 3
            return True
        elif game_level == "hard":
            hide_numbers_length = length * 5
            return True
        else:
            return False
        
    def hide_numbers():
        hide_count = 0
        while hide_count != hide_numbers_length:
            random_x = random.randrange(0, length - 1)
            random_y = random.randrange(0, length - 1)
            if board[random_x][random_y] != " ":
                board[random_x][random_y] = " "
                hide_count += 1

    def print_board(board_to_print):
        for row in range(len(board_to_print)):
            for col in range(len(board_to_print[row])):
                print(" "+ str(board_to_print[row][col]) + " ", end="")
                if((col + 1) != length and (col + 1) % 3 == 0):
                    print("|", end="")
            print()
            if((row + 1) != length and (row + 1) % 3 == 0):
                print(((length * 3) + 2) * "-")
    
    def play():
        nonlocal game_level
        print("welcome to sudoku...");
        while True:
            selected_level = input("Game level easy/medium/hard: ")
            game_level = selected_level.lower()
            level_set = set_level()
            if level_set == True:
                break
        
        generate_board()
        
        print_board(board)

        result_visible = input("Want to see result? (y/n): ")

        if result_visible.lower() == "y" or result_visible.lower() == "yes":
            print_board(board_result)
        else:
            print("Enjoy your play!!")

    play()

play_sudoku()