class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        def dfs(i,j):
            if 0>i or i>=m or 0>j or j>=n or board[i][j] != 'O':return
            board[i][j] = 'I'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':board[i][j] = 'X'
                elif board[i][j] == 'I':board[i][j] = 'O'
                
                
                
        