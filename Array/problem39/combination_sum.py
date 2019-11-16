class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()

        ans = []
        self.recursive(candidates, target, [], 0, ans)
        return ans

    def recursive(self, sortedCandidates, target, wip, wipSum, ans):
        '''
        Populate ans recursively

        Args:
            sortedCandidates: sorted set of original candidates
            wip (List[int]): current work in progress combination.
            wipSum (int): sum(wip)
            ans (List[List[int]]): answer to be populated
        '''
        if wipSum == target:
            ans.append(list(wip))

        for n in sortedCandidates:
            # Skip all numbers that make wipSum > target
            if n + wipSum > target:
                break

            # To avoid duplication, only consider adding number larger or equal to the last number
            if wip and n < wip[-1]:
                continue

            # Add n to wip, and call recursive method
            self.recursive(sortedCandidates, target, wip + [n], wipSum + n, ans)
nums1=[-1, 0, 1, 2, -1, -4, -5, 3]
function = Solution()
function.combinationSum(nums1, 4)