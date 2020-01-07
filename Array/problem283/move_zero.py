'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the
relative order of the non-zero elements.
'''
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                index = i
                while nums[index] == 0:
                    index += 1
                    if index > len(nums) - 1:
                        #print(nums)
                        return
                nums[i], nums[index] = nums[index], 0
        #print(nums)
        answer = []
        zero_num = 0
        if len(nums) < 2:
            return answer
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_num += 1
            else:
                answer.append(nums[i])
        for i in range(zero_num):
            answer.append(0)
        nums = answer
        print(nums)
        return 0

nums1 = [0,1,0,3,12]
function = Solution()
function.moveZeroes(nums1)