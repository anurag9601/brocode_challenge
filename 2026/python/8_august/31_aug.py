import os, time, msvcrt, random

class snake_game:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.area_length = 9
        self.snake_speed = 1
        self.snake_length = [[self.x_position, self.y_position]]
        self.snake_food = []
        self.play_area = [[" " for _ in range(self.area_length)]for _ in range(self.area_length)]
        self.current_direction = "right"
        self.player_score = 0

    def print_play_area(self):
        print("-"* (self.area_length * 3 + 2))
        for i in range(self.area_length):
            for j in range(self.area_length):
                if j == 0:
                    print("|", end="")
                if [i, j] in self.snake_length:
                    print("*", end="  ")
                elif [i, j] == self.snake_food:
                    print("$", end="  ")
                else:
                    print(" ", end="  ")
                if j == self.area_length - 1:
                    print("|", end="")
            print()
        print("-"*(self.area_length * 3 + 2))

    def set_snake_position(self, direction):
        if direction == "up":
            if self.x_position == 0:
                self.x_position = self.area_length - 1
            else:
                self.x_position = self.x_position - 1
        elif direction == "down":
            if self.x_position == self.area_length - 1:
                self.x_position = 0
            else:
                self.x_position = self.x_position + 1
        elif direction == "left":
            if self.y_position == 0:
                self.y_position = self.area_length - 1
            else:
                self.y_position = self.y_position - 1
        elif direction == "right":
            if self.y_position == self.area_length - 1:
                self.y_position = 0
            else:
                self.y_position = self.y_position + 1
        new_head = [self.x_position, self.y_position]

        self.snake_length.append(new_head)

        if new_head == self.snake_food:
            self.player_score += 1
            self.generate_random_food()
        else:
            self.snake_length.pop(0)



    def handle_keyboard_action(self):

        if msvcrt.kbhit() == True:
            key = msvcrt.getch()

            if key in (b'\x00', b'\xe0'):
                key = msvcrt.getch()
                if key == b'H':
                    self.set_snake_position("up")
                    self.current_direction = "up"
                elif key == b'P':
                    self.set_snake_position("down")
                    self.current_direction = "down"
                elif key == b'K':
                    self.set_snake_position("left")
                    self.current_direction = "left"
                elif key == b'M':
                    self.set_snake_position("right")
                    self.current_direction = "right"
            else:
                key = key.decode().lower()

                if key == 'w':
                    self.set_snake_position("up")
                    self.current_direction = "up"
                elif key == 's':
                    self.set_snake_position("down")
                    self.current_direction = "down"
                elif key == 'a':
                    self.set_snake_position("left")
                    self.current_direction = "left"
                elif key == 'd':
                    self.set_snake_position("right")
                    self.current_direction = "right"
        else:
            self.set_snake_position(self.current_direction)

    def generate_random_food(self):
        while True:
            random_x = random.randint(0, self.area_length - 1)
            random_y = random.randint(0, self.area_length - 1)

            if self.snake_food != [random_x, random_y]:
                self.snake_food = [random_x, random_y]
                return
            continue

    def play(self):
        self.generate_random_food()
        while(True):
            time.sleep(self.snake_speed)
            os.system("cls")
            self.handle_keyboard_action()
            self.print_play_area()
            print(f"Player Score: {self.player_score}")

snake_game().play()