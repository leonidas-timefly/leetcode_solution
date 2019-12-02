class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex - 1)
            answer = []
            for i in range(len(prev)-1):
                answer.append(prev[i] + prev[i+1])
            answer.append(1)
            answer.insert(0, 1)
            return answer




nums1 = [3, 4, 0, 2]
function = Solution()
function.getRow(4)