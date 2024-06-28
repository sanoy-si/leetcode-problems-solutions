class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = Counter()
        for a, b in roads:
            counter[a] += 1
            counter[b] += 1
        
        values = list(counter.values())
        values.sort()
        answer = 0

        for i, value in enumerate(values):
            answer += value * (i + 1)
        
        return answer
