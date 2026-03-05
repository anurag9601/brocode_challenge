class find_pairs:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        self.arr_length = len(arr)
        self.result = []
    
    def __call__(self):
        for i in range(self.arr_length - 1):
            for j in range(i + 1, self.arr_length):
                if self.arr[i] + self.arr[j] == self.target and (self.arr[i], self.arr[j]) not in self.result:
                    self.result.append((self.arr[i], self.arr[j]))
        return self.result
    
result_find_paris = find_pairs([2,7,11,15], 9)()
print(result_find_paris)