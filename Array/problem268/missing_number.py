'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                #print(i)
                return i
        #print(len(nums))
        return len(nums)
nums1 = [0]
function = Solution()
function.missingNumber(nums1)