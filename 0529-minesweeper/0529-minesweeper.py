class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.visited = set()
        self.dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        def isThere(row,col): 
            n = 0
            for nrow,ncol in self.dirs:
                if 0 > row+nrow or row+nrow >= len(board) or 0 > col+ncol or col+ncol >= len(board[0]):continue
                if board[row+nrow][col+ncol] == 'M':n += 1
            return str(n)
            


        def dfs(row,col):
            if 0 > row or row >= len(board) or 0 > col or col >= len(board[0]) or (row,col) in self.visited:return
            if board[row][col] == 'E':
                self.visited.add((row,col))
                near =  isThere(row,col)
                if near != "0":
                    board[row][col] = near
                    return
                board[row][col] = 'B'
                for nrow,ncol in self.dirs:
                    dfs(row + nrow,col + ncol)
                    
        dfs(click[0],click[1])
        return board

        