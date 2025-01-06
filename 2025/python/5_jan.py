def is_palindrome(input_str, index=0, filter_str=""):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if(len(input_str) == 1 or len(input_str) == 0):
        return True

    if(index < len(input_str)):
        if(input_str[index].lower() in alphabet):
            filter_str = filter_str + input_str[index]
            return is_palindrome(input_str, index + 1, filter_str)
        else:
            return is_palindrome(input_str, index + 1, filter_str)
    else:
        reversed_str = filter_str[::-1]
        return filter_str.lower() == reversed_str.lower()

# print(is_palindrome("Go hang a salami, I'm a lasagna hog!"))
# print(is_palindrome("This phrase, surely, is not a palindrome!"))
# print(is_palindrome("Eva, can I see bees in a cave?"))

def sum_of_arr(nums_arr, arr_sum=0):
    if(len(nums_arr) == 0):
        return 0
    elif(len(nums_arr) == 1):
        return nums_arr[0]
    else:
        arr_sum += sum_of_arr(nums_arr[1:], arr_sum)
        return arr_sum + nums_arr[0]

# print(sum_of_arr([1,2,3,4,5]))

def is_happy(num):
    str_num = str(num)
    if(len(str_num) == 1 and num == 1):
        return True
    elif(len(str_num) == 1 and num > 1):
        return False
    else:
        current_sum = 0
        for i in str_num:
            current_sum += int(i)**2
        num = current_sum
        return is_happy(num)

# print(is_happy(67))
# print(is_happy(139)) #This will return True
# print(is_happy(1327))
# print(is_happy(3970)) #This will return True
# print(is_happy(2871))

def collect(input_str, n):
    if len(input_str) < n:
        return []

    current_slice = input_str[:n]
    remaining_slice = collect(input_str[n:], n)

    return sorted([current_slice] + remaining_slice)

# print(collect("intercontinentalisationalism", 6))
# print(collect("strengths", 3))