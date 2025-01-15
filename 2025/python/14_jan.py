import os
import time
import keyboard
import random

row = 10    
col = 20
board = [[" " for _ in range(col)] for _ in range(row)]
snake = [[5,5]]
direction = "right"
food = [random.randint(0, row - 1), random.randint(0, col - 1)]
game_over = False
score = 0

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(board):
    global game_over
    clear_screen()
    for row in range(len(board)):
        if(row == 0):
            print("--" * (len(board[row])+1))
        print("|", end="")
        print(" ".join(board[row]), "|")
    print("--" * (len(board[row])+1))
    if not game_over:
        print(f"Current Score: {score}")
    if game_over:
        print(f"Final Score: {score}")
        print("Game Over! You collided with yourself.")
        

def update_snake(board):
    global game_over, score, food

    head = snake[-1]
    if direction == "top":
        new_head = [head[0] - 1 if head[0] > 0 else row - 1, head[1]]
    elif direction == "bottom":
        new_head = [head[0] + 1 if head[0] < row - 1 else 0, head[1]]
    elif direction == "left":
        new_head = [head[0], head[1] - 1 if head[1] > 0 else col - 1]
    elif direction == "right":
        new_head = [head[0], head[1] + 1 if head[1] < col - 1 else 0]

    if new_head in snake:
        game_over = True
        return

    snake.append(new_head)

    if new_head == food:
        score += 1
        food = [random.randint(0, row - 1), random.randint(0, col - 1)]
    else:
        snake.pop(0)

    for segment in snake:
        board[segment[0]][segment[1]] = "O"

def update_food(board):
    board[food[0]][food[1]] = "#"

def update_board(board):
    for r in range(row):
        for c in range(col):
            board[r][c] = " "
    update_snake(board)
    update_food(board)

def handle_key_press(e):
    global direction
    if e.name in ['w','W','up'] and direction != "bottom":
        direction = "top"
    elif e.name in ['s', 'S', 'down'] and direction != "top":
        direction = "bottom"
    elif e.name in ['a','A','left'] and direction != "right":
        direction = "left"
    elif e.name in ['d','D','right'] and direction != "left":
        direction = "right"

def run_snake_game():
    global game_over

    keyboard.hook(handle_key_press)

    while not game_over:
        update_board(board)
        print_board(board)
        time.sleep(.2)

run_snake_game()

