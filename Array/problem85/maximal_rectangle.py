'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''
class Solution:
    def maximalRectangle(self, matrix):
        max_answer = 0
        if matrix == []:
            return 0
        len_x = len(matrix[0])
        len_y = len(matrix)
        for i in range(len_x):
            for j in range(len_y):
                if matrix[j][i] == "1":
                    start_j = j
                    start_i = i
                    high_now = 0
                    min_len = 100
                    while matrix[start_j][start_i] == "1" and start_j < len_y:
                        high_now += 1
                        len_now = 0
                        while start_i < len_x and matrix[start_j][start_i] == "1":
                            len_now += 1
                            start_i += 1
                        start_i = i
                        min_len = min(min_len, len_now)
                        max_answer = max(high_now * min_len, max_answer)
                        start_j += 1
                        if start_j == len_y:
                            break
        #print(max_answer)
        return max_answer

nums1 = [
  ["1","0","1","0","0","0"],
  ["1","0","1","1","1","1"],
  ["1","1","1","1","1","1"],
  ["1","0","0","1","0","0"]
]
function = Solution()
function.maximalRectangle(nums1)