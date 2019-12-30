'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in
the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 0 or len(nums) == 1:
            return 0
        m = 0
        while nums[m] == nums[m+1] - 1:
            m += 1
            if m == len(nums) - 1:
                return 0
        for i in range(len(nums)):
            for j in range(1, k + 1):
                if i + j >= len(nums):
                    break
                if nums[i] == nums[i+j]:
                    #print("1")
                    return 1
        #print("0")
        return 0


nums1 = [1,2,3,1]
function = Solution()
function.containsNearbyDuplicate(nums1, 3)