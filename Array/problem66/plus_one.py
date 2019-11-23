'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each
element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

'''
class Solution:
    def plusOne(self, digits):
        counter = 0
        if digits[-1] == 9:
            for i in range(len(digits)):
                if digits[len(digits) - 1 - (i)] == 9:
                    digits[len(digits) - 1 - (i)] = 0

                else:
                    counter += 1
                    digits[len(digits) - 1 - (i)] += 1
                    break

            if counter > 0:
                return digits
            else:
                return [1] + digits


        else:
            digits[-1] += 1

        return digits


nums1 = [2, 1, 3, 4, 1, 2, 1, 5, 4]
function = Solution()
function.plusOne(nums1)