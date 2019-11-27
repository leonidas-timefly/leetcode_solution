'''

'''
class Solution:
    def generate(self, numRows):
        if numRows <= 0:
            return []
        List=[[1]]
        for i in range(2, numRows + 1):
            List.append([1])

            for j in range(1, i - 1):
                List[-1].append(List[-2][j] + List[-2][j - 1])
            List[-1].append(1)
        print(List)
        return List


nums1 = [[2, 1], [3, 4], [1, 2, 1], 5, 4]
function = Solution()
function.generate(5)