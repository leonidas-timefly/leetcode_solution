'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            elif nums[i] == 2:
                blue += 1
        print(red)
        print(white)
        print(blue)
        print(nums[0: red])
        #print(nums[red : red + white])
        for i in range(0, red):
            nums[i] = 0
        for j in range(red, red + white):
            nums[j] = 1
        for k in range(red + white, red + white + blue):
            nums[k] = 2
        return


nums1 = [0, 2, 1, 2, 0, 1]
function = Solution()
function.sortColors(nums1)