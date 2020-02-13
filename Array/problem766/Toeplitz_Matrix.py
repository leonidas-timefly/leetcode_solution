'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
'''
class Solution:
    def isToeplitzMatrix(self, matrix):
        len_x = len(matrix)
        len_y = len(matrix[0])
        if len_x <= 1 or len_y <= 1:
            return True
        for i in range(len_x):
            k = 1
            while i + k < len_x and k < len_y:
                if matrix[i + k - 1][k - 1] != matrix[i + k][k]:
                    #print("False")
                    return False
                k += 1
        for j in range(1, len_y):
            t = 1
            while t < len_x and j + t < len_y:
                if matrix[t - 1][j + t - 1] != matrix[t][j + t]:
                    return False
                t += 1
        #print("True")
        return True
'''          
    def recursive(self,x,y,len_x,len_y,matrix):
        if x + 1 >= len_x or y + 1 >= len_y:
            if matrix[x][y] == matrix[x+1][y+1]:
                return 1
            else:
                return 0
            self.recursive(x+1,y+1,len_x,len_y)
'''


nums1 = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
function = Solution()
function.isToeplitzMatrix(nums1)