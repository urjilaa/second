class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        me_max = 0
        
        for i in range(len(processorTime)):
            me_max = max(me_max, processorTime[i] + tasks[4*i])

        return me_max 