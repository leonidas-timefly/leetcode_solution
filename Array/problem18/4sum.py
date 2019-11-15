class Solution:
    def fourSum(self, nums, target):
        d = {}
        nums.sort()
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    key = (nums[i], nums[j], nums[start], nums[end])
                    sum_ = sum(key)
                    if target == sum_:
                        d[key] = True
                        start += 1
                        end -= 1
                    if target < sum_:
                        end -= 1
                    elif target > sum_:
                        start += 1
        return d.keys()