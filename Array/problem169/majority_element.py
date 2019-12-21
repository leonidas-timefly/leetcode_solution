'''
Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        num = [0]*(nums[-1] + 1)
        for i in range(len(nums)):
            num[nums[i]] += 1
            if num[nums[i]] > len(nums)/2:
                #print(nums[i])
                return nums[i]
nums1 = [3,2,3]
function = Solution()
function.majorityElement(nums1)