'''
Given an unsorted integer array, find the smallest missing positive integer.
'''
class Solution:
    def firstMissingPositive(self, nums):
          n = len(nums)
          i = 0
          while i < n:
              if nums[i] <= 0 or nums[i] > n or nums[i] == i+1 or nums[i] == nums[nums[i] - 1]:
                  i += 1
                  continue
              temp = nums[i]
              nums[i] = nums[temp - 1]
              nums[temp- 1] = temp
              #nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
          for i in range(0, n):
              if nums[i] != i+1:
                   #print(i + 1)
                   return i + 1
          return n + 1
'''
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > n or nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            tmp = nums[i]
            nums[i] = nums[tmp - 1]
            nums[tmp - 1] = tmp

        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
'''
nums1 = [3, 4, 0, 2]
function = Solution()
function.firstMissingPositive(nums1)