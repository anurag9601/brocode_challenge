#shorting DSA algorithoms

#bubble shorting

class bubble_short:
    def __init__(self, num_list):
        self.num_list = num_list
        self.list_length = len(num_list)

    def __call__(self):
        for i in range(self.list_length):
            for j in range(self.list_length - i - 1):
                if self.num_list[j] > self.num_list[j + 1]:
                    self.num_list[j],self.num_list[j + 1] = self.num_list[j + 1], self.num_list[j]
        return self.num_list
    
result_bubble_short = bubble_short([64, 34, 25, 12, 22, 11, 90, 5])()
print(result_bubble_short)