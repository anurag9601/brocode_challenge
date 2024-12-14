#Find minimum in rotated sorted array

def minimum_of_array(arr):
    minimum = float("inf")
    for i in arr:
        if(i < minimum):
            minimum = i
    return minimum

# print(minimum_of_array([4, 5, 6, 7, 0, 1, 2]))

def count_layers(lst):
    layer_count = 0
    # if(len(lst) == 1 or len(lst) == 2):
    #     return layer_count
    # else:
    #     center_index = round(len(lst)/2)
    #     left,right = 0, len(lst[0])-1
    #     while left < right:
    #         if(lst[center_index][left] == lst[center_index][right] and lst[center_index][left] == lst[center_index-1][left]):
    #             layer_count += 1
    #         left += 1
    #         right -= 1
    #     return layer_count

    #This will collect the unique line of the rug
    unique_layers = set(lst)

    return len(unique_layers)

# print(count_layers([
#   "AAAAAAAAAAA",
#   "AABBBBBBBAA",
#   "AABCCCCCBAA",
#   "AABCAAACBAA",
#   "AABCADACBAA",
#   "AABCAAACBAA",
#   "AABCCCCCBAA",
#   "AABBBBBBBAA",
#   "AAAAAAAAAAA"
# ]))

def cup_swapping(lst):
    current_position = "B"

    for i in lst:
        if(current_position == i[0]):
            current_position = i[1]
        elif(current_position == i[1]):
            current_position = i[0]
    
    return current_position

# print(cup_swapping(["AB", "CA"]))
# print(cup_swapping(["AC", "CA", "CA", "AC"]))

def row_sum(num):
    count = 0
    result = 0
    for i in range(1, num+1):
        for j in range(i):
            count += 1
            if(i == num):
                result += count
    return result

print(row_sum(2))

            
