'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums):
        res = [[]]
        for idx, i in enumerate(nums):
            tmp = nums[idx + 1:]
            for j in self.subsets(tmp):
                res.append([i] + j)
        return res

nums1 = [3, 4, 0, 2]
function = Solution()
function.subsets(nums1)