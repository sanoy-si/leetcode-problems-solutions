class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ma = 0
        self.visited = set()

        def dfs(i,j,c):
            if (i,j) in self.visited  or 0>i or i>= m or 0 > j or j >= n or not grid[i][j]:return 0
            self.visited.add((i,j))
            c+=1
            c+=dfs(i,j+1,0)
            c+=dfs(i,j-1,0)
            c+=dfs(i+1,j,0)
            c+=dfs(i-1,j,0)
            return c


        for i in range(m):
            for j in range(n):
                if (i,j) not in self.visited and grid[i][j]:
                    ma = max(ma,dfs(i,j,0))
        

        return ma

        