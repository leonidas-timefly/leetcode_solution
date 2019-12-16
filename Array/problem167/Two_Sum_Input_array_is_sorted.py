class Solution:
    def twoSum(self, numbers, target):
        dic = {} #collection
        for i, v in enumerate(numbers):
            if (target - v) in dic: break #find the pair present in dic.
            else: dic[v] = i+1 #Making a collection of 1st pair.
        return sorted([dic[target - v],i+1])