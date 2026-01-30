# inc = 1
# for i in range(5, 0, -1):
#     print(" " * (i - 1), end="")
#     print("*" * inc, end="")
#     print()
#     inc += 2

#     *
#    ***
#   *****
#  *******
# *********

# inc = 9
# for i in range(5):
#     print(" " * i, end="")
#     for j in range(1, inc + 1):
#         print("*", end="") if j % 2 != 0 else print(" ", end="") 
#     print()
#     inc -= 2

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# for i in range(5, 0, -1):
#     print(" " * (5 - i), end="")
#     for j in range(i, 0, -1):
#         print(chr(j + 64), end=" ")
#     print()

# E D C B A 
#  D C B A 
#   C B A 
#    B A 
#     A 


