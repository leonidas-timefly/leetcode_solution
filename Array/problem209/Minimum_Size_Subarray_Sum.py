'''
Given an array of n positive integers and a positive integer s, find the minimal length of a
contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
'''
class Solution:
    def minSubArrayLen(self, s, nums):
        start = 0
        sum_num = 0
        min_length = 10000
        for i in range(len(nums)):
            sum_num += nums[i]
            while sum_num >= s:
                min_length = min(min_length, i - start + 1)
                sum_num -= nums[start]
                start += 1
        if min_length == 10000:
            return 0
        return min_length
'''
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        if nums[0] >= s:
            return 1
        else:
            return 0
    g_min = 1000000
    for i in range(len(nums)):
        now_min = 1
        sum_num = 0
        j = i
        while sum_num + nums[j] < s:
            sum_num += nums[j]
            now_min += 1
            j += 1
            if j >= len(nums):
                now_min = 1000000
                break
        # print(g_min)
        # print("*")
        g_min = min(now_min, g_min)
    if g_min == 1000000:
        return 0
    # print(g_min)
    return g_min
'''


nums1 = [1,2,3,4,5]
function = Solution()
function.minSubArrayLen(15, nums1)