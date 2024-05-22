class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def dp(i, j):
            if i == n - 1:
                return triangle[i][j]
            
            if memo[i][j] == -1:
                memo[i][j] = triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
            
            return memo[i][j]
        
        return dp(0, 0)