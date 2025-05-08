def is_magic(nums):
    constant_sum = None

    left_diagonal_sum = 0
    right_diagonal_sum = 0

    #Check row col and diagonal sum
    for i in range(len(nums)):
        vertical_sum = 0
        horizontal_sum = 0
        for j in range(len(nums[0])):
            vertical_sum += nums[j][i]
            horizontal_sum += nums[i][j] 
        if constant_sum == None:
            constant_sum = vertical_sum
        if vertical_sum != horizontal_sum or constant_sum != vertical_sum or constant_sum != horizontal_sum:
            return False
        left_diagonal_sum += nums[i][i]
        right_diagonal_sum += nums[i][(len(nums[0]) - 1) - i]
    if left_diagonal_sum != constant_sum or right_diagonal_sum != constant_sum:
        return False
    
    return True

# print(is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
# print(is_magic([[1, 2], [3, 4]]))

def identify(*args):
    cube_length = len(args)

    missing_part = 0
    for cube_part in args:
        if len(cube_part) != 3:
            missing_part += (3 - len(cube_part))
    
    if missing_part == 0:
        if cube_length == 1:
            return f"Missing ${1}"
        elif cube_length == 2:
            return "Non-full"
        elif cube_length == 3:
            return "Full"
    else:
        return f"Missing {missing_part}"
    
# print(identify(
#     ["O", "O", "O"],
#     ["O", "O", "O"],
#     ["O", "O", "O"]
# ))
# print(identify(
#   ["O", "O", "O"],
#   ["O", "O", "O"])
#   )
# print(identify(
#   ["O", "O"],
#   ["O", "O", "O"],
#   ["O", "O", "O"]
#   ))

def overlapping_rectangles(pointer1, pointer2):
    pointer1_width = pointer1[0] + pointer1[2]
    pointer1_height = pointer1[1] + pointer1[3]

    pointer2_width = pointer2[0] + pointer2[2]
    pointer2_height = pointer2[1] + pointer2[3]

    min_w = pointer1_width if pointer1_width < pointer2_width else pointer2_width
    min_h = pointer1_height if pointer1_height < pointer2_height else pointer2_height
    max_x = pointer1[0] if pointer1[0] > pointer2[0] else pointer2[0]
    max_y = pointer1[1] if pointer1[1] > pointer2[1] else pointer2[1]

    overlap_x =  min_w - max_x
    overlap_y = min_h - max_y

    return overlap_x * overlap_y

# print(overlapping_rectangles([ 2, 1, 3, 4 ], [ 3, 2, 2, 5 ]))
# print(overlapping_rectangles([ 2, -9, 11, 5 ], [ 5, -11, 2, 9 ]))
# print(overlapping_rectangles([ -8, -7, 4, 7 ],  [-5, -9, 4, 7 ]))
    
