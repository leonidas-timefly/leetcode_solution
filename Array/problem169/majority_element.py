'''
Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    def majorityElement(self, nums):
        num = int(len(nums) / 2)
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(num + 1):
            if nums[i] == nums[i + num]:
                print(nums[i])
                return nums[i]
'''
        now_num = 1
        for i in range(len(nums) - 1):
            while nums[i] == nums[i+1]:
                now_num += 1
                i += 1
                if now_num > len(nums) / 2:
                    #print(nums[i])
                    return nums[i]
                if i == len(nums) - 1:
                    break

            if now_num < len(nums) / 2:
                now_num = 1
'''

nums1 = [3,2,3]
function = Solution()
function.majorityElement(nums1)