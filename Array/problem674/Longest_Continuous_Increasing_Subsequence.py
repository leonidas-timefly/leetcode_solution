'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
'''
class Solution:
    def findLengthOfLCIS(self, nums):
        i = 0
        count_num = 1
        max_count = 1
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                count_num += 1
                i += 1
            else:
                if i == len(nums) - 1:
                    return max_count
                else:
                    max_count = max(max_count, count_num)
                    count_num = 1
                    i += 1
        #print(max_count)
        return max_count
nums1 = [1,3,5,4,7]
function = Solution()
function.findLengthOfLCIS(nums1)