'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2),
..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
'''
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        min_max = sum(nums[::2])
        pr#int(min_max)
        return min_max
nums1 = [1,4,3,2]
function = Solution()
function.arrayPairSum(nums1)
