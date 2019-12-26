'''
Given an array nums of n integers where n > 1,  return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].
'''


class Solution:
    def productExceptSelf(self, nums):
        answer = [1]*len(nums)
        left_scan = 1
        right_scan = 1
        for i in range(1, len(nums)):
            left_scan *= nums[i-1]
            answer[i] = left_scan * answer[i]
        for j in range(len(nums) - 2, -1, -1):
            right_scan *= nums[j+1]
            answer[j] = right_scan * answer[j]
        print(answer)
        return answer


'''
        answer = []
        index = 0
        for i in range(len(nums)):
            answer[i] = self.recursion(nums, i, index)
        print(answer)
        return answer
    def recursion(self, nums, i, index):
        if index == len(nums):
            return 1
        return self.recursion(nums, i, index) * nums[index]
'''

nums1 = [1,2,3,4]
function = Solution()
function.productExceptSelf(nums1)