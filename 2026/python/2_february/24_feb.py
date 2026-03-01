#sorting DSA algorithoms

#bubble sorting

class bubble_sort:
    def __init__(self, num_list):
        self.num_list = num_list
        self.list_length = len(num_list)

    def __call__(self):
        for i in range(self.list_length):
            for j in range(self.list_length - i - 1):
                if self.num_list[j] > self.num_list[j + 1]:
                    self.num_list[j],self.num_list[j + 1] = self.num_list[j + 1], self.num_list[j]
        return self.num_list
    
# result_bubble_sort = bubble_sort([64, 34, 25, 12, 22, 11, 90, 5])()
# print(result_bubble_sort)

#selection sorting

class selection_sort:
    def __init__(self, num_list):
        self.num_list = num_list
        self.list_length = len(num_list)
        
    def __call__(self):
        for i in range(self.list_length):
            min_i = i
            for j in range(i, self.list_length):
                if self.num_list[j] < self.num_list[min_i]:
                    min_i = j
            self.num_list[min_i],self.num_list[i] = self.num_list[i],self.num_list[min_i]
        return self.num_list
    
# result_selection_sort = selection_sort([64, 34, 25, 5, 22, 11, 90, 12])()
# print(result_selection_sort)
                
