'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.
'''
class Solution:
    def search(self, nums, target):
        # O(N) - Runtime Complexity
        # O(1) - Space Complexity

        return self.search_rotated_sorted(nums, 0, len(nums) - 1, target)

    def search_rotated_sorted(self, nums, lo, hi, target):
        # Case 1: Invalid indexes
        if lo > hi:
            return False

        # Case 2: Array has only 1 element, and not target
        elif lo == hi and nums[lo] != target:
            return False

        # Case 3: Array has only 1 element, and is target
        elif lo == hi and nums[lo] == target:
            return True

        # Case 4: Array is a sorted array between lo and hi
        elif nums[lo] < nums[hi]:
            mid = ((lo + hi) // 2) + 1
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                return self.search_rotated_sorted(nums, mid + 1, hi, target)
            else:
                return self.search_rotated_sorted(nums, lo, mid - 1, target)

        # Case 5: Array is rotated for sure, but cannot contain element
        elif nums[lo] >= nums[hi] and target > nums[lo] and target < nums[hi]:
            return False

        # Case 6: Pivot in between, rotated array or all same elements and target can exist.
        else:
            for i in range(lo, hi + 1):
                if nums[i] == target:
                    return True
            return False
'''
        if not nums:
            return 0
        if len(nums) == 0:
            return 0
        num = len(nums)
        if num == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        k = 1
        while nums[k] == nums[k - 1] and k < num - 1:
            k += 1
        if k == num - 1 and target != nums[0] and nums[k] == nums[k-1]:
            return 0
        elif k == num - 1 and target == nums[0] and nums[k] == nums[k-1]:
            return 1
        for i in range(num - 1):
            if nums[i] > nums[i + 1]:
                index = i
                continue
        #print(nums[index])
        #print(nums[index + 1])
        if target > nums[index] or target < nums[index + 1]:
            return 0
        #print(nums[index])
        if nums[0] <= target <= nums[index]:
            for i in range(index):
                if target == nums[i]:
                    #print("&")
                    return 1
        if nums[index + 1] <= target <= nums[num - 1]:
            for i in range(index, num):
                if target == nums[i]:
                    #print("&")
                    return 1
        #print("&")
        return 0
'''



nums1 = [2,5,6,0,0,1,2]
function = Solution()
function.search(nums1, 0)