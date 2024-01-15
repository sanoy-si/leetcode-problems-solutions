class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()

        min_time = 0
        while tasks:
            min_time = max(min_time, processorTime.pop() + max([tasks.pop(), tasks.pop(), tasks.pop(), tasks.pop()]))
        
        return min_time

        
        