class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        memo = {}

        def dp(idx):
            if idx == n:
                return 0
            
            if idx not in memo:
                memo[idx] = 1
                for i in range(idx + 1, n):
                    if arr[i] - arr[idx] == difference:
                        memo[idx] = 1 + dp(i)
                        break

            return memo[idx]

        answer = 1
        for i in range(n):
            answer = max(answer, dp(i))
        
        return answer