def bitwise_index(nums):
    max_even_i , max_even_n = None, None

    for i, num in enumerate(nums):
        if num & 1 == 0:
            if not max_even_i and not max_even_n:
                max_even_i = i
                max_even_n = num
            elif max_even_n < num:
                max_even_i = i
                max_even_n = num

    if not max_even_i and not max_even_n:
        return "No even integer found!"
    else:
        return {f"@even index {max_even_i}" : max_even_n}

# print(bitwise_index([107, 19, 36, -18, -78, 24, 97]))
# print(bitwise_index([4, 4, 4, 4, 4, 4]))
# print(bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]))
# print(bitwise_index([-31, -7, -13, -7, -9, -13]))

def pentagonal(n):
    dots = 0
    for i in range(n):
        if i == 0:
            dots += 1
        else:
            dots += 5 * i
    return dots

# print(pentagonal(3))
# print(pentagonal(8))
# print(pentagonal(6))
# print(pentagonal(1))

#Digit count using recursion way
def digits_count(n, n_count=0):
    if n == 0:
        return n_count
    else:
        n_count += 1
        n = n // 10
        return  digits_count(n, n_count)
    
# print(digits_count(1289396387328))
# print(digits_count(4666))

def remove_letters(s_list, s):
    for char in s:
        if char in s_list:
            index = s_list.index(char)
            #Both methods will work same

            # del s_list[index]
            s_list = s_list[:index] + s_list[index + 1:]

    return s_list

# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))

def count_layers(layers):
    return len(set(layers))

# print(count_layers([
#   "AAAA",
#   "ABBA",
#   "AAAA"
# ]))
# print(count_layers([
#   "AAAAAAAAA",
#   "ABBBBBBBA",
#   "ABBAAABBA",
#   "ABBBBBBBA",
#   "AAAAAAAAA"
# ]))
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