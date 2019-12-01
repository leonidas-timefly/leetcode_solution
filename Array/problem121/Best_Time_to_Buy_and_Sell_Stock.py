'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''


class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        bestProfit = currProfit = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - minBuy > currProfit:
                currProfit = prices[i] - minBuy
            else:
                if prices[i] < minBuy:
                    minBuy = prices[i]
                currProfit = 0
            if currProfit > bestProfit:
                bestProfit = currProfit

        return bestProfit

nums1 = [3, 4, 0, 2]
function = Solution()
function.maxProfit(4)