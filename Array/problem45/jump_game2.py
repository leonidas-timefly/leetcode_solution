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
            max_index = max(max_index, i + nums[i])  # Keep finding max jump in current level (until end of level is reached below)

            if max_index >= n - 1:  # Reached end of list
                 return (level + 1)

            if i == level_end:  # If reached end of current level
                 level += 1  # Start new level (jump)
                 level_end = max_index  # Set end of new level
        #print(level)

        return level



nums1 = [3, 4, 0, 2]
function = Solution()
function.jump(nums1)