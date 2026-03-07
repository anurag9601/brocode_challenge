class knight_jumps:
    def __init__(self, knight_position):
        self.y = ["1","2","3","4","5","6","7","8"]
        self.x = ["A","B","C","D","E","F","G","H"]
        self.knight_position = knight_position
        self.knight_moves = []
        
    def __call__(self):
        [x,y] = [*self.knight_position]
        current_x_index = self.x.index(x)
        current_y_index = self.y.index(y)
        

        if current_y_index + 1 <= 7 and current_x_index + 2 <= 7:
            self.knight_moves.append(self.x[current_x_index + 2] + self.y[current_y_index + 1])
        if current_y_index + 2 <= 7 and current_x_index + 1 <= 7:
            self.knight_moves.append(self.x[current_x_index + 1] + self.y[current_y_index + 2])
        if current_y_index + 2 <= 7 and current_x_index - 1 >= 0:
            self.knight_moves.append(self.x[current_x_index - 1] + self.y[current_y_index + 2])
        if current_y_index + 1 <= 7 and current_x_index - 2 >= 0:
            self.knight_moves.append(self.x[current_x_index - 2] + self.y[current_y_index + 1])
        if current_y_index - 1 >= 0 and current_x_index - 2 >= 0:
            self.knight_moves.append(self.x[current_x_index - 2] + self.y[current_y_index - 1])
        if current_y_index - 2 >= 0 and current_x_index - 1 >= 0:
            self.knight_moves.append(self.x[current_x_index - 1] + self.y[current_y_index - 2])
        if current_y_index - 2 >= 0 and current_x_index + 1 <= 7:
            self.knight_moves.append(self.x[current_x_index + 1] + self.y[current_y_index - 2])
        if current_y_index - 1 >= 0 and current_x_index + 2 <= 7:
            self.knight_moves.append(self.x[current_x_index + 2] + self.y[current_y_index - 1])
        return ",".join(self.knight_moves)

# possible_knight_moves = knight_jumps("F4")()
# print(possible_knight_moves)
