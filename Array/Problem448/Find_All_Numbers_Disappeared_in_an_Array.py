'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''
class Solution:
    def findDisappearedNumbers(self, nums):
        answer = []
        index_num = 0
        while index_num < len(nums):
            if nums[index_num] != nums[nums[index_num] - 1]:
                  nums[nums[index_num] - 1], nums[index_num] = nums[index_num],nums[nums[index_num] - 1]
            else:
                index_num += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                answer.append(i + 1)
        #print(answer)
        return answer

nums1 = [4,3,2,7,8,2,3,1]
function = Solution()
function.findDisappearedNumbers(nums1)