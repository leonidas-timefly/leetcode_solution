'''
Given a binary array, find the maximum number of consecutive 1s in this array.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        answer = []
        for i in range(len(nums)):
            if nums[i] == 0:
                answer.append(i)
        answer.append(len(nums))
        #print(answer)
        for j in range(len(answer) - 1, 0, -1):
            #print("cycle")
            #print(answer[j])
            answer[j]= answer[j] - answer[j-1] - 1
        #print(answer)
        max_num = max(answer)
        #print(max_num)
        return max_num
nums1 = [1,0,1,1,0,1]
function = Solution()
function.findMaxConsecutiveOnes(nums1)