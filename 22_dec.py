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
# print(shift_letters("Boom", 2))