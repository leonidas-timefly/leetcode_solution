'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least
one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''
class Solution:
    def findDuplicate(self, nums):
        answer = [0]*len(nums)
        for i in range(len(nums)):
            answer[nums[i]] += 1
            if answer[nums[i]] == 2:
                #print(nums[i])
                return nums[i]


nums1 = [3,1,3,4,2]
function = Solution()
function.findDuplicate(nums1)