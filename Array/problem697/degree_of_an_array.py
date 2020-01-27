'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
class Solution:
    def findShortestSubArray(self, nums):
        if len(nums) == 1:
            return 0
        temp = [0]*(max(nums) + 1)
        for i in range(len(nums)):
            temp[nums[i]] += 1
        index_num = temp.index(max(temp))
        #print(index_num)
        for k in range(len(nums)):
            if nums[k] == index_num:
                begin_index = k
                break
        for m in range(len(nums) - 1, -1, -1):
            if nums[m] == index_num:
                end_index = m
                break
        #print(end_index - begin_index + 1)
        return end_index - begin_index + 1

nums1 = [1,2,2,3,1,4,2]
function = Solution()
function.findShortestSubArray(nums1)