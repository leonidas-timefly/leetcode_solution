'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.
'''
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        cost = [0] * n
        cost[0] = triangle[0][0]
        for i in range(n):
            tmp = cost[:]
            for j in range(i + 1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    tmp[0] = cost[0] + triangle[i][j]
                elif j == i:
                    tmp[j] = cost[j - 1] + triangle[i][j]
                else:
                    tmp[j] = min(cost[j - 1], cost[j]) + triangle[i][j]
            cost = tmp[:]
        return min(cost)
'''
        answer = triangle[0][0]
        index = 0
        for i in range(1, len(triangle)):
            min_num = min(triangle[i][index], triangle[i][index + 1])
            answer += min_num
            index = triangle[i].index(min_num)
        #print(answer)
        return answer
'''
nums1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
function = Solution()
function.minimumTotal(nums1)