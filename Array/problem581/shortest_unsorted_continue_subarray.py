'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
'''
class Solution:
    def findUnsortedSubarray(self, nums):
        new_nums = sorted(nums)
        min_index = 0
        max_index = 0
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                min_index = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != new_nums[j]:
                max_index = j
                break
        if min_index == 0 and max_index == 0:
            return 0
        else:
            #print(max_index - min_index + 1)
            return max_index - min_index + 1
nums1 = [2, 6, 4, 8, 10, 9, 15]
function = Solution()
function.findUnsortedSubarray(nums1)