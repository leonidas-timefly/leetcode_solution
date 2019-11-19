'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        if len(nums) == 1 or len(nums) == 0:
            return

        #detect if num is the bigest
        point = 0
        for i in range(len(nums)):
            if nums[point] < nums[point + 1]:
                break
            elif i == len(nums) - 2:
                nums.reverse()
                print(nums)
                return
        k = nums[point]
        for j in range(len(nums) - 1, 0, -1):
            k.append(nums[j])
            if nums[j] < nums[j - 1]:
                continue
            else:
                if nums[j] == nums[j - 1] + 1:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    print(nums)
                    return
                else
        '''
        if len(nums) < 2: return

        swap = False
        j = len(nums)
        for i in range(len(nums) - 2, -1, -1):

            while nums[j - 1] > nums[i] and j > i:
                j -= 1
                swap = True

            if swap:
                nums[i], nums[j] = nums[j], nums[i]
                return

            else:
                nums.append(nums[i])
                nums.pop(i)
                j = len(nums)








nums1 = [1, 2, 3, 5, 4, 7, 8, 4]
function = Solution()
function.nextPermutation(nums1)