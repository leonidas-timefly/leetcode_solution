'''
Given a collection of intervals, merge all overlapping intervals
'''
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda i:i[0])
        i = 1
        temp = intervals[0]
        while i < len(intervals):
            if temp[1] >= intervals[i][0]:
                temp[1] = max(temp[1], intervals[i][1])
                intervals[i-1] = temp
                intervals.pop(i)
            else:
                temp = intervals[i]
                i += 1
        #print(intervals)
        return intervals

nums1 = [[1,3],[2,6],[8,10],[15,18]]
function = Solution()
function.merge(nums1)