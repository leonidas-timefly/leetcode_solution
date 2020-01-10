'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
class Solution:
    def findDuplicates(self, nums):
        answer =[]
        if len(nums) == 2 and nums[0] == nums[1]:
            answer.append(nums[0])
            return answer
        if len(nums) == 2 and nums[0] != nums[1]:
            return answer
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            elif nums[i] != i+1 and nums[nums[i] - 1] != i+1:
                while nums[i] != i+1:
                    temp = nums[i]
                    nums[i] = nums[nums[i] - 1]
                    #print("#")
                    #print(i)
                    #print(nums)
                    #print(temp)
                    #print(nums[i])
                    #print(nums[i] - 1)
                    #print("*")
                    nums[temp - 1] = temp
                    #print(nums)
                    if nums[nums[i] - 1] == nums[i]:
                        #answer.append(nums[i])
                        break
                continue
        for i in range(len(nums)):
            if nums[i] != i + 1:
                answer.append(nums[i])
        #print(answer)
        return answer


nums1 = [10,2,5,10,9,1,1,4,3,7]
function = Solution()
function.findDuplicates(nums1)