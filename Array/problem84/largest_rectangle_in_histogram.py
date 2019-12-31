'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
'''
class Solution:
    def largestRectangleArea(self, heights):
        # make right boundary\
        heights.append(0)
        # store left boundary index
        stack = [-1] # tricky: -1 also denotes the left index of 0
        # keep track of max area
        area = 0
        # iterate through heights
        for idx, h in enumerate(heights):
            # we now find the right boundary for stacks[-1]
            while h < heights[stack[-1]]:
                cur_idx = stack.pop()
                cur_h = heights[cur_idx]
                # right boundary (idx) is certainly lower than 'cur_idx'
                right_boundary = idx
                # tricky part, note that every index stored in 'stack' is in ascending order, but not necessary continguous
                # also note that the reason we initially put '-1' in 'stack' is that -1 is instinctively left to 0, so it's naturally the left boundary for index 0
                left_boundary = stack[-1]
                cur_w = right_boundary - left_boundary - 1
                area = max(area, cur_h * cur_w)
            # we put every index to stack once
            # note that eventually every index except '-1' in stack will be popped out
            stack.append(idx)
        return area
nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.largestRectangleArea(nums1)