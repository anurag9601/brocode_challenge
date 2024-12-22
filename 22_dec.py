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