'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, )
        return max_area
    def recurse_find_max(self, grid, m, n):
        if 0 < m < len(grid) and 0 < n < len(grid[0]) and grid[m][n] == 1:
            grid[m][n] = 0
            return 1 + recurse_find_max(grid, m + 1, n) + recurse_find_max(grid, m - 1, n) + recurse_find_max(grid, m, n + 1) + recurse_find_max(grid, m, n - 1)
        return 0
nums1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
function = Solution()
function.maxAreaOfIsland(nums1)