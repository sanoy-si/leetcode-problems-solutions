class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        inbound = lambda i, j: 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
        memo = {}
        def dp(i, j):
            if not inbound(i, j):
                return 0

            if matrix[i][j] == '0':
                memo[(i, j)] = 0
                return 0

            if (i, j) not in memo:
                memo[(i, j)] = 1 + min(dp(i + 1, j + 1), dp(i + 1, j), dp(i, j + 1))
            
            return memo[(i, j)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp(i, j)

        return max(memo.values()) ** 2



