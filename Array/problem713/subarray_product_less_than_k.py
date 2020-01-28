'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        count_num = 0
        if k < 1:
            return count_num
        index1, product = 0, 1
        for index2, value in enumerate(nums):
            print(index2, value)

            product *= value
            while product >= k and index1 < len(nums):
                product /= nums[index1]
                index1 += 1
            if index1 == len(nums):
                break
            count_num += index2 - index1 + 1
        #print(count_num)
        return count_num

nums1 = [1, 1, 1]
function = Solution()
function.numSubarrayProductLessThanK(nums1, 1)