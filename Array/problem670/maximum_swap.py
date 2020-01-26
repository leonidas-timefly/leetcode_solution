'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the
maximum valued number you could get.
'''
class Solution:
    def maximumSwap(self, num):
        _temp = num
        temp = []
        while _temp > 0:
            temp.append(int(_temp%10))
            _temp = int((_temp - _temp%10)/10)
        answer = 0
        if len(temp) < 2:
            return num
        if max(temp) == temp[-1] and temp[-1] == temp[-2]:
            for i in range(len(temp) - 1, -1, -1):
                answer += temp[i] * 10**i
            #print(answer)
            return answer

        temp2 = [0]*(max(temp) + 1)
        for j in range(len(temp)):
            temp2[temp[j]] += 1
        #print(answer)
        print(temp)
        #print(temp2)
        if max(temp) != temp[-1]:
            index1 = len(temp) - 1
            while index1 > 0:
                if temp[index1] == max(temp) and temp[index1-1] == temp[index1]:
                    index1 -= 1
                    continue
                elif temp[index1] == max(temp) and temp[index1 - 1] != temp[index1]:
                    k = temp[index1]
                    temp[index1] = temp[-1]
                    temp[-1] = k
                    break
                else:
                    index1 -= 1
                if index1 == 0:
                    k = temp[index1]
                    temp[index1] = temp[-1]
                    temp[-1] = k
                    break
        #print(temp)
        for m in range(len(temp) - 1, -1, -1):
            answer += temp[m] * 10 ** m
        print(answer)
        return answer

        #print(temp)
nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.maximumSwap(98368)