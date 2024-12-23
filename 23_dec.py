def is_happy(n):
    str_n = str(n)

    while(len(str_n) != 1):
        current_sum = 0
        for i in str_n:
            i = int(i)
            current_sum += i**2
        str_n = str(current_sum)

    if(int(str_n) == 1):
        return True
    else:
        return False

def is_happy_using_recur(n):
    str_n = str(n)

    len_str_n = len(str_n)

    if(len_str_n == 1 and n == 1):
        return True
    elif(len_str_n == 1 and n > 1):
        return False
        
    current_sum = 0

    for i in str_n:
        i = int(i)
        current_sum += i**2
    return is_happy_using_recur(int(current_sum))
        

# print(is_happy(67))
# print(is_happy(139))
# print(is_happy_using_recur(139))
# print(is_happy_using_recur(67))

def num_split(n):
    result = []
    is_nagative = False

    if(n < 0):
        is_nagative = True
        n = n * -1

    count = 0

    while(n != 0):
        temp = str(n%10)
        n = n//10
        for i in range(count):
            temp += "0"
        if(is_nagative == True):
            temp = int(temp) * -1
            result.insert(0, temp)
        else:
            temp = int(temp)
            result.insert(0, temp)
        count += 1
    return result

# print(num_split(-434))
# print(num_split(100))
# print(num_split(39))
# print(num_split(1234))

import time

def tic_tac_toe():
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    game_over = False

    turn = "X"

    turn_count = 0

    def update_board(index):
        nonlocal turn

        try:
            int(index)
        except:
            return "Invalid"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == index):
                    board[i][j] = turn
                    check_win()
                    turn = "O" if turn == "X" else "X"
                    return "Valid"
        return "Invalid"
        
    def celebration(message, delay):
        for char in message:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
        print("Final board")

    def print_board():
        nonlocal game_over

        if(turn_count >= 9 and game_over == False):
            game_over = True
            message = "Game Draw 😉"
            celebration(message, 0.2)
        for i in board:
            print(i)

    def check_win():
        nonlocal game_over

        for i in range(len(board)):
            if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
                game_over = True
                celebration_message = f"{turn} Won🥳 AAHA TAMATAR BADE MAJEDAAR..."
                celebration(celebration_message, 0.2)
                return

        for j in range(len(board[0])):
            if(board[0][j] == board[1][j] and board[1][j] == board[2][j]):
                game_over = True
                celebration_message = f"{turn} Won🥳 AAHA TAMATAR BADE MAJEDAAR..."
                celebration(celebration_message, 0.2)
                return

        if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            game_over = True
            celebration_message = f"{turn} Won🥳 AAHA TAMATAR BADE MAJEDAAR..."
            celebration(celebration_message, 0.2)
            return

        if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            game_over = True
            celebration_message = f"{turn} Won🥳 AAHA TAMATAR BADE MAJEDAAR..."
            celebration(celebration_message, 0.2)
            return

    print_board()

    while(game_over == False):
        player1_enter_valid_key = False
        player2_enter_valid_key = False
        while(player1_enter_valid_key == False):
            player1 = input(f"{turn}'s turn: ")
            response = update_board(player1)
            if(response == "Valid"):
                turn_count += 1
                player1_enter_valid_key = True
                print_board()
            else:
                print("Entered key is invalid try again.")
                

        if(game_over == False):
            while(player2_enter_valid_key == False):
                player2 = input(f"{turn}'s turn: ")
                response = update_board(player2)
                if(response == "Valid"):
                    turn_count += 1
                    player2_enter_valid_key = True
                    print_board()
                else:
                    print("Entered key is invalid try again.")

tic_tac_toe()
            



        

