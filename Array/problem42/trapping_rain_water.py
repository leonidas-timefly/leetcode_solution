class Solution:
    def trap(self, height):
          if len(height) == 0:
              return 0
          max_num_index = height.index(max(height))
          sum_water=0
          left_index=0
          right_index=0
          for i in range(max_num_index):
              if left_index <= height[i]:
                  left_index = height[i]
              else:
                  sum_water += left_index - height[i]
          for i in range(len(height) - 1, max_num_index, -1):
              if right_index <= height[i]:
                  right_index = height[i]
              else:
                  sum_water += right_index - height[i]
          print(sum_water)
          return sum_water



nums1 = [3, 4, 0, 2]
function = Solution()
function.trap(nums1)