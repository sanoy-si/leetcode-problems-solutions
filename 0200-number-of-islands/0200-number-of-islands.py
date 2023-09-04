class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=0
        visited = set()
        self.movements = [(0,1),(0,-1),(1,0),(-1,0)] 
        def dfs(i,j,visited):
            if (i,j) in visited or 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] == '0':return
            visited.add((i,j))
            for rowc,colc in self.movements:
                dfs(i+rowc,j+colc,visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i,j) in visited :continue
                else:
                    dfs(i,j,visited)
                    n+=1
        return n
                
                