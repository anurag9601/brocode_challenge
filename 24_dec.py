def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    filter_str_A = ""
    filter_str_Z = ""

    str_A_points = 0
    str_Z_points = 0

    for i in range(len(str_A)):
        if(i not in ind_Z):
            filter_str_A += str_A[i]
    for j in range(len(str_Z)):
        if(j not in ind_A):
            filter_str_Z += str_Z[j]

    player_A_asci_val = [ord(x) for x in filter_str_A] 
    #List comprehension
    player_Z_asci_val = [ord(y) for y in filter_str_Z]

    for i in range(len(player_A_asci_val)):
        if(player_A_asci_val[i] > player_Z_asci_val[i]):
            str_A_points += player_A_asci_val[i] - player_Z_asci_val[i]
        elif(player_Z_asci_val[i] > player_A_asci_val[i]):
            str_Z_points += player_Z_asci_val[i] - player_A_asci_val[i]

    return { "A" : str_A_points, "Z" : str_Z_points }

# print(alpha_clash("MZNHUVIOEPTWFJCBXKALSDQGYR",
#   [1, 3, 2, 8, 10, 12, 9, 7, 4, 22],
#   "YFTUCSQOMGKPXNDWHIVJRABZEL",
#   [21, 24, 25, 3, 4, 1, 8, 9, 10, 17]))

# print(alpha_clash(
#   "OZLICHFRKYBVUDSPWXJNGTQAEM",
#   [8, 6, 4, 2, 0, 10, 12, 14, 16, 18],
#   "WKJVUNXHRFDIOBTCSLZMPYGQAE",
#   [7, 5, 3, 1, 9, 11, 13, 15, 17, 19]
# ))

def longest_run(lst):
    longest_run = 0

    temp = []

    for i in range(len(lst)):
        if(temp == []):
            temp.append(lst[i])
        elif(lst[i] == (temp[-1]-1) or lst[i] == (temp[-1]+1)):
            temp.append(lst[i])
        else:
            temp = []
            temp.append(lst[i])
        if(len(temp) > longest_run):
            longest_run = len(temp)
    return longest_run

# print(longest_run([1, 2, 3, 10, 11, 15]))
# print(longest_run([5, 4, 2, 1]))
# print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]))

#Greatest common divisor of string

def great_common_div_of_strs(str1, str2):

    def gcd(a, b):
        while b:
            a , b = b , a % b
            return a
    
    if( str1 + str2 != str2 + str1 ):
        return ""

    gcd_length = gcd(len(str1), len(str2))

    return str1[:gcd_length]

# print(great_common_div_of_strs("ABCABC", "ABC"))
# print(great_common_div_of_strs("ABABAB", "AB"))
# print(great_common_div_of_strs("LEET", "CODE"))
