'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell
has less than 8 surrounding cells, then use as many as you can.
'''
class Solution:
    def imageSmoother(self, M):
        import math
        temp = []
        for i in range(len(M)):
            temp.append(M[i])
        #if len(M) == 1:

        for m in range(len(temp)):
            for n in range(len(temp[0])):
                if 0 < m < len(temp) and 0 < n < len(temp[0]):
                    temp[m][n] = math.floor((M[m-1][n] + M[m+1][n] + M[m][n-1] + M[m][n+1] + M[m][n])/5)
                if m == 0 and n != 0 and n != len(M[0]):
                    temp[m][n] = math.floor((M[m][n-1]+M[m][n+1]+M[m+1][n-1]+M[m+1][n]+M[m+1][n+1]+M[m][n])/6)
                if m == len(temp) and n != 0 and n != len(M[0]):
                    temp[m][n] = math.floor((M[m][n - 1] + M[m][n + 1] + M[m - 1][n - 1] + M[m - 1][n] + M[m - 1][n + 1] + M[m][n]) / 6)
                if n == 0 and m != 0 and m != len(M):
                    temp[m][n] = math.floor((M[m][n] + M[m-1][n] + M[m+1][n] + M[m][n+1] + M[m-1][n+1] + M[m+1][n]))
                if n == len(M[0]) and m != 0 and m != len(M):
                    temp[m][n] = math.floor((M[m][n] + M[m - 1][n] + M[m + 1][n] + M[m][n - 1] + M[m - 1][n - 1] + M[m + 1][n-1]) / 6)
                if m == 0 and n == 0:
                    temp[m][n] = math.floor((M[0][0] + M[0][1] + M[1][0] + M[1][1]) / 4)
                if m == 0 and n == len(M[0]):
                    temp[m][n] = math.floor((M[0][len(M[0])] + M[0][len(M[0]) - 1] + M[1][len(M[0])] + M[1][len(M[0]) - 1]) / 4)
                if m == len(M) and n == 0:
                    temp[m][n] = math.floor((M[len(M)][0] + M[len(M)][1] + M[len(M) - 1][0] + M[len(M) - 1][1]) / 4)
                if m == len(M) and n == len(M[0]):
                    temp[m][n] = math.floor((M[len(M)][len(M[0])] + M[len(M)][len(M[0] - 1)] + M[len(M) - 1][len(M[0])] + M[len(M) - 1][len(M[0])]) / 4)
        print(temp)
        return
nums1 = [[1,1,1],
 [1,0,1],
 [1,1,1]]
function = Solution()
function.imageSmoother(nums1)