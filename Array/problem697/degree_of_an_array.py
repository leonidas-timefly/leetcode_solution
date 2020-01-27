'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of
any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
class Solution:
    def findShortestSubArray(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return 1
        temp = [0]*(max(nums) + 1)
        for i in range(len_nums):
            temp[nums[i]] += 1
        same_degree = []
        k = max(temp)
        if k == 1:
            return 1
        for j in range(len(temp)):
            if temp[j] == k:
                same_degree.append(j)
        for h in range(len(same_degree)):
            for k in range(len_nums):
                begin_index = nums.index(same_degree[h])
                break
            for m in range(len_nums - 1, -1, -1):
                if nums[m] == same_degree[h]:
                    end_index = m
                    break
            same_degree[h] = end_index - begin_index + 1
        return min(same_degree)

nums1 = [49999,1,1,1,2,1]
function = Solution()
function.findShortestSubArray(nums1)