def find_median_sorted_array(nums1, nums2):
    merge = []

    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1

    merge.extend(nums1[i:])
    merge.extend(nums2[j:])
    
    merge_l = len(merge)

    if merge_l % 2 == 0:
        return (merge[merge_l//2 - 1] + merge[merge_l//2]) / 2
    else:
        return merge[merge_l//2]

# print(find_median_sorted_array([1,2],[3,4]))