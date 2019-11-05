'''
solution1:Runtime: 5396 ms, faster than 13.71% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 10.46% of Python3 online submissions for Two Sum.
Next challenges:
'''
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    #print([i, j])
                    return [i, j]

nums = [2, 7, 11, 15]
target = 13
function = Solution()
function.twoSum(nums, target）