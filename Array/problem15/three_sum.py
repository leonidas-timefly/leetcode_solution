'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
'''
'''
class Solution:
    def threeSum(self, nums):
          nums.sort()
          m = len(nums)
          num0 = 0
          numf = 0
          numz = 0
          out_nums = []
          for i in range(m):
              if nums[i] == 0:
                  num0 += 1
              elif nums[i] < 0:
                  numf += 1
          numz = m - num0 - numf
          i = 0
          j = m-1
          print(numf)
          print("666")
          print(num0)
          print(numz)
          print(nums)
          if numf == 0 or numz == 0:
              if num0 > 2:
                  return [[0, 0, 0]]
              else:
                  return []
          else:
              while i < numf and j > m - numz - 1:
                  if nums[i] + nums[j] == 0 and num0 != 0 and j > m - numz - 1:
                      out_nums.append([nums[i], 0, nums[j]])
                  if -(nums[i] + nums[j]) < 0:
                      if nums[i] == nums[i+1]:
                          while nums[i] == nums[i+1]:
                              i += 1
                      if i > 0:
                          if -(nums[i] + nums[j]) == nums[i - 1]:
                              out_nums.append([nums[i], nums[i], nums[j]])
                              #i += 1
                              j -= 1
                          else:
                              for k in range(i):
                                  if -(nums[i] + nums[j]) == nums[i]:
                                      out_nums.append([nums[k], nums[i], nums[j]])
                                      i += 1
                                  elif k == 0:
                                      i += 1
                      else:
                          i += 1
                  print(-(nums[i] + nums[j]))
                  if nums[i] + nums[j] == 0 and num0 != 0:
                      out_nums.append([nums[i], 0, nums[j]])
                      j -= 1
                      continue
                  if -(nums[i] + nums[j]) > 0:
                      if nums[j] == nums[j-1]:
                          while nums[j] == nums[j-1]:
                              j -= 1
                      print(j)
                      print(m-1)
                      print(".")
                      if j < m-1:
                          if -(nums[i] + nums[j]) == nums[j + 1]:
                              out_nums.append([nums[i], nums[j], nums[j]])
                              j -= 1
                          else:
                              for k in range(j + 1, m):
                                  if -(nums[i] + nums[j]) == nums[k]:
                                      out_nums.append([nums[i], nums[j], nums[k]])
                                      j -= 1
                                  elif k == m-1:
                                      j -= 1
                      else:
                          j -= 1
                      print(j)
                  if j == m - numz - 1 and i < numf:
                      j = m-1
                      i += 1
          print(out_nums)
          return out_nums
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        lennums = len(nums)

        for i in range(lennums):
            left = i + 1
            right = lennums - 1

            if i > 0 and nums[i - 1] == nums[i]:
                left += 1
                continue

            while left < right:
                sumthree = nums[i] + nums[left] + nums[right]
                if sumthree == 0:
                    res_col = [nums[i], nums[left], nums[right]]
                    res.append(res_col)
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

                if sumthree < 0:
                    left += 1
                if sumthree > 0:
                    right -= 1
        print(res)
        return res


nums1=[-1, 0, 1, 2, -1, -4, -5, 3]
function = Solution()
function.threeSum(nums1)