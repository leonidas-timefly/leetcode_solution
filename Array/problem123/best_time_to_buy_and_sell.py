'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
class Solution:
    def maxProfit(self, prices):
        firstBuy, firstSell = float("-inf"), 0
        secondBuy, secondSell = float("-inf"), 0
        for price in prices:
            if firstBuy < -price:
                firstBuy = -price
            if firstSell < firstBuy + price:
                firstSell = firstBuy + price
            print(firstSell)
            print(secondSell)
            if secondBuy < firstSell - price:
                secondBuy = firstSell - price
            if secondSell < secondBuy + price:
                secondSell = secondBuy + price
            print(secondSell)
        #print(secondSell)
        return secondSell

nums1 = [3,3,5,0,0,3,1,4]
function = Solution()
function.maxProfit(nums1)