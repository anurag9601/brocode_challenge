def longest_substring(input_str):
    longest_sub_str = ""
    for i in range(len(input_str)):
        temp_str = ""
        for j in range(i, len(input_str)):
            if(input_str[j] not in temp_str):
                temp_str += input_str[j]
            else:
                break
        if(len(temp_str) > len(longest_sub_str)):
            longest_sub_str = temp_str
    return len(longest_sub_str)

# print(longest_substring("abcabcbb"))
# print(longest_substring("bbbbb"))
# print(longest_substring(" "))
# print(longest_substring("pwwkew"))

def find_median_sort_arr(nums1, nums2):
    merge_nums = nums1 + nums2
    for i in range(len(merge_nums)-1):
        min_val_i = i
        for j in range(i, len(merge_nums)):
            if(merge_nums[j] < merge_nums[min_val_i]):
                min_val_i = j
        merge_nums[min_val_i],merge_nums[i] = merge_nums[i],merge_nums[min_val_i]
    merge_lst_modules = len(merge_nums)%2
    if(merge_lst_modules > 0):
        return merge_nums[len(merge_nums)//2]
    if(merge_lst_modules == 0):
        center_i = len(merge_nums)//2 - 1
        return (merge_nums[center_i] + merge_nums[(center_i + 1)])/2

# print(find_median_sort_arr([1,2],[3,4]))
# print(find_median_sort_arr([1,2,5],[8,3,4]))

def day_of_year(input_date_str):
    date_split = input_date_str.split("/")
    year = int(date_split[2])
    month = int(date_split[0])
    days = int(date_split[1])
    
    days_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0 ):
        days_lst[1] = 29

    total_days = 0
    for i in range(len(days_lst)):
        if(i == month-1):
            break
        else:
            total_days += days_lst[i]
        
    return total_days + days
    
# print(day_of_year("11/16/2020"))
# print(day_of_year("1/9/2019"))
# print(day_of_year("3/1/2004"))
# print(day_of_year("12/31/2000"))
