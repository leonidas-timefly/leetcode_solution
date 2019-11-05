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
         n = len(nums2)
         i = 0
         j = 0
         while i != m and j!=n:
             if nums1[i] < nums2[j]:
                 nums3[i+j] = nums1[i]
                 i += 1
             else:
                 nums3[i+j]=nums2[j]
                 j += 1
         if i==m:
             while j != n:
                 nums3[i+j] = nums2[j]
                 j += 1
         elif j==n:
             while i != m:
                 nums3[i+j] = nums1[i]
                 i += 1
         if (m + n)%2 == 0:
             mid = (nums3[(m+n)/2]+nums3[(m+n)/2+1])/2
         else:
             mid = nums3[(m+n+1)/2]
         print(mid)
         return mid
nums1 = [1, 3]
nums2 = [2]
function = Solution()
function.twoSum(nums1, nums2)