#mario game

import os
import keyboard
import time

row = 10
col = 20

board = [[ " " for _ in range(col)] for _ in range(row)]

player_position = [[len(board) - 1,1],[len(board) - 2 ,1]]

def print_board():
    global board
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(board)):
        if(i == 0 or i == len(board) - 1):
            print("-"*(col * 2 -1))
        else:
            for j in range(len(board[0])):
                if j == 0 or j== len(board[0]) - 1:
                    print("|", end=" ")
                else:
                    print(" ", end=" ")
        if(i != 0 and i != len(board) - 1):
            print()

def print_player():
    global board
    global player_position
    iteration_count = 0
    while(iteration_count != 2):
        board[player_position[iteration_count][0]][player_position[iteration_count][1]] = "*"
        iteration_count += 1

def handle_key_down_event(key):
    print(key.name)

def game_start():
    keyboard.hook(handle_key_down_event)
    while(True):
        time.sleep(.3)
        print_board()

game_start()
