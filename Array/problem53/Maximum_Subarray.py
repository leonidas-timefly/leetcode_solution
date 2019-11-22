'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
'''

class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        #print(max(nums))
        return max(nums)

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
function = Solution()
function.maxSubArray(nums1)