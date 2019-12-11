'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''


class Solution:
    def exist(self, board, word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        def search(row, col, word, pos, visited):
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols: return False

            if visited[row][col]: return False

            if word[pos] != board[row][col]:
                return False
            elif len(word) == pos + 1:
                return True

            visited[row][col] = True

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if search(row + i, col + j, word, pos + 1, visited):
                    return True

            visited[row][col] = False
            return False

        if not word:
            return False

        visited = [[False for j in range(num_cols)] for i in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                if search(row, col, word, 0, visited):
                    return True

        return False

nums1 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
function = Solution()
function.exist(board, word)