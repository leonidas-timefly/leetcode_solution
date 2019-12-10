'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for m in range(len(matrix[0])):
                        if matrix[i][m] != 0:
                            matrix[i][m] = 't'
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 't'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 't':
                    matrix[i][j] = 0
        print(matrix)
        return


nums1 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
function = Solution()
function.setZeroes(nums1)