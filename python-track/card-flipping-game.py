class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        difference = set(backs) - set(fronts)
        if difference:
            answer = min(difference)
        else:
            answer = 0
        
        d = defaultdict(set)
        for i in range(len(fronts)):
            d[fronts[i]].add(backs[i])
        
        for front in set(fronts):
            if front not in d[front]:
                answer = min(answer,front) if answer else front
            

        return answer
        