'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
'''
class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            print(nums[0])
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                print(nums[i+1])
                return nums[i+1]
        if i == len(nums) - 2:
            print(nums[0])
            return nums[0]

nums1 = [2,2,2,0,1]
function = Solution()
function.findMin(nums1)