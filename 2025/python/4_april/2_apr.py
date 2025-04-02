# for i in range(4):
#     for j in range(7-i):
#         if j >= i:
#             print(4-i, end="")
#         else:
#             print(" ", end="")
#     print()

# 4444444
#  33333
#   222
#    1

# for i in range(4):
#     for j in range(7-i):
#         if(j >= i):
#             print(7-(i*2), end="")
#         else:
#             print(" ", end="")
#     print()

# 7777777
#  55555
#   333
#    1

# for i in range(4):
#     current_count = 0
#     for j in range(7-i):
#         if j >= i:
#             current_count += 1
#             print(current_count, end="")
#         else:
#             print(" ", end="")
#     print()

# 1234567
#  12345
#   123
#    1

# for i in range(7):
#     if i > 3:
#         for j in range(3, i-4, -1):
#             print(j, end="")
#     else:
#         for j in range(3, 2-i, -1):
#             print(j, end="")
#     print()

# 3
# 32
# 321
# 3210
# 321
# 32
# 3

# for i in range(7, 0, -1):
#     for j in range(abs(i-4), 4):
#         print(j, end="")
#     print()

# 3
# 23
# 123
# 0123
# 123
# 23
# 3

# for i in range(7, 0, -1):
#     print_state = 3
#     for j in range(4):
#         if j >= (abs(i-4)):
#             print(print_state, end="")
#             print_state -= 1
#         else:
#             print(" ", end="")
#     print()

#    3
#   32
#  321
# 3210
#  321
#   32
#    3

# for i in range(7, 0, -1):
#     for j in range(4):
#         if j >= abs(i-4):
#             print(j, end="")
#         else:
#             print(" ", end="")
#     print()

#    3
#   23
#  123
# 0123
#  123
#   23
#    3

# for i in range(1,6):
#     for j in range(4+i):
#         if j > (4-i):
#             if i%2 != 0:
#                 if j%2 == 0:
#                     print(i, end="")
#                 else:
#                     print(" ", end="")
#             elif i%2 == 0:
#                 if j%2 != 0:
#                     print(i, end="")
#                 else:
#                     print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

# for i in range(1 , 6):
#     print_state = 1
#     for j in range(4+i):
#         if j > (4 - i):
#             if i%2 != 0:
#                 if j%2 == 0:
#                     print(print_state, end="")
#                     print_state += 1
#                 else:
#                     print(" ", end="")
#             elif i%2 == 0:
#                 if j%2 != 0:
#                     print(print_state, end="")
#                     print_state += 1
#                 else:
#                     print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

