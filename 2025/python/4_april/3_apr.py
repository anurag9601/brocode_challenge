# for i in range(5):
#     for j in range(9-i):
#         if j >= i:
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(5-i, end="")
#                 else:
#                     print(" ", end="")
#             elif i%2 != 0:
#                 if j%2 != 0:
#                     print(5-i, end="")
#                 else:
#                     print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1

# for i in range(5):
#     print_state = 5-i
#     for j in range(9-i):
#         if j >= i:
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(print_state, end="")
#                     print_state -= 1
#                 else:
#                     print(" ", end="")
#             elif i%2 != 0:
#                 if j%2 != 0:
#                     print(print_state, end="")
#                     print_state -= 1
#                 else:
#                     print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

# 5 4 3 2 1
#  4 3 2 1
#   3 2 1
#    2 1
#     1

# for i in range(9):
#     iterate = 5+i if i < 5 else iterate - 1
#     print_state = iterate - 4
#     for j in range(iterate):
#         if j >= abs(5-(i+1)):
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(print_state, end="")
#                 else:
#                     print(" ", end="")
#             elif i%2 != 0:
#                 if j%2 != 0:
#                     print(print_state, end="")
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
#  4 4 4 4
#   3 3 3
#    2 2
#     1

# for i in range(9):
#     iterate = 5 + i if i < 5 else iterate - 1
#     print_state = 1 if i < 5 else i - 3
#     for j in range(iterate):
#         if j >= abs(5-(i+1)):
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(print_state, end="")
#                     print_state += 1
#                 else:
#                     print(" ", end="")
#             elif i%2 != 0:
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
#  2 3 4 5
#   3 4 5
#    4 5
#     5

# for i in range(9):
#     iterate = 5 + i if i < 5 else iterate - 1
#     print_state = 1
#     for j in range(iterate):
#         if j >= abs(5 - (i + 1)):
#             if i%2 == 0:
#                 if j%2 == 0:
#                     print(print_state, end="")
#                     print_state += 1
#                 else:
#                     print(" ", end="")
#             elif i%2 != 0:
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
#  1 2 3 4
#   1 2 3
#    1 2
#     1
