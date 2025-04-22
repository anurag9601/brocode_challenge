def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    filter_A = ""
    filter_Z = ""

    for i in range(len(str_A)):
        if i not in ind_Z:
            filter_A += str_A[i]
        if i not in ind_A:
            filter_Z += str_Z[i]

    A_score = 0
    Z_score = 0

    for i in range(len(filter_A)):
        value_A = ord(filter_A[i])
        value_Z = ord(filter_Z[i])

        if value_A > value_Z:
            A_score += (value_A - value_Z)
        elif value_Z > value_A:
            Z_score += (value_Z - value_A)

    return { "A" : A_score, "Z" : Z_score }

# print(alpha_clash("MZNHUVIOEPTWFJCBXKALSDQGYR",
#   [1, 3, 2, 8, 10, 12, 9, 7, 4, 22],
#   "YFTUCSQOMGKPXNDWHIVJRABZEL",
#   [21, 24, 25, 3, 4, 1, 8, 9, 10, 17]))
# print(alpha_clash("OZLICHFRKYBVUDSPWXJNGTQAEM",
#   [8, 6, 4, 2, 0, 10, 12, 14, 16, 18],
#   "WKJVUNXHRFDIOBTCSLZMPYGQAE",
#   [7, 5, 3, 1, 9, 11, 13, 15, 17, 19]))

def longest_run(nums):
    longest_run = 0

    temp_run = 1
    prev_diff = 0

    for i in range(len(nums) - 1):
        next_num_diff = nums[i + 1] - nums[i]
        if abs(next_num_diff) > 1 or abs(next_num_diff) == 0 or prev_diff > 0 and prev_diff != next_num_diff:
            if temp_run > longest_run:
                longest_run = temp_run
            temp_run = 1
            prev_diff = 0
        elif nums[i + 1] == (nums[i] + next_num_diff):
            prev_diff = next_num_diff
            temp_run += 1
    if temp_run > longest_run:
        longest_run = temp_run
    
    return longest_run

# print(longest_run([1, 2, 3, 10, 11, 15]))
# print(longest_run([5, 4, 2, 1]))
# print(longest_run([3, 5, 7, 10, 15]))
# print(longest_run([1, 2, 1, 2, 1, 2, 1, 2]))
# print(longest_run([10, 11, 12, 20, 19, 18, 17, 25, 26, 27, 28, 1]))
# print(longest_run([5, 5, 5, 5, 5]))
# print(longest_run([1, 2, 4, 3, 6, 5, 7, 8, 20, 19, 18, 17, 40, 41, 42, 10, 9]))