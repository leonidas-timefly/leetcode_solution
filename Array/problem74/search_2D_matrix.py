'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            #print("0")
            return 0
        line_num = len(matrix)
        row_num = len(matrix[0])
        if len(matrix[0]) == 0:
            return 0
        if target < matrix[0][0] or target > matrix[line_num - 1][row_num - 1]:
            return 0
        for i in range(line_num):
            if target >= matrix[i][0]:
                if target <= matrix[i][row_num - 1]:
                    if target in matrix[i][0:row_num]:
                        #print("1")
                        return 1
                    continue
        #print("0")
        return 0






nums1 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
function = Solution()
function.searchMatrix(nums1, 10)