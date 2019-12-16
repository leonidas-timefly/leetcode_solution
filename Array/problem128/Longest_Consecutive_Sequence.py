'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    def longestConsecutive(self, nums):
        max_len = 0
        nums = list(set(nums))
        nums.sort()
        num = len(nums)
        if num == 0 or num == 1:
            return num
        num_now = 1
        i = 0
        while i < num - 1:
            while nums[i] == nums[i + 1] - 1:
                num_now += 1
                i += 1
                if i == num - 1:
                    break
            max_len = max(max_len, num_now)
            num_now = 1
            i += 1
        return max_len

nums1 = [100,4,200,1,3,2]
function = Solution()
function.longestConsecutive(nums1)