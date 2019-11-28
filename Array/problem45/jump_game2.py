'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
'''
class Solution:
    def jump(self, nums):
        n = len(nums)
        level = level_end = max_index = 0
        for i in range(n - 1):
            max_index = max(max_index, i + nums[i])
            if max_index >= n - 1:
                 return (level + 1)
            if i == level_end:
                 level += 1
                 level_end = max_index
        return level





nums1 = [3, 4, 0, 2]
function = Solution()
function.jump(nums1)