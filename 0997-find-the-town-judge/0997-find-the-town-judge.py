class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not (n * n - n >= len(trust) >= n - 1):
            return -1
        if n == 1:
            return 1
        
        pjudges = defaultdict(int)
        not_judges = set()
        for t in trust:
            pjudges[t[1]] += 1
            not_judges.add(t[0])
        
        for pjudge in pjudges:
            if pjudge not in not_judges and pjudges[pjudge] == n - 1:
                return pjudge
        
        return -1
        