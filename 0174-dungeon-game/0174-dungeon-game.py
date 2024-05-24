class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0]) 
        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        memo = {}
        def dp(i, j):
            if (i, j) == (n - 1, m - 1):
                return dungeon[i][j]
            
            if not inbound(i, j):
                return -inf

            if(i, j) not in memo:
                right_health = dp(i, j + 1)
                down_health = dp(i + 1, j)

                memo[(i, j)] = max(min(dungeon[i][j] + right_health, dungeon[i][j]), min(dungeon[i][j] + down_health, dungeon[i][j]))
            
            return memo[(i, j)]
        
        return max(1, -dp(0, 0) + 1)
