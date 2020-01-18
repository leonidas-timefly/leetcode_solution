'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be
planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number
n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return 1
        sum_num = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return 0
            else:
                if n == 1:
                    return 1
                else:
                    return 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            sum_num += 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                sum_num += 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            sum_num += 1
        if sum_num >= n:
            return 1
        else:
            return 0
nums1 = [1,0,0,0,1]
function = Solution()
function.canPlaceFlowers(nums1, 2)