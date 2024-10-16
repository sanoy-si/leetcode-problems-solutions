class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (max(2, n + m - 1))
        dp[0] = dp[1] = 1
        for i in range(2, n + m - 1):
            dp[i] = i * dp[i - 1]

        down_count = m - 1
        right_count = n - 1

        return dp[down_count + right_count] // (dp[down_count] * dp[right_count])