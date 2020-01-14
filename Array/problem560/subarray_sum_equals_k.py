'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals
to k.
'''


class Solution:
    def subarraySum(self, nums, k):
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        num = 0
        for i in range(len(nums)):
            if nums[i] == k:
                num += 1
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    num += 1
        #print(num)
        return num

nums1 = [1,1,1]
function = Solution()
function.subarraySum(nums1, 2)