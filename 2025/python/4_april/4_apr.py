# for i in range(1,6):
#     for j in range(4+i):
#         if j > 4-i:
#             if j == (4-i + 1) or j == (4+i - 1):
#                 print(i, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    2 2
#   3   3
#  4     4
# 5       5

# for i in range(1,6):
#     for j in range(4+i):
#         if j > 4-i:
#             if j == (4-i + 1) or j == (4 + i - 1):
#                 print(6-i, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     5
#    4 4
#   3   3
#  2     2
# 1       1

# for i in range(5):
#     for j in range(9-i):
#         if j >= i:
#             if j == i or j == (9-i-1):
#                 print(i+1, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

# 1       1
#  2     2
#   3   3
#    4 4
#     5

# for i in range(5):
#     for j in range(9-i):
#         if j >= i:
#             if j == i or j == (9-i-1):
#                 print(5-i, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

# 5       5
#  4     4
#   3   3
#    2 2
#     1

# for i in range(9):
#     iteration = 5+i if i < 5 else iteration - 1
#     print_state = i+1 if i < 5 else print_state - 1
#     for j in range(iteration):
#         if j >= abs(4-i):
#             if j == abs(4-i) or j == (iteration - 1):
#                 print(print_state, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     1
#    2 2
#   3   3
#  4     4
# 5       5
#  4     4
#   3   3
#    2 2
#     1

# for i in range(9):
#     iteration = 5+i if i < 5 else iteration - 1
#     print_state = 5-i if i < 5 else print_state + 1
#     for j in range(iteration):
#         if j >= abs(4-i):
#             if j == abs(4-i) or j == (iteration - 1):
#                 print(print_state, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

#     5
#    4 4
#   3   3
#  2     2
# 1       1
#  2     2
#   3   3
#    4 4
#     5

# for i in range(5):
#     iteration = 5 - i if i < 3 else iteration + 1
#     num_print = i if i < 3 else num_print - 1
#     for j in range(iteration):
#         if j >= num_print:
#             if j == num_print or j == (iteration - 1):
#                 print(i+1, end="")
#             else:
#                 print(" ", end="")
#         else:
#             print(" ", end="")
#     print()

# 1   1
#  2 2
#   3
#  4 4
# 5   5

