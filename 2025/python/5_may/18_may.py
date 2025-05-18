# Hight order function problem , The hight order function is if function taking function as a parameter

def final(r, c, i):
    matrix = [[0 for _ in range(c)]for _ in range(r)]

    for operation in i:
        if operation[-1] == "r" and int(operation[:-1]) <= r - 1:
            row = int(operation[:-1])
            for col in range(c):
                matrix[row][col] += 1
        elif operation[-1] == "c" and int(operation[:-1]) <= c - 1:
            col = int(operation[:-1])
            for row in range(r):
                matrix[row][col] += 1
    return matrix

# print(final(3, 3, ["2r", "2c", "1r", "0c"]))
# print(final(2, 2, ["0r", "0r", "0r", "1c"]))
# print(final(2, 2, ["0c"]))
# print(final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]))
# print(final(3, 3, []))