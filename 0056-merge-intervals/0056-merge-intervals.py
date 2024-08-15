class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for i in range(len(intervals)):
            if intervals[i][0] <= answer[-1][-1]:
                answer[-1][-1] = max(answer[-1][-1], intervals[i][-1])

            else:
                answer.append(intervals[i])

        return answer 
