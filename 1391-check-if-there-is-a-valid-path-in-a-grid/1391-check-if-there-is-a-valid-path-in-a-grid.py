class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.d = {
            1:[(0,1),(0,-1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }
        self.visited = set()

        def dfs(row,col,parent):
            if (row,col) in self.visited or 0 > row or row >= len(grid) or 0 > col or col >= len(grid[0]) :return
            a1,a2 = self.d[grid[row][col]]
            if parent not in (None,(row + a1[0],col+a1[1]),(row+a2[0],col+a2[1])):return False
            self.visited.add((row,col))

            if row == len(grid) -1 and col == len(grid[0])-1:return True

            for rowc,colc in self.d[grid[row][col]]:
                if dfs(row + rowc,col + colc,(row,col)):return True
            return False
        return dfs(0,0,None)



        