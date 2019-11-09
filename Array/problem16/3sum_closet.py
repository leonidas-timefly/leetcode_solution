class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = float('inf')

        for p1 in range(len(nums) - 2):
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                current_sum = nums[p1] + nums[p2] + nums[p3]
                if target == current_sum:
                    return current_sum
                elif abs(current_sum - target) < abs(result - target):
                    result = current_sum
                elif current_sum > target:
                    p3 -= 1
                else:
                    p2 += 1
        print(result)
        return result


nums1=[-1, 0, 1, 2, -1, -4, -5, 3]
function = Solution()
function.threeSumClosest(nums1, 4)