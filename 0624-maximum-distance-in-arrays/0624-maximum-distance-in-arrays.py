class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_ = arrays[0][0]
        answer = -inf        
        for i in range(1, len(arrays)):
            answer = max(answer, abs(arrays[i][-1] - min_))
            min_ = min(min_, arrays[i][0])
        
        min_ = arrays[-1][0]
        for i in range(len(arrays) - 2, -1, -1):
            answer = max(answer, abs(arrays[i][-1] - min_))
            min_ = min(min_, arrays[i][0])
        
        return answer
        
        return answer