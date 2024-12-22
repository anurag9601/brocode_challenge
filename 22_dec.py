def shift_letters(s, n):
    lst_s = [*s]
    length_count = 0
    while(length_count != len(s)):
        if(s[length_count] != " "):
            insert_value = s[length_count]
            current_i_count = length_count
            shift_count = 0
            while(shift_count != n):
                if(current_i_count == len(s)-1):
                    current_i_count = 0
                else:
                    current_i_count += 1
                if(s[current_i_count] != " "):
                    shift_count += 1
            lst_s[current_i_count] = insert_value
            length_count += 1
        elif(s[length_count] == " "):
            length_count += 1
    
    return "".join(lst_s)

# print(shift_letters("This is a test",  4))
# print(shift_letters("A B C D E F G H", 5))
# print(shift_letters("Boom", 7))


def subtract_matrix(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        temp = []
        for j in range(len(lst1[0])):
            subtract_val = lst1[i][j] - lst2[i][j]
            temp.append(subtract_val)
        result.append(temp)
    
    for i in result:
        print(i)
    
# subtract_matrix([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ], [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ])

def is_prime_binary_search(primes, target):
    left = 0
    right = len(primes) - 1

    while(left <= right):
        mid = (left + right) // 2

        if(primes[mid] == target):
            return "yes"

        if(primes[mid] > target):
            right -= 1
        else:
            left += 1
    
    return "no"

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# print(is_prime_binary_search(primes, 3))
# print(is_prime_binary_search(primes, 4))
# print(is_prime_binary_search(primes, 67))
# print(is_prime_binary_search(primes, 36))

# Write a function that sorts the positive numbers in ascending order, and keeps the negative numbers untouched.

def pos_neg_sort(input_lst):
    for i in range(len(input_lst)):
        if(input_lst[i] > 0):
            min_i = i
            for j in range(i,len(input_lst)):
                if(input_lst[j] > 0):
                    if(input_lst[min_i] > input_lst[j]):
                        min_i = j
            input_lst[min_i],input_lst[i] = input_lst[i],input_lst[min_i]
    return input_lst

# print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))
# print(pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]))
# print(pos_neg_sort([-5, -5, -5, -5, 7, -5]))
# print(pos_neg_sort([]))

def string_extension(s):
    ints = "0123456789"
    recurs_i = 1

    result = ""

    for i in s:
        if(i in ints):
            recurs_i = int(i)
        else:
            for j in range(recurs_i):
                result += i

    return result

# print(string_extension("3Mat"))
# print(string_extension("3M123u42b12a"))
# print(string_extension("3M2u5b2a1s1h2i1r"))
# print(string_extension("airforce"))
# print(string_extension(""))