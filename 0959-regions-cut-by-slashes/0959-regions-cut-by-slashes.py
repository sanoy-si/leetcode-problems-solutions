class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])

        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        visited = set()

        def dfs(i, j, p):
            if not inbound(i, j) or (i, j, p) in visited:
                return

            visited.add((i, j, p))

            if p == 0:
                dfs(i - 1, j, 2)
            
            elif p == 1:
                dfs(i, j + 1, 3)
            
            elif p == 2:
                dfs(i + 1, j, 0)
            
            else:
                dfs(i, j - 1, 1)
            
            if grid[i][j] != '\\':
                dfs(i, j, p ^ 3)
            
            if grid[i][j] != '/':
                dfs(i, j, p ^ 1)
        
        answer = 0

        for i in range(n):
            for j in range(m):
                for p in range(4):
                    if (i, j, p) not in visited:
                        dfs(i, j, p)
                        answer += 1
        
        return answer
            
