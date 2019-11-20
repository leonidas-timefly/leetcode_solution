'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

'''

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        diff = [0] * n
        for i in range(1, n):
            diff[i] = prices[i] - prices[i - 1]
        profit = 0
        for a in diff:
            if a > 0:
                profit += a
        return profit


nums1 = [1, 2, 3, 5, 4, 7, 8, 4]
function = Solution()
function.maxProfit(nums1)