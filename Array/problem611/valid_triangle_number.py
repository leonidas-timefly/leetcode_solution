'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.
'''
class Solution:
    def triangleNumber(self, nums):
        answer = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            answer[nums[i]] += 1
        count_nums = 0
        for k in range(len(answer)):
            for m in range(k + 1, len(answer)):
                if answer[k] != 0 and answer[m] != 0:
                    for n in range(m - k + 1, min(len(answer), k + m - 1)):
                        count_nums += answer[n]
                    count_nums -= 2
        #print(count_nums)
        return count_nums
nums1 =  [2,2,3,4]
function = Solution()
function.triangleNumber(nums1)