class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for u, v in edges:
            indegree[v] += 1

        champion = []
        for i in range(n):
            if indegree[i] == 0:
                champion.append(i)

        if len(champion) == 1:
            return champion[0]

        return -1 