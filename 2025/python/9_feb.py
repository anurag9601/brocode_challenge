def rearranged_defference(big_num):
    lst_big_num = []
    sort_int = 0
    reverse_int = 0

    while(big_num != 0):   
        current_num = big_num % 10
        big_num = big_num // 10
        set_value = False
        if(len(lst_big_num) == 0):
            lst_big_num.append(current_num)
        else:
            for i in range(len(lst_big_num)):
                if(current_num <= lst_big_num[i]):
                    lst_big_num.insert(i, current_num)
                    set_value = True
                    break
            if not set_value:
                lst_big_num.insert(len(lst_big_num), current_num)
    
    for i in range(len(lst_big_num)):
        sort_int = sort_int * 10 + lst_big_num[i]
        reverse_int = reverse_int * 10 + lst_big_num[len(lst_big_num) - 1 - i]
    
    return reverse_int - sort_int

# print(rearranged_defference(972882))
# print(rearranged_defference(3320707))
# print(rearranged_defference(90010))

def alphabet_index(alphabet, input_str):
    highest_index , highest_index_letter = 0 , ""

    for letter in input_str:
        index_of_current_letter = alphabet.index(letter.lower()) + 1
        if(index_of_current_letter > highest_index):
            highest_index = index_of_current_letter
            highest_index_letter = letter
        
    return str(highest_index) + highest_index_letter

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# print(alphabet_index(alphabet, "Flavio"))
# print(alphabet_index(alphabet, "Andrey"))
# print(alphabet_index(alphabet, "Oscar"))

def sort_by_letter(input_lst, alphabet=alphabet):
    letter_index_lst = []

    for str in input_lst:
        for el in str:
            if(el in alphabet):
                letter_index_lst.append(alphabet.index(el))
    
    for i in range(len(letter_index_lst)):
        min_value_i = i
        for j in range(i, len(letter_index_lst)):
            if(letter_index_lst[j] < letter_index_lst[min_value_i]):
                min_value_i = j
        letter_index_lst[min_value_i],letter_index_lst[i] = letter_index_lst[i],letter_index_lst[min_value_i]
        input_lst[min_value_i],input_lst[i] = input_lst[i],input_lst[min_value_i]
    
    return input_lst

# print(sort_by_letter(["932c", "832u32", "2344b"]))
# print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
# print(sort_by_letter(["572z", "5y5", "304q2"]))
# print(sort_by_letter([]))

def last_name_lensort(name_lst):
    for i in range(len(name_lst)):
        mini_last_name_i = i
        for j in range(i, len(name_lst)):
            current_last_name_len = name_lst[j].split(" ")[1]
            if(len(current_last_name_len) < len(name_lst[mini_last_name_i].split(" ")[1])):
                mini_last_name_i = j
        name_lst[mini_last_name_i],name_lst[i] = name_lst[i],name_lst[mini_last_name_i]
    return name_lst

# print(last_name_lensort([
#   "Jennifer Figueroa",
#   "Heather Mcgee",
#   "Amanda Schwartz",
#   "Nicole Yoder",
#   "Melissa Hoffman"
# ]))

def who_passed(students_marks_dic):
    passed_student_lst = []
    
    for student_name, student_marks in students_marks_dic.items():
        is_passed = True
        for mark in student_marks:
            mark_split = mark.split("/")

            if(mark_split[0] != mark_split[1]):
                is_passed = False
                break
        
        if is_passed:
            passed_student_lst.append(student_name)
        
    return sorted(passed_student_lst)

# print(who_passed({
#   "John" : ["5/5", "50/50", "10/10", "10/10"],
#   "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
#   "Adam" : ["8/10", "22/25", "3/5", "5/5"],
#   "Barry" : ["3/3", "20/20"]
# }))
# print(who_passed({
#   "Zara" : ["10/10"],
#   "Kris" : ["30/30"],
#   "Charlie" : ["100/100"],
#   "Alex" : ["1/1"]
# }))
# print(who_passed({
#   "Zach" : ["10/10", "2/4"],
#   "Fred" : ["7/9", "2/3"]
# }))

def get_best_student(students_names_marks):
    max_ava = 0
    max_ava_stu = ""

    for student_name, student_marks in students_names_marks.items():
        current_stu_ava = 0
        for mark in student_marks:
            current_stu_ava += mark
        current_stu_ava = current_stu_ava / len(student_marks)
        if(current_stu_ava > max_ava):
            max_ava = current_stu_ava
            max_ava_stu = student_name
    
    return max_ava_stu

# print(get_best_student({
#   "John": [100, 90, 80],
#   "Bob": [100, 70, 80]
# }))
# print(get_best_student({
#   "Susan": [67, 84, 75, 63],
#   "Mike": [87, 98, 64, 71],
#   "Jim": [90, 58, 73, 86]
# }))

def odd_sort(num_lst):
    for i in range(len(num_lst)):
        if(num_lst[i]%2 != 0):
            min_num_i = i
            for j in range(i, len(num_lst)):
                if(num_lst[j] < num_lst[min_num_i] and num_lst[j] % 2 != 0):
                    min_num_i = j
            num_lst[min_num_i],num_lst[i] = num_lst[i],num_lst[min_num_i]
    return num_lst

# print(odd_sort([7, 5, 2, 3, 1]))
# print(odd_sort([3, 7, 0, 9, 3, 2, 4, 8]))
# print(odd_sort([2, 2, 8, 4]))
# print(odd_sort([7, 9, 7]))
