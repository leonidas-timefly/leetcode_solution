'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
'''
class Solution:
    def findPeakElement(self, nums):
        num = len(nums)
        if num == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return num - 1
        else:
            for i in range(1, num - 1):
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    #print(i)
                    return i

nums1 = [1,2,3,1]
function = Solution()
function.findPeakElement(nums1)