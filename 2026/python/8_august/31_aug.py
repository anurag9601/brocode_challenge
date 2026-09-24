import os, time

class snake_game:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.area_length = 9
        self.snake_speed = 1
        self.snake_length = [[self.x_position, self.y_position]]
        self.play_area = [[" " for _ in range(self.area_length)]for _ in range(self.area_length)]

    def print_play_area(self):
        print("-"* (self.area_length * 3 + 2))
        for i in range(self.area_length):
            for j in range(self.area_length):
                if j == 0:
                    print("|", end="")
                if [i, j] in self.snake_length:
                    print("*", end="  ")
                else:
                    print(" ", end="  ")
                if j == self.area_length - 1:
                    print("|", end="")
            print()
        print("-"*(self.area_length * 3 + 2))

    def set_snake_position(self):
        self.play_area[self.x_position][self.y_position] = "*"
        if self.x_position == self.area_length - 1:
            self.x_position = 0
        else:
            self.x_position += 1

    def play(self):
        while(True):
            self.set_snake_position()
            self.print_play_area()
            time.sleep(1)
            os.system("cls")


snake_game().play()