class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for _ in range(m)] for _ in range(n)] 

        def dfs(i, j):

            curr_gold = grid[i][j]

            for di, dj in dirs:
                newi, newj = i + di, j + dj
                if inbound(newi, newj) and grid[i][j] and not visited[newi][newj]:
                    visited[i][j] = 1
                    curr_gold = max(curr_gold, grid[i][j] + dfs(newi, newj))
                    visited[i][j] = 0

            return curr_gold

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    visited[i][j] = 1
                    answer = max(answer, dfs(i, j))           
                    visited[i][j] = 0

        return answer