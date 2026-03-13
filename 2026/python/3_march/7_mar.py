class minesweeper:
    def __init__(self, list_of_sublist):
        self.list_of_sublist = list_of_sublist
        self.list_length = len(list_of_sublist)
        self.sublist_length = len(list_of_sublist[0])

    def mine_in_diagonal(self, y_index, x_index):

        x_start = x_index - 1 if x_index - 1 >= 0 else x_index
        y_start = y_index - 1 if y_index  - 1 >= 0 else y_index
        x_end = x_index + 1 if x_index + 1 <= self.sublist_length - 1 else x_index
        y_end = y_index + 1 if y_index + 1 <= self.list_length - 1 else y_index

        mine_count = 0

        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if self.list_of_sublist[y][x] == "#":
                    mine_count += 1
        return mine_count
                    

    def __call__(self):
        for i in range(self.list_length):
            for j in range(self.sublist_length):
                if self.list_of_sublist[i][j] == "?":
                    mine_count = self.mine_in_diagonal(i, j)
                    self.list_of_sublist[i][j] = mine_count
        
        return self.list_of_sublist
    
# result_minesweeper_1 = minesweeper([
#   ["-", "#", "-"],
#   ["-", "?", "-"],
#   ["-", "-", "-"]
# ])()
# print(result_minesweeper_1)
# result_minesweeper_2 = minesweeper([
#   ["-", "#", "-"],
#   ["#", "-", "?"],
#   ["#", "#", "-"]
# ])()
# print(result_minesweeper_2)
# result_minesweeper_3 = minesweeper([
#   ["-", "#", "#"],
#   ["?", "#", ""],
#   ["#", "?", "-"]
# ])()
# print(result_minesweeper_3)