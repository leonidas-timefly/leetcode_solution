'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
'''
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        answer = []

        for i in range(len(nums)-int(len(nums)/3)):
            if nums[i] == nums[i + int(len(nums)/3)]:
                answer.append(nums[i])
        answer = list(set(answer))
        #print(answer)
        return answer


    if len(nums) < 3:
        answer = list(set(nums))
        return answer



nums1 = [0, 0, 0]
function = Solution()
function.majorityElement(nums1)