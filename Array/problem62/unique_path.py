'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution:
    def uniquePaths(self, m, n):
        array = [1] * n

        for _ in range(1, m):
            for i in range(1, n):
                array[i] = array[i-1] + array[i]
        #print(array)
        return array[-1]


nums1 = [3, 4, 0, 2]
function = Solution()
function.uniquePaths(4, 3)