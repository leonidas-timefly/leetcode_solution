'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
'''
class Solution:
    def dominantIndex(self, nums):
        max_num = max(nums)
        part_max_num = max_num / 2
        for i in range(len(nums)):
            if nums[i] != max_num and part_max_num < nums[i]:
                #print("-1")
                return -1
        #print("1")
        return nums.index(max_num)


nums1 = [1, 2, 3, 4]
function = Solution()
function.dominantIndex(nums1)