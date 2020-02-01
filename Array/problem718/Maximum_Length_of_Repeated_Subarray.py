'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
'''
class Solution:
    def findLength(self, A, B):
        length1 = len(A)
        length2 = len(B)
        temp = [[0] * (length2 + 1) for k in range(length1 + 2)]
        max_num = 0
        for i in range(1, length1 + 1):
            #print(temp[i - 1])
            for j in range(1, length2 + 1):
                if A[i - 1] == B[j - 1]:
                    #print(temp[i][j], temp[i - 1][j - 1], i, j)
                    temp[i][j] = temp[i - 1][j - 1] + 1
                    #print(temp[0])
                    #print(temp[1])
                    #print(temp[i - 1])
                    #print(temp[i])
                    #print(temp)
        for m in range(len(temp)):
            max_num = max(max_num, max(temp[m]))
        #print(max_num)
        #(temp)
        return max_num
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
function = Solution()
function.findLength(nums1, nums2)
[0, 1, 0, 0, 0, 1]
[1, 1, 0, 0, 1, 2]
[0, 1, 2, 3, 1, 2]
[0, 1, 2, 3, 1, 2]
[1, 1, 2, 3, 1, 2]
[1, 1, 2, 3, 4, 5]