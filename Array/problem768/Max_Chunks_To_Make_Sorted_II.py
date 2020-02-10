'''
This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily
distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions)
, and individually sort each chunk.  After concatenating them, the result equals the sorted array.

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
'''
        number = 0
        value_first = -1
        index_first = 0
        index_later = 0
        while index_later < len(arr) - 1:
            value_first = arr[index_first]
            if value_first > arr[index_later + 1] and arr[index_later] >= arr[index_later + 1] and index_later < len(arr) - 1:
                print("+", index_later)
                index_later += 1
            else:
                number += 1
                index_later += 1
                index_first = index_later
        if arr[-2] >= arr[-1]:
            number += 1
        print(number)
        return number
'''

nums1 = [0,3,0,3,2]
function = Solution()
function.maxChunksToSorted(nums1)