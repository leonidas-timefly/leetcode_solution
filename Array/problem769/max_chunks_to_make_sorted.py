'''
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of
"chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?
'''
class Solution:
    def maxChunksToSorted(self, arr):
        temp = []
        for i in range(len(arr)):
            temp.append(arr[i])
        temp.sort()
        sum_num = 0
        sum_temp = 0
        sum_arr = 0
        for j in range(len(arr)):
            sum_temp += temp[j]
            sum_arr += arr[j]
            if sum_temp == sum_arr:
                sum_num += 1
        return sum_num
nums1 = [0,3,0,3,2]
function = Solution()
function.maxChunksToSorted(nums1)