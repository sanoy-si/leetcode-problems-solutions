class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m

        heap = [(grid[0][0], 0, 0)]
        cost = [[-inf for _ in range(m)] for _ in range(n)]
        
        while heap:
            time, i, j = heappop(heap)
            if cost[i][j] != -inf:
                continue

            cost[i][j] = time

            for di, dj in dirs:
                newi, newj = i + di, j + dj
                if inbound(newi, newj) and cost[newi][newj] == -inf:
                    heappush(heap, (max(grid[newi][newj], time), newi, newj))

        return cost[n - 1][m - 1]
            