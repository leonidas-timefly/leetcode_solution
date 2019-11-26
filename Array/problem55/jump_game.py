'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums):
        maxi = 0
        for i in range(len(nums)):
            if i > maxi:
                return False
            maxi = max(maxi, i + nums[i])
        return True

'''
        else:
            i = 0
            while(i + nums[i] <= len(nums) - 1):

                if i + nums[i] == len(nums) - 1:
                    #print("1")
                    return 1
                if nums[i] == 0:
                    #print("0")
                    return 0
                i = i + nums[i]
            #print("0")
            return 0
'''


nums1 = [3, 4, 0, 2, 4, 5, 0, 0, 0, 0, 0, 0]
function = Solution()
function.canJump(nums1)