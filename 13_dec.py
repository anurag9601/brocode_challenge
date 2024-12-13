#find the longest palindrome in the given string

def get_longest_palindrome(input_str):
    longest_palin = ""
    length_long_palin = 0

    if(len(input_str) == 1):
        return input_str
    else:
        for i in range(len(input_str)):
            temp = ""
            reverse_temp = ""
            for j in range(i, len(input_str)):
                temp += input_str[j]
                reverse_temp = temp[::-1]
                if(temp == reverse_temp):
                    if(length_long_palin < len(temp)):
                        longest_palin = temp
                        length_long_palin = len(temp)
        return longest_palin

# print(get_longest_palindrome("abcba12321"))
# print(get_longest_palindrome("forgeeksskeegfor"))
# print(get_longest_palindrome("aaaa"))
# print(get_longest_palindrome("a"))
# print(get_longest_palindrome("ac"))

def two_sum(numbers, target):
    left ,right = 0, len(numbers) -1 

    result = []

    while left < right:
        sum = numbers[left] + numbers[right]

        if sum == target:
            result.append(left + 1)
            result.append(right + 1)
            return result
        elif sum < target:
            left += 1
        else:
            right += 1

# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum(list(range(1, 10001)), 19999))