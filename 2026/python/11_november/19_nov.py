def can_see_stage(num_list: list[list[int]]) -> bool:
    for i in range(len(num_list[0])):
        for j in range(len(num_list) - 1):
            if num_list[j][i] > num_list[j + 1][i]:
                return False
    return True

# print(can_see_stage([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))
# print(can_see_stage([
#   [0, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]))
# print(can_see_stage([
#   [2, 0, 0], 
#   [1, 1, 1], 
#   [2, 2, 2]
# ]))

