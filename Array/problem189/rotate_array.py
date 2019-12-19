'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:]+ nums[:-k]
        #print(nums)
        return
'''
        if k == 0:
            return
        num = len(nums)
        k = k % num
        if num == 0 or num == 1:
            return
        if num == 2 and k == 1:
            nums[0], nums[1] = nums[1], nums[0]
            return
        left = num - k - 1
        nums[0:left], nums[left:num] = nums[k + 1:len(nums)], nums[0:k + 1]
        print(nums)
        return
'''
nums1 = [100,4,200,1,3,2]
function = Solution()
function.rotate(nums1, 2)