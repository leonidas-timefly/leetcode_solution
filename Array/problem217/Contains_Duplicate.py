'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums):
        num = len(nums)
        if num == 0 or num == 1:
            print("false")
            return 0
        nums.sort()
        for i in range(num - 1):
            if nums[i] == nums[i+1]:
                print("true")
                return 1
        print("false")
        return 0


nums1 = [1,2,3,1]
function = Solution()
function.containsDuplicate(nums1)