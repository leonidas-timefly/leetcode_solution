'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a
k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.
'''
class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        nums.sort()
        if k == 0:
            i = 0
            temp = []
            while i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    temp.append(nums[i])
                    i += 1
                i += 1
            temp = list(set(temp))
            return len(temp)
        nums=list(set(nums))
        k_num = 0
        for i in range(len(nums)):
            if nums[i] + k in nums:
                k_num += 1
        #print(k_num)
        return k_num

nums1 = [3, 1, 4, 1, 5]
function = Solution()
function.findPairs(nums1, 2)