#In python how to define public , private and protected variables in the class

####Examples####

#Public var
#Protected _var
#Private __var

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

# possible_knight_moves_1 = knight_jumps("F4")()
# possible_knight_moves_2 = knight_jumps("A1")()
# print(possible_knight_moves_1)
# print(possible_knight_moves_2)

class minesweeper_game:
    def __init__(self, list_of_sublist):
        self.__list_of_sublist = list_of_sublist
        self.__list_min = 0
        self.__list_max = len(list_of_sublist) - 1
        self.__sub_list_max = len(list_of_sublist[0]) - 1
        self._onmine_set_value = 9

    def count_neighbour(self, list_index, current_index):
        total_count = 0
        if list_index - 1 >= self.__list_min and self.__list_of_sublist[list_index - 1][current_index] == self._onmine_set_value:
            total_count += 1
        if list_index - 1 >= self.__list_min and current_index + 1 <= self.__sub_list_max and self.__list_of_sublist[list_index - 1][current_index + 1] == self._onmine_set_value:
            total_count += 1
        if list_index - 1 >= self.__list_min and current_index - 1 >= self.__list_min and self.__list_of_sublist[list_index - 1][current_index - 1] == self._onmine_set_value:
            total_count += 1
        if current_index - 1 >= self.__list_min and self.__list_of_sublist[list_index][current_index - 1] == self._onmine_set_value:
            total_count += 1
        if current_index + 1 <= self.__sub_list_max and self.__list_of_sublist[list_index][current_index + 1] == self._onmine_set_value:
            total_count += 1
        if list_index + 1 <= self.__list_max and self.__list_of_sublist[list_index - 1][current_index] == self._onmine_set_value:
            total_count += 1
        if list_index + 1 <= self.__list_max and current_index - 1 >= self.__list_min and self.__list_of_sublist[list_index + 1][current_index - 1] == self._onmine_set_value:
            total_count += 1 
        if list_index + 1 <= self.__list_max and current_index + 1 <= self.__sub_list_max and self.__list_of_sublist[list_index + 1][current_index + 1] == self._onmine_set_value:
            total_count += 1
        return total_count
    
    def print_sub_list(self, list_of_sublist):
        for list in list_of_sublist:
            print(list)
            

    def __call__(self):
        for index in range(len(self.__list_of_sublist)):
            for sub_index in range(len(self.__list_of_sublist[index])):
                if self.__list_of_sublist[index][sub_index] == 1:
                    self.__list_of_sublist[index][sub_index] = 9
                elif self.__list_of_sublist[index][sub_index] == 0:
                    neighbour_count = self.count_neighbour(index, sub_index)
                    self.__list_of_sublist[index][sub_index] = neighbour_count
        self.print_sub_list(self.__list_of_sublist)
    
result_minesweeper_game = minesweeper_game([
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
])()
print(result_minesweeper_game)