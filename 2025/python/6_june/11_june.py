def group(nums, length):
    list_divide = round(len(nums) / length)
    result = []

    if(len(nums) < length):
        return "Invalid length"
    
    index = 0
    while list_divide != index:
        temp = []
        for i in range(index, len(nums), list_divide):
            temp.append(nums[i])
        result.append(temp)
        index += 1
    
    return result

# print(group([1, 2, 3, 4], 2))
# print(group([1, 2, 3, 4, 5, 6, 7], 4))
# print(group([1, 2, 3, 4, 5], 1))
# print(group([1, 2, 3, 4, 5, 6], 4))

def valid_word_nest(word, nested_word):
    while word in nested_word and nested_word != "":
        new_nested_word = nested_word.replace(word, "")
        nested_word = new_nested_word
    
    return True if nested_word == "" else False

# print(valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel"))
# print(valid_word_nest("painter", "ppaintppapaipainterinternteraintererainter"))
# print(valid_word_nest("shape", "sssshapeshapehahapehpeape"))
