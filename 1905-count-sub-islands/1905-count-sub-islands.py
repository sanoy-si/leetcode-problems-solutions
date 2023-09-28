class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.visited = set()
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cnt = 0

        def dfs(row,col):

            if 0 <= row and row < len(grid1) and 0 <= col and col < len(grid1[0]) and (row,col) not in self.visited:
                val = True
                self.visited.add((row,col))
                if grid2[row][col] == 0:return
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    val = False
                for nrow,ncol in self.directions:
                    if dfs(row+nrow,col+ncol) == False:
                        val = False 
                return val
            


        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if dfs(i,j) == True:cnt += 1
        
        return cnt

        