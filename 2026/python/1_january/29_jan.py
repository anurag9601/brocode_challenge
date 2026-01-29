alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

space_c = 4
for i in range(1, 10, 2):
    for j in range(space_c):
        print(" ", end="")
    for k in range(i):
        print(alpha[i - 1], end="")
    space_c -= 1
    print()

#     A
#    CCC
#   EEEEE
#  GGGGGGG
# IIIIIIIII
