def timmy_is_in_dict(items):
    return "Timmy is gone" if items["timmy"] else "Timmy is here!"

# print(timmy_is_in_dict({
#   "tv": 30,
#   "timmy": 20,
#   "stereo": 50,
# }))

def can_plant_flowers(flowerbed, n):
    plant_flowers = 0

    for i in range(len(flowerbed)):
        if i == 0 and flowerbed[i] == 0 :
            if len(flowerbed) == 1 or flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                plant_flowers += 1
        elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            plant_flowers += 1 
        elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            plant_flowers += 1
    
    return True if plant_flowers >= n else False

# print(can_plant_flowers([1,0,0,0,1], 1))
# print(can_plant_flowers([1,0,0,0,1], 2))

def move_zero(nums):
    non_zero_move_i = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_move_i],nums[i] = nums[i],nums[non_zero_move_i]
            non_zero_move_i += 1
    return nums

# print(move_zero([0,1,0,3,12]))
# print(move_zero([0]))

def is_subsequence():
    if(s == ""):
        return True

    s_i = 0
    for i in range(len(t)):
        if t[i] == s[s_i]:
            s_i += 1
            if(s_i == len(s)):
                return True
    
    return False

# print(is_subsequence("abc", "ahbgdc"))

