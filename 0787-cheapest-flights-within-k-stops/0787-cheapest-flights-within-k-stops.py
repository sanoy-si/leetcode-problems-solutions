class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [inf] * (n)
        prev[0] = 0

        for _ in range(k + 1):
            curr = prev[:]
            for u, v, w in flights:
                curr[v] = min(curr[v], prev[u] + w)
            prev = curr[:]
        
        if prev[dst] == inf:
            return -1

        return prev[dst]  