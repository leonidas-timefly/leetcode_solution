'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<=2: return len(nums)
        nums[:] = nums[:2]+[nums[i] for i in range(2, len(nums)) if nums[i]!=nums[i-2]]
        return len(nums)
'''
        num_negetive = 0
        length = len(nums)
        if length < 3:
            return length
        max_nums = max(nums)
        count_num = [0]*(max_nums+1)
        for i in range(length):
            count_num[nums[i]] += 1
        final_num = 0
        index_nums = 0
        #print(count_num)
        #print(max_nums)
        for j in range(max_nums + 1):
            if count_num[j] > 2:
                count_num[j] = 2
            elif count_num[j] == 0:
                continue
            elif count_num[j] == 1:
                nums[index_nums] = j
            if count_num[j] == 2:
                nums[index_nums] = j
                nums[index_nums + 1] = j
            index_nums += count_num[j]
            final_num += count_num[j]
            #print(count_num[j])
            #print(nums)
            #print(final_num)
            #print(index_nums)
        print(nums)
        #print(final_num)
        return final_num
'''




nums1 = [1,1,1,2,2,2,3,3]
function = Solution()
function.removeDuplicates(nums1)