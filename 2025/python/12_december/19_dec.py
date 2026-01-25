# Find missing number of the list problem

class missing_n:
    def __init__(self, num_list):
        self.num_list = num_list

    def find(self):
        expected_num = 1
        for i in range(len(self.num_list)):
            min_i = i
            for j in range(i, len(self.num_list)):
                if self.num_list[min_i] > self.num_list[j]:
                    min_i = j
            self.num_list[min_i],self.num_list[i] = self.num_list[i], self.num_list[min_i]
            
            if self.num_list[i] != expected_num:
                return expected_num
            else:
                expected_num += 1
        return expected_num

# if __name__ == "__main__":
#     obj = missing_n([1,2,3,5])
#     obj1 = missing_n([8, 2, 4, 5, 3, 7, 1])

#     result = obj.find()
#     result1 = obj1.find()

#     print(result)
#     print(result1)

class max_sub_array_sum:
    def __init__(self, num_list):
        self.num_list = num_list
        self.sub_arr_list = []
        self.max_sum = float("-inf")
        self.sum_list = []

    def find(self):
        for i in range(len(self.num_list)):
            temp = []
            for j in range(i, len(self.num_list)):
                temp.append(self.num_list[j])

                curr_sum = sum(temp)

                self.sub_arr_list.append(temp)

                self.sum_list.append(curr_sum)

                if curr_sum > self.max_sum:
                    self.max_sum = curr_sum
    
        max_num_index = self.sum_list.index(self.max_sum)
        return f"max_sum: {self.max_sum} arr:{self.sub_arr_list[max_num_index]}"
    
# if __name__ == "__main__":
#     obj = max_sub_array_sum([2, 3, -8, 7, -1, 2, 3])
#     obj1 = max_sub_array_sum([-2, -4])
#     obj2 = max_sub_array_sum([5, 4, 1, 7, 8])

#     result = obj.find()
#     result1 = obj1.find()
#     result2 = obj2.find()

#     print(result)
#     print(result1)
#     print(result2)
    

