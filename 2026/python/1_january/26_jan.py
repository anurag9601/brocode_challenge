class sort:
    def __init__(self, num_list):
        self.num_list = num_list

    def __call__(self):
        zeros_last_i = 0
        result = []

        for n in self.num_list:
            if n == 0:
                result.insert(0, n)
                zeros_last_i += 1
            elif n == 1:
                result.insert(zeros_last_i, n)
            elif n == 2:
                result.append(n)
        return result
    
# if __name__ == "__main__":
#     result = sort([0, 1, 2, 0, 1, 2])()
#     result1 = sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])()

#     print(result)
#     print(result1)

