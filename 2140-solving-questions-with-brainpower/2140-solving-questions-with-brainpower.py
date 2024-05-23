class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(len(questions))]
        dp[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):
            if i + questions[i][1] + 1 < len(dp):
                take = questions[i][0] + dp[i + questions[i][1] + 1]
            else:
                take = questions[i][0]
            
            dont_take =dp[i + 1]

            dp[i] = max(take, dont_take)

        return dp[0]

