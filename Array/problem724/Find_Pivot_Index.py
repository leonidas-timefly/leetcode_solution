'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the
numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot
index.
'''
class Solution:
    def pivotIndex(self, nums):
        k = len(nums)
        if k < 2:
            return k - 1
        if k == 2:
            if nums[0] == 0:
                return 1
            if nums[1] == 0:
                return 0
        for i in range(1, k):
            nums[i] += nums[i - 1]
        if nums[0] == nums[-1]:
            return 0
        for j in range(1, k - 1):
            if nums[j - 1] == nums[-1] - nums[j]:
                return j
        if nums[-2] == 0:
            return k - 2
        return -1

nums1 = [-1,-1,-1,0,1,1]
function = Solution()
function.pivotIndex(nums1)