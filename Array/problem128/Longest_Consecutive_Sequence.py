'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) < 2:
            return len(nums)

        output = 0
        tem = 1

        nums = list(set(nums))
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                tem += 1

            else:
                if tem > output:
                    output = tem
                tem = 1

        if output < tem:
            output = tem

        return output
        max_len = 0
        nums = list(set(nums))
        nums.sort()
        num = len(nums)
        if num == 0 or num == 1:
            return num
        num_now = 1
        #print(nums)
        i = 0
        while i < num - 1:
            #print(nums[i])
            #print(nums[i+1])
            while nums[i] == nums[i + 1] - 1:
                num_now += 1
                i += 1
                if i == num - 1:
                    break
            #print(i)
            #print(max_len)
            #print(num_now)
            max_len = max(max_len, num_now)
            num_now = 1
        print(max_len)
        return max_len

nums1 = [0,0,-1]
function = Solution()
function.longestConsecutive(nums1)