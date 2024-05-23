class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        answer = 0
        def dp(idx):
            if idx >= len(questions):
                return 0
            
            if idx not in memo:    
                take = questions[idx][0] + dp(idx + questions[idx][1] + 1)
                dont_take = dp(idx + 1)

                memo[idx] = max(take, dont_take)

            return memo[idx]
        
        return dp(0)

