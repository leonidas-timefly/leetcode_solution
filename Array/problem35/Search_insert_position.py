class Solution:
    def searchInsert(self, nums, target):
          if target in nums:
              return nums.index(target)
          else:
              nums.append(target)
              nums.sort()
          return nums.index(target)