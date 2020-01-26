'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the
maximum valued number you could get.
'''
class Solution:
    def maximumSwap(self, num):
        temp = []
        while num > 0:
            temp.append(int(num%10))
            num = int((num - num%10)/10)
        answer = 0
        if max(temp) == temp[-1] and temp[-1] == temp[-2]:
            for i in range(len(temp) - 1, 1, -1):
                answer += temp[i] * 10**i
        temp2 = [0]*(max(temp) + 1)
        for j in range(len(temp)):
            temp2[temp[j]] += 1
        if max(temp) != temp[-1]:
            index1 = len(temp) - 1
            while index1 > 0:
                if temp[index1] == max(temp) and temp[index1-1] == temp[index1]:
                    index1 -= 1
                    continue
                else:
                    k = temp[index1]
                    temp[index1] = temp[-1]
                    temp[-1] = k
        for m in range(len(temp) - 1, 1, -1):
            answer += temp[m] * 10 ** m
        print(answer)
        return answer

        print(temp)
nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.maximumSwap(9973)