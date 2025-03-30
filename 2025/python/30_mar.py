#Number printing

# for i in range(5):
#     for j in range(5):
#         print(i + 1, end="")
#     print()

# 11111
# 22222
# 33333
# 44444
# 55555

# for i in range(5):
#     for j in range(5):
#         print(j + 1, end = "")
#     print()

# 12345
# 12345
# 12345
# 12345
# 12345

# for i in range(5, 0, -1):
#     for j in range(5):
#         print(i, end="")
#     print()

# 55555
# 44444
# 33333
# 22222
# 11111

# for i in range(5):
#     for j in range(5,0,-1):
#         print(j, end="")
#     print()

# 54321
# 54321
# 54321
# 54321
# 54321

# for i in range(5):
#     for j in range(i+1):
#         print(i+1, end="")
#     print()

# 1
# 22
# 333
# 4444
# 55555

# for i in range(5):
#     for j in range(i+1):
#         print(j+1, end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# for i in range(5):
#     for j in range(5-i):
#         print(i+1, end="")
#     print()

# 11111
# 2222
# 333
# 44
# 5

# for i in range(5, 0, -1):
#     for j in range(i):
#         print(j+1, end="")
#     print()

# 12345
# 1234
# 123
# 12
# 1

# for i in range(5, 0, -1):
#     for j in range(i):
#         print(i, end="")
#     print()

# 55555
# 4444
# 333
# 22
# 1

# for i in range(5, 0, -1):
#     for j in range(i):
#         print(5-j, end="")
#     print()

# 54321
# 5432
# 543
# 54
# 5

# for i in range(1,6):
#     for j in range(5, 0, -1):
#         if j <= (i):
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    22
#   333
#  4444
# 55555

# for i in range(5, 0, -1):
#     for j in range(5):
#         if(j >= i - 1):
#             print(j-(i-2), end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    12
#   123
#  1234
# 12345

# for i in range(5, 0, -1):
#     for j in range(5):
#         if(j >= (5-i)):
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()

# 55555
#  4444
#   333
#    22
#     1

# for i in range(5):
#     for j in range(1,6):
#         if j > i:
#             print(j-i, end="")
#         else:
#             print(" ", end="")
#     print()

# 12345
#  1234
#   123
#    12
#     1

# for i in range(5):
#     for j in range(5+i):
#         if (5-1-i <= j):
#             print(i + 1, end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    222
#   33333
#  4444444
# 555555555

# for i in range(5):
#     for j in range(5+i):
#         if j >= 4-i:
#             print(1+i+i, end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    333
#   55555
#  7777777
# 999999999

# for i in range(5):
#     print_state = 1
#     for j in range(5+i):
#         if j >= 4-i:
#             print(print_state, end="")
#             print_state += 1
#         else:
#             print(" ", end="")
#     print()

#     1
#    123
#   12345
#  1234567
# 123456789

# for i in range(5):
#     print_state = 1 + i + i
#     for j in range(5+i):
#         if j >= 4 - i:
#             print(print_state, end="")
#             print_state -= 1
#         else:
#             print(" ", end="")
#     print()

#     1
#    321
#   54321
#  7654321
# 987654321

# for i in range(5):
#     print_state = i
#     right_print = False
#     for j in range(5+i):
#         if j >= 4 - i:
#             if print_state == 0 or right_print == True:
#                 right_print = True
#                 print(print_state, end="")
#                 print_state += 1
#             else:
#                 print(print_state, end="")
#                 print_state -= 1
#         else:
#             print(" ", end="")
#     print()

#     0
#    101
#   21012
#  3210123
# 432101234



