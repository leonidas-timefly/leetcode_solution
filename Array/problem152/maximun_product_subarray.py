'''
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
'''
class Solution:
    def maxProduct(self, nums):

        min1=nums[0]
        max1=nums[0]
        g_max=nums[0]
        for num in nums[1:]:
            if num >= 0:
                min1 = min(num, min1*num)
                max1 = max(num, max1*num)
            else:
                min1, max1 = min(num, max1*num), max(num, min1*num)

            g_max = max(max1, g_max)

        #print(g_max)
        return g_max

nums1 = [2,3,-2,4]
function = Solution()
function.maxProduct(nums1)