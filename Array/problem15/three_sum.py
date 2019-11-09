'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        lennums = len(nums)

        for i in range(lennums):
            left = i + 1
            right = lennums - 1

            if i > 0 and nums[i - 1] == nums[i]:
                left += 1
                continue

            while left < right:
                sumthree = nums[i] + nums[left] + nums[right]
                if sumthree == 0:
                    res_col = [nums[i], nums[left], nums[right]]
                    res.append(res_col)
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

                if sumthree < 0:
                    left += 1
                if sumthree > 0:
                    right -= 1
        print(res)
        return res
nums1=[-1, 0, 1, 2, -1, -4, -5, 3]
function = Solution()
function.threeSum(nums1)