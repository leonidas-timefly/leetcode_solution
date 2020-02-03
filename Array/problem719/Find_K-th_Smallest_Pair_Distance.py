'''
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is
defined as the absolute difference between A and B.
'''
class Solution:
    def smallestDistancePair(self, nums, k):
        len_count = max(nums) + 1
        #print(len_count)
        count_num = [0] * len_count
        for m in range(len(nums)):
            count_num[nums[m]] += 1
        #print(count_num)
        for i in range(len_count):
            #print(i)
            for j in range(len_count - i):
                k = k - (count_num[j] * (count_num[j] - 1) / 2 if i == 0 else count_num[j] * count_num[j + i])
                #print(j, k)
                if k <= 0:
                    #print(i)
                    return i

nums1 = [1,6,1]
function = Solution()
function.smallestDistancePair(nums1, 3)