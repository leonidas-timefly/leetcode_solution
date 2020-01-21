'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average
value. And you need to output the maximum average value.
'''
class Solution:
    def findMaxAverage(self, nums, k):
        max_sum = sum(nums[0:k])
        sum_windows = max_sum
        for i in range(k, len(nums)):
            sum_windows = sum_windows + nums[i] - nums[i -k]
            max_sum = max(max_sum, sum_windows)
        #print(head_index)
        #print(max_sum / k)
        return max_sum / k
nums1 = [1,12,-5,-6,50,3]
function = Solution()
function.findMaxAverage(nums1, 4)