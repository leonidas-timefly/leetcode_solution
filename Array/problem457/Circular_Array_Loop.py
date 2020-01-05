'''
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move
 forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume
that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's
length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not
consist of both forward and backward movements.
'''
class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        if n < 2: return False
        for i in range(n):
            if nums[i] < 2000:
                i0 = i
                v = 2000+i
                sgn = 1 if nums[i] > 0 else -1
                while True:
                    i1 = (i0 + nums[i0]) % n
                    nums[i0] = v
                    if i1 == i0:
                        break
                    elif nums[i1] == v:
                        return True
                    elif nums[i1] >=2000:
                        break
                    elif nums[i1]*sgn < 0:
                        break
                    else:
                        i0 = i1
        return False
nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.circularArrayLoop(nums1)