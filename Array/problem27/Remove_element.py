class Solution:
    def removeElement(self, nums, val):
           i = 0
           while i < len(nums):
               if nums[i] == val:
                   del nums[i]
                   i -= 1
               i += 1
           print(len(nums))
           return len(nums)

nums1=[-1, 0, 1, 2, -1, -4, -5, 3]
function = Solution()
function.removeElement(nums1, -1)