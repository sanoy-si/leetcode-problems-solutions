class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[False for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        dp[0] = [True for _ in range(len(t) + 1)]

        for i in range(1, len(s) + 1):
            dp[i][0] = False

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = (dp[i][j - 1] or s[i - 1] == t[j - 1]) and dp[i - 1][j - 1]  
        
        return dp[len(s)][len(t)]
                
        