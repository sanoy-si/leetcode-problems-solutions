class Solution:
    def minimumDeletions(self, s: str) -> int:
        memo = [[-1, -1] for _ in range(len(s))]
        def dp(idx, is_there_b):
            if idx == len(s):
                return 0
            
            if memo[idx][is_there_b] == -1:
                if is_there_b and s[idx] == 'a':
                    memo[idx][is_there_b] = 1 + dp(idx + 1, is_there_b)
                
                elif s[idx] == 'a':
                    memo[idx][is_there_b] = dp(idx + 1, is_there_b)
                
                else:
                    delete_b = 1 + dp(idx + 1, is_there_b)
                    dont_delete_b = dp(idx + 1, 1)
                    memo[idx][is_there_b] = min(delete_b, dont_delete_b)
                
            return memo[idx][is_there_b]

        return dp(0, False)