'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''

class Solution:
    def searchRange(self, nums, target):
        import bisect
        if not nums:
            return [-1, -1]
        f = bisect.bisect_left(nums, target)
        l = bisect.bisect_left(nums, target + 1) - 1
        return [f, l] if f < len(nums) and nums[f] == target and nums[l] == target else [-1, -1]


nums1 = [-2,1,-3,4,-1,2,1,-5,4]
function = Solution()
function.searchRange(nums1)