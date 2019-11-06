"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
         nums3 = []
         m = len(nums1)
         print(m)

         n = len(nums2)
         print(n)
         i = 0
         j = 0
         if m > 0 and n > 0:
            while i != m and j != n:
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
            #print(nums3)
            if i == m:
                while j != n:
                    nums3.append(nums2[j])
                    j += 1
            elif j == n:
                while i != m:
                    nums3.append(nums1[i])
                    i += 1
            #print(nums3)
            if (m + n) % 2 == 0:
                mid = (nums3[int((m + n) / 2)-1] + nums3[int((m + n) / 2 + 1)-1]) / 2


            else:
                #print(int((m + n + 1) / 2))
                mid = nums3[int((m + n + 1) / 2)-1]
            print(mid)
            return mid
         elif m==0:
             if n%2 == 0:
                 print((nums2[int(n/2-1)]+nums2[int(n/2)])/2.0)
                 return (nums2[int(n/2-1)]+nums2[int(n/2)])/2.0
             else:
                 print(nums2[int((n+1)/2-1)])
                 return nums2[int((n+1)/2-1)]
         elif n==0:
             if m%2 == 0:
                 print((nums1[int(m/2-1)]+nums1[int(m/2)])/2.0)
                 return (nums1[int(m/2-1)]+nums1[int(m/2)])/2.0
             else:
                 print(nums1[int((m+1)/2-1)])
                 return nums1[int((m+1)/2-1)]
         else:
             raise ValueError

nums1 = [1, 2, 5, 6]
nums2 = []
function = Solution()
function.findMedianSortedArrays(nums1, nums2)