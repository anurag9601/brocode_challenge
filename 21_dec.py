def reverse_integer(int):
    temp_int = int if int >= 0 else -int
    reverse_int = 0
    while temp_int != 0:
        lst_dig = temp_int%10
        temp_int = temp_int//10

        #32-bit range 
        #maximum value = 2^31 - 1 = 2147483647
        #minimum value = -2^31 = -2147483647

        if (reverse_int > 2147483647 // 10 or (reverse_int == 2147483647 // 10 and lst_dig > 7)):
            return 0

        if (reverse_int < -2147483648 // 10 or (reverse_int == -2147483648 // 10 and lst_dig < -8)):
            return 0 

        reverse_int = reverse_int * 10 + lst_dig

    if(int < 0):
        return reverse_int * -1
    else:
        return reverse_int

# print(reverse_integer(120))
# print(reverse_integer(-123))