class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        memory = {}
        inbound = lambda row, col: 0 <= row < n and 0 <= col < m

        def dp(row, col):
            if (row, col) == (n - 1, m - 1):
                return grid[row][col] 
            
            if not inbound(row, col):
                return inf

            if (row, col) not in memory:
                memory[(row, col)] = min(dp(row + 1, col), dp(row, col + 1)) + grid[row][col] 
            
            return memory[(row, col)]

        return dp(0, 0)