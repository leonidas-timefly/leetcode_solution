'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''
class Solution:
    def maximalRectangle(self, matrix):
        max_answer = 0
        if matrix == []:
            return 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == "1":
                    start_j = j
                    start_i = i
                    high_now = 0
                    min_len = 1000
                    while matrix[start_j][start_i] == "1" and start_j < len(matrix):
                        high_now += 1
                        start_i = i
                        len_now = 0
                        while start_i < len(matrix[0]) and matrix[start_j][start_i] == "1":
                            len_now += 1
                            start_i += 1
                            if start_i == len(matrix[0]):
                                break
                        start_i = i
                        min_len = min(min_len, len_now)
                        max_now = high_now * min_len
                        max_answer = max(max_now, max_answer)
                        start_j += 1
                        if start_j == len(matrix):
                            break
        return max_answer

nums1 = [
  ["1","0","1","0","0","0"],
  ["1","0","1","1","1","1"],
  ["1","1","1","1","1","1"],
  ["1","0","0","1","0","0"]
]
function = Solution()
function.maximalRectangle(nums1)