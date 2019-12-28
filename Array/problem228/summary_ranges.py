'''
Given a sorted integer array without duplicates, return the summary of its ranges.
'''
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        answer = []
        low = nums[0]
        high = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == high + 1:
                high = nums[i]
            else:
                if low == high:
                    answer.append(str(low))
                else:
                    answer.append(str(low)+"->"+str(high))
                low = nums[i]
                high = nums[i]
        if low == high:
            answer.append(str(low))
        else:
            answer.append(str(low)+"->"+str(high))
        #print(answer)
        return answer
nums1 = [0,1,2,4,5,7]
function = Solution()
function.summaryRanges(nums1)