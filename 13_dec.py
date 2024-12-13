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
# print(two_sum([1, 3, 5, 7, 9], 12))
# print(two_sum(list(range(1, 10001)), 19999))

def find_long_substr(input_str):
    longest_substr = ""

    if(len(input_str) == 1):
        return input_str
    else:
        for i in range(len(input_str)):
            temp = ""
            for j in range(i, len(input_str)):
                if(input_str[j] not in temp):
                    temp += input_str[j]
                    if(len(temp) > len(longest_substr)):
                        longest_substr = temp
                else:
                    break
    return len(longest_substr)

# print(find_long_substr("abc def ghi"))
# print(find_long_substr("abcdabcdabcdabcd"))

#Return an array where each element is the product of all elements except itself.

def array_accept_self(lst):
    result = []

    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst)):
            if(j != i):
                if(sum == 0):
                    sum = lst[j]
                else:
                    sum *= lst[j]
        result.append(sum)
    return result

# print(array_accept_self([1, 2, 3, 4]))

