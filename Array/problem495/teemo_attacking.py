'''
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now,
given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking,
you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned
condition immediately.
'''
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0:
            return 0
        timeSeries.append(timeSeries[-1] + duration)
        for i in range(len(timeSeries) - 1, 0, -1):
            timeSeries[i] = timeSeries[i] - timeSeries[i - 1]
        #timeSeries.pop(timeSeries[0])
        #print(timeSeries)
        smaller_duration= 0
        full_duration = 0
        #print(len(timeSeries))
        for j in range(1, len(timeSeries)):
            if timeSeries[j] < duration:
                smaller_duration += timeSeries[j]
            else:
                full_duration += 1
        #print(smaller_duration)
        #print(full_duration)
        full_time = smaller_duration + full_duration*duration
        #print(full_time)
        return full_time



nums1 = [1,4]
function = Solution()
function.findPoisonedDuration(nums1, 2)