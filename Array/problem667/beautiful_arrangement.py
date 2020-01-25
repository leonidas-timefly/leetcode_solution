'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to
n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has
exactly k distinct integers.

If there are multiple answers, print any of them.
'''
class Solution:
    def constructArray(self, n, k):
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1, 2]
        answer = [1]
        t = 1
        for i in range(k, 0, -1):
            answer.append(answer[k-i] + i*(-1)**(t+1))
            t += 1
        for j in range(k+1, n):
            answer.append(j+1)
        return answer
nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.constructArray(3, 1)