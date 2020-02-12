'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
'''
class Solution:
    def isToeplitzMatrix(self, matrix):
        if len(matrix) <= 1 or len(matrix[0]) <= 1:
            return True

nums1 = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
function = Solution()
function.isToeplitzMatrix(nums1)