'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row
number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as
they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
output the original matrix.
'''
class Solution:
    def matrixReshape(self, nums, r, c):
        if r*c != len(nums)*len(nums[0]):
            return nums
        answer = []
        for i in range(r):
            answer.append([])
        print(answer)
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i][0])
            temp.append(nums[i][1])
        print(temp)
        for m in range(len(answer)):
            for n in range(c*m, c*(m + 1) + 1):
                answer[m].append(temp(n))
        print(answer)
        return answer

nums1 = [[1,2],
 [3,4]]
function = Solution()
function.matrixReshape(nums1, 1, 4)