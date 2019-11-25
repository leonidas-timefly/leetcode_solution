'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.
'''
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        def search(nums, cands, target):
            if target == 0:
                return result.append(cands)
            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if i == len(nums)-1:
                    if target - num ==0:
                        result.append(cands+[num])
                    break
                else:
                    if target - num >= 0:
                        search(nums[(i+1):],cands+[num],target-num)
                    else:
                        break
        search(candidates,[],target)
        print(result)
        return(result)





nums1 = [3, 4, 0, 2]
function = Solution()
function.combinationSum2(nums1, 7)