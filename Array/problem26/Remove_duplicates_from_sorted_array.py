class Solution:
    def removeDuplicates(self, nums):
          for i in range(len(nums) - 1, -1, -1):
              if i > 0:
                  if nums[i] == nums[i - 1]:
                      nums.pop(i)


          #print(nums)
          return len(nums)






nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
function = Solution()
function.removeDuplicates(nums1)