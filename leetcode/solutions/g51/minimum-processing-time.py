class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        tasks.sort(reverse = True)
        processorTime.sort()
        n = len(processorTime)
        ans = 0
        j = 0
        for i in range(n):
            ans = max(ans, tasks[j] + processorTime[i])
            j += 4
        return ans




        