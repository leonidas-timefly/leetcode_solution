'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''
class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return intervals
        else:
            interval_left = newInterval[0]
            interval_right = newInterval[1]
            set_len = len(intervals)
            i = 0
            if interval_right < intervals[0][0]:
                intervals.insert(0, newInterval)
            while i < set_len and intervals[i][1] < interval_left:
                i += 1
            if i == set_len:
                intervals.append(newInterval)
                return intervals
            while (i < set_len and intervals[i][0] <= interval_right):
                i += 1
            if (intervals[i - 1][1] < interval_right):
                intervals[i - 1][1] = interval_right
            i_s = i
            # find end
            while (i < set_len and intervals[i][0] <= interval_right):
                i += 1
            if (intervals[i - 1][1] < interval_right):
                intervals[i - 1][1] = interval_right
            i_e = i
            del intervals[i_s + 1: i_e - 1]
            if (i_e - 1 >= i_s + 1):
                intervals[i_s][1] = intervals[i_s + 1][1]
                intervals.pop(i_s + 1)
            return intervals
            '''
            else:
                if interval_right < intervals[i][0]:
                    intervals.insert(i, newInterval)
                    return intervals
                elif interval_left < intervals[i][0] and interval_right > intervals[i][1]:
                    intervals[i][0] = interval_left
                    return intervals
                elif interval_left > intervals[i][0] and interval_right < intervals[i][1]:
                    return intervals
                elif interval_left < intervals[i][0] and interval_right > intervals[i][0]:
                    intervals[i][0] = interval_left
                    while interval_right > intervals[i][1] and i < set_len:
                        if interval_right > intervals[i+1][1]:
                            intervals.pop(i+1)
            '''





nums1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
nums2 = [4,8]
function = Solution()
function.insert(nums1, nums2)
'''
        t_s, t_e = newInterval[0], newInterval[1]
        i_s, i_e = -1, -1
        N = len(intervals)
        if not N:
            intervals.append(newInterval)
            return intervals
        i = 0
        while (i < N and intervals[i][1] < t_s):
            i+=1
            
        if (i == N and intervals[N-1][1]<t_s):
            intervals.append([t_s, t_e])
            return intervals
        
        if intervals[i][0] > t_s:
            if intervals[i][0] > t_e:
                intervals.insert(i, [t_s, t_e])
                return intervals
            else:
                intervals[i][0] = t_s
        i_s = i
        # find end
        while (i < N and intervals[i][0] <= t_e):
            i += 1
        if (intervals[i - 1][1] < t_e):
            intervals[i - 1][1] = t_e
        i_e = i
        del intervals[i_s + 1 : i_e - 1]
        if (i_e - 1 >= i_s + 1):
            intervals[i_s][1] = intervals[i_s + 1][1]
            intervals.pop(i_s + 1)
        return intervals
        '''