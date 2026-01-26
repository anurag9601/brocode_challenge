class min_jump:
    def __init__(self, jump_list):
        self.jump_list = jump_list

    def __call__(self):
        n = len(self.jump_list)
        jump_i = 0
        jump = 0

        if n == 1:
            return jump
        elif self.jump_list[0] == 0:
            return -1
        
        while(True):
            if jump_i >= n - 1:
                return jump
            elif self.jump_list[jump_i] == 0:
                return jump
            else:
                jump_i += self.jump_list[jump_i]
                jump += 1

# if __name__ == "__main__":
#     result = min_jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])()
#     result1 = min_jump([1, 4, 3, 2, 6, 7])()
#     result2 = min_jump([0, 10, 20])()

#     print(result)
#     print(result1)
#     print(result2)