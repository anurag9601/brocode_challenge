#Problem 1
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

#Solution 1
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if(n==0):
            return nums1
        else:
            count = n
            for i in range((m+n)-1,-1,-1):
                if(nums1[i] == 0 and count != 0):
                    nums1[i] = nums2[count-1]
                    count -= 1
            for i in range(m+n):
                mini = i
                for j in range(i,m+n):
                    if(nums1[mini]>nums1[j]):
                        mini = j
                nums1[i],nums1[mini] = nums1[mini],nums1[i]
            return nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
