'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
'''
class Solution:
    def checkPossibility(self, nums):
        count_num = 0
        if len(nums) == 0 or len(nums) == 1:
            return 1
        if nums[0] > nums[1]:
            count_num += 1
        for i in range(1, len(nums) - 2):
            if nums[i] > nums[i+1]:
                count_num += 1
                if nums[i-1] > nums[i+1] and nums[i-1] == nums[i] and nums[i+1] == nums[i+2] or nums[i-1] > nums[i+1] and nums[i] > nums[i+2]:
                    return 0
        if nums[-2] > nums[-1]:
            count_num += 1
        if count_num > 1:
            #print("0")
            return 0
        #print("1")
        return 1
nums1 = [4,2,3]
function = Solution()
function.checkPossibility(nums1)