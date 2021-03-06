'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    grid[i][j]=grid[i][j]
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        print(grid[len(grid)-1][len(grid[0])-1])
        return grid[len(grid)-1][len(grid[0])-1]


nums1 = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
function = Solution()
function.minPathSum(nums1)