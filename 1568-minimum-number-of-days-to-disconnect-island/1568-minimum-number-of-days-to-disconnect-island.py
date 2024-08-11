class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),]
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            visited[i][j] = True
            for di, dj in dirs:
                newi, newj = i + di, j + dj
                if inbound(newi, newj) and not visited[newi][newj] and grid[newi][newj] == 1:
                    dfs(newi, newj)


        def is_connected():
            count = 0 
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and not visited[i][j]:
                        if count == 1:
                            return False
                        count += 1
                        dfs(i, j)

            return True
        
        res = is_connected()
        if res == False:
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    if not is_connected():
                        return 1
                    grid[i][j] = 1

        return 2
       
                    

        
            
            
                        