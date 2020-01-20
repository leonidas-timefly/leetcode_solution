'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''
class Solution:
    def maximumProduct(self, nums):
        if len(nums) == 3:
            return nums[-1]*nums[-2]*nums[-3]
        nums.sort()
        product = 0
        negetive = []
        positive = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negetive.append(nums[i])
            else:
                positive.append(nums[i])
        if len(negetive) > 1:
            product = negetive[0] * negetive[1]
        if 0 <len(positive) < 3:
            return product * positive[-1]
        if len(positive) == 0:
            return negetive[0]*negetive[1]*negetive[-1]
        else:
            return max(product*nums[-1], nums[-1]*nums[-2]*nums[-3])

nums1 = [1,2,3,4]
function = Solution()
function.maximumProduct(nums1)