class DSU:
    
    def __init__(self, n, m, grid):
        self.parent = {(i, j):(i, j) for i in range(n) for j in range(m)}
        self.size = {(i, j):1 for i in range(n) for j in range(m)}
        self.fish = {(i, j):grid[i][j] for i in range(n) for j in range(m)}

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp != yp:
            if self.size[xp] >= self.size[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]
                self.fish[xp] += self.fish[yp]

            else:
                self.parent[xp] = yp
                self.size[yp] += self.size[xp]
                self.fish[yp] += self.fish[xp]



    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dsu = DSU(n, m, grid)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    for di, dj in dirs:
                        newi, newj = i + di, j + dj
                        if inbound(newi, newj) and grid[newi][newj] != 0:
                            dsu.union((i, j), (newi, newj))
        
        answer = 0
        for i in range(n):
            for j in range(m):
                answer = max(answer, dsu.fish[dsu.find((i, j))])
        
        return answer

            

        