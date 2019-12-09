'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            step = [[0 for i in range(m)]for j in range(n)]
            step[0][0] = 1
            for i in range(1, m):
                step[i][0] = 0 if obstacleGrid[i][0] == 1 else step[i - 1][0]
            for j in range(1, n):
                step[0][j] = 0 if obstacleGrid[0][j] == 1 else step[0][j - 1]
            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 1:
                        step[i][j] = 0
                    else:
                        step[i][j] = step[i][j-1] + step[i-1][j]
            #print(step[-1][-1])
            return step[-1][-1]
'''
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m,n = len(obstacleGrid),len(obstacleGrid[0])       
        steps = [[0 for x in range(n)] for x in range(m)]
        steps[0][0] = 1
        for i in range(1,m):
            steps[i][0] = 0 if obstacleGrid[i][0] == 1 else steps[i-1][0]          
        for j in range(1,n):
            steps[0][j] = 0 if obstacleGrid[0][j] == 1 else steps[0][j-1]  
     
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    steps[i][j] = 0
                else:
                    steps[i][j] = steps[i-1][j] + steps[i][j-1]
        return steps[-1][-1]
'''


nums1 = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
function = Solution()
function.uniquePathsWithObstacles(nums1)