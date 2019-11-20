'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''

class Solution:
    def search(self, nums, target):
        if target in nums:
            #print(nums.index(target))
            return nums.index(target)
        else:
            return -1

nums1 = [1, 2, 3, 5, 4, 7, 8, 4]
function = Solution()
function.search(nums1, 4)