'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0],nums[2])
        else:
            for i in range(len(nums) - 2):
                if nums[i] > nums[i + 1]:
                    return nums[i + 1]
            return nums[0]


nums1 = [3,4,5,1,2]
function = Solution()
function.findMin(nums1)