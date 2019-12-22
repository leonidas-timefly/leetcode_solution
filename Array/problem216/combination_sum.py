'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can
be used and each combination should be a unique set of numbers.
'''
class Solution:
    def combinationSum3(self, k, n):
        temp = [[]]
        for i in range(1, 10):
            temp += [k+[i] for k in temp]
        #print(temp)
        answer = []
        for m in temp:
            if len(m) == k and sum(m) == n:
                answer.append(m)
        print(answer)
        return answer
nums1 = [100,4,200,1,3,2]
function = Solution()
function.combinationSum3(3, 9)