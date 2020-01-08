'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is
created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        weight = len(board[0])
        if height < 2 or weight < 2:
            for i in range(height):
                for j in range(weight):
                    board[i][j] = 0
        else:
            for i in range(height):
                for j in range(weight):
                    if i==0 and j==0:
                        nbs = [board[i+1][j],board[i][j+1],board[i+1][j+1]]
                    elif i==0 and j==weight-1:
                        nbs = [board[i+1][j],board[i][j-1],board[i+1][j-1]]
                    elif i == height-1 and j ==0:
                        nbs = [board[i-1][j],board[i-1][j+1],board[i][j+1]]
                    elif i == height-1 and j == weight-1:
                        nbs = [board[i-1][j],board[i-1][j-1],board[i][j-1]]
                    elif i == 0:
                        nbs = [board[i][j-1],board[i+1][j-1],board[i+1][j],board[i+1][j+1],board[i][j+1]]
                    elif i == height-1:
                        nbs = [board[i][j-1],board[i-1][j-1],board[i-1][j],board[i-1][j+1],board[i][j+1]]
                    elif j == 0:
                        nbs = [board[i-1][j],board[i-1][j+1],board[i][j+1],board[i+1][j+1],board[i+1][j]]
                    elif j == weight - 1:
                        nbs = [board[i-1][j],board[i-1][j-1],board[i][j-1],board[i+1][j-1],board[i+1][j]]
                    else:
                        nbs = [board[i-1][j-1],board[i-1][j],board[i-1][j+1],board[i][j-1],board[i][j+1],board[i+1][j-1],board[i+1][j],board[i+1][j+1]]

                    if board[i][j] == 1:
                        if nbs.count(1)+nbs.count(-1) < 2:
                            board[i][j] = -1
                        elif nbs.count(1)+nbs.count(-1) > 3:
                            board[i][j] = -1
                    elif board[i][j] == 0:
                        if nbs.count(1)+nbs.count(-1) == 3:
                            board[i][j] = 2

            for i in range(height):
                for j in range(weight):
                    if board[i][j] == 2:
                        board[i][j] = 1
                    elif board[i][j] == -1:
                        board[i][j] = 0

nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.gameOfLife(nums1)