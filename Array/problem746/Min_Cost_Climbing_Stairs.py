'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the
floor, and you can either start from the step with index 0, or the step with index 1.
'''
class Solution:
    def minCostClimbingStairs(self, cost):
        len_cost = len(cost)
        if len_cost == 1:
            return cost[0]
        if len_cost == 2:
            return min(cost[0], cost[1])
        for i in range(2, len_cost - 1):
            cost[i] = min(cost[i] + cost[i - 1], cost[i] + cost[i - 2])
        return min(cost[len_cost - 2], cost[len_cost - 1])

nums1 = [10, 15, 20]
function = Solution()
function.minCostClimbingStairs(nums1)