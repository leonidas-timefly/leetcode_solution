'''
We have two special characters. The first character can be represented by one bit 0. The second character can be
represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.
'''
class Solution:
    def isOneBitCharacter(self, bits):
        stack = ""
        for bit in bits:
            if bit == 1:
                if stack == "11" or stack == "10":
                    stack = str(bit)
                else:
                    stack += str(bit)
            if bit == 0:
                if stack == "1":
                    stack += str(bit)
                else:
                    stack = ""
        if len(stack) == 0:
            return True
        return False
        stack = ""
        for b in bits:
            if b == 1:
                if stack == "11" or stack == "10":
                    stack = str(b)
                else:
                    stack += str(b)
            if b == 0:
                if stack == "1":
                    stack += str(b)
                else:
                    stack = ""
        if len(stack) == 0:
            return True
        return False
nums1 = [1, 0, 0]
function = Solution()
function.isOneBitCharacter(nums1)