'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
                import math
        print(matrix)
        j = 0
        k = 0
        for i in range(math.floor(0.5 * len(matrix))):
            if j >= 0 and k >= 0 and j < len(matrix) - i and k < len(matrix) - i:
                if j != len(matrix) - 1 and k ==i:
                    j += 1
                elif j == len(matrix) - 1 and k ==i:
        '''
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #print(matrix)
        return




nums1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
function = Solution()
function.rotate(nums1)