'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        powerSet = [[]]
        self.subsetsHelper(0, [], powerSet, nums)
        return powerSet

    def subsetsHelper(self, index, subset, powerSet, nums):
        lastNum = None
        for i in range(index, len(nums)):
            if nums[i] != lastNum:
                subset.append(nums[i])
                powerSet.append(list(subset))
                self.subsetsHelper(i + 1, subset, powerSet, nums)
                subset.pop()
                lastNum = nums[i]
        return




nums1 = [2,2,1]
function = Solution()
function.subsetsWithDup(nums1)