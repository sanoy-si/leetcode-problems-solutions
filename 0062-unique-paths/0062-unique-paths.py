class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}

        inbound = lambda row, col: 0 <= row < m and 0 <= col < n

        def dp(row, col):
            if (row, col) == (m - 1, n - 1):
                return 1
            
            if not inbound(row, col):
                return False
            
            if (row, col) not in memory:
                memory[(row, col)] = dp(row + 1, col) + dp(row, col + 1)
            
            return memory[(row, col)]
        
        return dp(0, 0)